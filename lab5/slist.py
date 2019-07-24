def main():
    first_repeat=[]
    word=0
    while word !="":
        word=input("Enter a word: ")
        i=1
        while i<len(word):
            if word[0]==word[i]:
                first_repeat.append(word)
            i+=1

    print(first_repeat)
main()
