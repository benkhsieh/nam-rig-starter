# NAM Rig Starter

Play guitar through [Neural Amp Modeler](https://www.neuralampmodeler.com) (NAM) on a Windows laptop with a Focusrite Scarlett, using 27 ready-made rigs: Fenders, Vox, Orange, Dumble-style, Mesa, Marshall Plexi/JCM800, a JC-120, 14 classic pedals, and **Van Halen** (Echoplex preamp → variac'd Plexi → Phase 90 → tape echo).

These are the same rigs that run on Ben's Raspberry Pi pedalboard in [PiPedal](https://github.com/rerdavies/pipedal). PiPedal only runs on Linux, so on Windows the same models, cabs and effects run in the NAM app, in **MOD Desktop** (a free pedalboard app much like PiPedal), or in REAPER.

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

Using MOD Desktop (step 7A)? Add `-ModDesktop`. It also copies every model and IR into MOD Desktop's own folders, so they show up in its file pickers. You can combine it with `-Full`:

```powershell
powershell -ExecutionPolicy Bypass -File .\windows\Get-NamStarterPack.ps1 -ModDesktop
```

## 6. Play (the quick way): one amp in NAM

In the NAM app:

1. Click the **model** slot and pick a rig folder's **`Amp`** file.
2. If that folder has a **`Cab`** file, load it into the **IR** slot. If there is no Cab file, the amp capture already includes a cabinet, so leave the IR slot off.
3. Use the **Noise Gate** for high-gain rigs, the EQ for tone, and **Output** for volume.
4. **Slim knob:** every model in this pack holds two versions, a light one and a full one with about 6x more detail. NAM starts at **Slim = 0**, which plays the *light* version. Turn Slim to **1** for the full version. Keep it there if it plays clean, and drop back to 0 if you get crackles.

Good first picks:

- **Van Halen — Eruption (Variac Plexi):** the variac'd Plexi brown sound. Roll your guitar's volume back a little for rhythm parts.
- **Fender Deluxe Reverb** for cleans.
- **Van Halen — 5150** for the later EVH sound.
- **Slash — Appetite #36**.

The NAM app holds one amp and one IR at a time. For the full chains with a pedal in front and phaser/delay/reverb after, use step 7.

## 7. Play the full rigs

Two ways to run a whole rig (pedal → amp → cab → effects), saved so you can switch between them:

- **7A. MOD Desktop:** free, and the closest thing to Ben's PiPedal: a drag-and-drop pedalboard in your web browser. It's still beta, so it may need some fiddling with the Scarlett.
- **7B. REAPER:** the most dependable option, and $60 after a free 60-day trial.

Try 7A first. If it won't run cleanly on your laptop, use 7B.

## 7A. MOD Desktop (free, PiPedal-style)

[MOD Desktop](https://mod.audio/desktop/) puts MOD Audio's pedalboard on your laptop. Version 0.0.13 (October 2026) has a Neural Amp Modeler block with built-in TONE3000 sign-in, cabinet and convolution IR loaders, and about 188 other effects.

> **Heads-up:**
> - **Beta software.** MOD's own notes say some USB interfaces on Windows only start reliably at **48 kHz** or with the **WDM-KS** driver instead of ASIO. The steps below cover both.
> - **Intel build only.** On a Snapdragon Surface the whole app runs through Windows' emulator, which uses more processor than the REAPER route. Start with a buffer of 256.
> - **Unconfirmed:** whether MOD's NAM block loads this pack's A2 models. The NAM plugin MOD is based on supports them, but if a model won't load, see Troubleshooting.

**Install and start it**

1. In **Focusrite Control** (2nd Gen: the Focusrite USB driver's settings panel), set the sample rate to **48 kHz**.
2. Download **`mod-desktop-…-win64-installer.exe`** (the newest version) from [MOD Desktop's releases page](https://github.com/mod-audio/mod-desktop/releases) and run it. If Windows warns about an unrecognized app, click **More info → Run anyway**.
3. Open **MOD Desktop**. A small settings window appears, and the app lives in the system tray (next to the clock) after that.
4. Set **Audio Device** to **Focusrite USB ASIO**, leave input and output on the same device, set **Buffer Size** to 256, and click **Start**. Once **Status** shows it running, click **Open Web GUI**. Your pedalboard opens in a browser tab.
   - If it won't start or you hear nothing, click **Stop**, pick the Scarlett's **WDM-KS** entry under Audio Device instead, and click **Start** again.
   - Once it plays cleanly, try **Buffer Size 128** for a little less delay.
5. Run the download script with `-ModDesktop` (step 5) if you haven't yet. The files land in `Documents\MOD Desktop\user-files\` under `NAM Models`, `Speaker Cabinets IRs` and `Reverb IRs`, each in a `NAM Starter Pack\<tone>` folder. The **Open User Files** button in MOD's settings window opens that folder.

**Build a rig.** Open the rig's `Recipe.txt` next to the browser. In MOD the signal flows **left to right**: your Scarlett's inputs are on the left edge (**input 1** is your guitar) and the outputs are on the right edge.

1. Find each block with the search box in the plugin bar along the bottom, and drag it onto the board.
2. Drag a cable from **input 1** into the first block, from each block's output to the next block's input, and from the last block to **both** outputs, so you hear it in both ears.
3. Click a block to open its controls.

| Recipe says | Block to add in MOD (search for it) |
|---|---|
| **Pedal** or **Amp** (`.nam`) | **Neural Amp Modeler** (search `NAM`). Click its file selector and pick the file under `NAM Starter Pack` → the tone folder named in `Recipe.txt`. If the block has a quality or size control, set it to the maximum. |
| **Cab** (`.wav`) | The **cabinet IR loader** (search `cab`). Pick the cab file. NAM in MOD has no IR slot of its own, so the cab is a separate block right after the amp. |
| Noise gate | A **gate** block (search `gate`) before the first NAM, set to the threshold listed |
| Phaser / Chorus / Tremolo / Delay | Search the effect's name and set it close to what `Recipe.txt` lists. For tape echo, use a delay with its tone or high end turned down. |
| **Reverb** (`.wav`) | The **convolution IR loader** (search `convolution`). Pick the reverb file and keep the wet level low, around the dB listed. |

When it sounds right, **Save** the pedalboard and name it after the rig. Your saved pedalboards appear in MOD's pedalboard library, where one click switches rigs.

The NAM block's file selector also has a **TONE3000** sign-in, so you can browse and add more amps and pedals right from MOD.

## 7B. REAPER

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
| Crackles or pops | Raise the buffer to **256**. Plug in the charger and set **Settings → System → Power → Power mode → Best performance**. Close Chrome and Teams. If you turned NAM's **Slim** knob up, turn it back to 0 (see the tip in step 6). |
| No sound | Check the driver is **Focusrite USB ASIO**, the input is **1**, and the outputs are **1/2**. Turn up the Scarlett's monitor/headphone knob. In REAPER, the track must be armed with monitoring on. |
| You hear the dry guitar too | Turn **Direct Monitor off** (step 2). |
| "Sample rate couldn't be set" | Set 48 kHz in Focusrite Control first, then restart the app. |
| A model won't load | Update NAM to 0.7.14 or newer. |
| Too quiet or too fuzzy | Revisit step 3, then adjust NAM's **Input** knob. Hot pickups may need it turned down. |
| The download script says some files failed | Run it again. It skips anything it already has. |
| MOD Desktop won't start, or starts with no sound | Set the Scarlett to 48 kHz (7A, step 1), try the **WDM-KS** device instead of ASIO, and use Buffer Size 256. Check the cables run from input 1 to both outputs. |
| A model won't load in MOD Desktop | MOD's NAM block may not handle these newer A2 models yet. Use the NAM app (step 6) or REAPER (7B) for that rig, and tell Ben which file failed. |
| MOD Desktop's file picker doesn't show the pack | Run the download script with `-ModDesktop`, then close and reopen the block's file selector. |

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
