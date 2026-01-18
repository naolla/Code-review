# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.
def average_valid_measurements(values):
    total = 0
    count = 0  # count only valid numeric values

    for v in values:
        if v is None:
            continue
        try:
            total += float(v)
            count += 1
        except (TypeError, ValueError):
            continue

    # Avoid division by zero
    return total / count if count > 0 else 0.0
