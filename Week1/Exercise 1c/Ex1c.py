sentence = 'Jim quickly realized that the beautiful gowns are expensive'

count_letters = {}

# Create your function here!
def counter (input_string):
    for l in sentence:
        if l in alphabet:
            if l in count_letters:
                count_letters[l] += 1
            else:
                count_letters[l] = 1
    return count_letters

counter(sentence)
