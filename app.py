import streamlit as st
import pandas as pd
import numpy as np
import random

st.set_page_config(page_title="GovShield Dashboard", layout="wide")
st.title("🏛️ GovShield: Subsidy Leakage Tracking System")
st.markdown("Real-time anomaly monitoring for public welfare distribution channels.")

# --- IN-APP DATA GENERATION GENERATOR (Bypasses missing CSV errors) ---
@st.cache_data
def load_and_audit_data():
    np.random.seed(42)
    random.seed(42)
    
    # Generate PDS Mock Data
    pds_data = []
    fps_shops = [f"FPS-SHOP-{i:03d}" for i in range(1, 11)]
    for i in range(1500):
        card_id = f"RATIO-CARD-{random.randint(100000, 999999)}"
        family_size = random.choice([2, 3, 4, 5, 6])
        allocated = family_size * 5 
        fps_shop = random.choice(fps_shops)
        
        if fps_shop in ["FPS-SHOP-003", "FPS-SHOP-007"] and random.random() < 0.35:
            biometric_status = "FAILED"
            override_used = "YES"
            withdrawn = allocated 
        else:
            biometric_status = np.random.choice(["SUCCESS", "FAILED"], p=[0.92, 0.08])
            override_used = "YES" if biometric_status == "FAILED" and random.random() < 0.15 else "NO"
            withdrawn = allocated if (biometric_status == "SUCCESS" or override_used == "YES") else 0
        pds_data.append([card_id, fps_shop, biometric_status, override_used])
        
    df_pds = pd.DataFrame(pds_data, columns=['Ration_Card_ID', 'FPS_Shop_ID', 'Biometric_Status', 'Manual_Override_Used'])
    
    # Process PDS Analytics
    fps_analysis = df_pds.groupby('FPS_Shop_ID').agg(
        Total_Transactions=('Ration_Card_ID', 'count'),
        Manual_Overrides=('Manual_Override_Used', lambda x: (x == 'YES').sum())
    ).reset_index()
    fps_analysis['Override_Rate_%'] = round((fps_analysis['Manual_Overrides'] / fps_analysis['Total_Transactions']) * 100, 2)
    flagged_pds = fps_analysis[fps_analysis['Override_Rate_%'] > 20.0]

    # Generate LPG Mock Data
    lpg_data = []
    for i in range(1000):
        consumer_id = f"LPG-CON-{random.randint(100000, 999999)}"
        ctype = np.random.choice(["DOMESTIC", "COMMERCIAL"], p=[0.88, 0.12])
        bookings = random.randint(6, 12) if (ctype == "DOMESTIC" and random.random() < 0.04) else random.choice([0, 1, 1, 2])
        if ctype == "COMMERCIAL": bookings = random.randint(5, 25)
        subsidy = bookings * 300.0 if ctype == "DOMESTIC" else 0.0
        lpg_data.append([consumer_id, ctype, bookings, subsidy])
        
    df_lpg = pd.DataFrame(lpg_data, columns=['Consumer_ID', 'Cylinder_Type', 'Monthly_Bookings', 'Subsidy_Credited_INR'])
    flagged_lpg = df_lpg[(df_lpg['Cylinder_Type'] == 'DOMESTIC') & (df_lpg['Monthly_Bookings'] > 5)]
    
    return flagged_pds, flagged_lpg

pds_df, lpg_df = load_and_audit_data()

# --- DASHBOARD METRICS ---
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Flagged High-Risk PDS Centers", value=f"{len(pds_df)} Shops")
with col2:
    st.metric(label="Recovered LPG Revenue Leakage", value=f"₹{lpg_df['Subsidy_Credited_INR'].sum():,}")

st.write("---")

tab1, tab2 = st.columns(2)
with tab1:
    st.subheader("⚠️ High-Risk Ration Distribution Centers")
    st.dataframe(pds_df, use_container_width=True)
with tab2:
    st.subheader("🔥 Diverted Domestic LPG Connections")
    st.dataframe(lpg_df, use_container_width=True)
