def is_prime(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        if result > 1:
            for i in range(2, int(result**0.5)+1):
                if not result % i:
                    print("Составное")
                    break
            else:
                print("Простое")
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)



















