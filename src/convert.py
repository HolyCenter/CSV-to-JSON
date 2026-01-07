import csv
import json
import re
import pathlib
import argparse

def normalize_spaces(s):
    if s is None: 
        return None
    return " ".join(s.strip().split())

def normalize_emails(s):
    if s is None:
        return None
    if "@" not in s: 
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
    with open(in_path, "r", newline="", encoding="utf-8") as f:
        rows = csv.DictReader(f)
        rows_to_json = [row_to_record(row) for row in rows]
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as j:
            json.dump(rows_to_json, j, ensure_ascii=False, indent=2)

def main():
    parser = argparse.ArgumentParser(description="Take an input-csv and create a clean output-json.")
    parser.add_argument("--input", type=pathlib.Path, required=True)
    parser.add_argument("--output", type=pathlib.Path, required=True)
    args = parser.parse_args()
    convert_csv_to_json(args.input, args.output)

if __name__ == "__main__":
    main()