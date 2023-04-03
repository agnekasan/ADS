def word_counter(s):
    words = {}
    for word in s.split():
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
            #print(word)
    sorted_words = {key: value for key, value in sorted(words.items())}
    # print(words)
    # print(sorted_words)
    for key, value in sorted_words.items():
        print(key, value)

word_counter("We tried list and we tried dicts also we tried Zen")