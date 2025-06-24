import streamlit as st
from datetime import datetime
import numpy as np
import joblib
from geopy.distance import geodesic
import time

st.set_page_config(page_title="Cab Fare Estimator", page_icon="🚖", layout="centered")

model = joblib.load("rf_model.pkl")

st.image("cab_img.jpeg", use_container_width=True)

st.markdown("---")

st.markdown("### 📍 Enter Pickup and Dropoff Coordinates")
pickup_lat = st.number_input("Pickup Latitude", format="%.6f")
pickup_lon = st.number_input("Pickup Longitude", format="%.6f")
dropoff_lat = st.number_input("Dropoff Latitude", format="%.6f")
dropoff_lon = st.number_input("Dropoff Longitude", format="%.6f")

st.markdown("### 🕒 Select Ride Date and Time")
pickup_date = st.date_input("Pickup Date", value=datetime.now().date())
pickup_time = st.time_input("Pickup Time", value=datetime.now().time())

passenger_count = st.slider("👥 Passenger Count", 1, 6, 1)

if st.button("🔍 Estimate Fare"):
    if (pickup_lat == 0 or pickup_lon == 0 or dropoff_lat == 0 or dropoff_lon == 0):
        st.warning("⚠️ Coordinates cannot be 0. Please enter valid pickup and dropoff latitude/longitude.")
    else:
        try:
            start_time=time.time()
            pickup=(pickup_lat, pickup_lon)
            dropoff=(dropoff_lat, dropoff_lon)
            distance_km=geodesic(pickup, dropoff).kilometers
            duration_min=(distance_km/30)*60 

            hour = pickup_time.hour
            day = pickup_date.day
            month = pickup_date.month
            weekday = pickup_date.weekday()
            is_weekend = 1 if weekday >= 5 else 0

            features = np.array([[passenger_count, hour, day, month, weekday, is_weekend, distance_km, duration_min]])
            predicted_fare = model.predict(features)[0]
            latency = (time.time() - start_time) * 1000

            st.markdown("---")
            st.markdown("### 📊 Trip Summary")
            col1, col2 = st.columns(2)
            col1.metric("Distance", f"{distance_km:.2f} km")
            col2.metric("Duration", f"{duration_min:.1f} mins")

            st.success(f"💰 Estimated Fare: ${predicted_fare:.2f}")
            st.markdown("---")
            print(latency)
        except Exception as e:
            st.error(f"--- Error: {e}")


st.markdown("---")
st.image("RIDE.png", width=700)
