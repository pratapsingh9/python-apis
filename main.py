from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/{url}")
def root(url:str):
    return {
        "status":"msg send successfully",
        "Url": url
    }