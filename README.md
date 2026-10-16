# Portfolio demo — Zero a Cem (synthetic data only, no real client data)
## Ex1 — Messy CSV -> clean Excel (ex1_csv_cleanup/)
- Before: `messy_sales.csv` (65 rows: 5 duplicates, inconsistent names/case/spaces, 3 date formats, "$"/"USD" in amounts, blank qty).
- After: `clean_sales.xlsx` — Data sheet (normalized, sorted, header styled, filter, frozen header, `line_total` formula, SUM/AVERAGE/SUMIF KPIs), `Pivot_Customer_Region`, `Change_Log` (65 in, 5 dups removed, 60 out, 14 blank qty set to 1 and flagged).
- Reproduce: `python3 make_messy.py && python3 clean.py`. Verified 2026-10-15: LibreOffice headless opened it and computed formulas (Total revenue 57,590.74).
## Ex2 — Python script merging differing CSV exports (ex2_merge_script/)
- Before: 3 store CSVs with different headers (SKU/sku/Item SKU; Units/units sold/Qty).
- After: `merge_reports.py input merged.xlsx` -> `merged.xlsx` (All_Rows with source_file + Summary_by_SKU), PDF preview `merged.pdf`. Verified: 3 files, 45 rows.
