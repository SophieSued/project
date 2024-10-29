import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import requests
from io import BytesIO

app = FastAPI()

# Cargar el modelo entrenado
MODEL_PATH = "trained_model_2.keras"
model = load_model(MODEL_PATH)

# Definir las clases (0 -> Sano, 1 -> Infectado)
CLASSES = ["Infectado", "Sano"]

@app.post("/analyze_image/")
async def analyze_image(url: str):
    try:
        # Descargar la imagen desde la URL
        response = requests.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="No se pudo descargar la imagen")

        # Abrir la imagen y preprocesarla
        img = Image.open(BytesIO(response.content))
        img = img.resize((100, 100))
        img_array = np.array(img)
        img_array = np.expand_dims(img_array, axis=0)

        # Realizar la predicción
        prediction = model.predict(img_array)
        predicted_class = np.argmax(prediction, axis=1)[0]

        # Traducir la clase en 'sano' o 'infectado'
        result = CLASSES[predicted_class]

        # Responder con la predicción
        return {"message": "Analysis successful", "prediction": result, "model output": str(prediction)}

    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Error processing image: {str(e)}"})
