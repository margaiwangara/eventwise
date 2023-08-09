from fastapi import APIRouter

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)


@router.get("/tickets")
def get_tickets():
    return {"tickets": []}


@router.get("/tickets/{ticket_id}")
def get_ticket(ticket_id: str):
    return {"ticket": {}}


@router.post("/tickets")
def create_ticket():
    return {"ticket": {}}


@router.put("/tickets/{ticket_id}")
def update_ticket(ticket_id: str):
    return {"ticket": {}}


@router.delete("/tickets/{ticket_id}")
def delete_ticket(ticket_id: str):
    return {"ticket": {}}
