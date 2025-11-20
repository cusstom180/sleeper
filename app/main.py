from fastapi import FastAPI

app = FastAPI(title="Sleeper API")


@app.get("/")
async def read_root():
    return {"message": "Hello from Sleeper!"}


@app.get("/health")
async def health_check():
    return {"status": "ok"}



