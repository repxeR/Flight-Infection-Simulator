from app_func import *
import pandas as pd
import plotly.express as px
import random #just for random function
import math
import numpy as np
import streamlit as st

page_bg_img="""
<style>
    [data-testid='stAppViewContainer"]{
    background-image: url("https://media.npr.org/assets/img/2021/06/22/ap_21159776567541-d2155d83cffd9b9dd281c5ae6b74ba3554560616.jpg")
    background-size: cover;
    }

    [data-testid="stHeader"]{
        background-color: rgba(0,0,0,0);
    }
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
st.header("Flight Infection Simulator")
tab1, tab2, tab3 = st.tabs(["Covid", "Flu", "Strep"])

desiredAirplane = "airbusA319"

seatingList = airplaneBuilder(desiredAirplane)
df = pd.DataFrame({'id': seatingList})
df["percent"] = 0
#for now, randomize percent.
#this will be deleted later, therefore warnding can be ignored!
for x in range(df.shape[0]):
    df["percent"][x] = random.randrange(100)
#end of deletable block

df["seatFilled"] = False
df["sick"] = False
df["vaccinated"] = False
df["asymptomatic"] = False
percentage = np.zeros(shape=(math.floor(df.shape[0]/6), 6))

counter = 0
indexHolder = 0


for x in range(df.shape[0]):
    if(counter < 6):
        percentage[indexHolder][counter] = df["percent"][x]
    else:
        counter = 0
        indexHolder+=1
        percentage[indexHolder][counter] = df["percent"][x]
        
    counter+=1
fig = px.imshow(percentage,
                labels=dict(x="Seat Letter", y="Seat Number", color="Percent 0-100"),
                x=['A', 'B', 'C', 'D', 'E', 'F'],
                y=['8', '9', '10', '11', '12', '13','14','15','16','17','18','19','20','21','22','23','24','25','26','27'], height=400, width=300
               )
with tab1:
    st.markdown("<h1 style='text-align: center; color: red;'></h1>", unsafe_allow_html=True)
    st.write(df)
    st.write(fig)
    st.write(
    """
    ## Symptoms include:
    - Fever or chills
    - Cough
    - Shortness of breath or difficulty breathing
    - Fatigue
    - Muscle or body aches
    - Headache
    """
)

counter = 0
indexHolder = 0
for x in range(df.shape[0]):
    df["percent"][x] = random.randrange(100)

for x in range(df.shape[0]):
    if(counter < 6):
        percentage[indexHolder][counter] = df["percent"][x]
    else:
        counter = 0
        indexHolder+=1
        percentage[indexHolder][counter] = df["percent"][x]
        
    counter+=1
fig = px.imshow(percentage,
                labels=dict(x="Seat Letter", y="Seat Number", color="Percent 0-100"),
                x=['A', 'B', 'C', 'D', 'E', 'F'],
                y=['8', '9', '10', '11', '12', '13','14','15','16','17','18','19','20','21','22','23','24','25','26','27'], height=400, width=300
               )

with tab2: 
    st.markdown("<h1 style='text-align: center; color: red;'></h1>", unsafe_allow_html=True)
    st.write(df)
    st.write(fig)
    st.write(
    """
    ## Symptoms include:
    In Children
    - Fast breathing or trouble breathing
    - Bluish lips or face
    - Ribs pulling in with each breath
    - Chest pain
    - Severe muscle pain (child refuses to walk)
    - Dehydration (no urine for 8 hours, dry mouth, no tears when crying)
    - Seizures
    - Fever above 104 degrees Fahrenheit that is not controlled by fever-reducing medicine
    - In children younger than 12 weeks, any fever
    - Fever or cough that improve but then return or worsen
    - Worsening of chronic medical conditions    
    In Adults
    - Difficulty breathing or shortness of breath
    - Persistent pain or pressure in the chest or abdomen
    - Persistent dizziness, confusion, inability to arouse
    - Seizures
    - Not urinating
    - Severe muscle pain
    - Severe weakness or unsteadiness
    - Fever or cough that improve but then return or worsen
    - Worsening of chronic medical conditions
    """
)

counter = 0
indexHolder = 0
for x in range(df.shape[0]):
    df["percent"][x] = random.randrange(100)

for x in range(df.shape[0]):
    if(counter < 6):
        percentage[indexHolder][counter] = df["percent"][x]
    else:
        counter = 0
        indexHolder+=1
        percentage[indexHolder][counter] = df["percent"][x]
        
    counter+=1
fig = px.imshow(percentage,
                labels=dict(x="Seat Letter", y="Seat Number", color="Percent 0-100"),
                x=['A', 'B', 'C', 'D', 'E', 'F'],
                y=['8', '9', '10', '11', '12', '13','14','15','16','17','18','19','20','21','22','23','24','25','26','27'], height=400, width=300
               )

with tab3:
    st.markdown("<h1 style='text-align: center; color: red;'></h1>", unsafe_allow_html=True)
    st.write(df)
    st.write(fig)
    st.write(
    """
    ## Symptoms include:
    - Sore throat that can start very quickly
    - Pain when swallowing
    - Fever
    - Red and swollen tonsils, sometimes with white patches or streaks of pus
    - Petechiae — pronounced pi-TEE-kee-eye — on the soft or hard palate (tiny, red spots on the roof of the mouth)
    - Swollen lymph nodes in the front of the neck 
    """  
    )



