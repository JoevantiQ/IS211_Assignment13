# recursion.py

def fibonacci(n):
    """Return the nth Fibonacci number using recursion."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def gcd(a, b):
    """Return the greatest common divisor of a and b using Euclid's algorithm."""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def compareTo(s1, s2):
    """
    Recursively compare two strings.
    Return negative if s1 < s2, 0 if s1 == s2, positive if s1 > s2.
    """
    if not s1 and not s2:
        return 0
    if not s1:
        return -ord(s2[0])
    if not s2:
        return ord(s1[0])
    if s1[0] != s2[0]:
        return ord(s1[0]) - ord(s2[0])
    return compareTo(s1[1:], s2[1:])

def main():
    # Demo for Fibonacci
    print("Fibonacci(10):", fibonacci(10))  # Expected: 55

    # Demo for GCD
    print("GCD(48, 18):", gcd(48, 18))      # Expected: 6

    # Demo for compareTo
    print("compareTo('apple', 'banana'):", compareTo("apple", "banana"))  # Negative
    print("compareTo('apple', 'apple'):", compareTo("apple", "apple"))    # 0
    print("compareTo('banana', 'apple'):", compareTo("banana", "apple"))  # Positive

if __name__ == "__main__":
    main()
