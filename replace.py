sentence= "Lorem Ipsum is simply dummy text of the printing and typesetting industry."

def capital():
    word=input("Please enter a word/letters which you want to replace")
    if word not in sentence:
        word =input("Please enter a correct word")
    new_word = sentence.replace(word, word.upper())
    return new_word

print(capital())
print(capital())