# Laptop Price Prediction

## Overview

This project aims to predict the price of laptops based on their specifications, using a DecisionTreeRegressor model and a user-friendly Streamlit web interface.

## Key Features

    Accurate Price Predictions: The model is trained on a comprehensive dataset of laptop specifications and prices, ensuring reliable predictions.
    Streamlit Web App: A user-friendly interface allows for easy interaction with the model, making it accessible to users of all levels.
    Data Source: The dataset is curated from multiple sources on Kaggle, providing a diverse range of laptop data.

## Technologies Used

    Python: Primary programming language
    Streamlit: Framework for building web applications
    scikit-learn: Machine learning library
    DecisionTreeRegressor: Machine learning algorithm for prediction
    pandas: Data analysis and manipulation library
    NumPy: Numerical computing library

## Getting Started

    Clone the repository:
    Bash

    git clone https://github.com/vishwaschaudhary/Laptop-price-prediction.git

    Use code with caution. Learn more

Install dependencies:
Bash

pip install -r requirements.txt

Use code with caution. Learn more
Run the Streamlit app:
Bash

streamlit run app.py

Use code with caution. Learn more

## Usage

    Access the web app in your browser (usually at http://localhost:8501).
    Enter the specifications of the laptop you want to predict the price for.
    Click the "Predict Price" button.
    The predicted price will be displayed on the screen.

## Project Structure

    app.py: Main Streamlit app file
    files/pipe.pkl: Saved DecisionTreeRegressor model
    files/df.pkl: Saved dataset
    requirements.txt: List of required Python libraries
    README.md: This file

## Contribute

Feel free to contribute to this project by:

    Suggesting improvements
    Reporting bugs
    Creating pull requests