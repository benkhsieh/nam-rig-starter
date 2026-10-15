#!/usr/bin/env python3
"""Build the "Pedal Starter Pack" PiPedal bank: each pedal capture in front of an amp that suits it."""
from t3k_presets import *

def pedal(tone, model, inputGain=0, outputGain=0):
    it = item(NAM_URI, inputGain=inputGain, outputGain=outputGain, gate=-80)
    it["title"] = tone.replace(" (experimental)", "")
    return with_file(it, NAM_URI + "#modelFile", f"NeuralAmpModels/T3K Pedals/{tone}/{model}")

# Amp platforms (model, plus cab when the capture is amp-only)
def deluxe():
    return [nam("Fender Deluxe Reverb (A2)", "Deluxe Reverb.nam")]
def bassman_clean():
    return [nam("1962 Fender Bassman", "62 Bassman 355.nam"), cab(*BASSMAN_CAB)]
def plexi():
    return [nam("1968 Marshall Super Lead 12 000 Series Drive A2", "MRSH SL68 I Drive BRI CAB.nam")]
def jc120():
    return [nam("Roland JC 120B Jazz Chorus", "Roland JC 120B Jazz Chorus- Bright Off, SM57.nam")]
def ac15(model="Vox AC15CH Edge of Breakup Normal.nam"):
    return [nam("Vox AC15", model), cab("'64 Vox AC30 Blue Alnicos 2x12 - XR", "TF 64 AC30 2X12 BLUE - 57 R121 70-30.wav")]
def ac30():
    return [nam("'02 Vox AC30-6 Top Boost", "AC30-6 TB Brl 2.nam")]
def orange_clean():
    return [nam("Orange Rockerverb MK3 v2 (Canov+Arnold)", "Orange Rockerverb MK3 - Clean - Canov+Arnold.nam"),
            cab("Orange 2x12 V30", "Orange 2x12 V30 SM57 A.wav")]
def jcm800_edge():
    return [nam("Marshall JCM800 2203 Modified", "[AMP] JCM800-2203-MODIFIED-LO Edge of Breakup - SM58.nam")]
def tworock_clean():
    return [nam("Two Rock Studio Signature + OX Box 2x12 Two Rock Cab (V2)", "All 5s Traditional A1 Conversion.nam")]

presets = [
    preset("King of Tone → Deluxe Reverb", [pedal("ANALOGMAN KING OF TONE", "RED OD 2.nam"), *deluxe(), reverb(*DLX_SPRING, mix_db=-15)]),
    preset("Klon Centaur → '62 Bassman", [pedal("Klon Silver Centaur", "Klon 555.nam"), *bassman_clean(), reverb(*SPRING, mix_db=-15)]),
    preset("TS808 → '68 Plexi", [pedal("Ibanez TS808 (Japan Reissue 2003)", "14-TS808_Hot_Lvl6_OD2_T2.nam"), *plexi(), reverb(*PLATE, mix_db=-20)]),
    preset("Echoplex EP101 preamp → '68 Plexi", [pedal("Dunlop EP101 Echoplex Preamp", "4. EP101 G5.nam"), *plexi(), tape("Classic Tape Echo", mix=0.2)]),
    preset("Boss CE-1 preamp + chorus → Deluxe", [pedal("BOSS CE 1 Chorus Ensemble 1970's (Dry) Pre Amp", "BOSS CE1 Low Input Gain 12 O'clock.nam"),
                                                *deluxe(), item("chorus", rate=0.3, depth=0.55, dryWet=1.0), reverb(*PLATE, mix_db=-20)]),
    preset("Boss DS-1 → JC-120", [item("gate", threshold=-60.0), pedal("Boss DS-1 Distortion", "Boss DS-1 T5_V10_G5.nam"), *jc120(), reverb(*PLATE, mix_db=-20)]),
    preset("ProCo RAT (vintage) → '62 Bassman", [item("gate", threshold=-60.0), pedal("ProCo Rat Vintage Reissue", "ProCo Rat Vintage Reissue SS 02 D2F2V6.nam"), *bassman_clean(), reverb(*SPRING, mix_db=-18)]),
    preset("ProCo RAT 2 → JCM800", [item("gate", threshold=-60.0), pedal("Pro Co RAT 2", "ST_RAT_DIST-1100_FILTER-1300.nam"), *jcm800_edge(), reverb(*PLATE, mix_db=-20)]),
    preset("Archer OD → AC15", [pedal("J. Rockett Audio Designs Archer OD", "5. J. Rockett Archer Gain 5 Output 5 Treble 5.nam"), *ac15(), reverb(*PLATE, mix_db=-18)]),
    preset("EP Booster → AC30", [pedal("Xotic EP Booster Pack", "GP EP Booster 50 Vintage.nam"), *ac30(), tape("Classic Tape Echo", mix=0.15), reverb(*PLATE, mix_db=-20)]),
    preset("JHS Bonsai (808) → Orange clean", [pedal("JHS Bonsai Pack (9 Tube Screamers)", "Boost-808.nam"), *orange_clean(), reverb(*HALL, mix_db=-20)]),
    preset("Green Russian Big Muff → Two-Rock", [item("gate", threshold=-60.0), pedal("Electro Harmonix - Green Russian Big Muff Pi", "GreenRussian-08 5-5.nam"), *tworock_clean(), reverb(*HALL, mix_db=-20)]),
    preset("Fuzz Factory (experimental) → JC-120", [pedal("ZVex Fuzz Factory Vexter (experimental)", "Fuzz Factory V-4 G-6 C-8 D-5 S-5.nam"), *jc120(), reverb(*PLATE, mix_db=-20)]),
    preset("Plasma (experimental) → AC15 clean", [pedal("Gamechanger Audio Plasma Pedal (experimental)", "PlasmaPedal_Voltage_12oclk.nam"), *ac15("Vox AC15CH Crystal Clean Normal.nam"), reverb(*PLATE, mix_db=-20)]),
]

write_bank("Pedal Starter Pack", presets, "Pedal+Starter+Pack.bank")
