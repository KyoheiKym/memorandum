import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import sklearn
import statsmodels.formula.api as sm
import scipy


Book1 = pd.read_csv("Book1.csv") #data install

#To remove NaN from pd.series
Isnull = Book1["0.10%"].isnull()
Hasvalue = np.logical_not(Isnull)
Book1["0.10%"][Hasvalue]












