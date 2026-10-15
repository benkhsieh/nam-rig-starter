#!/usr/bin/env python3
"""Turn the PiPedal bank recipes into host-neutral presets for any NAM host.

Reads pipedal/*.recipes.json (written by the bank builders) and manifests/*.tsv,
writes presets/presets.json (read by windows/Get-NamStarterPack.ps1) and presets/PRESETS.md.
Run from the repo root after rebuilding the banks.
"""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BANKS = ["Rig+Starter+Pack", "Pedal+Starter+Pack"]
KIND_DIRS = {"amp": "NeuralAmpModels/T3K Starter Pack", "pedal": "NeuralAmpModels/T3K Pedals",
             "cab": "CabIR/T3K Starter Pack", "rev": "ReverbImpulseFiles/T3K Starter Pack"}

# PiPedal effect -> what to use in REAPER (stock plugins) and how to set it
TAPE = {"Classic Tape Echo": "about 300 ms, 2-3 repeats, darkened (lowpass ~3 kHz)",
        "Rockabilly Guitar": "slapback: about 110 ms, a single repeat, darkened (lowpass ~3 kHz)"}


def effect_step(r):
    s, e = r["settings"], r["effect"]
    if e == "gate":
        return "Noise gate", "the Noise Gate knob in NAM (or ReaGate)", f"threshold {s['threshold']:.0f} dB"
    if e == "phaser":
        return "Phaser (MXR Phase 90)", "JS: Phaser", f"slow sweep, rate {s['rate']} Hz"
    if e == "chorus":
        return "Chorus", "JS: Chorus", f"rate {s['rate']} Hz, depth {int(s['depth'] * 100)}%"
    if e == "delay":
        return "Delay", "ReaDelay", f"{s['delay']:.0f} ms, feedback {s['feedback']:.0f}%, wet low (about -15 dB)"
    if e in ("trem", "gxtrem"):
        rate = s.get("rate", s.get("freq"))
        return "Tremolo", "JS: Tremolo", f"rate {rate} Hz, depth {int(s['depth'] * 100)}%"
    if e == "wah":
        return "Wah", "JS: Wah (or a wah plugin you like)", "rock it with an expression pedal or leave it parked"
    if e == "tape echo":
        mix = s.get("mix")
        return "Tape echo", "ReaDelay", TAPE[s["preset"]] + (f", mix {int(mix * 100)}%" if mix else "")
    return e, r["plugin"], json.dumps(s)


def manifest_urls():
    urls = {}
    for tsv in sorted((ROOT / "manifests").glob("manifest*.tsv")):
        for line in tsv.read_text().splitlines():
            kind, title, name, url = line.split("\t")
            urls[f"{KIND_DIRS[kind]}/{title}/{name}"] = url
    return urls


def folder_name(name):
    return re.sub(r'[/\\:*?"<>|]', "-", name).strip(" .")


def build():
    urls = manifest_urls()
    out = []
    for bank in BANKS:
        recipes = json.loads((ROOT / "pipedal" / f"{bank}.recipes.json").read_text())
        for p in recipes["presets"]:
            chain = p["chain"]
            nams = [i for i, r in enumerate(chain) if r["type"] == "nam"]
            has_cab = any(r["type"] == "cab_ir" for r in chain)
            steps = []
            for i, r in enumerate(chain):
                step = {"n": len(steps) + 1, "enabled": r.get("enabled", True)}
                if r["type"] in ("nam", "cab_ir", "reverb_ir"):
                    step["url"] = urls[r["file"]]
                    step["file"] = r["file"].split("/")[-1]
                    step["source"] = r["file"].split("/")[-2]
                if r["type"] == "nam":
                    is_amp = i == nams[-1]
                    step["kind"] = "Amp" if is_amp else "Pedal"
                    step["where"] = "NAM (amp slot)" if is_amp else "NAM (a second instance, before the amp)"
                    step["notes"] = ("model file; load the cab IR from the next step into this NAM's IR slot" if is_amp and has_cab
                                     else "model file; the capture already includes a cab, so leave NAM's IR slot off" if is_amp
                                     else "model file; IR slot off, EQ flat")
                elif r["type"] == "cab_ir":
                    step.update(kind="Cab", where="IR slot of the amp's NAM", notes="cabinet impulse response")
                elif r["type"] == "reverb_ir":
                    step.update(kind="Reverb", where="ReaVerb (File: load this .wav)",
                                notes=f"reverb impulse response; wet about {r['mix_db']} dB, dry 0 dB")
                else:
                    step["kind"], step["where"], step["notes"] = effect_step(r)
                    if not step["enabled"]:
                        step["notes"] += " (starts bypassed)"
                steps.append(step)
            out.append({"bank": recipes["bank"], "name": p["name"], "folder": folder_name(p["name"]), "steps": steps})
    return out


def markdown(presets):
    lines = ["# Presets", "",
             "Every preset from Ben's PiPedal banks, written out as a signal chain you can rebuild in any NAM host.",
             "`Get-NamStarterPack.ps1` downloads the files for each one into its own folder, numbered in chain order.", ""]
    bank = None
    for p in presets:
        if p["bank"] != bank:
            bank = p["bank"]
            lines += [f"## {bank}", ""]
        lines += [f"### {p['name']}", "", "| # | Stage | Load / use | File or setting |", "|---|---|---|---|"]
        for s in p["steps"]:
            what = f"`{s['file']}` ({s['source']})" if "file" in s else s["notes"]
            lines.append(f"| {s['n']} | {s['kind']} | {s['where']} | {what} |")
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    presets = build()
    (ROOT / "presets").mkdir(exist_ok=True)
    (ROOT / "presets" / "presets.json").write_text(json.dumps(presets, indent=2, ensure_ascii=False) + "\n")
    (ROOT / "presets" / "PRESETS.md").write_text(markdown(presets))
    files = {s["url"] for p in presets for s in p["steps"] if "url" in s}
    print(f"{len(presets)} presets, {len(files)} distinct files")
