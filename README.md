# 📊 US Data: Inflation, Presidents, and Economic Trends

**Author:** Alex Murray (@wizrdcodes)  
**Language:** Python (pandas, matplotlib, numpy)

---

## 🧠 Overview

This project explores **US inflation data since 1976**, aligning annual inflation rates with **presidential terms** to visualize economic trends by political party.

The analysis uses public CPI data and presidential term information to calculate annual inflation rates, merge them by year, and color-code results by party affiliation for clear visual storytelling.

---

## 🧩 Features

- **Data Cleaning & Transformation**
  - Reads monthly CPI data and aggregates to annual inflation rates.
  - Parses and expands presidential terms (e.g., `1977–1981`) into individual years.
  - Merges inflation and presidency data into a single analysis dataset.

- **Visualization**
  - Plots inflation rate vs. year using `matplotlib`.
  - Colors points by political party (`blue` = Democrat, `red` = Republican).
  - Optionally saves output to `/output` as a `.png`.

- **Reproducible Structure**
  - `/data` — CSV input files  
  - `/src` — source code for analysis and plotting  
  - `/output` — generated graphs  
  - `.gitignore` — excludes private or unnecessary files  
  - `requirements.txt` — library dependencies

---

## 🧰 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
