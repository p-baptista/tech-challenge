from fastapi import FastAPI
from router.api import router

app = FastAPI(
    debug=True,
    title="Tutorial",
)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)