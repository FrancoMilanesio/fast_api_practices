from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config import Base

class OrderModel(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, index=True)
    status = Column(String, default='pending')
    comment = Column(String)

    items = relationship("OrderItemModel", back_populates="order")


class OrderItemModel(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer)

    order = relationship("OrderModel", back_populates="items")