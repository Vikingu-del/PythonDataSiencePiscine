import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a dataset from a CSV file.

    Args:
        path (str): Path to the CSV file.

    Returns:
        pd.DataFrame | None: Returns the DataFrame if successful, else None.
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as e:
        print(e)
        return None
    # except FileNotFoundError as e:
    #     raise e
    # except pd.errors.EmptyDataError as e:
    #     raise e
    # except pd.errors.ParserError as e:
    #     raise e
    # except Exception as e:
    #     raise e


def main():
    """
    Main Entrypoint of load_csv module
    """
    df = load("Erik")
    print(df)


if __name__ == "__main__":
    main()
