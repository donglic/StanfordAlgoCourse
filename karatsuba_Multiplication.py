def karatsuba(x: int, y: int) -> int:
    # Base case for recursion
    if x < 10 or y < 10:
        return x * y

    # Calculates the size of the numbers
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Split x and y
    high1, low1 = divmod(x, 10**m)
    high2, low2 = divmod(y, 10**m)

    # 3 recursive calls
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)

    # Combine the results using the Karatsuba formula
    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0

# This block runs only when the script is executed directly
if __name__ == "__main__":
    # Example test cases
    a = 12345678
    b = 87654321

    print("Multiplying:", a, "*", b)
    result = karatsuba(a, b)
    print("Karatsuba result:", result)
    print("Built-in multiplication:", a * b)
    print("Correct:", result == a * b)