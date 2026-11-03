# Task 01: Descriptive Statistics

## Project Overview

This project explores a dataset of Facebook political advertisements
associated with the 2024 US presidential election.

The goal is to calculate descriptive statistics using two approaches:
standard Python and Pandas, and compare their results.

## Dataset

Source: Facebook Political Ads Dataset

Dataset link:
https://drive.google.com/file/d/1gvtvX8fATFrrzraPmTSf205U8u3JExUR/view?usp=sharing

- Total records: 246,745
- Total columns: 40
- Numeric columns: 26
- Other columns: 14

The dataset contains Facebook page information, advertising dates,
estimated spending, impressions, audience size, and political content indicators.

The original dataset is not included in this repository.

## Project Files

- pure_python_stats.py: Analysis using Python's standard library
- pandas_stats.py: Analysis using Pandas
- FINDINGS.md: Key observations from the dataset
- COMPARISON.md: Comparison of both approaches
- requirements.txt: Required third-party packages

## Running the Project

1. Install Python 3.
2. Download the dataset from the link above.
3. Save it as fb_ads_president_scored_anon.csv in the parent
   directory of Task_01_Descriptive_Stats.
4. Open a terminal in the Task_01_Descriptive_Stats folder.
5. Install dependencies:

   pip install -r requirements.txt

6. Run the scripts:

   python pure_python_stats.py

   python pandas_stats.py

## Statistics Calculated

For numeric columns:
- Non-null count
- Mean
- Minimum and maximum
- Median
- Sample standard deviation

For categorical columns:
- Non-null count
- Number of unique values
- Mode and its frequency
- Five most frequent values

The scripts also examine missing values and calculate estimated
midpoints for spending, impressions, and audience-size ranges.

## Limitations

Spending and impressions are provided as ranges rather than exact values.
Midpoints are estimates and should not be interpreted as actual measurements.

The dataset contains multiple currencies. USD-only spending estimates
are calculated separately to avoid combining different currencies.

Some audience-size ranges have no upper bound, so a midpoint
cannot be calculated for those records.
