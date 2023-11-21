from fastapi import APIRouter

router = APIRouter()

@router.get("/history/{event_id}")
async def read_event(event_id: int):
    return {"event_id": event_id}
