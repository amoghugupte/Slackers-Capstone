# About

This repo contains the code UD capstone project for cohort 2021, for data science certification

- `Capstone-Exploratory-assignment_6_Clean_Final`: basic full pipeline with EDA, preprocessing, model tuning/evaluation/selection/persistence
- `CreditCardApp.py`: machine learning web app via Streamlit

## Local Setup

Python 3 required, see tutorial to setup Python 3: https://bit.ly/2uX6wAX

Clone the repo, go to the repo folder in Terminal, setup the virtual environment and install the required packages as follows:

```shell
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Run `$ jupyter lab` or `$ code .` (if use VSCode) to go over the notebooks.

## Kaggle Data

You will need data from kaggle
[https://www.kaggle.com/mishra5001/credit-card](https://www.kaggle.com/mishra5001/credit-card)

## Machine Learning Web App

Steps to get the streamlit app running (make sure to use the Terminal and the virtual environment is activated):

1. Get the data and model files ready
2. Create a notebook to do analysis and prediction
3. Create an app python file based on the notebook, such as `CreditCardApp.py`
4. Run the app locally (Local URL: http://localhost:8501) using terminal: `streamlit run CreditCardApp.py` 
5. Stop the app by using ctrl + C or closing the terminal
6. Deploy the app to the cloud for public access via services such as streamlit share, heroku, aws

## Final presentation
Credit Default detector_v6.pptx
