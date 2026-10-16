"""Merge all CSV exports in a folder into one Excel workbook.
Usage: python merge_reports.py input/ merged.xlsx
- normalizes differing headers (SKU/sku/Item SKU, Units/units sold/Qty)
- adds a 'source_file' column, totals per SKU in a Summary sheet"""
import sys, pathlib, pandas as pd
ALIASES={"sku":"sku","item sku":"sku","product":"product","product name":"product",
         "units":"units","units sold":"units","qty":"units"}
def load(p):
    df=pd.read_csv(p); df.columns=[ALIASES.get(c.strip().lower(),c.strip().lower()) for c in df.columns]
    df["source_file"]=p.name; return df
src=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else "input")
out=sys.argv[2] if len(sys.argv)>2 else "merged.xlsx"
files=sorted(src.glob("*.csv"))
if not files: sys.exit(f"No CSV files in {src}")
all_=pd.concat([load(f) for f in files],ignore_index=True)
summary=all_.groupby("sku",as_index=False)["units"].sum().sort_values("units",ascending=False)
with pd.ExcelWriter(out,engine="openpyxl") as xw:
    all_.to_excel(xw,sheet_name="All_Rows",index=False)
    summary.to_excel(xw,sheet_name="Summary_by_SKU",index=False)
print(f"Merged {len(files)} files, {len(all_)} rows -> {out}")
