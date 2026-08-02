import os
from data import ENERGY_PRODUCT_TRENDS, TOTAL_CONSUMPTION, ENERGY_MIX_2024, TOP_SECTORS_2024
from analysis import add_percent_change, rank_by_change, total_decline_summary
from visualize import plot_product_change, plot_2024_mix, plot_top_sectors

OUTPUT_DIR = "output"


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    product_trends = add_percent_change(ENERGY_PRODUCT_TRENDS, "pj_1990", "pj_2024")
    product_trends = rank_by_change(product_trends)
    overall = total_decline_summary(TOTAL_CONSUMPTION)

    plot_product_change(product_trends, os.path.join(OUTPUT_DIR, "product_change.png"))
    plot_2024_mix(ENERGY_MIX_2024, os.path.join(OUTPUT_DIR, "energy_mix_2024.png"))
    plot_top_sectors(TOP_SECTORS_2024, os.path.join(OUTPUT_DIR, "top_sectors_2024.png"))

    print("EU INDUSTRY FINAL ENERGY CONSUMPTION -- SUMMARY")
    print(
        f"\nTotal final energy consumption in EU industry fell from "
        f"{overall['start_pj']:,} PJ in {overall['start_year']} to "
        f"{overall['end_pj']:,} PJ in {overall['end_year']} "
        f"({overall['pct_change']}%)."
    )
    print("\nBy energy product, 1990 -> 2024:")
    for _, row in product_trends.iterrows():
        print(f"  - {row['energy_product']:<28} {row['pct_change']:+.1f}%")

    
    print(f"\nCharts saved to ./{OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
