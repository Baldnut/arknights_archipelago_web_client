import json
from pathlib import Path

base = Path(__file__).resolve().parent
json_path = base / "character_table.json"

with json_path.open("r", encoding="utf-8") as f:
    data = json.load(f)

# name -> object key
# Also keep the object ID itself available as a lookup key, since some entries
# like char_264_f12yin are referenced by ID rather than display name.
name_to_object_id = {}
for obj_id, entry in data.items():
    if not isinstance(entry, dict):
        continue

    if entry.get("name"):
        name_to_object_id.setdefault(entry["name"].strip().lower(), obj_id)

    #name_to_object_id.setdefault(obj_id, obj_id)

# optional: save it to a file
mapping_path = base / "name_to_object_id.json"
with mapping_path.open("w", encoding="utf-8") as f:
    json.dump(name_to_object_id, f, ensure_ascii=False, indent=2)

print(name_to_object_id.get("Lancet-2"))
print(name_to_object_id.get("Castle-3"))
print(name_to_object_id.get("Suzuran"))
print(name_to_object_id.get("Mountain"))