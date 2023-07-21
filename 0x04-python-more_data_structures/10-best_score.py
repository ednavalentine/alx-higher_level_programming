#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        if not a_dictionary:
            return None
        maxscore_key = None
        maxscore = float('-inf')
        for inkkey, keyvalue in a_dictionary.items():
            if isinstance(keyvalue, int) and keyvalue > maxscore:
                maxscore = keyvalue
                maxscore_key = inkkey
        return maxscore_key
