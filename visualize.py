import matplotlib.pyplot as plt


def plot_product_change(df, out_path):
    df_sorted = df.sort_values("pct_change")
    colors = ["#c0392b" if v < 0 else "#27ae60" for v in df_sorted["pct_change"]]

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.barh(df_sorted["energy_product"], df_sorted["pct_change"], color=colors)
    ax.axvline(0, color="black", linewidth=0.8)
    ax.set_xlabel("% change, 1990 to 2024")
    ax.set_title("EU Industry Final Energy Consumption by Product\n(% change, 1990\u20132024)")

    for bar, val in zip(bars, df_sorted["pct_change"]):
        x = bar.get_width()
        align = "left" if x >= 0 else "right"
        offset = 2 if x >= 0 else -2
        ax.text(x + offset, bar.get_y() + bar.get_height() / 2, f"{val:+.1f}%",
                 va="center", ha=align, fontsize=9)

    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def plot_2024_mix(df, out_path):
    df_sorted = df.sort_values("share_pct", ascending=True)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(df_sorted["energy_product"], df_sorted["share_pct"], color="#2980b9")
    ax.set_xlabel("% share of total final energy consumption")
    ax.set_title("EU Industry Energy Mix, 2024")

    for i, val in enumerate(df_sorted["share_pct"]):
        ax.text(val + 0.3, i, f"{val}%", va="center", fontsize=9)

    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def plot_top_sectors(df, out_path):
    df_sorted = df.sort_values("pj_2024", ascending=True)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(df_sorted["sector"], df_sorted["pj_2024"], color="#8e44ad")
    ax.set_xlabel("Final energy consumption, 2024 (PJ)")
    ax.set_title("Top 5 EU Industrial Sub-Sectors by Energy Consumption, 2024")

    for i, val in enumerate(df_sorted["pj_2024"]):
        ax.text(val + 15, i, f"{val:,.0f}", va="center", fontsize=9)

    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
