from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import io
import cv2
import base64
import os
import numpy as np
app = FastAPI()

# Setup CORS (Cross-Origin Resource Sharing)
#origins = ["*"]  # You might want to change this to a more restrictive list of allowed origins
#app.add_middleware(
    #CORSMiddleware,
    #allow_origins=origins,
    #allow_credentials=True,
    #allow_methods=["*"],
    #allow_headers=["*"],
#)

@app.get("/")
def func():
    return {"name":"plantasap"}
@app.post("/save_image")
def save_and_convert_image(base64_image:str):
    # Decode base64 image
    image_data = base64.b64decode(base64_image)
    image = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)

    # Save the original image
    original_path = "original_image.jpg"
    cv2.imwrite(original_path, image)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image
    gray_path = "gray_image.jpg"
    cv2.imwrite(gray_path, gray_image)

    # Remove the original image

    return "Converted successfully"

@app.post("/delete-image")
async def delete_image(file: str):
    try:
        # contents = await file.read()
        # base64_image = base64.b64encode(contents).decode("utf-8")
        # result = save_and_convert_image(base64_image)
        # return {"message": result}
        os.remove(file)
        return "deleted"

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
