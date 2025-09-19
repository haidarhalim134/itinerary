import os
import json
from typing import List
from pydantic import BaseModel
from fastapi import FastAPI, Query
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.get("/api/test")
async def test_endpoint():
    import random
    return f"testing testing {random.randint(1, 100)}"