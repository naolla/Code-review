# AI Code Review Assignment (Python)

## Candidate
- Name: Naol Lamesa
- Approximate time spent: ~70 minutes

---

# Task 1:  Average Order Value

## 1) Code Review Findings
### Critical bugs
- The function divides by the total number of orders, including cancelled ones, which produces an incorrect average.
- Division by zero occurs when the input list is empty or all orders are cancelled.

### Edge cases & risks
- Empty order list.
- All orders cancelled.
- Missing `status` or `amount` keys.
- Non-numeric `amount` values.

### Code quality / design issues
- `count` is misleading; it does not represent the number of included orders.
- Assumes perfectly structured input without validation.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Count only non-cancelled orders.
- Use safe key access.
- Guard against division by zero.
- Use generator expressions instead of manual loops.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

### Testing Considerations
- Empty list input.
- All orders cancelled.
- Mixed cancelled and non-cancelled orders.


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- Incorrectly states that cancelled orders are excluded from the divisor.
- Does not mention division-by-zero behavior.

### Rewritten explanation
- This function calculates the average order value by summing the amounts of non-cancelled orders and dividing by the number of non-cancelled orders. If there are no valid orders, it safely returns 0.0.

## 4) Final Judgment
- Decision: Request Changes
- Justification: The original logic produces incorrect averages and can crash.
- Confidence & unknowns: High confidence after fix; assumes consistent order schema.

---

# Task 2: Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- Any string containing `@` is treated as a valid email, which leads to many false positives.

### Edge cases & risks
- Non-string inputs (e.g., `None`, numbers) are not handled safely.
- Strings like `"@"`, `"test@"`, or `"@test"` are incorrectly counted as valid.
- No validation of domain or top-level domain structure.

### Code quality / design issues
- Email validation logic is overly simplistic.
- The explanation claims correctness that the implementation does not provide.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Validate that each input is a string.
- Use a regular expression to check for a basic email structure (`username@domain.tld`).
- Use `re.fullmatch` to ensure the entire string matches the pattern.
- Keep the overall structure close to the original implementation.

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`.

### Testing Considerations
- Empty input list.
- Valid emails with different domains and TLD lengths.
- Clearly invalid emails (missing username, domain, or TLD).
- Non-string inputs such as `None` or integers.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- Overstates correctness of email validation.
- Does not clarify what “valid” means.
- Omits behavior for non-string inputs.

### Rewritten explanation
- This function counts email addresses that match a basic regular-expression pattern for common email formats. It ignores non-string values and emails that do not fully match the expected structure. The function safely returns zero for empty input.

## 4) Final Judgment
- Decision: Request Changes
- Justification: The original implementation performs incorrect validation and does not match its explanation.
- Confidence & unknowns: High confidence in the fix; the regex intentionally avoids full RFC-level validation.


# Task 3: Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- The function divides by the total number of values instead of valid values.
- Division by zero occurs when all values are `None`.
- `float(v)` may raise exceptions.

### Edge cases & risks
- Empty list.
- All values are `None`.
- Mixed numeric and non-numeric strings.

### Code quality / design issues
- Unsafe type assumptions.
- Misleading averaging logic.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Convert values safely.
- Count only successfully parsed numbers.
- Avoid explicit loops and guard against division by zero.

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
- Empty input.
- All invalid values.
- Mixed valid and invalid numeric strings.
- Large numeric inputs.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average.

### Issues in original explanation
- The original code does not compute a correct average.
- Does not safely handle invalid numeric conversions.

### Rewritten explanation
- This function computes the average of numeric measurement values by ignoring `None` and non-numeric inputs. Only successfully converted values are averaged, and the function returns 0.0 if no valid measurements exist.

## 4) Final Judgment
- Decision: Reject
- Justification: The original implementation is incorrect and unsafe.
- Confidence & unknowns: High confidence after correction.
