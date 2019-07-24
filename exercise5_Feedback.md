### Feedback for Exercise Set 5

Run on February 27, 17:50:47 PM.

+ :white_check_mark: Change into directory "exercise5".

+ :white_check_mark: Check that file "ex5a.py" exists.

+ :white_check_mark: Check that file "ex5b.py" exists.

+ :white_check_mark: Check that file "ex5c.py" exists.

+ :white_check_mark: Check that file "ex5d.py" exists.

#### Running Unit Tests

Exercise 5a: Matrix Data

+ :white_check_mark: Run unit test of `printMatrix([[4, 5, 6, 7, 8], [1, 2, 3, 4, 5], [5, 5, 5, 5, 5], [6, 7, 8, 9, 0]])`

+ :white_check_mark: Run unit test of `printMatrix([[1, 5, 6], [1, 2, 3], [5, 5, 5], [6, 7, 8]])`

+ :white_check_mark: Run unit test of `main()`
```python
# Exercise 5a

# mechanism for inputting and printing matrices

def getMatrix():
    matrix = []
    instring = input("enter values separated by commas: ")
    while instring != "":
        rowdata = list(eval(instring)) # converting input to list
        matrix += [rowdata]
        instring = input("enter values separated by commas: ")
    return matrix


def printMatrix(m):
    printstring = ""
    for row in m:
        for value in row:
            printstring += str(value) + "\t" # data separated by tabs
        printstring += "\n" # separating rows
    print(printstring)

def main():
    printMatrix(getMatrix())

if __name__ == "__main__":
    main()

```

Exercise 5b: Matrix Addition

+ :white_check_mark: Run unit test of `matrixSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[0, 0, 0], [1, 1, 1], [2, 2, 2]])`

+ :white_check_mark: Run unit test of `sizeMatch([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[0, 0, 0], [1, 1, 1], [2, 2, 2]])`

+ :white_large_square: Run unit test of `main()`
```
FAIL 
Traceback (most recent call last):
    student_ans = tools.handle_input(student_fn, self.fn_args, self.inputs)
    retvalue = fn(*args)
  File "/ex5b.py", line 43, in main
    if sizeMatch(a,b):
  File "/ex5b.py", line 14, in sizeMatch
    colsB=len(B[0])
IndexError: list index out of range
```

Exercise 5c: List Insertion

+ :white_check_mark: Run unit test of `insertString(['fun', 'hello', 'this'], 'is')`

+ :white_check_mark: Run unit test of `insertString(['alpha', 'numeric', 'why', 'zed'], 'computer')`

+ :white_check_mark: Run unit test of `main()`
```python
# Exercise 5c

# takes an ordered list of strings and inserts a new string
# in lexicographic order (returns a new list)

def insertString(alist, newstr):
    newlist = [] # creates a new list to be returned
    if len(alist) == 0: # if we passed an empty list
        newlist += [newstr]
        return newlist
    i = 0
    while i < len(alist) and alist[i] < newstr: # lexicographic comparison
        newlist += [alist[i]]
        i += 1
    newlist += [newstr]
    while i < len(alist): # adding the remaining strings
        newlist += [alist[i]]
        i += 1
    return newlist

def main():
    wordlist = []
    word = input("enter a word: ")
    while word != "":
        wordlist = insertString(wordlist, word)
        word = input("enter a word: ")
    for word in wordlist:
        print(word)

if __name__ == "__main__":
    main()

```

Exercise 5d: Shortest Distance

+ :white_large_square: Run unit test of `shortestDist([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]])`
```
FAIL 
Traceback (most recent call last):
    self.student_module = importlib.import_module(module_name)
  File "/usr/lib/python3.5/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 986, in _gcd_import
  File "<frozen importlib._bootstrap>", line 969, in _find_and_load
  File "<frozen importlib._bootstrap>", line 958, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 673, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 661, in exec_module
  File "<frozen importlib._bootstrap_external>", line 767, in get_code
  File "<frozen importlib._bootstrap_external>", line 727, in source_to_code
  File "<frozen importlib._bootstrap>", line 222, in _call_with_frames_removed
  File "/ex5d.py", line 6
    def getMatrix():
      ^
IndentationError: expected an indented block
```

+ Skip: Run unit test of `shortestDist([[5, 2, 3, 3], [0, 3, 7, 5], [8, 4, 4, 2], [1, 5, 8, 0]])`

  This test was not run because of an earlier failing test.

+ Skip: Run unit test of `main()`

  This test was not run because of an earlier failing test.

