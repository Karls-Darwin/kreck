### Feedback for Exercise Set 6

Run on March 11, 17:41:02 PM.

+ :white_check_mark: Change into directory "exercise6".

+ :white_check_mark: Check that file "ex6a.py" exists.

+ :white_check_mark: Check that file "ex6b.py" exists.

+ :white_check_mark: Check that file "ex6c.py" exists.

+ :white_large_square: Check that file "ex6d.py" exists.

     "ex6d.py" not found.

#### Running Unit Tests

Exercise 6a: Strings and Lists

+ :white_check_mark: Run unit test of `wordlist('It was the best of times, it was the worst of times; it was the age of wisdom,            it was the age of foolishness')`

+ :white_check_mark: Run unit test of `wordlist('This is fun, CSCI1133 is my favorite class,      go python')`

+ :white_check_mark: Run unit test of `main()`
```python
"""The goal of this program is to create a function called
   wordlist that will take in a string (prose), and return a list
   of the unique words in that prose piece."""

def wordlist(prose): #start of function  definition
    uniqueWordsList = []
    proseToArray = prose.split(' ') #create a list of all the words
    for words in proseToArray: #create a loop to itterate through each word
        #Make the word lowercase
        strippedWord = words.lower()
        removedPunctuation = "" #remove the punctuation from the words
        for ch in strippedWord:
            if ch.isalpha() or ch.isnumeric(): #if the character is a letter or number add it to new string
                removedPunctuation += ch
        if removedPunctuation not in uniqueWordsList and removedPunctuation != "":
            #if word is not in the unique list, then add it
            uniqueWordsList.append(removedPunctuation)
    return uniqueWordsList #return the uniqueWordsList


#end of wordlist function definition
def main():
    userProse = input("Enter a prose piece: ")
    print(wordlist(userProse))


if __name__ == '__main__':
    main()

```

Exercise 6b: Word Separation

+ :white_check_mark: Run unit test of `separate('StopAndSmellTheRoses')`

+ :white_check_mark: Run unit test of `combine('Two roads diverged in a yellow wood')`

+ :white_check_mark: Run unit test of `main()`
```python
""""
   The goal of this program is to write two pure functions;
   separate and combine.  Separate will take a string in
   camel case and separate it into a sentence.  Combine will take
   a sentence and combine it into a camel case string."""


def separate(phrase):
    index = 1
    separatedWord = phrase[0] #start a string to add to
    while index < len(phrase):
        if phrase[index].isupper():
            #if letter is upercase then add a space, then that letter lowercase
            separatedWord += " "
            separatedWord += phrase[index].lower()
        else:
            #add the letter to the separated string
            separatedWord += phrase[index]
        index += 1

    return separatedWord


def combine(phrase):
    combinedWord = ''
    index = 0
    while index < len(phrase):
        if phrase[index] == " ":
            #if the letter is a space, don't add it
            index += 1
            #add the next character uppercase if it is still a valid index
            if index < len(phrase):
                combinedWord += phrase[index].upper()
        else:
            combinedWord += phrase[index]
        index += 1

    return combinedWord


def main():
    done = False
    while not done:
        userString = input("Enter a phrase: ")
        camelCase = combine(userString)
        print(separate(camelCase))
        cont = input("Shall we enter another phrase? (y/n) ")
        if cont == "n":
            done = True


if __name__ == '__main__':
    main()

```

Exercise 6c: Pig Latin Translator

+ :white_check_mark: Run unit test of `igpay('I can speak pig latin, can you?')`

+ :white_check_mark: Run unit test of `igpay('These are not the droids you are looking for')`

+ :white_check_mark: Run unit test of `main()`
```python
# define an english to pig latin translator

def translateWord(s): #helper function for igpay
    isVowel = 'aeiou'
    translatedString = ''

    valid = True
    if s[0].lower() in isVowel:

        translatedString = s + 'way'
        valid = False

    cnt = 1
    while valid:

        if s[cnt] in isVowel:

            translatedString = s[cnt:] + s[:cnt] + 'ay'
            valid = False
        cnt += 1

    return translatedString


def igpay(phrase): #igpay translater
    punctuation = "!.,?:;"
    phrase = phrase.strip()
    fullyTranslatedString = ''
    helperList = [] #store seperate words in here
    phrase = phrase.lstrip()
    helperList = phrase.split(' ')

    for x in range(len(helperList)):

        if ord(helperList[x][0]) in range(ord('A'), ord('Z')+1):

            if helperList[x][-1] in punctuation:

                partial = translateWord(helperList[x][:-1])
                partial = partial.lower()
                fullyTranslatedString += partial[0].upper() + partial[1:] + helperList[x][-1] + ' '

            else:
                partial = translateWord(helperList[x])
                partial = partial.lower()
                fullyTranslatedString += partial[0].upper() + partial[1:] + ' '
        else:

            if helperList[x][-1] in punctuation:

                partial = translateWord(helperList[x][:-1])
                fullyTranslatedString += partial + helperList[x][-1] + ' '
            else:

                fullyTranslatedString += translateWord(helperList[x]) + ' '

    return fullyTranslatedString


def main():
    english = input('Please enter an english phrase to translate: ')
    pigLatin = igpay(english)
    print('Pig Latin: ', pigLatin)


if __name__ == "__main__":

    main()

```

Exercise 6d: Telephone Number Translater

+ :white_large_square: Run unit test of `charNumber('Z')`
```
FAIL 
Traceback (most recent call last):
    self.student_module = importlib.import_module(module_name)
  File "/usr/lib/python3.5/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 986, in _gcd_import
  File "<frozen importlib._bootstrap>", line 969, in _find_and_load
  File "<frozen importlib._bootstrap>", line 956, in _find_and_load_unlocked
ImportError: No module named 'ex6d'
```

+ Skip: Run unit test of `telTranslate('1-800-TEL-PHON')`

  This test was not run because of an earlier failing test.

+ Skip: Run unit test of `main()`

  This test was not run because of an earlier failing test.

