from fastapi import APIRouter
from app.application.commands import CreateOrderCommand, UpdateCommentOrderCommand
from app.application.handlers.command_handlers import handle_create_order, handle_cancel_order, handle_update_order_comment
from app.adapters.database.repositories import OrderRepository

router = APIRouter()

@router.post("/orders/")
def create_order(command: CreateOrderCommand):
    return handle_create_order(command)

@router.get("/orders/")
def list_orders():
    repo = OrderRepository()
    return repo.list_orders()

@router.put("/orders/{id_order}/cancel/")
def cancel_order(id_order: int):
    return handle_cancel_order(id_order)

@router.put("/orders/{id_order}/comment/")
def update_order_comment_order(id_order: int, command: UpdateCommentOrderCommand):
    return handle_update_order_comment(id_order, command)