from fastapi.responses import HTMLResponse
from fastapi import FastAPI, UploadFile, File
from langchain_community.document_loaders import PyPDFLoader
from typing import List
from vectordatabase import save_embeddings
import os

app = FastAPI(title='Upload files to vectore database')

@app.get("/")
async def read_root():
    context = """
    <html>
	<head>
		<title>Add new files</title>
	</head>
    <body>Simple API for upload docs in our vectore database</body>
    </html>
    """
    return HTMLResponse(context)

@app.post("/upload-pdf/")
async def upload_pdf(
    files: List[UploadFile] = File(...),
    coleccion: str="Constitucion"):
    try:
        for file in files:
            file_location = f"temp_{file.filename}"
            with open(file_location, "wb") as f:
                f.write(await file.read())
            loader = PyPDFLoader(file_location)
            documents = loader.load()
            save_embeddings(documents,coleccion)
            # Remove temp file
            os.remove(file_location)
        return {"message":"Embeddings save in database"}
    except Exception as e:
        return {"message":f"Error {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
