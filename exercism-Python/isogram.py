def is_isogram(string):
    string = string.lower()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    hash_map = {}
    for c in string:
        if c in letters and c not in hash_map:
            hash_map[c] = 1
        elif c in letters and c in hash_map:
            return False
    return True
