from fastapi import FastAPI

from app.api.v1.routers import pathogens,patient,antibiotic

app=FastAPI(title="Clinical Decision Support System Backend")



app.include_router(patient.router)

app.include_router(pathogens.router)
app.include_router(antibiotic.router)


@app.get("/test")
def test():
    return{
        "message":"welcome to our clinical support system backend"
    }