def is_pangram(sentence):
    sentence = sentence.lower()
    count = 0
    sent = 'abcdefghijklmnopqrstuvwxyz'
    dic = {}
    for c in sentence:
        if c in sent and c not in dic:
            dic[c] = 1
            count += 1
        elif c in sent and c in dic:
            dic[c] += 1
        else:
            continue
    return count == 26
