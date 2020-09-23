from typing import List, Tuple


def prep_text(self, text: str) -> Tuple[str, List]:
    inline_code_tuples = []
    start = -1
    c = 0
    result = ""
    for char in text:
        if char == '`':
            if start == -1:
                start = c
            else:
                inline_code_tuples.append((start, c - 1))
                start = -1
        else:
            result = result + char
            c = c + 1

    return result, inline_code_tuples
