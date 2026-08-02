# EU Industrial Energy Demand: Trend Analysis

Small exercise mirroring the core task loop described in the IIP Chair of
Energy Economics HiWi posting: pull energy economics statistics, process
them, compute a trend, and visualize the result.

## Structure
- `data.py` -- source data, taken from Eurostat's published statistics
  (see comments in the file for the exact source and why only two years
  are used).
- `analysis.py` -- reusable functions for computing % change and rankings.
- `visualize.py` -- chart-building functions, kept separate from analysis.
- `main.py` -- ties it together, prints a written interpretation, and
  saves charts to `output/`.

## Run it
```
pip install pandas matplotlib
python main.py
```

## How to explain this in an interview (read this before you send your CV)
Be ready to answer, in your own words:
1. **Where did the numbers come from?** Eurostat's "Final energy
   consumption in industry" article (nrg_bal_s dataset). You used the
   two endpoint years (1990, 2024) that Eurostat itself highlights,
   not a full manually-downloaded series.
2. **What does the main chart show?** Which energy products grew and
   which shrank in EU industry between 1990 and 2024, as a percentage
   change -- not absolute PJ, so very different-sized fuels are
   comparable.
3. **Why does the interpretation matter?** Total consumption fell ~31%
   overall, but that single number hides very different stories per
   fuel: fossil fuels collapsed, renewables roughly doubled (from a
   smaller base). This is the kind of nuance that matters for
   decarbonization scenario modeling -- the actual research area in
   the job posting.
4. **What would you do with more time/access?** Pull the full annual
   series (not just two years) from Eurostat's database browser
   (dataset code `nrg_bal_s` or `ten00124`), to see the year-by-year
   path instead of just two endpoints -- and break it down by country
   instead of EU-aggregate.

## Extending it yourself (do this before the interview if you can)
1. Go to https://ec.europa.eu/eurostat/databrowser/view/ten00124
2. Filter to "Industry" sector, export as CSV
3. Load it with `pandas.read_csv()` in place of the dict in `data.py`
4. Re-run `main.py` -- the analysis/visualize functions don't need to
   change at all, since they were written to take any dataframe with
   the right column names. That's the point of keeping them modular.
