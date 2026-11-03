import csv
from pathlib import Path

# Locate the dataset in the same folder as this script
file_path = Path(__file__).resolve().parent.parent / "fb_ads_president_scored_anon.csv"

# Read the dataset using standard Python
with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)
    columns = reader.fieldnames
    rows = list(reader)

print("Total rows:", len(rows))
print("Total columns:", len(columns))
print("Dataset loaded successfully!")

import math
from statistics import median

def compute_numeric_stats(values):
    # Remove missing values
    numbers = [float(v) for v in values if v is not None]

    if not numbers:
        return None

    count = len(numbers)
    mean = sum(numbers) / count

    # Sample standard deviation (same default as Pandas)
    variance = (
        sum((x - mean) ** 2 for x in numbers) / (count - 1)
        if count > 1 else None
    )

    return {
        "count": count,
        "mean": mean,
        "min": min(numbers),
        "max": max(numbers),
        "median": median(numbers),
        "std_dev": math.sqrt(variance) if variance is not None else None
    }


# Test the function using the binary political topic column
values = [
    int(row["illuminating_topic_economy"])
    for row in rows
    if row["illuminating_topic_economy"].strip()
]

stats = compute_numeric_stats(values)

print("\nEconomy Topic Statistics:")
for key, value in stats.items():
    print(f"{key}: {value}")


"============="
from collections import Counter

def compute_categorical_stats(values):
    # Remove missing or empty values
    cleaned = [
        str(v).strip()
        for v in values
        if v is not None and str(v).strip()
    ]

    if not cleaned:
        return {
            "count": 0,
            "unique_values": 0,
            "mode": None,
            "mode_frequency": 0,
            "top_5": []
        }

    frequencies = Counter(cleaned)
    top_five = frequencies.most_common(5)

    return {
        "count": len(cleaned),
        "unique_values": len(frequencies),
        "mode": top_five[0][0],
        "mode_frequency": top_five[0][1],
        "top_5": top_five
    }


# Test using Facebook page names
page_names = [row["page_name"] for row in rows]

stats = compute_categorical_stats(page_names)

print("\nPage Name Statistics:")
for key, value in stats.items():
    print(f"{key}: {value}")

"================"
# Analyze every column automatically

missing_tokens = {"", "n/a", "na", "null", "none", "nan"}

def is_missing(value):
    return value is None or str(value).strip().lower() in missing_tokens

def is_numeric_column(values):
    valid = [v for v in values if not is_missing(v)]

    if not valid:
        return False

    try:
        for value in valid:
            float(value)
        return True
    except (ValueError, TypeError):
        return False


print("\n" + "=" * 60)
print("COMPLETE DATASET ANALYSIS")
print("=" * 60)

for column in columns:
    values = [row[column] for row in rows]

    missing_count = sum(is_missing(v) for v in values)
    valid_values = [v for v in values if not is_missing(v)]

    print(f"\nCOLUMN: {column}")
    print(f"Missing values: {missing_count}")
    print(f"Inferred type: {'Numeric' if is_numeric_column(values) else 'Categorical'}")

    if is_numeric_column(values):
        stats = compute_numeric_stats(valid_values)
    else:
        stats = compute_categorical_stats(valid_values)

    if stats:
        for key, value in stats.items():
            print(f"{key}: {value}")



'================'
import ast

def extract_midpoint(value):
    # Convert a reported range into an estimated midpoint
    try:
        data = ast.literal_eval(value)

        lower = float(data["lower_bound"])
        upper = data.get("upper_bound")

        if upper is None:
            return None

        return (lower + float(upper)) / 2

    except (ValueError, TypeError, SyntaxError, KeyError):
        return None


# Analyze the three columns containing numeric ranges
range_columns = [
    "spend",
    "impressions",
    "estimated_audience_size"
]

print("\n" + "=" * 60)
print("ESTIMATED RANGE STATISTICS")
print("=" * 60)

for column in range_columns:
    midpoints = [
        extract_midpoint(row[column])
        for row in rows
    ]

    valid_midpoints = [v for v in midpoints if v is not None]

    print(f"\nCOLUMN: {column}")
    print(f"Valid estimates: {len(valid_midpoints)}")
    print(f"Unavailable estimates: {len(rows) - len(valid_midpoints)}")

    stats = compute_numeric_stats(valid_midpoints)

    if stats:
        for key, value in stats.items():
            print(f"{key}: {value}")