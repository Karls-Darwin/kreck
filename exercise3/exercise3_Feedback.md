### Feedback for Exercise Set 3

Run on February 13, 22:05:00 PM.

+ :white_check_mark: Change into directory "exercise3".

+ :white_check_mark: Check that file "ex3a.py" exists.

+ :white_check_mark: Check that file "ex3b.py" exists.

+ :white_check_mark: Check that file "ex3c.py" exists.

+ :white_check_mark: Check that file "ex3d.py" exists.

+ :white_check_mark: Check that file "ex3e.py" exists.

+ :white_check_mark: Check that file "ex3f.py" exists.

#### Running Unit Tests

Exercise 3a: Compound Intrest

+ :white_check_mark: Run unit test of `compound_interest(1000, 10000, 0.02)`

+ :white_check_mark: Run unit test of `compound_interest(234, 576, 0.05)`

+ :white_check_mark: Run unit test of `main()`
```python
# Exercise 3a

# How many years of interest until starting is more than target?
def compound_interest(starting, target, interest_rate):
    interest_rate += 1 # Growing each year (100% + interest_rate)
    years = 0
    amount = starting
    while amount < target:
        amount *= interest_rate
        years += 1
    return years

def main():
    starting_amt = float(input('Enter a starting amount: '))
    target_amt = float(input('Enter a target amount: '))
    interest_rate = float(input('Enter an interest rate: '))
    print(compound_interest(starting_amt, target_amt, interest_rate), 'years')

if __name__ == '__main__':
    main()

```

Exercise 3b: Perfect Numbers

+ :white_check_mark: Run unit test of `perfect(9)`

+ :white_check_mark: Run unit test of `perfect(123)`

+ :white_check_mark: Run unit test of `perfect(6)`

+ :white_check_mark: Run unit test of `main()`
```python
# Exercise 3b

# Find if a number is perfect
def perfect(num):
    total = 0
    i = 1
    while i < num:
        if num % i == 0:
            total += i
        i += 1
    if total == num:
        return True
    else:
        return False

def main():
    lower = int(input('Enter the lower bound: '))
    upper = int(input('Enter the upper bound: '))
    while lower <= upper:
        if perfect(lower):
            print(lower)
        lower += 1

if __name__ == "__main__":
    main()

```

Exercise 3c: Orbiting Turtles

+ :white_large_square: Run unit test of `main()`
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
  File "<frozen importlib._bootstrap_external>", line 665, in exec_module
  File "<frozen importlib._bootstrap>", line 222, in _call_with_frames_removed
  File "/ex3c.py", line 30, in <module>
    sun()
  File "/ex3c.py", line 6, in sun
    t1=turtle.Turtle()
  File "/usr/lib/python3.5/turtle.py", line 3812, in __init__
    Turtle._screen = Screen()
  File "/usr/lib/python3.5/turtle.py", line 3662, in Screen
    Turtle._screen = _Screen()
  File "/usr/lib/python3.5/turtle.py", line 3678, in __init__
    _Screen._root = self._root = _Root()
  File "/usr/lib/python3.5/turtle.py", line 434, in __init__
    TK.Tk.__init__(self)
  File "/usr/lib/python3.5/tkinter/__init__.py", line 1871, in __init__
    self.tk = _tkinter.create(screenName, baseName, className, interactive, wantobjects, useTk, sync, use)
_tkinter.TclError: no display name and no $DISPLAY environment variable
```

Exercise 3d: More Orbiting Turtles

+ :white_check_mark: Run unit test of `main()`
```python
# Exercise 3d

import turtle
import math

def main():
    planet = turtle.Turtle()
    planet.color('yellow')
    planet.dot(40)
    planet.shape('circle')
    planet.color('blue')
    planet.penup()
    planet.speed(0)
    p_radius = 150
    moon = turtle.Turtle()
    moon.color('green')
    moon.shape('circle')
    moon.penup()
    moon.speed(0)
    moon.shapesize(0.5, 0.5)
    m_radius = 80
    num_rev = 0
    while num_rev < 3:
        degree = 0
        while degree < 360:
            x = math.cos(math.radians(degree)) * p_radius
            y = math.sin(math.radians(degree)) * p_radius
            planet.goto(x,y)
            degree += 2
            m_deg = 0
            while m_deg < 360:
                mx = x + math.cos(math.radians(m_deg)) * m_radius
                my = y + math.sin(math.radians(m_deg)) * m_radius
                moon.goto(mx, my)
                m_deg += 5
        num_rev += 1
    return

if __name__ == "__main__":
    main()

```

Exercise 3e: Greatest Common Denominator

+ :white_large_square: Run unit test of `gcd(4, 7)`
```
FAIL 
Function gcd not in file ex3e.py
```

+ Skip: Run unit test of `gcd(9, 15)`

  This test was not run because of an earlier failing test.

+ Skip: Run unit test of `gcd(23, 53)`

  This test was not run because of an earlier failing test.

+ Skip: Run unit test of `main()`

  This test was not run because of an earlier failing test.

Exercise 3f: Craps

+ :white_check_mark: Run unit test of `main()`
```python
# Exercise 3f
import random

def main():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    come_out = d1 + d2
    print('Initial roll is: [' + str(d1) + ',' + str(d2) + '] =', come_out)
    if come_out == 7 or come_out == 11:
        print('You win!')
    elif come_out == 2 or come_out == 3 or come_out == 12:
        print('Craps!  Sorry, you lose')
    else:
        point = come_out
        print('Point is ' + str(point) + '. Roll again.')
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        total = d1 + d2
        print('  Roll is: [' + str(d1) + ',' + str(d2) + '] =', total, end=' ')
        while total != point and total != 7:
            d1 = random.randint(1, 6)
            d2 = random.randint(1, 6)
            total = d1 + d2
            print('\n  Roll is: [' + str(d1) + ',' + str(d2) + '] =', total,
                  end=' ')
        if total == point:
            print('You win!')
        else:
            print('Sorry, you lose')

if __name__ == "__main__":
    main()

```

