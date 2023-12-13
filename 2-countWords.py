def count_word_occurrences(xt):
    text = xt.lower().split()
    print(text)
    words = {}

    for i in text:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
            
    print(words)

count_word_occurrences("A man a plan a canal Panama")


    
