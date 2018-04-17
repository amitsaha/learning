message = [ 'e', 'k', 'a', 'c', ' ',
            'd', 'n', 'u', 'o', 'p', ' ',
            'l', 'a', 'e', 't', 's']

def reversed_words(message):
    cur_pos = 0
    end_pos = len(message)
    current_word_start = cur_pos

    while cur_pos < end_pos:
        if message[cur_pos] == ' ':
            message[current_word_start:cur_pos] = reversed(message[current_word_start:cur_pos])
            current_word_start = cur_pos + 1
        if cur_pos == end_pos - 1:
            message[current_word_start:end_pos] = reversed(message[current_word_start:end_pos])
        cur_pos += 1

reversed_words(message)

# Prints: 'steal pound cake'
print(''.join(message))
