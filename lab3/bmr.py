def main():
  intro()
  GetWeight()
  GetHeight()
  Calculate()

def intro():
  print ("Welcome to the BMI Calculator by Rabucc")
  def GetWeight():
  weight = float(input("How much do you weigh in pounds?\n "))
  return weight

def GetHeight():
  height = input("Enter your height in inches:\n ")
  return height

def Calculate():
  height = GetHeight()
  weight = GetWeight()
  BMI = (weight * 703) / (height * height)
  print ("Your BMI is", BMI)
main()
