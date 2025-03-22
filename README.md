# Border Entry Traffic Analysis and Forecasting Using Machine Learning

This project is a comprehensive data analysis and forecasting tool built to study **US border entry traffic**, primarily focusing on the **US-Mexico (US-MX)** and **US-Canada (US-CN)** land borders. The goal is to uncover insights related to border traffic trends, detect anomalies, forecast future activity, and classify high-risk ports using **machine learning models**.

---

## 📌 Project Goals

This project addresses several core objectives:

1. **Anomaly Detection**  
   Identify unusual traffic patterns at border ports using Isolation Forest to flag anomalies in traffic volume.

2. **High-Risk Port Prediction**  
   Use Random Forest Classification to detect and predict high-risk ports based on z-scores, season, and geographic data.

3. **Traffic Normalization**  
   Normalize traffic by population and calculate z-scores to assess deviations from seasonal norms.

4. **Forecasting Future Traffic**  
   Apply linear regression to forecast traffic at all ports over the next 10 years (2026–2036), then rank them yearly.

5. **Seasonal and Temporal Patterns**  
   Understand how traffic, anomalies, and high-risk labels vary by **season (Spring, Summer, Fall, Winter)** and **month**.

6. **Top Transportation Modes**  
   Analyze the most used transport methods (e.g., trucks, buses, pedestrians) for entry into the US.

---

## 🗃️ Dataset Overview

Data was loaded from a PostgreSQL database and includes the following fields:

| Column        | Description                                       |
|---------------|---------------------------------------------------|
| `port_name`   | Name of the border port                           |
| `state`       | US state abbreviation (e.g., TX, NY, WA)          |
| `port_code`   | Unique code assigned to each port                 |
| `border`      | Either 'US-MX' or 'US-CN'                         |
| `month`       | Month of entry (converted from string to int)     |
| `year`        | Year of entry                                     |
| `measure`     | Mode of transportation (e.g., trucks, buses)      |
| `value`       | Number of people or vehicles crossing             |
| `latitude`    | Geolocation coordinate                            |
| `longitude`   | Geolocation coordinate                            |
| `season`      | Season assigned based on the month                |

**Total records analyzed:** 398,648  
**Total distinct ports:** 116  
**States covered:** 14  
**Time range:** 1996–2025

---

## 🧠 Machine Learning Models Used

| Task                     | Model                | Output                          |
|--------------------------|----------------------|----------------------------------|
| Anomaly Detection        | Isolation Forest     | Binary label: Normal/Anomaly     |
| High-Risk Classification| Random Forest Classifier | Binary prediction (Risk/No Risk) |
| Forecasting              | Linear Regression    | Future traffic predictions       |

---

## 🔬 Analysis Workflow

1. **Data Normalization**
   - Calculate total traffic by (`state`, `year`, `month`)
   - Normalize using population data per state
   - Compute `z-score` of traffic to measure deviation

2. **Anomaly Detection**
   - Use Isolation Forest on normalized traffic values
   - Flag records with anomaly scores < 0 as anomalies

3. **High-Risk Prediction**
   - Label ports in top 10% of z-score as risky
   - Train Random Forest model using:
     - `year`, `month`, `state_code`, `season_code`
     - `traffic_density`, `traffic_z_score`, `traffic_per_capita`

4. **Forecast Future Traffic**
   - Aggregate historical traffic per port/year
   - Fit linear regression models per port
   - Predict traffic for 2026–2036
   - Rank busiest ports per year

5. **Find Busiest Months**
   - For the top 10 busiest ports, find the busiest month in each year
   - Create count plot of most frequent peak months

6. **Top Transportation Methods**
   - Rank `measure` types (trucks, pedestrians, etc.) by total traffic volume
   - Display the top 5 transportation modes

---

## 📊 Visualizations Included

- **Top 10 Ports Traffic Forecast (Line Graph)**
- **Busiest Month per Port (Bar Plot)**
- **Anomaly Count by Season**
- **Average Traffic by Season**
- **High Risk Prediction by Season**
- **Top 5 Transportation Modes**

All graphs are plotted using **Matplotlib** and **Seaborn**, and displayed in real-time using `TkAgg`.

---

## 📁 Outputs

CSV files saved to the project directory:

| File                    | Description                                      |
|-------------------------|--------------------------------------------------|
| `forecasted_ports.csv`  | Traffic predictions (2026–2036) and yearly ranks |
| `busiest_months.csv`    | Peak traffic month per year for top ports        |
| `transport_modes.csv`   | Ranked transportation modes by total volume      |
| `final_report.txt`      | Wrap-up of analysis, ranked ports, and summaries |

---

## 🧾 Final Summary Report

The final report (both printed and saved as `final_report.txt`) includes:

- Total records processed
- Forecast period: 2026–2036
- Top 10 forecasted busiest ports
- Explanation of modeling process and how rankings were derived
- Busiest months per port
- Most common transportation methods

It includes clear divider lines and is formatted for both terminal display and GitHub readability.

---

## 🧰 Requirements

To run this project:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn sqlalchemy psycopg2
