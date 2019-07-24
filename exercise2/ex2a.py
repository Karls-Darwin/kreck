
def bmr(weight, height, age, sex):
  if sex == "F" or sex == "f":
      basal_metabolic_rate = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)
      bars=(basal_metabolic_rate/230)
  elif sex == "M" or sex == "m":
      basal_metabolic_rate = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)
      bars=(basal_metabolic_rate/230)
  return bars

def main():
  weight=float(input("Enter weight in pounds: \n"))
  height=float(input("Enter height in inches: \n"))
  age=float(input("Enter age: \n"))
  sex=input("Enter M for male or F for female: ")
  bmr(weight, height, age, sex)
  print('You can have', bmr(weight, height, age, sex), 'candy bars!')

if __name__ == "__main__":
    main()
