import pandas as pd
import plotly.express as px
import random as rand
import math
import numpy as np


#chooses the correct template build function based on the option chosen
def airplaneBuilder(airplane):
    if(airplane == "airbusA319"):
        return airbusA319SeatingBuilder()

#template for the airbusA319
def airbusA319SeatingBuilder():
    seatingList = []
    
    for x in range(8, 28):
        for y in range(1,7):
            if(y == 1):
                seatingList.append(str(x)+"A")
            elif(y == 2):
                seatingList.append(str(x)+"B")
            elif(y == 3):
                seatingList.append(str(x)+"C")
            elif(y == 4):
                seatingList.append(str(x)+"D")
            elif(y == 5):
                seatingList.append(str(x)+"E")
            else:
                seatingList.append(str(x)+"F")
          
    return seatingList



