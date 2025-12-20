import random

s="i love cooking food. i love playing chess. i like singing"
w=s.split()
print(w)
word_dict={}
#Create Dictionary of word pair
for i in range(len(w)-1):
    word=w[i]
    next_word=w[i+1]
    print(f'i : {i} {word} ":" {next_word}')
    if word not in word_dict:
        word_dict[word]=[]
    if next_word not in word_dict[word]:
        word_dict[word].append(next_word)

print(word_dict)


