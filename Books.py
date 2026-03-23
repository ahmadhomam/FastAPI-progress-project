from fastapi import FastAPI     # importing the dependencies FastAPI from fastapi directory

app = FastAPI()                 # help the uvicorn(surver) to identify this application is FastAPI

@app.get("/api-endpoint")
async def first_api() :         # python function 
    return {"message" : "Hello User !"}