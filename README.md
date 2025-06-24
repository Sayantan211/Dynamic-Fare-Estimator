# 🚕 Dynamic Fare Estimator

A machine learning project to predict taxi fare prices dynamically based on pickup/dropoff location, time of ride, and passenger count. This estimator is trained on real-world cab data and uses distance and temporal features to predict fare amounts.

![Screenshot 2025-05-10 180106](https://github.com/user-attachments/assets/f78f12a8-e463-405b-884c-2a913c5bf94b)
![Screenshot 2025-05-10 181701](https://github.com/user-attachments/assets/373712fd-ee71-42c5-a601-2a9ce4d31f85)

---

## 📂 Dataset

The dataset used is `cab_dataset.csv` and contains:

- `fare_amount`: Actual fare paid.
- `pickup_datetime`: Timestamp of the ride.
- `pickup_longitude`, `pickup_latitude`: Pickup location coordinates.
- `dropoff_longitude`, `dropoff_latitude`: Dropoff location coordinates.
- `passenger_count`: Number of passengers in the cab.

---

## ⚙️ Technologies Used

- Python 
- Pandas & NumPy
- Scikit-learn
- Random Forest Regressor
- Matplotlib & Seaborn

---

## 📈 Project Workflow

### 1. Data Cleaning
- Removed missing values and duplicates.
- Filtered outliers and unrealistic values (e.g., invalid coordinates, negative fares).
- Converted datetime to useful features like hour, day, and month.

### 2. Feature Engineering
- Extracted features from `pickup_datetime`.
- Calculated distance between pickup and dropoff points using the Haversine formula.

### 3. Model Building
- Used `RandomForestRegressor` from scikit-learn.
- Tuned hyperparameters using `RandomizedSearchCV`.

### 4. Model Evaluation
- Evaluated model performance using:
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE) 
  - Root Mean Squared Error (RMSE)
  - R² Score

---

## 📊 Results

- The model shows good performance with MAE of 1.394, MSE of 3.591,R² Score of 0.654(65.4%) and RMSE of 1.895.
- Distance and hour of the ride were found to be the most important features influencing fare.
- Can accurately estimate dynamic fares within a reasonable error margin.

---

## 📌 Future Improvements

- Integrate real-time traffic and weather data.
- Deploy the model using Flask or Django as a web app.
- Implement surge pricing models based on demand.

---

