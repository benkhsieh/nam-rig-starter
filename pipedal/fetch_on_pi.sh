#!/bin/bash
# Download the manifest's NAM models and IRs into PiPedal's upload folders.
# Usage: fetch_on_pi.sh manifest.tsv
set -u
ROOT=/var/pipedal/audio_uploads
PACK="T3K Starter Pack"
STAGE=$(mktemp -d)
ok=0; skip=0; fail=0
while IFS=$'\t' read -r kind title name url; do
  case "$kind" in
    amp) dir="$ROOT/NeuralAmpModels/$PACK/$title" ;;
    pedal) dir="$ROOT/NeuralAmpModels/T3K Pedals/$title" ;;
    cab) dir="$ROOT/CabIR/$PACK/$title" ;;
    rev) dir="$ROOT/ReverbImpulseFiles/$PACK/$title" ;;
    *) continue ;;
  esac
  if sudo test -s "$dir/$name"; then skip=$((skip+1)); continue; fi
  if curl -fsS --retry 3 --retry-delay 2 --max-time 120 -o "$STAGE/f" "$url"; then
    sudo install -d -o pipedal_d -g pipedal_d -m 2775 "$dir"
    sudo install -o pipedal_d -g pipedal_d -m 664 "$STAGE/f" "$dir/$name"
    ok=$((ok+1))
  else
    echo "FAIL: $title / $name ($url)"; fail=$((fail+1))
  fi
  sleep 0.2
done < "$1"
rm -rf "$STAGE"
echo "downloaded=$ok skipped=$skip failed=$fail"
sudo du -sh "$ROOT/NeuralAmpModels/T3K Pedals" "$ROOT/NeuralAmpModels/$PACK" "$ROOT/CabIR/$PACK" "$ROOT/ReverbImpulseFiles/$PACK" 2>/dev/null
