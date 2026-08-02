# EU Industrial Energy Demand Analysis

Small Python project analyzing trends in final energy consumption across EU industry, broken down by energy product and sub-sector. Built as a quick exercise in working with energy economics statistics.

## Dataset

Source: [Eurostat](https://ec.europa.eu/eurostat) — "Final energy consumption in industry - detailed statistics" (dataset code `nrg_bal_s`), data extracted May 2026.

The dataset covers EU industrial final energy consumption by energy product (electricity, natural gas, solid fossil fuels, oil/petroleum, renewables, etc.) and by industrial sub-sector (chemicals, metals, food & beverages, etc.). Figures are in Petajoules (PJ). This project uses the two reference years Eurostat highlights in its summary article — 1990 and 2024 — to capture the long-term trend rather than a full year-by-year series.

Full dataset: https://ec.europa.eu/eurostat/databrowser/view/ten00124

## Project structure

```
.
├── data.py         # source data + citation
├── analysis.py     # % change / ranking calculations
├── visualize.py    # chart generation
├── main.py         # runs everything, prints summary
└── output/         # generated charts (created on run)
```

## Setup

```bash
pip install pandas matplotlib
```

## Usage

```bash
python main.py
```

This prints a summary of the trend to the console and saves three charts to `output/`:
- `product_change.png` — % change by energy product, 1990–2024
- `energy_mix_2024.png` — 2024 energy mix breakdown
- `top_sectors_2024.png` — top 5 industrial sub-sectors by energy consumption

## Example output

```
Total final energy consumption in EU industry fell from 12,795 PJ in 1990 to 8,835 PJ in 2024 (-30.9%).

By energy product, 1990 -> 2024:
  - Solid fossil fuels           -79.8%
  - Oil and petroleum products   -58.3%
  - Renewables and biofuels      +101.0%
```

## Notes

- Data is hardcoded in `data.py` rather than fetched via API, since this was built as a quick standalone exercise. Swapping in a full CSV from the Eurostat database browser would just mean replacing the DataFrames in `data.py` — the analysis and visualization functions take any DataFrame with the right columns.
- Only two years (1990, 2024) are used because that's what Eurostat's summary article reports directly; a full annual series would need to be pulled separately.