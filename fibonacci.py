def fibonnaci(n):
    if n <= 1:
        return n

    return fibonnaci(n - 1) + fibonnaci(n - 2)


print(fibonnaci(7))
# 1 1 2 3 5 8 13


def fibonacci2(target_index: int, current_index=1, result=[1, 1]):
    if target_index == current_index:
        return result

    current_index += 1
    result.append(result[-2] + result[-1])

    return fibonacci2(
        target_index,
        current_index,
        result
    )


print(fibonacci2(100))
