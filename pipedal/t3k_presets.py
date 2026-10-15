#!/usr/bin/env python3
"""Shared helpers for building PiPedal banks from the T3K Starter Pack files.

Inputs (same folder): item_templates.json (factory-preset plugin items from the Pi),
plugin_ports.json (control defaults for plugins with no factory template),
tapeecho_presets.json (Tape Echo 2's built-in presets).
"""
import copy, json, sys

TPL = json.load(open("item_templates.json"))
PORTS = json.load(open("plugin_ports.json"))
TAPE = {p["label"]: p["controlValues"] for p in json.load(open("tapeecho_presets.json"))["presets"]}

PACK = "T3K Starter Pack"
NAM_URI = "http://two-play.com/plugins/toob-nam"
CAB_URI = "http://two-play.com/plugins/toob-cab-ir"
REV_URI = "http://two-play.com/plugins/toob-convolution-reverb-stereo"
TAPE_URI = "https://dusk-audio.github.io/plugins/tape-echo"
U = {
    "tuner": "http://two-play.com/plugins/toob-tuner",
    "gate": "http://two-play.com/plugins/toob-noise-gate",
    "trem": "http://two-play.com/plugins/toob-tremolo-mono",
    "delay": "http://two-play.com/plugins/toob-delay",
    "phaser": "http://two-play.com/plugins/toob-phaser",
    "chorus": "http://two-play.com/plugins/toob-chorus",
    "gxtrem": "http://guitarix.sourceforge.net/plugins/gx_tremolo#_tremolo",
    "wah": "http://guitarix.sourceforge.net/plugins/gx_gcb_95_#_gcb_95_",
    "echocat": "http://guitarix.sourceforge.net/plugins/gxechocat#echocat",
    "plate": "urn:dragonfly:plate",
}

_next = [100]
RECIPE = {}  # instanceId -> host-neutral description of the item, for presets/presets.json
def nid():
    _next[0] += 1
    return _next[0]

def path_state(key, rel, atom="http://lv2plug.in/ns/ext/atom#Path"):
    return {"flags": 3, "atomType": atom, "value": rel}

def base_item(uri):
    """A fresh item for `uri`: the factory template if one exists, else built from LV2 port defaults."""
    if uri in TPL:
        it = copy.deepcopy(TPL[uri])
        it["midiBindings"] = []
        it["stateUpdateCount"] = 0
    else:
        p = PORTS[uri]
        it = {
            "uri": uri, "isEnabled": True,
            "controlValues": [{"key": s, "value": d if d is not None else 0} for s, d, *_ in p["ports"]],
            "pluginName": p["name"], "midiBindings": [], "midiChannelBinding": None,
            "stateUpdateCount": 0, "lv2State": [False, {}], "lilvPresetUri": "",
            "pathProperties": {}, "title": "", "useModUi": False, "iconColor": "default",
            "sideChainInputId": -1,
        }
    it["instanceId"] = nid()
    return it

def item(key_or_uri, enabled=True, **controls):
    it = base_item(U.get(key_or_uri, key_or_uri))
    if it["uri"] == NAM_URI:
        controls.setdefault("modelSize", 1.0)  # "Quality": run the full tier of slimmable A2 models (0 = light tier)
    it["isEnabled"] = enabled
    key = next((k for k, u in U.items() if u == it["uri"]), it["pluginName"])
    RECIPE[it["instanceId"]] = {"effect": key, "plugin": it["pluginName"], "enabled": enabled, "settings": controls}
    known = {c["key"] for c in it["controlValues"]}
    for k, v in controls.items():
        if k not in known:
            sys.exit(f"unknown control {k} for {it['pluginName']}")
        for c in it["controlValues"]:
            if c["key"] == k:
                c["value"] = v
    return it

def with_file(it, prop, rel):
    st = it["lv2State"][1] if it["lv2State"][0] else {}
    st[prop] = path_state(prop, rel)
    it["lv2State"] = [True, st]
    it["pathProperties"][prop] = json.dumps({"otype_": "Path", "value": rel}).replace('", "', '","').replace('{"otype_', '{"otype_')
    return it

def nam(tone, model, inputGain=0, outputGain=0, gate=-80):
    it = item(NAM_URI, inputGain=inputGain, outputGain=outputGain, gate=gate)
    return with_file(it, NAM_URI + "#modelFile", f"NeuralAmpModels/{PACK}/{tone}/{model}")

def cab(tone, ir):
    it = item(CAB_URI)
    with_file(it, CAB_URI + "#impulseFile", f"CabIR/{PACK}/{tone}/{ir}")
    for extra in ("#impulseFile2", "#impulseFile3"):
        it["lv2State"][1][CAB_URI + extra] = path_state(None, "", "http://lv2plug.in/ns/ext/atom#String")
        it["pathProperties"].pop(CAB_URI + extra, None)
    return it

def reverb(tone, ir, mix_db=-12):
    it = item(REV_URI, reverb_mix=mix_db)
    return with_file(it, "http://two-play.com/plugins/toob-impulse#impulseFile", f"ReverbImpulseFiles/{PACK}/{tone}/{ir}")

def tape(preset_label, **overrides):
    it = item(TAPE_URI)
    vals = dict(TAPE[preset_label]); vals.update(overrides)
    for c in it["controlValues"]:
        if c["key"] in vals:
            c["value"] = vals[c["key"]]
    it["title"] = f"Tape Echo 2 ({preset_label})"
    RECIPE[it["instanceId"]].update(effect="tape echo", settings={"preset": preset_label, **overrides})
    return it

def preset(name, items):
    items = [item("tuner")] + items
    return {
        "instanceId": nid(),
        "preset": {
            "name": name, "input_volume_db": 0, "output_volume_db": 0,
            "items": items, "nextInstanceId": _next[0] + 1, "snapshots": [],
        },
    }

BASSMAN_CAB = ("1966 Fender Bassman Cabinet Jensen C12NA Speaker", "1966 Bassman Cabinet with Jensen C12N - SM57 - Cap Edge.wav")
SPRING = ("Fender Spring Reverb Tank", "Fender Reverb Tank_Dwell 08_Tone 08.wav")
DLX_SPRING = ("Deluxe Reverb Tank", "Deluxe Medium.wav")
PLATE = ("Lexicon MPX100", "Plate_2_Medium_Plate.wav")
HALL = ("Lexicon MPX100", "Hall_6_Medium_Hall.wav")


def recipe(it):
    """Describe one bank item without PiPedal specifics: model/IR files, or an effect and its settings."""
    r = dict(RECIPE[it["instanceId"]])
    files = [v["value"] for v in it["lv2State"][1].values() if isinstance(v, dict) and v.get("value")]
    if it["uri"] == NAM_URI:
        r = {"type": "nam", "file": files[0], "enabled": it["isEnabled"]}
    elif it["uri"] == CAB_URI:
        r = {"type": "cab_ir", "file": files[0]}
    elif it["uri"] == REV_URI:
        r = {"type": "reverb_ir", "file": files[0], "mix_db": r["settings"]["reverb_mix"]}
    else:
        r["type"] = "effect"
    return r


def write_bank(name, presets, filename):
    """Write a PiPedal bank file plus a list of every model/IR file it references."""
    bank = {"name": name, "nextInstanceId": nid() + 1,
            "selectedPreset": presets[0]["instanceId"], "presets": presets}
    json.dump(bank, open(filename, "w"), indent=2)
    refs = sorted({v["value"] for p in presets for it in p["preset"]["items"]
                   for v in it["lv2State"][1].values() if isinstance(v, dict) and v.get("value")})
    refs_file = filename.replace(".bank", ".refs.txt")
    open(refs_file, "w").write("\n".join(refs) + "\n")
    recipes = [{"name": p["preset"]["name"], "chain": [recipe(it) for it in p["preset"]["items"][1:]]} for p in presets]
    json.dump({"bank": name, "presets": recipes}, open(filename.replace(".bank", ".recipes.json"), "w"), indent=2, ensure_ascii=False)
    print(f"{filename}: {len(presets)} presets, {len(refs)} file references -> {refs_file}")
