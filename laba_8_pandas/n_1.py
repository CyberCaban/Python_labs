import csv
import pandas as pd


def print_values(data: dict) -> None:
    for key, value in data.items():
        print(f"{key}: \n{value}\n")


def handle_input(msg: str = "Enter value: ") -> int:
    try:
        return int(input(msg))
    except ValueError:
        exit("enter integer please!!!")


try:
    with open("data_tallest_buildings.csv", "r") as f:
        reader = csv.DictReader(f, delimiter=",")
        data = list(reader)
except FileNotFoundError:
    exit("no file")

df = pd.DataFrame(data)
df = df.astype(
    {
        "height_m": float,
        "year_built": int,
        "floors_above": int,
        "floors_below_ground": int,
    }
)
height = df["height_m"]
year = df["year_built"]
floors_above = df["floors_above"]
floors_below = df["floors_below_ground"]

highest = df.sort_values("height_m", ascending=False).head(5)
lowest = df.sort_values("height_m", ascending=True).head(5)
max_height = height.max()
min_height = height.min()
median_height = height.median()
mid_height = height.sum() / len(height)
num_of_countries = len(set(df["country"]))
newest_building = df.loc[year == year.max()]
oldest_building = df.loc[year == year.min()]
num_of_floors = handle_input("Enter number of floors: ")
num_of_floors = df.loc[floors_above + floors_below == num_of_floors]
exact_year = handle_input("Enter year: ")
exact_year = df.loc[year == exact_year]["name"]
buildings_in_country = input("Enter country: ")
buildings_in_country = len(df.loc[df["country"] == buildings_in_country])

print_values(
    {
        "5 tallest buildings": highest,
        "5 lowest buildings": lowest,
        "Max height": max_height,
        "Min height": min_height,
        "Median height": median_height,
        "Number of countries": num_of_countries,
        "Newest building(s)": newest_building,
        "Oldest building(s)": oldest_building,
        "Number of floors": (
            num_of_floors if not num_of_floors.empty else "No such floors"
        ),
        "Exact year": exact_year if not exact_year.empty else "Year not found",
        "Buildings in country": (
            buildings_in_country if buildings_in_country else "Country not found"
        ),
    }
)
