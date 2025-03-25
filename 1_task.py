def caching_fibonacci():

    cache = {}

    def fibonacci(n):

        if n <= 0:
            return 0
        if n == 1:
            return 1

        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # Return the inner function
    return fibonacci


# Example usage
if __name__ == "__main__":
    fib = caching_fibonacci()

    print(fib(10))
    print(fib(15))
    print(fib(5))

    print(fib(10))
