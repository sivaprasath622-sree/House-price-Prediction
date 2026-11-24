# House Price Prediction

I’ll inspect the project files so the explanation matches what this app actually does.

Find files matching `*`

Find files matching `**/*.{py,ipynb,js,jsx,ts,tsx,html,css,json,csv}`

Read 
Completed with input: {
  "path": "E:\\house price web app\\README.md"
}

Read 
Completed with input: {
  "path": "E:\\house price web app\\app.py"
}

Read 
Completed with input: {
  "path": "E:\\house price web app\\requirement.txt"
}

Read 
Completed with input: {
  "path": "E:\\house price web app\\.gitignore"
}

# House Price Prediction

This is a Streamlit web application that predicts house prices using a machine-learning model.

## How It Works

1. The user enters:
   - Average area income
   - Average house age
   - Average number of rooms
   - Average number of bedrooms
   - Area population
2. The application scales the entered values using `scaler.pkl`.
3. The trained machine-learning model from `house price.pkl` predicts the house price.
4. Streamlit displays the estimated price on the webpage.

## Main Files

- `app.py` – Contains the Streamlit interface and prediction logic.
- `house price.pkl` – Stores the trained machine-learning model.
- `scaler.pkl` – Stores the data scaler used during preprocessing.
- `requirement.txt` – Lists required Python packages.

## Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Joblib

The project demonstrates an end-to-end regression workflow: collecting user input, preprocessing it, running a trained model, and presenting the prediction through a simple web interface.
