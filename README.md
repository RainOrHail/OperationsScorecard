# Scorecard Visual App

Simple Docker-ready Streamlit app for visualizing Excel scorecards.

## Run locally
pip install -r requirements.txt
streamlit run app.py

## Run with Docker
docker build -t scorecard-visual-app .
docker run -p 8501:8501 scorecard-visual-app
