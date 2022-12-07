#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    b_score = max(a_dictionary.values(), default=None)
    for x, y in a_dictionary.items():
        if y == b_score:
            return x
