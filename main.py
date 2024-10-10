import os
from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image



app = FastAPI()

# Cargar el modelo entrenado
MODEL_PATH = "trained_model_2.keras"
# MODEL_PATH = "model.weights.h5"
model = load_model(MODEL_PATH)

# Definir el directorio donde se guardará el archivo
UPLOAD_FOLDER = "uploads" # es la carpeta de uploads en visual

# Definir las clases (0 -> Sano, 1 -> Infectado)
CLASSES = ["Infectado", "Sano"]

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    try:
        # Crear la ruta completa del archivo
        # file_path = os.path.join(UPLOAD_FOLDER, file.filename)

        # Guardar el archivo en el sistema
        # with open(file_path, "wb") as f:
        #   f.write(await file.read()) 

        # Cargar y preprocesar la imagen para el modelo
        img = Image.open(file.file)  
        # img = img.convert('RGB')
        img = img.resize((100, 100))
        img_array = np.array(img) # / 255.0  
        img_array = np.expand_dims(img_array, axis=0)  
        
        # Realizar la predicción
        prediction = model.predict(img_array)
        print(prediction)
        predicted_class = np.argmax(prediction, axis=1)[0] 

        prediction = model.predict(img_array)
        print("Predicciones del modelo:", prediction) 


        # Traducir la clase en 'sano' o 'infectado'
        result = CLASSES[predicted_class]

        print(result)

        # Responder con la predicción
        return {"message": "File saved successfully", "prediction": result, "model output": str(prediction)}
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Error processing file: {str(e)}"})

