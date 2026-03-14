from fastapi import APIRouter, UploadFile, File, HTTPException
from app.engine.inference import engine
import numpy as np
import cv2
import io

router = APIRouter()

@router.post("/process/3d-reconstruction")
async def process_3d(file: UploadFile = File(...)):
    """
    Endpoint for submitting imagery for 3D scene reconstruction.
    """
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type. Image required.")
    
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    if img is None:
        raise HTTPException(status_code=400, detail="Could not decode image.")
    
    result = await engine.reconstruct_3d(img)
    return result

@router.post("/process/traffic-analysis")
async def process_traffic(file: UploadFile = File(...)):
    """
    Endpoint for real-time traffic analysis.
    """
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type. Image required.")
    
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    if img is None:
        raise HTTPException(status_code=400, detail="Could not decode image.")
    
    result = await engine.analyze_traffic(img)
    return result