from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import os
from collector import collect_data
import asyncio

app = FastAPI()

@app.on_event("startup")
async def schedule_data_collection():
    async def periodic():
        while True:
            print("[Background] Collecting AtCoder statistics...")
            try:
                collect_data()
            except Exception as e:
                print(f"[Background] Error: {e}")
            await asyncio.sleep(3 * 60 * 60)  # 3 hours
    asyncio.create_task(periodic())

@app.post("/collect")
def collect():
    try:
        result = collect_data()
        return {"message": "Data collected and files saved.", "files": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/json/{filename}")
def get_json(filename: str):
    file_path = os.path.join("json", filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path, media_type="application/json")
