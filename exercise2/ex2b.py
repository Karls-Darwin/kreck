
def wind_chill(temp, wind_velocity):
  return 35.74 + (0.6215 * temp) - (35.75 * wind_velocity**0.16) + (0.4275*temp*wind_velocity**0.16)



def main():
  temp=int(input("Enter temperature (F): \n"))
  wind_velocity=int(input("Enter wind velocity(MPH): \n"))
  print("Windchill is: ", wind_chill(temp,wind_velocity))


if __name__ == '__main__':
    main()
