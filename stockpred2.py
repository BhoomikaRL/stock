x=trainDataset[:-1,:]

y=trainDataset[1:,:]

from keras.model import Sequential 
from keras.layers import Dense
from keras.layers import LSTM

model=Sequential()

model.add(LSTM(units=32,activation='sigmoid',input_shape=(None,1)))

model.add(Dense(units=1))

model.compile(optimizer='adam',loss='mean_squared_error')

model.fit(x,y,epochs=100,batch_size=32)

realStock=pd.read_csv('Google_Stock_Price_Test.csv')

realStock=realStock.iloc[:,4:5].values

plt.plot(realStock,'r')
