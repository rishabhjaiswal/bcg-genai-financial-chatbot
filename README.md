# Financial Data Analysis - BCG GenAI Consulting

## Project Overview
This project is part of the BCG GenAI Consulting virtual job simulation. It focuses on extracting, structuring, and analyzing key financial data from 10-K documents to lay the groundwork for an AI-driven financial chatbot. 

The analysis compares the financial health and year-over-year (YoY) growth of three major technology companies: **Apple, Microsoft, and Tesla** over a three-year period (2023–2025).

## Tech Stack
* python: Core programming language
* Pandas: Data manipulation, aggregation, and YoY percentage calculations
* Matplotlib & Seaborn: Data visualization and grouped bar charts
* Jupyter Notebook: Interactive analysis and reporting

## Key Metrics Analyzed
The following metrics were extracted and analyzed for YoY percentage growth:
* Total Revenue
* Net Income
* Total Assets
* Total Liabilities
* Cash Flow

## Key Findings & Conclusion
* Microsoft: Showed the most promising and aggressive growth, exhibiting compounding positive trends across almost all financial health indicators (including the highest revenue and cash flow growth).
* Apple: Demonstrated highly mature, steady trends with a massive jump in net income in 2025 (19.49%), even as they slightly contracted their asset footprint.
* Tesla: Exhibited concerning negative profitability trends in 2025 (Net income dropped ~46% and revenue growth turned negative) despite an overall increase in total assets and expanding footprint.

## Visualizations
The notebook includes automated, visually accessible grouped bar charts comparing the YoY growth percentages of all three companies across each metric to easily identify performance anomalies.

## How to Run
1. Clone the repository.
2. Ensure you have the required libraries installed: `pip install pandas matplotlib seaborn`.
3. Open `financial_data_analysis.ipynb` in Jupyter Notebook or VS Code.
4. Select "Restart & Run All" to execute the data pipeline and generate the visualizations.