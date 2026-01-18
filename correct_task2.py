# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.
def count_valid_emails(emails):
    count = 0

    for email in emails:
        # Basic email structure check
        if isinstance(email, str) and email.count("@") == 1:
            parts = email.split("@")
            if parts[0] and parts[1]:
                count += 1

    return count
