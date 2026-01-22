#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None
    else:
        best = 0
        for key in a_dictionary:
            if a_dictionary[key] > 0:
                best = a_dictionary[key]
        return best
