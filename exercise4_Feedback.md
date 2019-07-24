### Feedback for Exercise Set 4

Run on February 27, 23:42:20 PM.

+ :white_check_mark: Change into directory "exercise4".

+ :white_check_mark: Check that file "ex4a.py" exists.

+ :white_check_mark: Check that file "ex4b.py" exists.

+ :white_check_mark: Check that file "ex4c.py" exists.

+ :white_check_mark: Check that file "ex4d.py" exists.

+ :white_check_mark: Check that file "ex4e.py" exists.

#### Running Unit Tests

Exercise 4a: Binary To Decimal

+ :white_check_mark: Run unit test of `binaryToInt('1110101')`

+ :white_check_mark: Run unit test of `binaryToInt('1000101')`

+ :white_check_mark: Run unit test of `main()`
```python
# Exercise 4a

# Takes a binary string and converts to decimal value

def binaryToInt(binarystring):
    exponent = 0
    total = 0
    for idx in range(len(binarystring)):
        next_term = int(binarystring[-1-idx]) * 2 ** (exponent) # traverses string backwards
        total += next_term
        exponent += 1
    return total

def main():
    binary_string = input("Enter a binary value: ")
    result = binaryToInt(binary_string)
    print(result)
    go_on = input("Continue? (y/n): ")
    while go_on != "n":
        binary_string = input("Enter a binary value: ")
        result = binaryToInt(binary_string)
        print(result)
        go_on = input("Continue? (y/n): ")

if __name__ == "__main__":
    main()

```

Exercise 4b: Password Check

+ :white_large_square: Run unit test of `passwordCheck('abcD.99')`
```
FAIL 

Failed test case passwordCheck('abcD.99').
    Expected: False.
    Got: ('abcD.99', 'is not a valid pasword').
NOTE: Arguments are expected in this order: ['input_string']
```

+ Skip: Run unit test of `passwordCheck('Abcde09.@9')`

  This test was not run because of an earlier failing test.

+ Skip: Run unit test of `main()`

  This test was not run because of an earlier failing test.

Exercise 4c: Alternating Sum

+ :white_check_mark: Run unit test of `altSum([1, 2, 3, 4, 5, 6, 7, 8, 9])`

+ :white_check_mark: Run unit test of `altSum([4, 7, 4, 24, 6, 7, 8, 3, 1])`

+ :white_check_mark: Run unit test of `main()`
```python
# Exercise 4c

# Determines the alternating sum of a list of floating point values


def altSum(input_list):
    total_sum = 0
    exponent = 0
    for idx in range(len(input_list)):
        #by raising -1 to odd or even powers, we alternate adding
        #  or subtracting the next value in the list
        total_sum += (-1) ** exponent * float(input_list[idx])
        exponent += 1
    return total_sum

def main():
    values_list = []
    next_term = input("Enter a value here: ")
    while next_term != "":
        values_list += [float(next_term)]
        next_term = input("Enter a value here: ")
    print(altSum(values_list))

if __name__ == "__main__":
    main()

```

Exercise 4d: Roman Numeral To Decimal

+ :white_check_mark: Run unit test of `romanToDecimal('X')`

+ :white_check_mark: Run unit test of `romanToDecimal('MXI')`

+ :white_check_mark: Run unit test of `main()`
```python
# Exercise 4d

# Takes a Roman Numeral in a string and turn it into a number
def romanToNumber(romanNum):
    if romanNum == 'I':
        y = 1
    elif romanNum == 'V':
        y = 5
    elif romanNum == 'X':
        y = 10
    elif romanNum == 'L':
        y = 50
    elif romanNum == 'C':
        y = 100
    elif romanNum == 'D':
        y = 500
    elif romanNum == 'M':
        y = 1000
    return y

# use the romanToDecimal function to add a string of roman numerals
def romanToDecimal(romanString):
    # start an accumulator variable
    total = 0
    for x in range(0, len(romanString) - 1):
        #check if this character is not a valid Roman numeral
        if romanString[x] not in "IVXLCDM":
            return 0
        # get current roman numeral and compare to next one
        if romanString[x] == "I":
            if romanString[x+1] == "V" or romanString[x+1] == "X":
                # If the current is I and the next is V or X
                # Subtract that current value from the total
                total -= romanToNumber(romanString[x])
            else: # Otherwise add it
                total += romanToNumber(romanString[x])
        elif romanString[x] == "X":
            if romanString[x+1] == "L" or romanString[x+1] == "C":
                # If current is X and the next is either L or C
                # Subtract current from total
                total -=romanToNumber(romanString[x])
            else:# Otherwise add it
                total += romanToNumber(romanString[x])
        elif romanString[x] == "C":
            if romanString[x+1] == "D":
                # if the current is C and the next is D
                # Subtract current from total
                total -= romanToNumber(romanString[x])
            else: # Otherwise add it
                total += romanToNumber(romanString[x])
        else: # otherwise we can only add the remaining numerals
            total += romanToNumber(romanString[x])
    #check the last character for being a valid Roman digit
    if romanString[-1] not in "IVXLCDM":
        return 0
    """Now we need to add the final roman numeral to the total
       Since there is no following roman numeral (after the last one)
       the only option we have is to add it to the total"""
    total += romanToNumber(romanString[-1])
    return total # return the total

def main():
    roman = input("Please enter a Roman Numeral: ")
    print(romanToDecimal(roman))

if __name__ == '__main__':
    main()

```

Exercise 4e: Sieve of Eratosthenes Primes

+ :white_check_mark: Run unit test of `main()`

+ :white_check_mark: Run unit test of `main()`

+ :white_check_mark: Run unit test of `main()`
```python
#Exercise 4e

# Implements the Sieve of Eratosthenes to determine primes

def sieve(upper_bound):
    if upper_bound < 2:
        print("Error: invalid input")
    else:
        all_numbers = []
        for each_number in range(2, upper_bound+1):
            all_numbers += [each_number]
        factor = 2
        while factor < upper_bound:
            for each_number in range(0, len(all_numbers)):
                if all_numbers[each_number] % factor == 0 and \
                        all_numbers[each_number] / factor != 1:
                    # overwrites the number with zero if it is divisble by factor
                    all_numbers[each_number] = 0
            factor += 1
    prime_list = []
    for each_number in all_numbers:
        if each_number != 0:
            prime_list += [each_number]
    return prime_list

def main():
    upper_bound = int(input("Enter an integer >2: "))
    print(sieve(upper_bound))

if __name__ == "__main__":
    main()

```

