### Feedback for Exercise Set 2

Run on February 06, 22:34:38 PM.

+ :white_check_mark: Change into directory "exercise2".

+ :white_check_mark: Check that file "ex2a.py" exists.

+ :white_check_mark: Check that file "ex2b.py" exists.

+ :white_check_mark: Check that file "ex2c.py" exists.

+ :white_check_mark: Check that file "ex2d.py" exists.

#### Running Unit Tests

Exercise 2a: Basal Metabolic Rate

+ :white_check_mark: Run unit test of `bmr(125, 65, 21, 'M')`

+ :white_check_mark: Run unit test of `bmr(134, 70, 25, 'F')`

+ :white_check_mark: Run unit test of `main()`
```python
# Exercise 2a
# Basal Metabolic Rate Calculation, plus candy bars

# Male-bodied BMR:
# 655 + (4.3 * weight in pounds) + (4.7 * height in inches) - (4.7 * age in years)
# Female-bodied BMR:
# 66 + (6.3 * weight in pounds) + (12.9 * height in inches) - (6.8 * age in years)

# Return number of candy bars a person can have
def bmr(weight, height, age, gender):
    if gender == 'F':
        return (655 + (4.3 * weight) + (4.7 * height) - (4.7 * age))/230
    elif gender == 'M':
        return (66 + (6.3 * weight) + (12.9 * height) - (6.8 * age))/230
    else:
        return 0

def main():
    # We are "casting" weight, height, and age to floating point numbers.
    user_weight = float(input('Enter your weight: '))
    user_height = float(input('Enter your height: '))
    user_age = float(input('Enter your age: '))
    user_gender = input('Enter your gender: ')
    # Note that the variable names here *do not* need to match the ones in the
    # function!
    print('You can have', bmr(user_weight, user_height, user_age, user_gender), 'candy bars!')

if __name__ == '__main__':
    main()

```

Exercise 2b: Windchill

+ :white_check_mark: Run unit test of `wind_chill(5, 20)`

+ :white_check_mark: Run unit test of `wind_chill(-10, 10)`

+ :white_check_mark: Run unit test of `main()`
```python
# Exercise 2b
# Windchill calculation

# Windchill formula:
# wind_chill = 35.74 + 0.6215*temp_ambient - 35.75*wind_velocity**0.16 +
#   0.4275*temp_ambient*v**0.16
def wind_chill(temp_ambient, wind_velocity):
    return 35.74 + 0.6215*temp_ambient - 35.75 * wind_velocity**0.16 + 0.4275 * temp_ambient * wind_velocity**0.16

def main():
    temp = float(input('Enter temperature (F): '))
    velocity = float(input('Enter wind velocity (MPH): '))
    print('The windchill is:', wind_chill(temp, velocity))

if __name__ == '__main__':
    main()

```

Exercise 2c: Turtle Star

+ :white_check_mark: Run unit test of `main()`
```python
# Exercise 2c
# Draw Star
import turtle

# Procedural abstraction to handle one side of the star
def make_line(length):
    turtle.backward(length)
    turtle.left(144) #this will make an interior angle of 36 degrees, as we want

def draw_star(length):
    make_line(length)
    make_line(length)
    make_line(length)
    make_line(length)
    make_line(length)

def main():
    l = turtle.numinput('', 'Side length: ')
    draw_star(l)

if __name__ == '__main__':
    main()

```

Exercise 2d: Slope of a line

+ :white_check_mark: Run unit test of `slope(2, -2, 7, 6)`

+ :white_check_mark: Run unit test of `slope(-1, 6, 0, 0)`

+ :white_check_mark: Run unit test of `main()`
```python
# Exercise 2d
# Slope of a line

def slope(x1, y1, x2, y2):
    if x2 - x1 != 0:
        return (y2 - y1) / (x2 - x1)
    else:
        return float('inf') # This is Python's way of handling an infinite value

def main():
    ux1 = float(input('Enter first x value: '))
    uy1 = float(input('Enter first y value: '))
    ux2 = float(input('Enter second x value: '))
    uy2 = float(input('Enter second y value: '))
    m = slope(ux1, uy1, ux2, uy2)
    if m != float('inf'):
        b = uy1 - m*ux1
    else:
        b = float('inf')

    print('y =', m, 'x +', b)

if __name__ == '__main__':
    main()

```

