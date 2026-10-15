# PiPedal banks

`Rig+Starter+Pack.bank` (13 presets) and `Pedal+Starter+Pack.bank` (14 presets) for [PiPedal](https://github.com/rerdavies/pipedal) 2.x.

1. Load the models/IRs into PiPedal's upload folders (run on the PiPedal machine, from the repo root):

   ```bash
   for m in manifests/manifest*.tsv; do ./pipedal/fetch_on_pi.sh "$m"; done
   ```

2. Upload the `.bank` files from PiPedal's **Banks** screen.

Plugins used besides PiPedal's built-in TooB set: Guitarix LV2 (tremolo, wah) and Dusk Audio Tape Echo 2.

## Rebuilding

The banks are generated. Edit `build_rig_bank.py` / `build_pedal_bank.py` (helpers in `t3k_presets.py`), then:

```bash
cd pipedal && python3 build_rig_bank.py && python3 build_pedal_bank.py && cd .. && python3 tools/make_presets.py
```

Each build also writes `*.refs.txt` (every file the bank uses) and `*.recipes.json` (the host-neutral chain that `tools/make_presets.py` turns into `presets/`).
`item_templates.json`, `plugin_ports.json` and `tapeecho_presets.json` are plugin defaults captured from a PiPedal 2.0.110 install.
