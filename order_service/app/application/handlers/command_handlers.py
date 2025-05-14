from app.domain.models import Order
from app.application.commands import CreateOrderCommand, UpdateCommentOrderCommand
from app.adapters.database.repositories import OrderRepository

def handle_create_order(command: CreateOrderCommand):
    order = Order(customer_id=command.customer_id, items=command.items, comment=command.comment)
    repo = OrderRepository()
    return repo.save(order)

def handle_cancel_order(order_id: int):
    repo = OrderRepository()
    db_order = repo.get_by_id(order_id)
    
    if not db_order:
        raise Exception("Order not found")

    # Creamos objeto del dominio a partir del modelo de infraestructura
    domain_order = Order(
        customer_id=db_order.customer_id,
        items=[],
        status=db_order.status
    )

    domain_order.cancel()
    return repo.update_status(order_id, domain_order.status)

def handle_update_order_comment(order_id: int, command: UpdateCommentOrderCommand):
    repo = OrderRepository()
    db_order = repo.get_by_id(order_id)

    if not db_order:
        raise Exception("Order not found")
    
    return repo.update_comment(order_id, command.comment)
