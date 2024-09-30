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
    
    try:
        file_path = f"C:\\Users\\hp\\OneDrive\\Documents\\gfg\\{file.filename}"

                # Guardar el archivo en el sistema
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        
        return {"message": "File saved successfully"}
    
    except Exception as e:
        return {"message": str(e)}