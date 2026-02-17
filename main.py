from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Balance Inquiry API",
    description="Backend server for agent access with Swagger documentation",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PostBody(BaseModel):
    """Optional JSON body for POST - any key-value pairs."""

    class Config:
        extra = "allow"


@app.get("/")
async def get_params(request: Request) -> dict:
    """
    GET endpoint: pass any query parameters.
    They are returned in the response.
    """
    params = dict(request.query_params)
    return {
        "ok": True,
        "method": "GET",
        "params": params,
        "message": "Server received your parameters",
    }


@app.post("/")
async def post_params(request: Request, body: Optional[PostBody] = None) -> dict:
    """
    POST endpoint: pass query params and/or a JSON body.
    Both are returned in the response.
    """
    query_params = dict(request.query_params)
    payload = body.model_dump() if body else {}
    return {
        "ok": True,
        "method": "POST",
        "query_params": query_params,
        "body": payload,
        "message": "Server received your parameters",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
