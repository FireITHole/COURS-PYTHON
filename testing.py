def add(x: float, y: float) -> int:
    return x + y

for i in range(1, 10):
    try:
        assert add(i, i) == i*2
        print(f"add({i}, {i}) == {i*2} passed!")
    except AssertionError:
        print(f"Test failed : {i} + {i} != {add(i, i)}")
