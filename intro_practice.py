import pandas as pd
import numpy as np 

num = 0
str = ""
list = [] 
dict = {
    "ls": [],
    "dt": {},
    "var": 0
}

def func(systole, diastole):
    print("systole:" , systole)
    print("diastole:" , diastole)
    if((systole <120) and (diastole <80)):
        return ("Normal Blood Pressure")
    else: 
        return ("High Blood pressure")

x = (func(110, 75))
print (x)
print (func (180, 90))

