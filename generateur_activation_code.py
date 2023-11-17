from random import choices
from string import ascii_uppercase

NUMBERS = "0123456789"


def generate_activation_code(
    nombre: int, length=5, char_length=5, separator="-"
) -> list[str]:
    results = []

    while len(results) < nombre:
        result = []
        while len(result) < length:
            result.append("".join(choices((*ascii_uppercase, *NUMBERS), k=char_length)))

        results.append(separator.join(result))

    return results


print(generate_activation_code(10, 3, 6, "_"))
