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
        "id": int(row[0]),
        "name": normalize_spaces(row[1]),
        "email": normalize_emails(row[2]),
        "city": normalize_spaces(row[3]),
        "slug": slugify(row[1])
    }

def convert_csv_to_json(in_path, out_path):
    with open(in_path, "r") as f:
        next(f)
        rows = csv.reader(f)
        rows_to_json = [row_to_record(row) for row in rows]
        with open(out_path, "w") as j:
            json.dump(rows_to_json, j)

convert_csv_to_json(pathlib.Path("data/input.csv"),pathlib.Path("out/output.json"))