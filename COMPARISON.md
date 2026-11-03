# Comparison: Pure Python vs Pandas

## Overview

This project uses two independent approaches to calculate
descriptive statistics on the same Facebook political ads dataset.

## Pure Python

The pure Python implementation uses standard-library tools,
including csv, math, statistics, collections, and ast.

Advantages:
- No third-party statistical packages required
- Greater visibility into each calculation
- Useful for understanding how descriptive statistics work

Challenges:
- More code is required
- Data types must be inferred manually
- Missing values need explicit handling
- Large datasets require more careful performance management

## Pandas

The Pandas implementation uses a DataFrame and built-in
statistical functions.

Advantages:
- Concise code
- Built-in data type inference
- Convenient missing-value analysis
- Fast descriptive statistics and frequency counts
- Easier to extend with grouping and filtering

Challenges:
- Requires an external dependency
- Some behavior depends on inferred data types
- Nested range values still require custom parsing

## Results Comparison

| Statistic | Pure Python | Pandas |
|---|---:|---:|
| Total records | 246,745 | 246,745 |
| Total columns | 40 | 40 |
| Economy indicator mean | 0.122122 | 0.122122 |
| Incivility indicator mean | 0.187526 | 0.187526 |
| Mean estimated spend | 1,061.79 | 1,061.79 |
| Mean estimated impressions | 36,756.00 | 36,756.00 |
| Mean estimated audience size | 254,474.72 | 254,474.72 |

The numeric results match within normal floating-point
rounding differences.

Both approaches use sample standard deviation, with
a denominator of n minus 1.

## Important Difference

Pure Python and Pandas can differ in their treatment of
categorical values and missing-value representations.

For example, strings such as NA may be interpreted as missing
values by Pandas, while a manually written parser must define
its own missing-value rules.

As a result, some categorical unique-value counts may differ
unless the same cleaning rules are applied.

## Conclusion

Both approaches successfully calculate descriptive statistics.

Pure Python provides more control and makes the underlying
calculations easier to understand.

Pandas is more convenient for exploratory analysis and
larger datasets because it provides concise, optimized methods.

For future analysis involving grouped statistics, filtering,
and time-based comparisons, Pandas would be the more
practical choice.
