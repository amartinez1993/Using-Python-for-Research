sentence = 'Jim quickly realized that the beautiful gowns are expensive'

count_letters = {}

for l in sentence:
    if l in alphabet:
        if l in count_letters:
            count_letters[l] += 1
        else:
            count_letters[l] = 1
