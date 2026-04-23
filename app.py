import streamlit as st
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAXResults

st.set_page_config(page_title="Reliance Stock Forecast", layout="centered")

st.title("Reliance Stock Price Forecast (SARIMA)")

# Load model safely
@st.cache_resource
def load_model():
    try:
        model = SARIMAXResults.load("sarima_mod_dep.pkl")
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model()

st.write("Enter number of future days to predict:")

steps = st.number_input(
    "Days to Forecast",
    min_value=1,
    max_value=60,
    value=10,
    step=1
)

if st.button("Predict"):

    if model is None:
        st.error("Model failed to load.")
    else:
        try:
            steps = int(steps)

            forecast = model.forecast(steps=steps)

            forecast_df = pd.DataFrame({
                "Day": range(1, steps + 1),
                "Predicted Price": forecast
            })

            st.subheader("Forecast Results")
            st.dataframe(forecast_df)

            st.subheader("Forecast Chart")
            st.line_chart(forecast_df.set_index("Day"))

        except Exception as e:
            st.error(f"Prediction failed: {e}")