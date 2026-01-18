# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.
import re

def count_valid_emails(emails):
    count = 0
    # Basic email pattern (username@domain.tld)
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}"

    for email in emails:
        # Count only fully matching email strings
        if isinstance(email, str) and re.fullmatch(pattern, email):
            count += 1

    return count

