import csv
import json
import re
import pathlib

def normalize_spaces(s):
    if s is None: 
        return None
    return " ".join(s.strip().split())

def normalize_emails(s):
    if "@" not in s: 
        return None
    if s is None:
        return None
    return s.lower().strip()

def slugify(name):
    if name is None:
        return None
    return "".join(re.findall("[a-z0-9-]", "-".join(name.lower().strip().split())))

def row_to_record(row):
    return {
        "id": int(row["id"]),
        "name": normalize_spaces(row["full_name"]),
        "email": normalize_emails(row["email"]),
        "city": normalize_spaces(row["city"]),
        "slug": slugify(row["full_name"])
    }

def convert_csv_to_json(in_path, out_path):
    with open(in_path, "r", newline="") as f:
        rows = csv.DictReader(f)
        rows_to_json = [row_to_record(row) for row in rows]
        with open(out_path, "w") as j:
            json.dump(rows_to_json, j, ensure_ascii=False, indent=2)

convert_csv_to_json(pathlib.Path("data/input.csv"),pathlib.Path("out/output.json"))