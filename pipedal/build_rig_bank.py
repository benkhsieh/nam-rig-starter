#!/usr/bin/env python3
"""Build the "Rig Starter Pack" PiPedal bank."""
from t3k_presets import *

def echoplex_preamp():
    """EVH ran an Echoplex EP-3 as an always-on preamp; the EP101 is Dunlop's pedal version of that circuit."""
    it = item(NAM_URI, gate=-80)
    it["title"] = "Echoplex EP101 preamp"
    return with_file(it, NAM_URI + "#modelFile", "NeuralAmpModels/T3K Pedals/Dunlop EP101 Echoplex Preamp/4. EP101 G5.nam")

presets = [
    preset("Setzer — '62 Blonde Bassman + Space Echo", [
        nam("Roland Space Echo RE-201", "RE-201 Instrument Level 5.nam"),
        nam("Fender Blonde Bassman Edge BAL DI", "Fender BL Bassman Edge FAT DI.nam"),
        cab(*BASSMAN_CAB),
        tape("Rockabilly Guitar"),
        reverb(*SPRING, mix_db=-18),
    ]),
    preset("'62 Fender Bassman", [
        nam("1962 Fender Bassman", "62 Bassman 755.nam"),
        cab(*BASSMAN_CAB),
        item("trem", enabled=False, rate=5.0, depth=0.5),
        reverb(*SPRING, mix_db=-15),
    ]),
    preset("Fender Deluxe Reverb", [
        nam("Fender Deluxe Reverb (A2)", "Deluxe Reverb.nam"),
        item("gxtrem", enabled=False, dry_wet=100.0, depth=0.5, freq=5.0),
        reverb(*DLX_SPRING, mix_db=-12),
    ]),
    preset("Fender Vibrolux Reverb", [
        nam("Fender Custom Vibrolux Reverb Amp", "Fender Custom Vibrolux 90s, Vol 2.7, Treb 5.5, Bass 6.2 e906.nam"),
        item("gxtrem", enabled=True, dry_wet=100.0, depth=0.45, freq=4.5),
        reverb(*SPRING, mix_db=-12),
    ]),
    preset("Vox AC30 Top Boost", [
        nam("'02 Vox AC30-6 Top Boost", "AC30-6 TB Brl 3.nam"),
        item("trem", enabled=False, rate=6.0, depth=0.5),
        reverb(*PLATE, mix_db=-15),
    ]),
    preset("Orange Rockerverb", [
        item("gate", threshold=-60.0),
        nam("Orange Rockerverb MK3 v2 (Canov+Arnold)", "Orange Rockerverb MK3 - Crunch G5 - Canov+Arnold.nam"),
        cab("Orange 2x12 V30", "Orange 2x12 V30 SM57 A.wav"),
        reverb(*HALL, mix_db=-18),
    ]),
    preset("Dumble-style ODS (Two-Rock)", [
        nam("Two Rock Studio Signature + OX Box 2x12 Two Rock Cab (V2)", "BMD G5 T5M5B5 Vol7 P5 BF A1 Conversion.nam"),
        item("delay", enabled=True, delay=380.0, level=18.0, feedback=25.0),
        reverb(*PLATE, mix_db=-15),
    ]),
    preset("Mesa Dual Rectifier", [
        item("gate", threshold=-55.0),
        nam("Mesa Dual Rectifier MW Red Modern - Mesa 4x12 - Full Rig", "FR MBDR MW Red Mdn - 3 - 4FB UR SM57a.nam"),
    ]),
    preset("Van Halen — '68 Plexi Brown", [
        nam("1968 Marshall Super Lead 12 000 Series Drive A2", "MRSH SL68 I Drive BRI CAB.nam"),
        item("phaser", enabled=False, rate=0.45, dryWet=1.0),
        tape("Classic Tape Echo", mix=0.2),
    ]),
    preset("Van Halen — Eruption (Variac Plexi)", [
        echoplex_preamp(),
        # 170 V of 230 V mains ~= the ~90 V of 120 V EVH dialed in on his variac, amp dimed
        nam("Marshall 1959HW Plexi Variac [Hyper Accuracy]", "SLAMMIN_MARSHALL_1959HW_170V_DIMED_10_S.nam"),
        cab("UK Greenback - Marshall 1960TV 4x12 M201", "M25 UL 1960TV 4x12 M201 1.50in 0.0in SA73.wav"),
        item("phaser", enabled=True, rate=0.3, dryWet=1.0),  # MXR Phase 90, slow sweep
        tape("Classic Tape Echo", mix=0.2),
        reverb(*PLATE, mix_db=-22),
    ]),
    preset("Van Halen — 5150", [
        item("gate", threshold=-55.0),
        nam("1992 Peavey 5150 Block Letter - Mesa OS 412 Full Rig", "1992 Peavey 5150 Block Letter - Mesa OS 412 Full Rig (@vivahatex).nam"),
        reverb(*PLATE, mix_db=-20),
    ]),
    preset("Slash — Appetite #36", [
        item("wah", enabled=False),
        nam("Marshall 1959 BRBS SIR #36 Slash [Standard]", "SLAMMIN_PLEXI_BRBS_SIR_#36_LG_MV3_SLASH_S.nam"),
        cab("UK Greenback - Marshall 1960TV 4x12 M201", "M25 UL 1960TV 4x12 M201 1.50in 0.0in SA73.wav"),
        item("delay", enabled=True, delay=420.0, level=15.0, feedback=20.0),
        reverb(*PLATE, mix_db=-20),
    ]),
    preset("Roland JC-120 Jazz Chorus", [
        nam("Roland JC 120B Jazz Chorus", "Roland JC 120B Jazz Chorus- Bright Off, SM57.nam"),
        item("chorus", rate=0.35, depth=0.5, dryWet=1.0),
        reverb(*PLATE, mix_db=-20),
    ]),
]

write_bank("Rig Starter Pack", presets, "Rig+Starter+Pack.bank")
