# SmartPulse AI

AI-powered heart rate prediction system using PPG signals.

## Project Overview

SmartPulse AI is a machine learning project that predicts heart rate (HR) from Photoplethysmography (PPG) signals.

The system is designed to work with PPG signals obtained from a sensor such as the MAX30102.

The predicted heart rate is then classified into three categories:

- Low
- Normal
- High

## System Pipeline

PPG Sensor (MAX30102)
        ↓
PPG Signal
        ↓
Preprocessing
        ↓
128 PPG Samples
        ↓
Random Forest Model
        ↓
Heart Rate Prediction (BPM)
        ↓
Low / Normal / High Classification

## Dataset

The project uses the BIDMC PPG and Respiration Dataset.

The dataset provides physiological signals including PPG (PLETH) and heart rate measurements.

## Data Preparation

The PPG signal is divided into windows of 128 samples.

Each window represents one input sample for the machine learning model.

The dataset was divided according to the required project split:

- 70% Training
- 15% Evaluation
- 15% Testing

### Dataset Split

| Dataset | Samples | Percentage |
|---|---:|---:|
| Training | 17,360 | 70% |
| Evaluation | 3,720 | 15% |
| Testing | 3,720 | 15% |
| Total | 24,800 | 100% |

## Machine Learning Model

## Machine Learning Models

Four machine learning algorithms were implemented and compared for heart rate prediction:

1. Linear Regression
2. Random Forest Regressor
3. Decision Tree Regressor
4. Support Vector Regression (SVR)

The models were evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

After comparing the four models, the Random Forest Regressor was selected as the final model because it achieved the best overall performance.

The final model is a:

**Random Forest Regressor**

## Model Performance

### Testing Results

| Metric | Result |
|---|---:|
| MAE | 3.69 BPM |
| RMSE | 5.86 BPM |
| R² | 0.805 |

### Evaluation Results

| Metric | Result |
|---|---:|
| MAE | 3.97 BPM |
| RMSE | 6.49 BPM |
| R² | 0.773 |

The final Random Forest model achieved an R² of approximately 0.805 on the testing dataset.

## Heart Rate Classification

The predicted heart rate is classified as:

| Heart Rate | Status |
|---|---|
| < 60 BPM | Low |
| 60–100 BPM | Normal |
| > 100 BPM | High |

## Project Files

```text
SmartPulse-AI/
│
├── app.py
├── heart_rate_model.pkl
├── requirements.txt
├── README.md
│
└── notebooks/
    └── heart_rate_prediction.ipynb
