#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pickle
import streamlit as st
import sklearn
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


# In[3]:


pickle_in = open("classifier.pkl", 'rb') 
classifier = pickle.load(pickle_in)


# In[4]:


#filename= r"D:/Data Science/DS Project/P76_deployment/Classifier.sav"


def predi(Education, Marriage,Income,Children,Recency,Spent,Purchase,Campaign,Complain,Response,Age):
    if Education=="Basic":
        Education=0
    if Education=="Master":
        Education=1
    if Education=="PhD":
        Education=2
    else:
        Education=3

    if Marriage=="Single":
        Marriage=0
    else:
        Marriage=1

    if Campaign=="Yes":
        Campaign=1
    else:
        Campaign=0

    if Complain=="Yes":
        Complain=1
    else:
        Complain=0

    if Response=="Yes":
        Response=1
    else:
        Response=0
    
    df2 = pd.DataFrame([[Education, Marriage,Income,Children,Recency,Spent,Purchase,Campaign,Complain,Response,Age]], columns=['Education', 'Marital_Status', 'Income','Children', 'Recency','Total_spent','Total_no_purchase','TotalAcceptedCmp','Complain', 'Response', 'Age'])

    result= classifier.predict(df2)

    if result==0:
        result= "Cluster-0: Average income & average spending, Average income & more no. of purchase, Elder age(above 55 years) customers are more"
    elif result==1:
        result= "Cluster 1: Low income & low spending, Low income & less no. of purchase, Middle age customers are more (46-55)"
    elif result==2:
        result="Cluster 2: High income & high spending group, High income & average no. of purchase, Most peoples do not have children, Almost equally all age group customers are there. It is having customers with highest individual spent"
    else:
        result="Cluster 3: High income & average spending, High income & more no. of purchase, Most peoples do not have children, Elder age(above 55 years) customers are more"
    
    return result


st.set_page_config(layout="wide")

st.title("Customer Segmentation")

col1,col2,col3= st.columns(3)

Education = col1.selectbox('Education',("UnderGraduate","Master","PhD","Basic"))
Marriage = col2.selectbox('Marital Status',("Together","Single"))
Income= col3.number_input("Income") 

col4,col5,col6= st.columns(3)

Children = col4.slider("Children",min_value=0, max_value=10,value=1,step=1)
Recency= col5.number_input('Recency', min_value=0, max_value=10000,value=5, step=1)
Spent=col6.number_input('Total Spent')


col7,col8,col9= st.columns(3)
Purchase=col7.number_input('Purchase', min_value=0, max_value=10000,value=5, step=1)
Campaign = col8.selectbox('Accepted Campaign ?',("Yes","No"))
Complain = col9.selectbox('Complain',("Yes","No"))

col10,col11= st.columns(2)
Response = col10.selectbox('Response',("Yes","No"))
Age=col11.slider("Age",min_value=1, max_value=100,value=18,step=1)

df = pd.DataFrame([[Education, Marriage,Income,Children,Recency,Spent,Purchase,Campaign,Complain,Response,Age]], columns=['Education', 'Marital_Status', 'Income','Children', 'Recency','Total_spent','Total_no_purchase','TotalAcceptedCmp','Complain', 'Response', 'Age'])

if st.button("View the Data"):
    st.write(df)
    


if st.button("Predict"):
    prediction= predi(Education, Marriage,Income,Children,Recency,Spent,Purchase,Campaign,Complain,Response,Age)
    st.write(prediction)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




