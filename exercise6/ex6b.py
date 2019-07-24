def separate(phrase):
    sep_phrase=""
    sep_phrase+=phrase[0]
    i=1
    while i<len(phrase):
        if phrase[i].isupper():
            sep_phrase+=" "
            sep_phrase+=phrase[i].lower()
        else:
            sep_phrase+=phrase[i]
        i+=1
    return sep_phrase


def combine(sep_phrase):
    com_phrase=""
    i=0
    while i<len(sep_phrase):
        if sep_phrase[i]==" ":
            com_phrase+=sep_phrase[i+1].upper()
            i+=2
        else:
            com_phrase+=sep_phrase[i]
            i+=1
    return com_phrase




def main():
    phrase=input("Enter a phrase: ")
    print(separate(combine(phrase)))

if __name__ == '__main__':
    main()
