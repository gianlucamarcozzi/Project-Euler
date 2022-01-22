def fibonacci(n):
    """
    Value of the n-th term in the Fibonacci sequence.
    Fibonacci sequence is defined as:
    fibonacci(0) = 1
    fibonacci(1) = 1
    fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)

    @param int n: index of the term of the Fibonacci sequence (n >= 0)

    @return int: value of the n-th term of the Fibonacci sequence
    """
    if n < 0:
        raise Exception('The function fibonacci takes in input only int >= 0')
    elif n == 0:
        return 1
    elif n == 1:
        return 2

    return fibonacci(n-1) + fibonacci(n-2) 

def fibonacci_index(value):
    """
    @param float value:

    @return int: maximum index n such that fibonacci(n) < value
    """
    n = 1
    while fibonacci(n) < value:
        n += 1
    return n


