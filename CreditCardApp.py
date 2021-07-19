import streamlit as st
import pandas as pd
import numpy as np
import joblib

print ("running")

# load models
tree_clf = joblib.load('clf-best.pickle')

st.title('Credit Card Application')
st.subheader('Making Prediction')
st.markdown('**Please provide customer information**:')  # you can use markdown like this

amt_annuity = float(st.number_input('Loan annuity'))
amt_credit = float(st.number_input('Credit amount of the loan'))
amt_goods_price = float(st.number_input('For consumer loans it is the price of the goods for which the loan is given'))
amt_income_total = float(st.number_input('Income of the client'))
amt_req_credit_bureau_year = float(st.number_input('Number of enquiries to Credit Bureau about the client one day year (excluding last 3 months before application)'))
days_birth = int(st.number_input("Client's age in years at the time of application"))
days_employed = int(st.number_input('How many months before the application the person started current employment'))


# this is how to dynamically change text
prediction_state = st.markdown('calculating...')

application = pd.DataFrame(
    {
		'AMT_ANNUITY': [amt_annuity],
		'AMT_CREDIT': [amt_credit],
		'AMT_GOODS_PRICE': [amt_goods_price],
		'AMT_INCOME_TOTAL': [amt_income_total],
		'AMT_REQ_CREDIT_BUREAU_YEAR': [amt_req_credit_bureau_year],
		'DAYS_BIRTH': [-days_birth * 365],
		'DAYS_EMPLOYED': [-days_employed * 30]
    }
)

y_pred = tree_clf.predict(application)

if y_pred[0] == 0:
    msg = 'This customer is predicted to be: **Not default**'
else:
    msg = 'This customer is predicted to be: **Default**'

prediction_state.markdown(msg)

