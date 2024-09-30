from math import ceil


def get_prime_numbers_to_n(n: int) -> list[int]:
    """
    Return a list of prime numbers up to n
    """
    prime_numbers = [2]

    for i in range(2, n):
        for j in range(2, ceil(i**0.5)+1):
            if not i % j:
                break
        else:
            prime_numbers.append(i)

    return prime_numbers


def get_x_primes_numbers(x: int) -> list[int]:
    """
    Return the first x prime numbers
    """
    prime_numbers = [2]

    compteur = 2
    while len(prime_numbers) < x:
        for i in range(2, ceil(compteur**0.5)+1):
            if not compteur % i:
                break
        else:
            prime_numbers.append(compteur)
        compteur += 1

    return prime_numbers


""" print(get_prime_numbers_to_n(100))
print(get_x_primes_numbers(100)) """


def get_prims_til_n_gen(n: int):
    if n >= 2:
        yield 2

    for i in range(2, n+1):
        for j in range(2, ceil(i**0.5)+1):
            if not i % j:
                break
        else:
            yield i


def get_x_first_primes_gen(x: int):
    yield 2

    i = 2
    compteur = 1

    while compteur < x:
        for j in range(2, ceil(i**0.5)+1):
            if not i % j:
                break
        else:
            yield i
            compteur += 1

        i += 1


for x in get_x_first_primes_gen(10):
    print(x)
