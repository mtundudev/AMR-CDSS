from fastapi import FastAPI

from app.api.v1.routers import detection

app=FastAPI(title="Clinical Decision Support System Backend")



app.include_router(detection.router)

@app.get("/test")
def test():
    return{
        "message":"welcome to our clinical support system backend"
    }