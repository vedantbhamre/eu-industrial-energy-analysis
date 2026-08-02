"""

All figures below are taken directly from Eurostat's published article
"Final energy consumption in industry - detailed statistics" (data extracted
May 2026), based on the nrg_bal_s dataset:
https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Final_energy_consumption_in_industry_-_detailed_statistics

"""

import pandas as pd


ENERGY_PRODUCT_TRENDS = pd.DataFrame([
    {"energy_product": "Solid fossil fuels",     "pj_1990": 2395, "pj_2024": 484},
    {"energy_product": "Oil and petroleum products", "pj_1990": 2212, "pj_2024": 922},
    {"energy_product": "Renewables and biofuels", "pj_1990": 497,  "pj_2024": 999},
])

# Total EU industry final energy consumption, PJ
TOTAL_CONSUMPTION = {
    "1990": 12795,
    "2024": 8835,
}

# 2024 breakdown by energy product, % share of total (as directly reported)
ENERGY_MIX_2024 = pd.DataFrame([
    {"energy_product": "Electricity", "share_pct": 33.3},
    {"energy_product": "Natural gas", "share_pct": 31.9},
    {"energy_product": "Renewables and biofuels", "share_pct": 11.3},
    {"energy_product": "Oil and petroleum products", "share_pct": 10.4},
    {"energy_product": "Solid fossil fuels", "share_pct": 5.5},
    {"energy_product": "Derived heat", "share_pct": 5.5},
    {"energy_product": "Non-renewable waste", "share_pct": 2.1},
])

# Top industrial sub-sectors by final energy consumption, EU, 2024, PJ
TOP_SECTORS_2024 = pd.DataFrame([
    {"sector": "Chemical and petrochemical", "pj_2024": 1888},
    {"sector": "Non-metallic minerals", "pj_2024": 1157},
    {"sector": "Food, beverages and tobacco", "pj_2024": 1134},
    {"sector": "Paper, pulp and printing", "pj_2024": 997},
    {"sector": "Iron and steel", "pj_2024": 860},
])
