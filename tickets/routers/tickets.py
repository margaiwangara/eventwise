from fastapi import APIRouter, HTTPException, Request, Path
from models.connect import DB_DEPENDENCY
from models.ticket import Ticket, TicketRequest
from starlette import status
from utils.auth import require_auth

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)


@router.get("/", status_code=status.HTTP_200_OK)
def get_tickets(request: Request, db: DB_DEPENDENCY):
    user = require_auth(request)

    tickets = db.query(Ticket).filter(Ticket.user_id == user.get("id")).all()
    return tickets


@router.get("/{ticket_id}", status_code=status.HTTP_200_OK)
def get_ticket(request: Request, db: DB_DEPENDENCY, ticket_id: int = Path(gt=0)):
    user = require_auth(request)

    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).filter(
        Ticket.user_id == user.get("id")).first()

    if ticket is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Ticket not found")

    return ticket


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_ticket(request: Request, db: DB_DEPENDENCY, ticket: TicketRequest):
    user = require_auth(request)

    ticket = Ticket(**ticket.model_dump(), user_id=user.get("id"))

    db.add(ticket)
    db.commit()


@router.put("/{ticket_id}", status_code=status.HTTP_204_NO_CONTENT)
def update_ticket(request: Request, db: DB_DEPENDENCY, input_ticket: TicketRequest, ticket_id: int = Path(gt=0)):
    user = require_auth(request)

    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).filter(
        Ticket.user_id == user.get("id")).first()

    if ticket is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Not found")

    ticket.title = input_ticket.title
    ticket.price = input_ticket.price

    db.add(ticket)
    db.commit()


@router.delete("/{ticket_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ticket(request: Request, db: DB_DEPENDENCY, ticket_id: int = Path(gt=0)):
    user = require_auth(request)

    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).filter(
        Ticket.user_id == user.get("id")).first()

    if ticket is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Not found")

    db.delete(ticket)
    db.commit()
