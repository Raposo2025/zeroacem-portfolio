# Projeto Zero a Cem

GitHub Pages guide for the digital products sold on Payhip: [payhip.com/ZeroaCem](https://payhip.com/ZeroaCem).

This repository explains the files and links out to Payhip. It is not a checkout. There is no payment form, and the old fixed-price spreadsheet service is not for sale here.

## Products

| Product | Pro | Lite (free) |
| --- | --- | --- |
| Small-Business Budget & Cash-Flow Tracker | [US$9](https://payhip.com/b/GpayP) | [Free](https://payhip.com/b/O0UrB) |
| Invoice + Client & Payment Tracker | [US$12](https://payhip.com/b/jd4yg) | [Free](https://payhip.com/b/6BsCa) |
| Data Cleaner for CSV/Excel (Python) | [US$15](https://payhip.com/b/3awQx) | [Free](https://payhip.com/b/v26Fz) |

The workbooks are bookkeeping aids for Excel, LibreOffice Calc, and Google Sheets. The cleaner is a local Python script (3.8+ and pandas for Pro). They were made with AI assistance. Mario Raposo is responsible for what is published. This is not accounting, tax, or legal advice. Sample data is fictional.

Custom one-off cleanup may be offered again later. It is not sold on this site.

Contact: [zeroacem@mail.grokbot.com](mailto:zeroacem@mail.grokbot.com)

## Portfolio demos (synthetic data only, no real client data)

These folders are proof of the cleanup approach. They are not the Payhip downloads.

### Ex1 — Messy CSV → clean Excel (`ex1_csv_cleanup/`)

- Before: `messy_sales.csv` (65 rows: 5 duplicates, inconsistent names/case/spaces, 3 date formats, "$"/"USD" in amounts, blank qty).
- After: `clean_sales.xlsx` — Data sheet (normalized, sorted, header styled, filter, frozen header, `line_total` formula, SUM/AVERAGE/SUMIF KPIs), `Pivot_Customer_Region`, `Change_Log` (65 in, 5 dups removed, 60 out, 14 blank qty set to 1 and flagged).
- Reproduce: `python3 make_messy.py && python3 clean.py`. Verified 2026-10-15: LibreOffice headless opened it and computed formulas (Total revenue 57,590.74).

### Ex2 — Python script merging differing CSV exports (`ex2_merge_script/`)

- Before: 3 store CSVs with different headers (SKU/sku/Item SKU; Units/units sold/Qty).
- After: `merge_reports.py input merged.xlsx` → `merged.xlsx` (All_Rows with source_file + Summary_by_SKU), PDF preview `merged.pdf`. Verified: 3 files, 45 rows.
