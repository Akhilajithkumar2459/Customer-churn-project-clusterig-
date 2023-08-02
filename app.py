import streamlit as st
from sklearn.cluster import kmeans
import pandas as pd
import numpy as np

def prediction(Education,Marital_Status,Income,Recency,Complain,Age,Expenses,Children,Campaign,NumPurchases):

    # Pre-processing user input
    # Education details

    if Education == "Undergraduate":
        Education = 0

    elif Education == "Graduate":
        Education = 1

    elif Education == "Postgraduate":
        Education = 2

    # Marital_Status
    if Marital_Status == "Single":
        Marital_Status = 0

    elif Marital_Status == "Relationship":
        Marital_Status = 1

    # Complains
    if Complain == "YES":
        Complain = 1

    elif Complain == "NO":
        Complain = 0

    prediction = classifier.predict([[Education,Marital_Status,Income,Recency,Complain,Age,Expenses,Children,Campaign,NumPurchases]])

    if prediction == 0:
        pred = 'cluster 2'

    elif prediction == 1:
        pred = 'cluster 1'

    elif prediction == 2:
        pred = 'cluster 4'

    elif prediction == 3:
        pred = 'cluster 3'

    elif prediction == 4:
        pred = 'cluster 5'

    return pred


# Define the prediction function (make sure to implement this)
def prediction(Education, Marital_Status, Income, Recency, Complain, Age, Expenses, Children, Campaign, NumPurchases):
    # Implement your prediction logic here
    # For example:
    return "Cluster_A"

def main():
    # ... (same as your code)

    # Following lines create boxes in which the user can enter data required to make a prediction

    Education = st.selectbox("Education", ("Undergraduate", "Graduate", "Postgraduate"))

    Marital_Status = st.radio("Marital_Status: ", ('Single', 'Relationship'))
    if (Marital_Status == 'Single'):
        st.success("Single")
    elif (Marital_Status == 'Relationship'):
        st.success("Relationship")

    Incomes = st.selectbox("Incomes", [25000, 100000])  # Corrected options

    Recency = st.slider("Last Purchase", 0, 100)
    st.text('Selected: {}'.format(Recency))

    Complain = st.selectbox("Complain", ("YES", "NO"))

    Age = st.slider("Your age", 0, 100)
    st.text('Selected: {}'.format(Age))  # Corrected display

    Expense = st.slider("Select Monthly Expense", 0, 3000)
    st.text('Selected: {}'.format(Expense))

    Children = st.slider("Children", 0, 30)
    st.text('Selected: {}'.format(Children))

    Campaign = st.selectbox("Campaign accepted?", ("YES", "NO"))

    NumPurchases = st.slider("Number of Purchase Made", 0, 50)
    st.text('Selected: {}'.format(NumPurchases))  # Corrected display

    result = ""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = prediction(Education, Marital_Status, Incomes, Recency, Complain, Age, Expense, Children, Campaign, NumPurchases)  # Corrected variable names
        st.success('Common cluster is {}'.format(result))


if __name__ == '__main__':
    main()