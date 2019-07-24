
def roundit(x):
  if x>0:
      return int((x+0.5))
  else:
      return int((x-0.5))


def main():
  print(roundit(0))

if __name__ == '__main__':
    main()
