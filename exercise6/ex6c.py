import string
def igpay(phrase):
    wordlist=phrase.split(" ")
    pyg=""
    for i in wordlist:
        index=vowel(i)
        if i==wordlist[0] and vowel(i)==0:
            pyg+=i+"way" + " "
        elif i==wordlist[0]:
            pyg+=i[index].upper()+ i[index+1:]+ i[:index].lower()+ "ay" + " "

        elif vowel(i)==0:
            if i[-1] in string.punctuation:
                pyg+=i[0:-1]+"way" + i[-1] + " "
            else:
                pyg+=i+"way" + " "
        else:
            if i[-1] in string.punctuation:
                pyg+=i[index:-1]+ i[:index].lower()+ "ay" + i[-1] + " "
            else:
                pyg+=i[index:]+ i[:index].lower()+ "ay" + " "

    return pyg



def vowel(word):
    vowels="aeiouAEIOU"
    i=0
    while i<len(word):
        if word[i] in vowels:
            return i
        i+=1






def main():
    phrase=input("Enter a phrase: ")
    print(igpay(phrase))


if __name__ == '__main__':
    main()
