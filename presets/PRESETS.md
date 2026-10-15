# Presets

Every preset from Ben's PiPedal banks, written out as a signal chain you can rebuild in any NAM host.
`Get-NamStarterPack.ps1` downloads the files for each one into its own folder, numbered in chain order.

## Rig Starter Pack

### Setzer — '62 Blonde Bassman + Space Echo

| # | Stage | Load / use | File or setting |
|---|---|---|---|
| 1 | Pedal | NAM (a second instance, before the amp) | `RE-201 Instrument Level 5.nam` (Roland Space Echo RE-201) |
| 2 | Amp | NAM (amp slot) | `Fender BL Bassman Edge FAT DI.nam` (Fender Blonde Bassman Edge BAL DI) |
| 3 | Cab | IR slot of the amp's NAM | `1966 Bassman Cabinet with Jensen C12N - SM57 - Cap Edge.wav` (1966 Fender Bassman Cabinet Jensen C12NA Speaker) |
| 4 | Tape echo | ReaDelay | slapback: about 110 ms, a single repeat, darkened (lowpass ~3 kHz) |
| 5 | Reverb | ReaVerb (File: load this .wav) | `Fender Reverb Tank_Dwell 08_Tone 08.wav` (Fender Spring Reverb Tank) |

### '62 Fender Bassman

| # | Stage | Load / use | File or setting |
|---|---|---|---|
| 1 | Amp | NAM (amp slot) | `62 Bassman 755.nam` (1962 Fender Bassman) |
| 2 | Cab | IR slot of the amp's NAM | `1966 Bassman Cabinet with Jensen C12N - SM57 - Cap Edge.wav` (1966 Fender Bassman Cabinet Jensen C12NA Speaker) |
| 3 | Tremolo | JS: Tremolo | rate 5.0 Hz, depth 50% (starts bypassed) |
| 4 | Reverb | ReaVerb (File: load this .wav) | `Fender Reverb Tank_Dwell 08_Tone 08.wav` (Fender Spring Reverb Tank) |

### Fender Deluxe Reverb

| # | Stage | Load / use | File or setting |
|---|---|---|---|
| 1 | Amp | NAM (amp slot) | `Deluxe Reverb.nam` (Fender Deluxe Reverb (A2)) |
| 2 | Tremolo | JS: Tremolo | rate 5.0 Hz, depth 50% (starts bypassed) |
| 3 | Reverb | ReaVerb (File: load this .wav) | `Deluxe Medium.wav` (Deluxe Reverb Tank) |

### Fender Vibrolux Reverb

| # | Stage | Load / use | File or setting |
|---|---|---|---|
| 1 | Amp | NAM (amp slot) | `Fender Custom Vibrolux 90s, Vol 2.7, Treb 5.5, Bass 6.2 e906.nam` (Fender Custom Vibrolux Reverb Amp) |
| 2 | Tremolo | JS: Tremolo | rate 4.5 Hz, depth 45% |
| 3 | Reverb | ReaVerb (File: load this .wav) | `Fender Reverb Tank_Dwell 08_Tone 08.wav` (Fender Spring Reverb Tank) |

### Vox AC30 Top Boost

| # | Stage | Load / use | File or setting |
|---|---|---|---|
| 1 | Amp | NAM (amp slot) | `AC30-6 TB Brl 3.nam` ('02 Vox AC30-6 Top Boost) |
| 2 | Tremolo | JS: Tremolo | rate 6.0 Hz, depth 50% (starts bypassed) |
| 3 | Reverb | ReaVerb (File: load this .wav) | `Plate_2_Medium_Plate.wav` (Lexicon MPX100) |

### Orange Rockerverb

| # | Stage | Load / use | File or setting |
|---|---|---|---|
| 1 | Noise gate | the Noise Gate knob in NAM (or ReaGate) | threshold -60 dB |
| 2 | Amp | NAM (amp slot) | `Orange Rockerverb MK3 - Crunch G5 - Canov+Arnold.nam` (Orange Rockerverb MK3 v2 (Canov+Arnold)) |
| 3 | Cab | IR slot of the amp's NAM | `Orange 2x12 V30 SM57 A.wav` (Orange 2x12 V30) |
| 4 | Reverb | ReaVerb (File: load this .wav) | `Hall_6_Medium_Hall.wav` (Lexicon MPX100) |

### Dumble-style ODS (Two-Rock)

| # | Stage | Load / use | File or setting |
|---|---|---|---|
| 1 | Amp | NAM (amp slot) | `BMD G5 T5M5B5 Vol7 P5 BF A1 Conversion.nam` (Two Rock Studio Signature + OX Box 2x12 Two Rock Cab (V2)) |
| 2 | Delay | ReaDelay | 380 ms, feedback 25%, wet low (about -15 dB) |
| 3 | Reverb | ReaVerb (File: load this .wav) | `Plate_2_Medium_Plate.wav` (Lexicon MPX100) |

### Mesa Dual Rectifier

| # | Stage | Load / use | File or setting |
|---|---|---|---|
| 1 | Noise gate | the Noise Gate knob in NAM (or ReaGate) | threshold -55 dB |
| 2 | Amp | NAM (amp slot) | `FR MBDR MW Red Mdn - 3 - 4FB UR SM57a.nam` (Mesa Dual Rectifier MW Red Modern - Mesa 4x12 - Full Rig) |

### Van Halen — '68 Plexi Brown

| # | Stage | Load / use | File or setting |
|---|---|---|---|
| 1 | Amp | NAM (amp slot) | `MRSH SL68 I Drive BRI CAB.nam` (1968 Marshall Super Lead 12 000 Series Drive A2) |
| 2 | Phaser (MXR Phase 90) | JS: Phaser | slow sweep, rate 0.45 Hz (starts bypassed) |
| 3 | Tape echo | ReaDelay | about 300 ms, 2-3 repeats, darkened (lowpass ~3 kHz), mix 20% |

### Van Halen — Eruption (Variac Plexi)

| # | Stage | Load / use | File or setting |
|---|---|---|---|
| 1 | Pedal | NAM (a second instance, before the amp) | `4. EP101 G5.nam` (Dunlop EP101 Echoplex Preamp) |
| 2 | Amp | NAM (amp slot) | `SLAMMIN_MARSHALL_1959HW_170V_DIMED_10_S.nam` (Marshall 1959HW Plexi Variac [Hyper Accuracy]) |
| 3 | Cab | IR slot of the amp's NAM | `M25 UL 1960TV 4x12 M201 1.50in 0.0in SA73.wav` (UK Greenback - Marshall 1960TV 4x12 M201) |
| 4 | Phaser (MXR Phase 90) | JS: Phaser | slow sweep, rate 0.3 Hz |
| 5 | Tape echo | ReaDelay | about 300 ms, 2-3 repeats, darkened (lowpass ~3 kHz), mix 20% |
| 6 | Reverb | ReaVerb (File: load this .wav) | `Plate_2_Medium_Plate.wav` (Lexicon MPX100) |

### Van Halen — 5150

| # | Stage | Load / use | File or setting |
|---|---|---|---|
| 1 | Noise gate | the Noise Gate knob in NAM (or ReaGate) | threshold -55 dB |
| 2 | Amp | NAM (amp slot) | `1992 Peavey 5150 Block Letter - Mesa OS 412 Full Rig (@vivahatex).nam` (1992 Peavey 5150 Block Letter - Mesa OS 412 Full Rig) |
| 3 | Reverb | ReaVerb (File: load this .wav) | `Plate_2_Medium_Plate.wav` (Lexicon MPX100) |

### Slash — Appetite #36

| # | Stage | Load / use | File or setting |
|---|---|---|---|
| 1 | Wah | JS: Wah (or a wah plugin you like) | rock it with an expression pedal or leave it parked (starts bypassed) |
| 2 | Amp | NAM (amp slot) | `SLAMMIN_PLEXI_BRBS_SIR_#36_LG_MV3_SLASH_S.nam` (Marshall 1959 BRBS SIR #36 Slash [Standard]) |
| 3 | Cab | IR slot of the amp's NAM | `M25 UL 1960TV 4x12 M201 1.50in 0.0in SA73.wav` (UK Greenback - Marshall 1960TV 4x12 M201) |
| 4 | Delay | ReaDelay | 420 ms, feedback 20%, wet low (about -15 dB) |
| 5 | Reverb | ReaVerb (File: load this .wav) | `Plate_2_Medium_Plate.wav` (Lexicon MPX100) |

### Roland JC-120 Jazz Chorus

| # | Stage | Load / use | File or setting |
|---|---|---|---|
| 1 | Amp | NAM (amp slot) | `Roland JC 120B Jazz Chorus- Bright Off, SM57.nam` (Roland JC 120B Jazz Chorus) |
| 2 | Chorus | JS: Chorus | rate 0.35 Hz, depth 50% |
| 3 | Reverb | ReaVerb (File: load this .wav) | `Plate_2_Medium_Plate.wav` (Lexicon MPX100) |

## Pedal Starter Pack

### King of Tone → Deluxe Reverb

| # | Stage | Load / use | File or setting |
|---|---|---|---|
| 1 | Pedal | NAM (a second instance, before the amp) | `RED OD 2.nam` (ANALOGMAN KING OF TONE) |
| 2 | Amp | NAM (amp slot) | `Deluxe Reverb.nam` (Fender Deluxe Reverb (A2)) |
| 3 | Reverb | ReaVerb (File: load this .wav) | `Deluxe Medium.wav` (Deluxe Reverb Tank) |

### Klon Centaur → '62 Bassman

| # | Stage | Load / use | File or setting |
|---|---|---|---|
| 1 | Pedal | NAM (a second instance, before the amp) | `Klon 555.nam` (Klon Silver Centaur) |
| 2 | Amp | NAM (amp slot) | `62 Bassman 355.nam` (1962 Fender Bassman) |
| 3 | Cab | IR slot of the amp's NAM | `1966 Bassman Cabinet with Jensen C12N - SM57 - Cap Edge.wav` (1966 Fender Bassman Cabinet Jensen C12NA Speaker) |
| 4 | Reverb | ReaVerb (File: load this .wav) | `Fender Reverb Tank_Dwell 08_Tone 08.wav` (Fender Spring Reverb Tank) |

### TS808 → '68 Plexi

| # | Stage | Load / use | File or setting |
|---|---|---|---|
| 1 | Pedal | NAM (a second instance, before the amp) | `14-TS808_Hot_Lvl6_OD2_T2.nam` (Ibanez TS808 (Japan Reissue 2003)) |
| 2 | Amp | NAM (amp slot) | `MRSH SL68 I Drive BRI CAB.nam` (1968 Marshall Super Lead 12 000 Series Drive A2) |
| 3 | Reverb | ReaVerb (File: load this .wav) | `Plate_2_Medium_Plate.wav` (Lexicon MPX100) |

### Echoplex EP101 preamp → '68 Plexi

| # | Stage | Load / use | File or setting |
|---|---|---|---|
| 1 | Pedal | NAM (a second instance, before the amp) | `4. EP101 G5.nam` (Dunlop EP101 Echoplex Preamp) |
| 2 | Amp | NAM (amp slot) | `MRSH SL68 I Drive BRI CAB.nam` (1968 Marshall Super Lead 12 000 Series Drive A2) |
| 3 | Tape echo | ReaDelay | about 300 ms, 2-3 repeats, darkened (lowpass ~3 kHz), mix 20% |

### Boss CE-1 preamp + chorus → Deluxe

| # | Stage | Load / use | File or setting |
|---|---|---|---|
| 1 | Pedal | NAM (a second instance, before the amp) | `BOSS CE1 Low Input Gain 12 O'clock.nam` (BOSS CE 1 Chorus Ensemble 1970's (Dry) Pre Amp) |
| 2 | Amp | NAM (amp slot) | `Deluxe Reverb.nam` (Fender Deluxe Reverb (A2)) |
| 3 | Chorus | JS: Chorus | rate 0.3 Hz, depth 55% |
| 4 | Reverb | ReaVerb (File: load this .wav) | `Plate_2_Medium_Plate.wav` (Lexicon MPX100) |

### Boss DS-1 → JC-120

| # | Stage | Load / use | File or setting |
|---|---|---|---|
| 1 | Noise gate | the Noise Gate knob in NAM (or ReaGate) | threshold -60 dB |
| 2 | Pedal | NAM (a second instance, before the amp) | `Boss DS-1 T5_V10_G5.nam` (Boss DS-1 Distortion) |
| 3 | Amp | NAM (amp slot) | `Roland JC 120B Jazz Chorus- Bright Off, SM57.nam` (Roland JC 120B Jazz Chorus) |
| 4 | Reverb | ReaVerb (File: load this .wav) | `Plate_2_Medium_Plate.wav` (Lexicon MPX100) |

### ProCo RAT (vintage) → '62 Bassman

| # | Stage | Load / use | File or setting |
|---|---|---|---|
| 1 | Noise gate | the Noise Gate knob in NAM (or ReaGate) | threshold -60 dB |
| 2 | Pedal | NAM (a second instance, before the amp) | `ProCo Rat Vintage Reissue SS 02 D2F2V6.nam` (ProCo Rat Vintage Reissue) |
| 3 | Amp | NAM (amp slot) | `62 Bassman 355.nam` (1962 Fender Bassman) |
| 4 | Cab | IR slot of the amp's NAM | `1966 Bassman Cabinet with Jensen C12N - SM57 - Cap Edge.wav` (1966 Fender Bassman Cabinet Jensen C12NA Speaker) |
| 5 | Reverb | ReaVerb (File: load this .wav) | `Fender Reverb Tank_Dwell 08_Tone 08.wav` (Fender Spring Reverb Tank) |

### ProCo RAT 2 → JCM800

| # | Stage | Load / use | File or setting |
|---|---|---|---|
| 1 | Noise gate | the Noise Gate knob in NAM (or ReaGate) | threshold -60 dB |
| 2 | Pedal | NAM (a second instance, before the amp) | `ST_RAT_DIST-1100_FILTER-1300.nam` (Pro Co RAT 2) |
| 3 | Amp | NAM (amp slot) | `[AMP] JCM800-2203-MODIFIED-LO Edge of Breakup - SM58.nam` (Marshall JCM800 2203 Modified) |
| 4 | Reverb | ReaVerb (File: load this .wav) | `Plate_2_Medium_Plate.wav` (Lexicon MPX100) |

### Archer OD → AC15

| # | Stage | Load / use | File or setting |
|---|---|---|---|
| 1 | Pedal | NAM (a second instance, before the amp) | `5. J. Rockett Archer Gain 5 Output 5 Treble 5.nam` (J. Rockett Audio Designs Archer OD) |
| 2 | Amp | NAM (amp slot) | `Vox AC15CH Edge of Breakup Normal.nam` (Vox AC15) |
| 3 | Cab | IR slot of the amp's NAM | `TF 64 AC30 2X12 BLUE - 57 R121 70-30.wav` ('64 Vox AC30 Blue Alnicos 2x12 - XR) |
| 4 | Reverb | ReaVerb (File: load this .wav) | `Plate_2_Medium_Plate.wav` (Lexicon MPX100) |

### EP Booster → AC30

| # | Stage | Load / use | File or setting |
|---|---|---|---|
| 1 | Pedal | NAM (a second instance, before the amp) | `GP EP Booster 50 Vintage.nam` (Xotic EP Booster Pack) |
| 2 | Amp | NAM (amp slot) | `AC30-6 TB Brl 2.nam` ('02 Vox AC30-6 Top Boost) |
| 3 | Tape echo | ReaDelay | about 300 ms, 2-3 repeats, darkened (lowpass ~3 kHz), mix 15% |
| 4 | Reverb | ReaVerb (File: load this .wav) | `Plate_2_Medium_Plate.wav` (Lexicon MPX100) |

### JHS Bonsai (808) → Orange clean

| # | Stage | Load / use | File or setting |
|---|---|---|---|
| 1 | Pedal | NAM (a second instance, before the amp) | `Boost-808.nam` (JHS Bonsai Pack (9 Tube Screamers)) |
| 2 | Amp | NAM (amp slot) | `Orange Rockerverb MK3 - Clean - Canov+Arnold.nam` (Orange Rockerverb MK3 v2 (Canov+Arnold)) |
| 3 | Cab | IR slot of the amp's NAM | `Orange 2x12 V30 SM57 A.wav` (Orange 2x12 V30) |
| 4 | Reverb | ReaVerb (File: load this .wav) | `Hall_6_Medium_Hall.wav` (Lexicon MPX100) |

### Green Russian Big Muff → Two-Rock

| # | Stage | Load / use | File or setting |
|---|---|---|---|
| 1 | Noise gate | the Noise Gate knob in NAM (or ReaGate) | threshold -60 dB |
| 2 | Pedal | NAM (a second instance, before the amp) | `GreenRussian-08 5-5.nam` (Electro Harmonix - Green Russian Big Muff Pi) |
| 3 | Amp | NAM (amp slot) | `All 5s Traditional A1 Conversion.nam` (Two Rock Studio Signature + OX Box 2x12 Two Rock Cab (V2)) |
| 4 | Reverb | ReaVerb (File: load this .wav) | `Hall_6_Medium_Hall.wav` (Lexicon MPX100) |

### Fuzz Factory (experimental) → JC-120

| # | Stage | Load / use | File or setting |
|---|---|---|---|
| 1 | Pedal | NAM (a second instance, before the amp) | `Fuzz Factory V-4 G-6 C-8 D-5 S-5.nam` (ZVex Fuzz Factory Vexter (experimental)) |
| 2 | Amp | NAM (amp slot) | `Roland JC 120B Jazz Chorus- Bright Off, SM57.nam` (Roland JC 120B Jazz Chorus) |
| 3 | Reverb | ReaVerb (File: load this .wav) | `Plate_2_Medium_Plate.wav` (Lexicon MPX100) |

### Plasma (experimental) → AC15 clean

| # | Stage | Load / use | File or setting |
|---|---|---|---|
| 1 | Pedal | NAM (a second instance, before the amp) | `PlasmaPedal_Voltage_12oclk.nam` (Gamechanger Audio Plasma Pedal (experimental)) |
| 2 | Amp | NAM (amp slot) | `Vox AC15CH Crystal Clean Normal.nam` (Vox AC15) |
| 3 | Cab | IR slot of the amp's NAM | `TF 64 AC30 2X12 BLUE - 57 R121 70-30.wav` ('64 Vox AC30 Blue Alnicos 2x12 - XR) |
| 4 | Reverb | ReaVerb (File: load this .wav) | `Plate_2_Medium_Plate.wav` (Lexicon MPX100) |
