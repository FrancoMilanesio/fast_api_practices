class Order:
    def __init__(self, customer_id, items, comment, status='pending'):
        self.customer_id = customer_id
        self.items = items
        self.status = status
        self.comment = comment

    def cancel(self):
        if self.status == 'shipped':
            raise Exception("Can't cancel a shipped order.")
        self.status = 'cancelled'