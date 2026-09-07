from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os


from app.api.v1.routers import detection,auth,patient,clinical_visit

app=FastAPI(title="Clinical Decision Support System Backend")


app.include_router(auth.router)
app.include_router(patient.router)
app.include_router(clinical_visit.router)
app.include_router(detection.router)


os.makedirs("uploads", exist_ok=True)
app.mount("/uplaods", StaticFiles(directory="uploads"), name="uploads")

@app.get("/test")
def test():
    return{
        "message":"welcome to our clinical support system backend"
    }