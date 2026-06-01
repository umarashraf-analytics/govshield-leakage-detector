# 🏛️ GovShield: Subsidy Leakage Tracking & Fraud Detection System

### 🔗 [Click Here to View the Live Interactive Dashboard][(https://govshield-subsidyleakage-detector.streamlit.app/)]

GovShield is an end-to-end data pipeline and risk analytics engine designed to identify financial leakages, biometric authentication bypasses, and unauthorized commercial diversions within public welfare schemes (specifically targetting Public Distribution Systems and Domestic LPG Subsidy programs).

---

## 🛠️ The Tech Stack & Ecosystem
- **Analytics & Processing Engine:** Python, Pandas, NumPy
- **Frontend Dashboard Layer:** Streamlit Community Cloud
- **Data Engineering Context:** Synthetic Simulation of National Transaction Registries

---

## 🔍 Core Detection Analytics (Fraud Vectors Tracked)

### 1. PDS Fair Price Shop (FPS) Manipulation
- **The Threat:** Unscrupulous operators using local "Manual Overrides" to distribute grains without validating citizen biometrics, pointing to open-market black diversion.
- **The Analytical Logic:** The system aggregates transactions by `FPS_Shop_ID` and flags centers where the biometric manual override failure rate exceeds an acceptable standard deviation threshold (>20%).

### 2. LPG Domestic-to-Commercial Diversion
- **The Threat:** Highly subsidized residential domestic cylinders being illegally diverted to commercial entities (restaurants, industries) for arbitrage profits.
- **The Analytical Logic:** Programmatic auditing flags consumer profiles breaking standard domestic consumption baselines (e.g., matching connections ordering >5 subsidized cylinders within a localized 30-day window).

---

## 📈 System Metrics & Insights
- **Cached Analytical Optimization:** Implements Streamlit memory caching (`@st.cache_data`) for lightning-fast algorithmic runs over data frames.
- **Automated Alerts:** Isolates and creates standalone operational data tables (`DataFrames`) containing high-risk endpoints for government audit groups to inspect.

---

## 🚀 How to Run the Environment Locally

1. Clone the repository:
   ```bash
   git clone [https://github.com/umarashraf-analytics/govshield-leakage-detector.git](https://github.com/umarashraf-analytics/govshield-leakage-detector.git)
   cd govshield-leakage-detector


   pip install -r requirements.txt

   streamlit run app.py
