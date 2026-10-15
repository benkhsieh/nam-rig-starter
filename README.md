# NAM Rig Starter

Play guitar through [Neural Amp Modeler](https://www.neuralampmodeler.com) (NAM) on a Windows laptop with a Focusrite Scarlett, using 27 ready-made rigs: Fenders, Vox, Orange, Dumble-style, Mesa, Marshall Plexi/JCM800, a JC-120, 14 classic pedals, and **Van Halen** (Echoplex preamp → variac'd Plexi → Phase 90 → tape echo).

These are the same rigs that run on Ben's Raspberry Pi pedalboard in [PiPedal](https://github.com/rerdavies/pipedal). PiPedal only runs on Linux, so on Windows the same models, cabs and effects run in NAM and REAPER instead.

```
guitar ──► Scarlett input 1 (INST) ──► NAM on the laptop ──► Scarlett headphones / monitor outs
```

**What you need:** the Surface Laptop, the Scarlett and its USB cable, headphones or monitors, a guitar cable, and about 30 minutes.

---

## 1. Find out which Surface and which Scarlett you have

- **Surface:** open **Settings → System → About** and look at *Processor*.
  - It says **Snapdragon** → an Arm laptop. Most Surface Laptops sold in the last year are. Everything below works, with one extra choice in step 5.
  - It says **Intel** → an x64 laptop. Ignore the Arm notes.
- **Scarlett:** the generation is printed on the label underneath. You can also tell from the buttons: an **Auto** (gain) button means 4th Gen; an **AIR** button but no Auto means 3rd Gen; neither means 2nd Gen or older.

## 2. Install the Focusrite driver

Go to <https://downloads.focusrite.com>, choose your model, and install the **latest** Windows driver. Focusrite added native Windows-on-Arm (Snapdragon) drivers in August 2025, so a current download covers both kinds of Surface.

| Your Scarlett | Install |
|---|---|
| 4th Gen | **Focusrite Control 2** |
| 3rd Gen (and 2nd Gen 6i6 / 18i8 / 18i20) | **Focusrite Control** |
| 2nd Gen Solo / 2i2 / 2i4, 1st Gen | the standalone **Focusrite USB Driver** |

Plug the Scarlett **directly** into the laptop (not into a dock or hub), and restart if the installer asks you to.

**Turn Direct Monitor OFF.** On the front panel it is a button or switch. On 3rd/4th Gen it can also be set in Focusrite Control. If Direct Monitor is on, you'll hear your dry guitar mixed under the amp.

## 3. Set your input level

1. Plug the guitar into **input 1** and press **INST** (on a 2nd Gen it's an INST/LINE switch).
2. Strum hard and raise the input 1 gain as high as it goes while the ring around the knob stays green (amber at most) on your loudest hits. It should never turn **red**. (4th Gen owners can just press **Auto** and play for 10 seconds.)

## 4. Install NAM

Download the Windows installer from <https://www.neuralampmodeler.com> (on the page you get to from **Download**). You need version **0.7.14 or newer**: the models in this pack are TONE3000's newer "A2" models, and older versions won't load them. The installer gives you a standalone app and a VST3 plugin.

> On a Snapdragon Surface, NAM is an Intel (x64) program that Windows runs through its built-in emulator. It works. If you hear crackles, see [Troubleshooting](#troubleshooting).

Open **Neural Amp Modeler** (the standalone app) and go to its settings (the ⚙ / *Settings* button):

- **Driver type:** ASIO
- **Device:** Focusrite USB ASIO
- **Input:** 1. **Outputs:** 1 and 2
- **Sample rate:** 48000
- **Buffer size:** 128 (try 64 later if it stays clean)

## 5. Get the presets

1. On this GitHub page, click **Code → Download ZIP** and unzip it somewhere, for example `Documents\nam-rig-starter`.
2. Open that folder in File Explorer, click the address bar, type `powershell`, and press Enter.
3. Paste this and press Enter:

   ```powershell
   powershell -ExecutionPolicy Bypass -File .\windows\Get-NamStarterPack.ps1
   ```

The script downloads about 35 MB into **`Documents\NAM Starter Pack\Presets\`**, one folder per rig. Files are numbered in signal-chain order, and each folder has a `Recipe.txt` describing the whole chain:

```
Van Halen — Eruption (Variac Plexi)\
  1 Pedal - 4. EP101 G5.nam
  2 Amp - SLAMMIN_MARSHALL_1959HW_170V_DIMED_10_S.nam
  3 Cab - M25 UL 1960TV 4x12 M201 1.50in 0.0in SA73.wav
  6 Reverb - Plate_2_Medium_Plate.wav
  Recipe.txt
```

Steps without a file (4 and 5 in this rig: phaser and tape echo) are settings, and they're described in `Recipe.txt`. Every rig is also listed in [presets/PRESETS.md](presets/PRESETS.md).

Want the whole library, about 1,250 models and IRs? Run the script again with `-Full`. It downloads everything into `Documents\NAM Starter Pack\Library\`.

## 6. Play (the quick way): one amp in NAM

In the NAM app:

1. Click the **model** slot and pick a rig folder's **`Amp`** file.
2. If that folder has a **`Cab`** file, load it into the **IR** slot. If there is no Cab file, the amp capture already includes a cabinet, so leave the IR slot off.
3. Use the **Noise Gate** for high-gain rigs, the EQ for tone, and **Output** for volume.

Good first picks:

- **Van Halen — Eruption (Variac Plexi):** the variac'd Plexi brown sound. Roll your guitar's volume back a little for rhythm parts.
- **Fender Deluxe Reverb** for cleans.
- **Van Halen — 5150** for the later EVH sound.
- **Slash — Appetite #36**.

The NAM app holds one amp and one IR at a time. For the full chains with a pedal in front and phaser/delay/reverb after, use step 7.

## 7. Play the full rigs (the PiPedal-style way): REAPER

[REAPER](https://www.reaper.fm/download.php) is a small, fast audio app that can host a whole pedalboard: two NAMs plus effects, saved as one-click chains. It has a free, fully working 60-day evaluation and costs $60 after that. It also comes with every effect these rigs use (ReaDelay, ReaVerb, JS Phaser, Chorus and Tremolo).

- **Snapdragon:** download the **Windows ARM64EC** version. It runs natively and can still load the x64 NAM plugin. If NAM doesn't appear in REAPER's plugin list, install the regular **Windows x64** version instead. It's slower, but it works.
- **Intel:** download the regular **Windows x64** version.

**One-time setup**

1. **Options → Preferences → Audio → Device:** Audio system **ASIO**, driver **Focusrite USB ASIO**. Tick **Request sample rate** (48000) and **Request block size** (128).
2. **Track → Insert new track.** On the track, click the red **record-arm** button. Right-click it, set the input to **Input: Mono → Input 1**, and set **Record monitoring: On**. Now you hear yourself through the track's effects.
3. Click the track's **FX** button.

**Building a rig** (open its `Recipe.txt` alongside REAPER):

| Recipe says | In REAPER's FX window |
|---|---|
| **Pedal** (`1 Pedal - …nam`) | Add **VST3: NeuralAmpModeler**, load the pedal file, leave IR off and EQ flat |
| **Amp** + **Cab** | Add another **NeuralAmpModeler**, load the amp file, and load the cab `.wav` into its IR slot |
| Noise gate | The amp NAM's Noise Gate knob |
| Phaser / Chorus / Tremolo | Add **JS: Phaser** / **JS: Chorus** / **JS: Tremolo** with the settings listed |
| Delay / Tape echo | Add **ReaDelay** and set the time and feedback listed. For tape echo, also turn the delay's lowpass down to about 3 kHz |
| Reverb (`… Reverb - …wav`) | Add **ReaVerb**, click **Add → File**, choose the reverb `.wav`, and set wet to the level listed |

FX run top to bottom in the order listed, the same order as the numbers. When a rig sounds right, use the FX window's **FX → Save FX chain…** menu and name it after the rig. After that, switching rigs is **FX → Load FX chain…**.

## Troubleshooting

| Problem | Fix |
|---|---|
| Crackles or pops | Raise the buffer to **256**. Plug in the charger and set **Settings → System → Power → Power mode → Best performance**. Close Chrome and Teams. If your NAM shows a **Slim** control, turn it up a little: A2 models can trade a little detail for much less CPU. |
| No sound | Check the driver is **Focusrite USB ASIO**, the input is **1**, and the outputs are **1/2**. Turn up the Scarlett's monitor/headphone knob. In REAPER, the track must be armed with monitoring on. |
| You hear the dry guitar too | Turn **Direct Monitor off** (step 2). |
| "Sample rate couldn't be set" | Set 48 kHz in Focusrite Control first, then restart the app. |
| A model won't load | Update NAM to 0.7.14 or newer. |
| Too quiet or too fuzzy | Revisit step 3, then adjust NAM's **Input** knob. Hot pickups may need it turned down. |
| The download script says some files failed | Run it again. It skips anything it already has. |

## Want the real PiPedal experience?

PiPedal runs on Linux on a Raspberry Pi 4/5 or a 64-bit Intel/AMD PC, and you control it from your phone's browser. Ben's version is a Pi 5 with a touchscreen and a cheap USB interface. The Scarlett works on Linux without drivers. Two ways to get there:

- **A Raspberry Pi 5** (about $100 with power supply and SD card). This is the most like Ben's setup.
- **An Intel Surface:** run Ubuntu 24.04 from a USB SSD and install `pipedal_*_amd64.deb` from [PiPedal's releases](https://github.com/rerdavies/pipedal/releases). A Snapdragon Surface isn't a good fit, because Linux support for those is still experimental.

Then:

1. Run `pipedal/fetch_on_pi.sh` with each manifest to load the models into PiPedal:

   ```bash
   for m in manifests/manifest*.tsv; do ./pipedal/fetch_on_pi.sh "$m"; done
   ```

2. Upload `pipedal/Rig+Starter+Pack.bank` and `pipedal/Pedal+Starter+Pack.bank` from PiPedal's **Banks** screen. They need the Guitarix LV2 plugins and Dusk Audio Tape Echo 2 installed.

## What's in this repo

| Path | What |
|---|---|
| `windows/Get-NamStarterPack.ps1` | The download script (step 5) |
| `presets/PRESETS.md`, `presets/presets.json` | Every rig as a signal chain, readable by people and by the script |
| `manifests/` | Download lists (tone, file, URL) for the full ~1,250-file library, plus the TONE3000 tone lists they came from |
| `pipedal/` | The PiPedal banks and the Python that builds them (`python3 build_rig_bank.py`, `python3 build_pedal_bank.py`) |
| `tools/make_presets.py` | Regenerates `presets/` from the banks. Run from the repo root after rebuilding them |

## Credits

The models and IRs are captures by the TONE3000 community. This repo links to them and doesn't copy them. See [CREDITS.md](CREDITS.md) for every tone page. If you like a capture, find its creator on [TONE3000](https://www.tone3000.com) and give it a like. The scripts here are MIT-licensed.
