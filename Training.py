import re

data = [
    "OrderID: 1001 | Customer: Alice | Total: $23.50",
    "OrderID: 1002 | Customer: Bob | Total: $7.99",
    "OrderID: 1003 | Customer: Charlie | Total: $105.00",
]

order_ids = []
customers = []
totals = []

for row in data:
    # Your regex here
    pass

print(order_ids)
print(customers)
print(totals)