import string

def wordlist(prose):
    no_punc=''
    for letter in prose:
        letter=letter.lower()
        
        if letter not in string.punctuation:
            no_punc+=letter

    plist=no_punc.split(" ")
    wordlist=[]
    for i in plist:
        if i not in wordlist:
            wordlist.append(i)


    wordlist.remove("")
    return wordlist

def main():
    prose=input("Enter prose: ")
    print (wordlist(prose))



if __name__ == '__main__':
    main()
