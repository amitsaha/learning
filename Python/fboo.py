master = 'facebook'
uniq_letters = set(master)

# number of each unique letters in facebook

l_count = {}
for l in uniq_letters:
    l_count[l] = master.count(l)

# In l_words we have how many letters of each of the letters
# of 'facebook' is present

l_words = {}
def num_stickers(words):
    words = [w for w in words if w in master]
    for l in uniq_letters:
        l_words[l] = words.count(l)
    
    tot_stickers = 1
    for k in l_words.keys():
        if l_words[k] > l_count[k]:
            current_stickers = (l_words[k] /l_count[k])+ (l_words[k] % l_count[k])
            if current_stickers > tot_stickers:
                tot_stickers = current_stickers
                
    print tot_stickers


num_stickers('ffacebook zdfgg')
