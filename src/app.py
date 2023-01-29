from app_func import *
import pandas as pd
import plotly.express as px
import random #just for random function
import math
import numpy as np
import streamlit as st


st.header(' Virus Detector ')
tab1, tab2, tab3 = st.tabs(["Covid", "Flu", "Fever"])

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
    #st.header("Covid-19")
    st.write(df)
    st.write(fig)
    st.write(
    """
    ## Symptoms include:
        Fever or chills
        Cough
        Shortness of breath or difficulty breathing
        Fatigue
        Muscle or body aches
        Headache

    """
)
with tab2: 
    st.header("Flu")
with tab3:
    st.header("Fever")
#st.write(fig)



