import tensorflow as tf

# Verificar que la importación funciona
print(tf.__version)

# Importar Keras de TensorFlow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Crear un modelo Keras simple
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(32,)))
model.add(Dense(10, activation='softmax'))

print("Modelo creado exitosamente.")