from fastapi import FastAPI

app= FastAPI()
@app.get("/")
async def root():
    return {"Name": "haqim"}

# To activate host uvicorn main:app --reload

