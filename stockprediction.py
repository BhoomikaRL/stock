

import tensorflow as tf
import pandas as pd
import numpy as np


Testdata=pd.read_csv('Google_Stock_Price_Test.csv')
Traindata=pd.read_csv('Google_Stock_Price_Train.csv')

import re

sample=[]
for data in Traindata:
    i=re.sub(',','',str(data))
    i=i[2:-2]
    sample.append([float(i)])
    
sample=np.array(sample)
sample=[int(x[0]) for x in sample]

from sklearn.preprocessing import MinMaxScaler
mScaler=MinMaxScaler(feature_range=(0,1))
Testdata=mScaler.fit_transform(Traindata)


xTrain=Traindata[:-1,:]
yTrain=Traindata[1:,:]

xTrain=np.reshape(xTrain,(xTrain.shape[0],xTrain.shape[1],1))

realStock=pd.read_csv('Google_Stock_Price_Test.csv')

realStock=realStock.iloc[:,4:5].values

plt.plot(realStock,'r')

inpStock=mScalar.transform(realStock)

inpStock=inpStock.reshape(inpStock,(20,1,1))

model.predict()

plt.plot(realStock,'r')





