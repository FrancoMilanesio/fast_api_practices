from pydantic import BaseModel
from typing import List

class CreateOrderCommand(BaseModel):
    customer_id: int
    items: List[int]
    comment: str

class UpdateCommentOrderCommand(BaseModel):
    comment: str