# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.
def calculate_average_order_value(orders):
    total = 0
    count = 0  # count only non-cancelled orders

    for order in orders:
        if order.get("status") != "cancelled":
            total += order.get("amount", 0)
            count += 1

    # Avoid division by zero
    return total / count if count > 0 else 0.0
