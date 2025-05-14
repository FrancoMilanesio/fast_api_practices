from app.config import SessionLocal
from app.adapters.database.models import OrderModel, OrderItemModel
from app.domain.models import Order

class OrderRepository:
    def __init__(self):
        self.db = SessionLocal()

    def save(self, order: Order):
        db_order = OrderModel(
            customer_id=order.customer_id,
            status=order.status,
            comment=order.comment,
        )
        self.db.add(db_order)
        self.db.commit()
        self.db.refresh(db_order)

        for item in order.items:
            db_item = OrderItemModel(order_id=db_order.id, product_id=item)
            self.db.add(db_item)
        self.db.commit()

        return db_order

    def list_orders(self):
        return self.db.query(OrderModel).order_by(OrderModel.id.asc()).all()
    
    def get_by_id(self, order_id: int):
        return self.db.query(OrderModel).filter(OrderModel.id == order_id).first()
    
    def update_status(self, order_id: int, status: str):
        order = self.get_by_id(order_id)
        if order:
            order.status = status
            self.db.commit()
            self.db.refresh(order)
        return order
    
    def update_comment(self, order_id: int, comment: str):
        order = self.get_by_id(order_id)
        if order:
            order.comment = comment
            self.db.commit()
            self.db.refresh(order)
        return order
