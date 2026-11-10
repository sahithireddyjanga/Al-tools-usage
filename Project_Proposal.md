# Project Proposal: AI Tools Usage Analytics Dashboard

## 1. Project Title
AI Tools Usage Analytics Dashboard

## 2. Introduction
Artificial Intelligence tools are increasingly used for learning and work. This project analyses user data to understand how often people use AI tools and how this usage relates to productivity, satisfaction, trust, and time saved.

## 3. Problem Statement
Users and organisations may not clearly understand how AI tool usage patterns relate to productivity and user experience. Raw spreadsheet data is difficult to interpret and compare.

## 4. Proposed Solution
The project cleans the supplied dataset, performs exploratory data analysis, creates visualisations, and presents key measures in an interactive Power BI dashboard.

## 5. Objectives
- Clean and prepare the AI tools usage dataset.
- Measure daily AI usage and the number of tools used.
- Analyse productivity, satisfaction, trust, and time saved.
- Identify patterns and relationships between numerical variables.
- Present findings through charts and a Power BI dashboard.

## 6. Dataset
The supplied Excel workbook contains a Dataset sheet and a Data_Dictionary sheet. The Dataset sheet has 1,050 records and 12 columns, including age, experience, daily AI usage, number of AI tools, queries per day, learning hours, subscription cost, productivity, satisfaction, trust, and weekly time saved.

## 7. Tools and Technologies
- Python 3
- VS Code
- Pandas and NumPy for data handling
- Matplotlib for charts
- Excel for source data
- Microsoft Power BI Desktop for the interactive dashboard

## 8. Methodology
1. Load the Excel dataset.
2. Check and remove duplicate records.
3. handle missing values and validate numeric ranges.
4. Save the cleaned data as clean_dataset.csv.
5. Generate descriptive statistics and correlation analysis.
6. Create charts for usage, productivity, satisfaction, trust, and time saved.
7. Import the cleaned CSV into Power BI and build dashboard visuals.

## 9. Expected Output
- Cleaned CSV dataset.
- Descriptive statistics and correlation matrix.
- Charts showing AI usage and user outcomes.
- Power BI dashboard with KPI cards, filters, and charts.

## 10. Conclusion
The project converts raw AI usage data into understandable analysis and visual summaries. It can help users explore AI usage patterns and evaluate reported productivity and experience measures. Correlation should not be interpreted as proof of causation.
