def GM_fibo(n):
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

def GM_fibo_index(value):
    """
    @param float value:

    @return int: maximum index n such that fibonacci(n) < value
    """
    n = 1
    while fibonacci(n) < value:
        n += 1
    return n


def GM_is_palindrome(n):
    """
    @param int n
    @return bool
    """
    digits = [x for x in str(n)]
    for i in range(len(digits)//2):
        if digits[i] != digits[-i - 1]:
            return False
    return True


def GM_factorize(N):
    p_fact = {}
    for i in range(2, N):
        while not N % i:
            if p_fact[i] == None:
                p_fact[i] = 1
            else:
                p_fact[i] += 1
            N /= i
        if N == 1:
            return p_fact
    return -1

def GM_dividends(N):
    d = []
    for i in range(1, N//2 + 1):
        if not N % i:
            d.append(i)
    d.append(N)
    return d
