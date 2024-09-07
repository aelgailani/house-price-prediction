
# House Price Prediction App 🏡

This repository contains a Streamlit-based web application that predicts house prices using a trained XGBoost regression model. The app allows users to input various features of a house and provides an estimated sale price based on the trained machine learning model.

## 🎯 Features
- **Interactive Input**: Users can input values for important house features such as overall quality, living area, garage size, year built, and more.
- **Real-Time Predictions**: The app instantly provides house price predictions based on the user’s inputs using a pre-trained XGBoost model.
- **User-Friendly Interface**: Simple and intuitive design with sliders and input boxes for easy data entry.

## 📊 Model Details
- The model used in this app is an XGBoost Regressor, trained with optimal hyperparameters found through extensive grid search.
- **Performance Metrics**:
  - **Mean Squared Error (MSE)**: 158,091,768.44
  - **R² Score**: 0.98
- The model captures complex relationships between house features and sale price, providing accurate and reliable predictions.

## 🚀 How to Use the App
1. **Input Features**: Adjust the sliders and input boxes to match the characteristics of the house you want to price.
2. **Get Predictions**: The app will display the predicted house price based on the inputs provided.
3. **Adjust Parameters**: Experiment with different values to see how changes in features affect the predicted price.

## 🛠️ Technology Stack
- **Front-end**: Streamlit - A framework for building interactive web applications in Python.
- **Model**: XGBoost - A powerful and efficient gradient boosting framework.
- **Language**: Python - The entire app is built using Python, leveraging machine learning and data visualization libraries.

## 📦 Setup and Installation
To run this app locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/house-price-prediction.git
   cd house-price-prediction
