# Findings: Facebook Political Ads

## 1. Dataset Overview

The dataset contains 246,745 advertisement records across 40 columns.

There are 4,475 unique page IDs and 4,546 unique page names.

The data includes 26 numeric binary indicators describing political
messaging, topics, and other characteristics.

## 2. Advertising Activity Is Concentrated

The five most frequent page names are:

| Page | Number of ads |
|---|---:|
| Kamala Harris | 55,503 |
| Donald J. Trump | 23,988 |
| Joe Biden | 14,822 |
| The Daily Scroll | 10,461 |
| Kamala HQ | 7,564 |

The Kamala Harris page accounts for approximately 22.5% of all
advertisement records.

This indicates that ad volume is concentrated among certain pages.
However, ad count alone does not establish which page spent the most.

## 3. Spending Distribution

Facebook reports advertising expenditure in ranges rather than
exact amounts.

The most common spending range is 0 to 99, appearing in
135,950 records, approximately 55.1% of the dataset.

Using the midpoint of each reported range:

- Mean estimated spend: 1,061.79
- Median estimated spend: 49.50
- Maximum estimated spend: 474,999.50

The large difference between mean and median indicates a
strongly right-skewed spending distribution.

These figures summarize numeric midpoints across records and should
not be interpreted as a single-currency spending total.

USD accounts for 246,599 of the 246,745 records.
The analysis also calculates USD-only spending estimates.

## 4. Impressions and Audience Size

For impressions:

- Valid midpoint estimates: 244,479
- Mean estimated impressions: 36,756
- Median estimated impressions: 3,499.50

For estimated audience size:

- Valid midpoint estimates: 146,020
- Mean estimated audience size: 254,474.72
- Median estimated audience size: 300,000.50

Audience-size midpoint estimates are unavailable for 100,725 records.

Of these, 100,146 records contain an open-ended range with
a lower bound of 1,000,001 and no upper bound.
Another 579 records have missing audience-size values.

This limitation is important when interpreting audience statistics.

## 5. Political Messaging

Approximately:

- 54.86% of ads are flagged for advocacy messaging.
- 38.16% are flagged for issue messaging.
- 27.19% are flagged for attack messaging.
- 57.28% are flagged for a call to action.
- 22.85% are flagged for fundraising calls to action.

These are binary classification indicators. Their percentages
are not necessarily mutually exclusive.

## 6. Political Topics and Incivility

The following proportions of ads were flagged:

| Indicator | Percentage |
|---|---:|
| Economy | 12.21% |
| Health | 10.92% |
| Social and cultural | 10.58% |
| Women's issues | 8.09% |
| Immigration | 3.36% |
| Incivility | 18.75% |

The economy and health are among the more frequently flagged
topics in the dataset.

## 7. Advertising Timeline

The most frequent ad creation date is October 27, 2024,
with 8,619 records.

October 28, 2024 is the most frequent delivery start date,
with 10,089 records.

These dates fall shortly before the November 2024 election,
suggesting substantial advertising activity near Election Day.

These observations describe daily frequencies rather than
a complete monthly trend analysis.

## 8. Missing Data and Limitations

The main missing values are:

- Ad delivery stop time: 2,159
- Bylines: 1,009
- Estimated audience size: 579

Missing values should be distinguished from ranges where a
numeric midpoint cannot be estimated.

Additionally, the dataset uses estimated ranges, multiple
currencies, and classification indicators.

These findings describe the dataset and do not establish
causal relationships or advertising effectiveness.
