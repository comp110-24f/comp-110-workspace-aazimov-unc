def factorial(n: int) -> int:
    """Calculates factorial of int n."""
    # Edge case
    if n < 0:
        return -1
    # Base case
    if n == 1 or n == 0:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)


print(factorial(6))
