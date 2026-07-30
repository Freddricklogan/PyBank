<h1 align="center">PyBank — Financial Analysis</h1>

<p align="center">
  <em>Automated profit-and-loss analysis of financial records — now with an interactive browser dashboard.</em>
</p>

<p align="center">
  <a href="https://freddricklogan.github.io/PyBank/"><img src="https://img.shields.io/badge/Live_Demo-Open_Dashboard-3b82f6?style=for-the-badge&logo=github" alt="Live Demo"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776ab?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Dashboard-Chart.js-3b82f6?logo=chartdotjs&logoColor=white" alt="Chart.js">
  <img src="https://img.shields.io/badge/License-MIT-lightgrey" alt="License">
</p>

---

## Overview

**PyBank** analyzes a company's financial records to surface the metrics that matter — total months,
net profit/loss, average month-over-month change, and the largest single-month swings. The original
analysis is a Python script (`main.py`); this repository now also ships an **interactive web dashboard**
that reproduces that exact analysis in the browser, visualizes it, and lets you drop in your own CSV.

> **▶ [Open the live dashboard](https://freddricklogan.github.io/PyBank/)**

![Financial Report](images/financial_report.png)

On the bundled dataset (86 months) the analysis reports:

| Metric | Value |
|:--|--:|
| Total Months | 86 |
| Net Total | $38,382,578 |
| Average Change | −$2,315.12 |
| Greatest Increase | Feb-2012 (+$1,926,159) |
| Greatest Decrease | Sep-2013 (−$2,196,167) |

The dashboard and the Python script produce identical results — the web version is a faithful,
visual port, not a re-interpretation.

---

## Why this project

| Skill demonstrated | Where it shows up |
|:--|:--|
| **Data analysis** | Aggregation, month-over-month deltas, and extrema detection over a time series |
| **Python fundamentals** | Clean CSV parsing and reporting with the standard library only |
| **Data visualization** | Time-series and change charts, KPI cards (Chart.js) |
| **Product thinking** | Turning a one-off script into a reusable tool with CSV upload |

---

## Two ways to run it

**1. The web dashboard** — no install; open [the live demo](https://freddricklogan.github.io/PyBank/) or `index.html`.
Use **Upload CSV** to analyze your own file (columns: `Date,Profit/Losses`).

**2. The Python script:**

```bash
git clone https://github.com/Freddricklogan/PyBank.git
cd PyBank
python main.py     # reads Resources/budget_data.csv, prints and exports the analysis
```

---

## Repository layout

```
main.py                     # the analysis script
Resources/budget_data.csv   # source data (86 months)
index.html                  # interactive web dashboard (served by GitHub Pages)
```

---

## Author

**Freddrick Logan** — Educational Technologist & Technology Leader
[GitHub](https://github.com/Freddricklogan) · [LinkedIn](https://www.linkedin.com/in/freddricklogan/)

## License

Released under the [MIT License](LICENSE).
