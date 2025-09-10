# Time-Series-Breakdown-of-Walmart-Retail-Sales-Task-04-Elevvo-
#  Time Series Breakdown of Walmart Retail Sales (Task 04)

## ** Project Overview**
This project is part of the **Elevvo Pathways Platform Internship 2025**, where I gained hands-on experience in time series analysis.  
The task focused on analyzing **Walmart’s historical sales data** to identify **overall trends, seasonal patterns, and fluctuations**, and to build a simple **baseline forecast** for future sales.

---

## ** Dataset Overview**
- **Source:** Walmart Sales Forecasting dataset (Kaggle)  
- **Size:** 421,570 rows × 5 columns  
- **Columns:** Store, Dept, Date, Weekly_Sales, IsHoliday  
- **Date Range:** February 2010 – October 2012  
- **Frequency:** Weekly data, aggregated into monthly totals  

---

## ** Steps Performed**
###  Data Preparation
- Converted Date column into datetime format  
- Sorted dataset by Date  
- Aggregated weekly sales into monthly totals  

###  Exploratory Analysis & Visualization
1. **Overall Sales Trend** → Monthly sales showed fluctuations with peaks around holidays/promotions  
2. **Moving Averages** → 3-month and 6-month averages highlighted long-term shifts  
3. **Seasonality Analysis** → Clear seasonal spikes, especially during holiday periods  
4. **Category/Regional Breakdown** → Some stores & departments showed sharper seasonal peaks  

###  Forecasting
- Applied simple models: Rolling Mean & Holt-Winters Exponential Smoothing  
- Forecasted next 3–6 months of sales  
- Evaluated results using **MAE** and **RMSE**  
- Exponential smoothing performed better but underpredicted holiday spikes  

---

## ** Key Findings**
- Sales patterns are **seasonal**, with strong peaks during holidays  
- **Moving averages** smoothed noise and revealed long-term trends  
- Baseline forecasting worked, but spikes during holidays were underestimated  

---

## ** Recommendations**
- Use advanced forecasting models like **SARIMA, Prophet, or LSTM**  
- Explicitly include **holiday & promotion features** in models  
- Plan **inventory & staffing** increases during high-demand months  
- Segment analysis by **store & department** to capture regional/category differences  

---

## ** Deliverables**
- **Jupyter Notebook:** `D.A Elevvo Task 4.ipynb`  
- **Cleaned Dataset:** `monthly_total_sales.csv`  
- **Visualizations:** Overall trend, Moving averages, Seasonal decomposition, Forecast plots  
- **Report:** `Task 4 Elevvo Report.pdf`  
- **Requirements File:** `requirements.txt`  

---
 ## Author

- Aleem Shoukat
- Gmail- iamaleemmm@gmail.com
- Linked in-www.linkedin.com/in/aleem-shoukat-9bb3b6356

⭐ If you found this project useful, feel free to star this repository!
