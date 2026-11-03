from pathlib import Path
import pandas as pd
import ast

# Load the Facebook political ads dataset
df = pd.read_csv(Path(__file__).resolve().parent.parent / "fb_ads_president_scored_anon.csv", low_memory=False)

print("=" * 60)
print("FACEBOOK POLITICAL ADS - PANDAS ANALYSIS")
print("=" * 60)

# 1. Dataset overview
print("\nDATASET OVERVIEW")
print("Total rows:", df.shape[0])
print("Total columns:", df.shape[1])

print("\nCOLUMN DATA TYPES")
print(df.dtypes.to_string())

print("\nDATAFRAME INFO")
df.info()

# 2. Missing values
print("\nMISSING VALUES")
missing = pd.DataFrame({
    "Missing Count": df.isna().sum(),
    "Missing Percentage": (df.isna().mean() * 100).round(2)
})
print(missing.to_string())

# 3. Numeric statistics
print("\nNUMERIC COLUMN STATISTICS")
numeric_cols = df.select_dtypes(include="number")

print(
    numeric_cols.describe().T[
        ["count", "mean", "std", "min", "50%", "max"]
    ].to_string()
)

# 4. Categorical statistics
print("\nCATEGORICAL COLUMN STATISTICS")

categorical_cols = df.select_dtypes(exclude="number")

for column in categorical_cols.columns:
    print(f"\nCOLUMN: {column}")
    print("Count:", df[column].count())
    print("Unique values:", df[column].nunique())

    top_five = df[column].value_counts().head(5)

    if not top_five.empty:
        print("Mode:", top_five.index[0])
        print("Mode frequency:", top_five.iloc[0])
        print("Top 5 values:")
        print(top_five.to_string())

# 5. Convert numeric ranges into estimated midpoints
def extract_midpoint(value):
    # Facebook provides ranges rather than exact numbers
    try:
        data = ast.literal_eval(value)

        lower = float(data["lower_bound"])
        upper = data.get("upper_bound")

        if upper is None:
            return None

        return (lower + float(upper)) / 2

    except (ValueError, TypeError, SyntaxError, KeyError):
        return None


range_columns = [
    "spend",
    "impressions",
    "estimated_audience_size"
]

print("\nESTIMATED RANGE STATISTICS")

for column in range_columns:
    midpoints = df[column].apply(extract_midpoint)

    print(f"\nCOLUMN: {column}")
    print("Valid estimates:", midpoints.count())
    print("Unavailable estimates:", midpoints.isna().sum())
    print("Mean:", midpoints.mean())
    print("Minimum:", midpoints.min())
    print("Maximum:", midpoints.max())
    print("Median:", midpoints.median())
    print("Standard deviation:", midpoints.std())

# 6. Top Facebook pages
print("\nTOP 5 FACEBOOK PAGES BY AD COUNT")
print(df["page_name"].value_counts().head(5).to_string())

# 7. Economy and incivility indicators
print("\nECONOMY TOPIC")
print("Percentage of ads:", df["illuminating_topic_economy"].mean() * 100)

print("\nINCIVILITY")
print("Percentage of ads:", df["illuminating_incivility"].mean() * 100)

# 8. USD-only spending estimates
usd_df = df[df["currency"] == "USD"].copy()
usd_spend = usd_df["spend"].apply(extract_midpoint)

print("\nUSD-ONLY SPENDING ESTIMATES")
print("USD ad records:", len(usd_df))
print("Estimated total spend (USD):", usd_spend.sum())
print("Estimated mean spend (USD):", usd_spend.mean())
print("Estimated median spend (USD):", usd_spend.median())

print("\nPANDAS ANALYSIS COMPLETED SUCCESSFULLY!")