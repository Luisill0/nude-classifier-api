import os
import io
import cv2

from fastapi import FastAPI, Request, File, UploadFile, HTTPException
from dotenv import load_dotenv, find_dotenv
from typing import List
from PIL import Image
from starlette.responses import RedirectResponse
from app.nude_classifier import Nude_Classifier

load_dotenv(find_dotenv())
prefix = os.getenv("CLUSTER_ROUTE_PREFIX", "").rstrip("/")

app = FastAPI(
    title="NSFW Classifier",
    version="0.5",
    description="Python API",
    openapi_prefix=prefix,
)

@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(f"{prefix}/docs")

def read_image(bin_data):
    """
    Load image, convert bytes to PIL matrix, saves it as jpg

    Arguments:
        bin_data {bytes} --Image binary data
    
    Returns:
        path to the saved image
    """
    image = Image.open(io.BytesIO(bin_data))
    image.save("image.jpg")
    return "image.jpg"

nsfw_classifier = Nude_Classifier('./models/classifier_model.onnx')

@app.post("/upload/classifier")
async def upload(files: List[UploadFile] = File(...)):
    images = []
    for file in files:
        #Is file format valid
        if((file.content_type != "image/jpeg") & (file.content_type != "image/png")):
            raise HTTPException(status_code=422, detail="The file format is invalid")
        
        #Read the image file
        try:
            contents = await file.read()
            path = read_image(contents)
            results = nsfw_classifier.classify(path)
            #image.show()
        except Exception:
            return {"message": "Error"}
        finally:
            await file.close()
    
    return results