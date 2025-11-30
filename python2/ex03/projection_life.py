import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from ..ex01.load_csv import load


def draw_graph(income_csv: str, life_csv) -> None:
    income_df = load(income_csv)
    life_df = load(life_csv)
    if income_df is None or life_df is None:
        print("Couldn't load data")
        return
    year = "1900"
    income = income_df[["country", year]].rename(columns={year: "income"})
    life = life_df[["country", year]].rename(columns={year: "life"})
    if income is None or life is None:
        print("Corrupted data")
        return
    merged_df = income.merge(life, on="country")
    merged_df[['income', 'life']] = merged_df[['income', 'life']].apply(
        pd.to_numeric, errors="coerce"
    )
    merged_df = merged_df.dropna(subset=['income', 'life']).astype({
        "income": int,
        "life": int
    })
    sns.scatterplot(
        data=merged_df,
        x="income",
        y="life",
        color="steelblue"
    )
    # log-scale for GDP
    plt.xscale("log")
    plt.xlabel("Gross Domestic Product")
    plt.ylabel("Life Expectancy")
    plt.yticks(range(20, 60, 5))
    plt.xticks([300, 1_000, 10_000])
    plt.gca().get_xaxis().set_major_formatter(plt.FuncFormatter(
        lambda x, p: f'{x/1_000:.0f}k' if x >= 1_000 else f'{x:.0f}'
    ))
    plt.title("1900")
    plt.show()
    # print(merged_df)


def main():
    """Main Entrypoing for projection_life"""
    path = "python2/ex03/"
    income = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    income_path = path + income
    life_path = path + "life_expectancy_years.csv"
    draw_graph(income_path, life_path)
    # draw_graph("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")


if __name__ == "__main__":
    main()
