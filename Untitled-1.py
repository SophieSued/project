import numpy as np

# Cargar el modelo guardado
model = load_model('modelo.keras')

# Datos de entrada de ejemplo
# Asegúrate de que las dimensiones coincidan con lo que espera tu modelo
input_data = np.array([[0.1, 0.2, 0.3, 0.4]])  # Ajusta según tu caso


# Hacer la predicción
prediction = model.predict(input_data)

# Imprimir la predicción
print(f'Predicción: {prediction}')
