import pandas as pd


CASES_FILE = "data/raw/cyclosporiasis-cases.csv"
POP_FILE = "data/raw/estimated-us-state-populations.csv"

OUTPUT_FILE = "data/processed/cyclospora_clean.csv"


states = [
    "Alabama","Alaska","Arizona","Arkansas",
    "California","Colorado","Connecticut",
    "Delaware","Florida","Georgia","Hawaii",
    "Idaho","Illinois","Indiana","Iowa",
    "Kansas","Kentucky","Louisiana","Maine",
    "Maryland","Massachusetts","Michigan",
    "Minnesota","Mississippi","Missouri",
    "Montana","Nebraska","Nevada",
    "New Hampshire","New Jersey",
    "New Mexico","New York",
    "North Carolina","North Dakota",
    "Ohio","Oklahoma","Oregon",
    "Pennsylvania","Rhode Island",
    "South Carolina","South Dakota",
    "Tennessee","Texas","Utah",
    "Vermont","Virginia","Washington",
    "West Virginia","Wisconsin","Wyoming"
]


def clean_cases():

    df = pd.read_csv(
        CASES_FILE,
        skiprows=3
    )

    df = df[
        df["Reporting Area"].isin(states)
    ]

    df = df.replace(
        ["-", "N", "NC"],
        0
    )

    numeric_columns = [
        "Current week",
        "Previous 52 weeks Max †",
        "Cum YTD 2026 †",
        "Cum YTD 2025 †"
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(
            df[col]
        )

    return df



def clean_population():

    pop = pd.read_csv(
        POP_FILE
    )

    pop["Estimated Population"] = (
        pop["Estimated Population"]
        .str.replace(",", "")
        .astype(int)
    )

    return pop



def main():

    cases = clean_cases()
    population = clean_population()


    df = cases.merge(
        population,
        left_on="Reporting Area",
        right_on="State"
    )


    df["Incidence Rate"] = (
        df["Cum YTD 2026 †"]
        /
        df["Estimated Population"]
        *
        100000
    )


    df.to_csv(
        OUTPUT_FILE,
        index=False
    )


    print("Data cleaning complete!")
    print(df.head())


if __name__ == "__main__":
    main()