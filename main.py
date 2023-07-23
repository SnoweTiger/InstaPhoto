from fastapi import FastAPI
import uvicorn

# from routers.instagram import instagram_router

app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "Dummy-InstaParser-response"}


# app.include_router(instagram_router)


# Run the API with uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
