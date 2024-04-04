def get_expo(num: int, count: int) -> int:
    if count <= 0:
        return num
    
    count -= 1
    return get_expo(num ** 2, count)

# print(get_expo(2, 3))

def sum_list(list: list) -> int:
    if len(list) == 1:
        return list[0]
    
    length = len(list)
    left = list[:length//2]
    right = list[length//2:]

    # print(f"left: {left}, right: {right}")

    return sum_list(left) + sum_list(right)

print(sum_list(range(1, 101)))
print(sum(range(1, 101)))

def factoriel(n: int) -> int:
    if n == 1:
        return 1

    return n * factoriel(n-1)

print(factoriel(5))