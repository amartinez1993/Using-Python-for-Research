message = "hi my name is caesar"

encoding_list = []
for char in message:
    position = positions[char]
    encoded_position = (position + 1) % 27
    encoding_list.append(alphabet[encoded_position])
encoded_message = "".join(encoding_list)
