import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from load_csv import load


def convert_population(pop_str: str):
    """
    Converts a population string with an optional 'M' suffix to a float.
    For example, '29M' becomes 29000000.0 and '29.1M' becomes 29100000.0.
    """
    if isinstance(pop_str, str) and 'M' in pop_str:
        return float(pop_str.replace('M', '')) * 1_000_000
    return pd.to_numeric(pop_str, errors='coerce')


def draw_graph(path: str, campus_country: str, compare_country: str) -> None:
    """Compares data for 2 different country for their population"""
    population = load(path)
    if population is None:
        print(f"Couldn't load data from {path}")
        return
    if not isinstance(campus_country, str):
        print(f"'{campus_country}' should be a string parameter")
        return
    countries_to_plot = population[population["country"].isin(
        [campus_country,
         compare_country]
    )]
    if countries_to_plot.empty:
        print("Provided countries: are not part of CSV file")
        return
    print(countries_to_plot)
    # Drop the 'country' column for a cleaner plot and melt to long format
    plot_data = countries_to_plot.melt(
        id_vars=["country"],
        var_name="Year",
        value_name="Population",
    )
    # Convert 'Year' to integer
    plot_data['Year'] = pd.to_numeric(plot_data['Year'], errors='coerce')
    plot_data = plot_data.dropna(subset=['Year'])
    plot_data['Year'] = plot_data['Year'].astype(int)
    # Apply the custom conversion function to the 'Population' column
    plot_data['Population'] = plot_data['Population'].apply(convert_population)
    plot_data = plot_data.dropna(subset=['Population'])
    # Filter data to the desired year range
    plot_data = plot_data[(plot_data['Year'] >= 1800)
                          & (plot_data['Year'] <= 2050)]
    country_colors = ["blue", "green"]
    # Create the plot using seaborn
    sns.lineplot(
        data=plot_data,
        x="Year",
        y="Population",
        hue="country",
        palette=country_colors,
        hue_order=[campus_country, compare_country],
    )
    plt.title(f"Population Comparison: {campus_country} vs {compare_country}")
    plt.ylim(0, 70_000_000)
    plt.yticks(range(20_000_000, 70_000_000, 20_000_000))
    plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(
        lambda x,
        p: f'{x/1_000_000:.0f}M'
    ))
    plt.xlim(1785, 2060)
    plt.xticks(range(1800, 2060, 40))
    plt.legend(loc='lower right')
    plt.show()


def main():
    """Main Entrypoint for aff_life"""
    try:
        draw_graph("population_total.csv", "Belgium", "France")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
