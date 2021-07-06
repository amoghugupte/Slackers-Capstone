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
days_birth = int(st.number_input("Client's age in days at the time of application"))
days_employed = int(st.number_input('How many days before the application the person started current employment'))
days_id_publish = int(st.number_input('How many days before the application did client change the identity document with which he applied for the loan'))
days_last_phone_change = int(st.number_input('How many days before application did client change phone'))
obs_30_cnt_social_circle = int(st.number_input("How many observation of client's social surroundings with observable 30 DPD (days past due) default"))


print(days_employed)
print(days_birth)
print(days_id_publish)
print(days_last_phone_change)
print(amt_annuity)
print(amt_credit)
print(amt_income_total)
print(amt_goods_price)
print(amt_req_credit_bureau_year)
print(obs_30_cnt_social_circle)



# this is how to dynamically change text
prediction_state = st.markdown('calculating...')

application = pd.DataFrame(
    {
		'AMT_ANNUITY': [amt_annuity],
		'AMT_CREDIT': [amt_credit],
		'AMT_GOODS_PRICE': [amt_goods_price],
		'AMT_INCOME_TOTAL': [amt_income_total],
		'AMT_REQ_CREDIT_BUREAU_YEAR': [amt_req_credit_bureau_year],
		'DAYS_BIRTH': [days_birth],
		'DAYS_EMPLOYED': [days_employed],
		'DAYS_ID_PUBLISH': [days_id_publish],
		'DAYS_LAST_PHONE_CHANGE': [days_last_phone_change],
		'OBS_30_CNT_SOCIAL_CIRCLE': [obs_30_cnt_social_circle]
    }
)

y_pred = tree_clf.predict(application)

print(y_pred)
print("*********************************************************")
if y_pred[0] == 0:
    msg = 'This customer is predicted to be: **Not defaultee**'
else:
    msg = 'This customer is predicted to be: **Defaultee**'

prediction_state.markdown(msg)

