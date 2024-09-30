import fastapi 
from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
import psycopg2
import uvicorn
from typing import Annotated
from fastapi import File, UploadFile

app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    print(file)
    return {"filename": file.filename}

# Define el directorio donde se guardará el archivo
UPLOAD_FOLDER = "C:\\Users\\48240152\\Downloads\\modelo"

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    try:
        # Crear la ruta completa del archivo
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)

        # Guardar el archivo en el sistema
        with open(file_path, "wb") as f:
            f.write(await file.read())  # `await` es necesario para manejar la lectura asincrónica del archivo
        
        # Responder con éxito
        return {"message": "File saved successfully", "file_path": file_path}
    
    except Exception as e:
        # Manejo de errores
        return {"message": f"Error saving file: {str(e)}"}