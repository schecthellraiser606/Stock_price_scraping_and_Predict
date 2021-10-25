from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import SimpleRNN
from tensorflow.keras.layers import GRU

class Keras_Model(object):
  def __init__(self, model_name, model_nummidle):
    self.model_name = model_name
    self.__nummiddle = model_nummidle
    self.__inoutDim = 1
  
  
  def build_model(self, length_of_sequences):
    # LSTMニューラルネットの構築
    model = Sequential()
    
    # RNN,LSTM、GRUを選択できるようにする
    if self.model_name == 'RNN':
      model.add(SimpleRNN(self.__nummiddle[0], batch_input_shape=(None, length_of_sequences, self.__inoutDim), return_sequences=True))
      model.add(Dropout(0.2))#念のためDropoutし、過学習を防ぐ
      for i in self.__nummiddle[1:]:
        model.add(SimpleRNN(i, return_sequences=False))
        model.add(Dropout(0.2))#念のためDropoutし、過学習を防ぐ
    
    if self.model_name == 'LSTM':
      model.add(LSTM(self.__nummiddle[0], batch_input_shape=(None, length_of_sequences, self.__inoutDim), return_sequences=True))
      model.add(Dropout(0.2))#念のためDropoutし、過学習を防ぐ
      for i in self.__nummiddle[1:]:
        model.add(LSTM(i, return_sequences=False))
        model.add(Dropout(0.2))#念のためDropoutし、過学習を防ぐ
    
    if self.model_name == 'GRU':
      model.add(GRU(self.__nummiddle[0], batch_input_shape=(None, length_of_sequences, self.__inoutDim), return_sequences=True))
      model.add(Dropout(0.2))#念のためDropoutし、過学習を防ぐ
      for i in self.__nummiddle[1:]:
        model.add(GRU(i, return_sequences=False))
        model.add(Dropout(0.2))#念のためDropoutし、過学習を防ぐ
    
    model.add(Dense(1))
    model.add(Activation("linear"))
    model.compile(loss="mean_squared_error", optimizer="adam")
    
    return model