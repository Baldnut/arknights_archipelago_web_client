import json, sys
from pathlib import Path

base = Path(__file__).resolve().parent
json_path = Path(sys.argv[1])
avatar_base = Path(sys.argv[2])

with json_path.open("r", encoding="utf-8") as f:
    data = json.load(f)

for obj_id, entry in data.items():
    if not isinstance(entry, dict):
        continue
    if entry["itemObtainApproach"] == None:
        continue

    match obj_id:
        case "char_271_spikes":
            path = avatar_base / "elite" / "char_271_spikes.png"
        case _:
            path = avatar_base / f"{obj_id}.png"

    path.copy(base / "img" / "avatars" / f"{entry["name"].strip().lower()}.png")