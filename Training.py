import re

# data = [
#     "OrderID: 1001 | Customer: Alice | Total: $23.50",
#     "OrderID: 1002 | Customer: Bob | Total: $7.99",
#     "OrderID: 1003 | Customer: Charlie | Total: $105.00",
# ]

# order_ids = []
# customers = []
# totals = []
# TotalRevenue = 0

# for row in data:
#     match_order = re.search(r"OrderID:\s*(\d+)",row)
#     if match_order:
#         order_ids.append(match_order.group(1))
#     match_customer = re.search(r"Customer:\s*([^|]+)\s*\|",row) 
#     if match_customer:
#         customers.append(match_customer.group(1).strip())     
#     match_totals = re.search(r"\$(\d+(?:\.\d+)?)",row)
#     if match_totals:
#         match_totals_float = float(match_totals.group(1))
#         totals.append(match_totals_float)
#         TotalRevenue += match_totals_float




# print(order_ids)
# print(customers)
# print(totals)
# print(TotalRevenue)


# results = []

# for row in data:
#     match_order = re.search(r"OrderID:\s*(\d+)", row)
#     match_customer = re.search(r"Customer:\s*([^|]+)\s*\|", row)
#     match_totals = re.search(r"\$(\d+(?:\.\d+)?)", row)

#     record = {
#         "order_id": match_order.group(1) if match_order else None,
#         "customer": match_customer.group(1).strip() if match_customer else None,
#         "total": float(match_totals.group(1)) if match_totals else None
#     }

#     results.append(record)


x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)