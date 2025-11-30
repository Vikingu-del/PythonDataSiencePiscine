import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from load_csv import load


def draw_graph(path: str, place: str) -> None:
    # Apply the default theme
    # sns.set_theme()
    life_expentancy = load(path)
    if life_expentancy is None:
        print(f"Couldn't load data from {path}")
        return
    if not isinstance(place, str):
        print(f"'{place}' should be a string parameter")
        return
    print(life_expentancy)
    # campus_country = life_expentancy[life_expentancy["country"] == place]
    # if campus_country.empty:
    #     print(f"Provided country '{place}' is not part of CSV file")
    #     return

    # # Drop the 'country' column for a cleaner plot, as it is constant
    # plot_data = campus_country.drop(columns=["country"])

    # # Melt the DataFrame to a "long-form" structure suitable for seaborn
    # plot_data = plot_data.melt(var_name="Year", value_name="Life Expectancy")

    # # Ensure Year is numeric and sort it for a continuous line
    # # Set non-numeric to NaN
    # plot_data['Year'] = pd.to_numeric(plot_data['Year'], errors='raise')
    # # Remove rows with NaNs
    # plot_data = plot_data.dropna(subset=['Year', 'Life Expectancy'])
    # # Convert it to int
    # plot_data['Year'] = plot_data['Year'].astype(int)
    # # Sort them
    # plot_data = plot_data.sort_values(by='Year')

    # # Create the plot, you can also save the axes in a variable
    # sns.lineplot(data=plot_data, x="Year", y="Life Expectancy")

    # Add a title and axis labels
    plt.title(f"{place} Life expectancy Projections")
    plt.xlim(1800, 2100)
    plt.ylim(30, 95)
    plt.xticks(range(1800, 2100, 40))
    plt.show()


def main():
    """Main Entrypoint for aff_life"""
    try:
        draw_graph("life_expectancy_years.csv", "Germany")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
