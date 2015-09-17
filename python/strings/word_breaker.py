# word breaker

words = ['hello',
         'world',
         'hand',
         'water',
         'bath']

s = 'hellowaterworld.com'

word_pos = []
cur_pos = 0
for pos in range(len(s)):
    if s[cur_pos:pos+1] in words:
        word_pos.append(s[cur_pos:pos+1])
        cur_pos = pos+1

print word_pos
