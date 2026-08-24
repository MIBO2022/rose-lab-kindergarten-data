#!/usr/bin/env python3
from pathlib import Path
import shutil, sys, json

SRC = Path("_source/docs/data/slip114")
DST = Path("docs/data/slip114")

if not SRC.exists():
    raise SystemExit(f"Missing source directory: {SRC}")

if DST.exists():
    shutil.rmtree(DST)
DST.parent.mkdir(parents=True, exist_ok=True)

# 完整複製來源 slip114 目錄：
# 學年度 → 縣市 → 每間園所一個 JSON
shutil.copytree(SRC, DST)

# 基本驗證
county_dirs = [p for p in DST.iterdir() if p.is_dir()]
json_files = list(DST.rglob("*.json"))

print(f"Counties: {len(county_dirs)}")
print(f"School JSON files: {len(json_files)}")

if len(json_files) < 1000:
    raise SystemExit("Unexpectedly few JSON files; stop to avoid committing incomplete data.")

# 產生簡單索引，不改任何逐園 JSON 內容
index = {
    "academic_year": "114",
    "structure": "academic_year/county/school.json",
    "source": {
        "publisher": "教育部",
        "dataset": "全國教保資訊網－幼兒園收費明細",
        "archive_acquisition": "kiang/ap.ece.moe.edu.tw"
    },
    "counties": []
}

for county in sorted(county_dirs, key=lambda p: p.name):
    files = sorted(county.glob("*.json"))
    index["counties"].append({
        "county": county.name,
        "school_count": len(files)
    })

index["school_count"] = len(json_files)

index_path = Path("docs/data/slip114-index.json")
index_path.write_text(
    json.dumps(index, ensure_ascii=False, indent=2),
    encoding="utf-8"
)

print(f"Index written to: {index_path}")
