import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("heart_rate_model.pkl")

# Page configuration
st.set_page_config(
    page_title="SmartPulse AI",
    page_icon="❤️",
    layout="centered"
)

st.title("❤️ SmartPulse AI")
st.subheader("AI-Powered Heart Rate Prediction")

st.write(
    "This application predicts heart rate from PPG signal data "
    "using a trained Random Forest model."
)

st.info("The model expects 128 PPG signal samples as input.")

# Input section
st.subheader("Enter PPG Signal")

ppg_input = st.text_area(
    "Enter 128 PPG values separated by commas:",
    placeholder="0.14, 0.18, 0.22, ..."
)

if st.button("Predict Heart Rate"):

    try:
        # Convert input to numbers
        values = np.array(
            [float(x.strip()) for x in ppg_input.split(",")]
        )

        # Check number of samples
        if len(values) != 128:
            st.error(
                f"Please enter exactly 128 PPG values. "
                f"You entered {len(values)}."
            )

        else:
            # Reshape for the model
            input_data = values.reshape(1, -1)

            # Prediction
            prediction = model.predict(input_data)[0]

            # Classify heart rate
            if prediction < 60:
                status = "Low"
            elif prediction <= 100:
                status = "Normal"
            else:
                status = "High"

            # Display results
            st.success(
                f"Heart Rate: {prediction:.2f} BPM"
            )

            if status == "Low":
                st.warning("Status: Low")

            elif status == "Normal":
                st.success("Status: Normal")

            else:
                st.error("Status: High")

    except ValueError:
        st.error(
            "Invalid input. Please enter numerical PPG values only."
        )
