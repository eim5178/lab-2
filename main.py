# Author: Evelyn Moore eim5178@psu.edu
# Collaborator:Zelin Chen zvc5228@psu.edu
# Section: 4
# Breakout: 3
def getLetterGrade(percent):
  if percent >= float(93.0):
    return 'A'
  elif percent >= float(90.0):
    return 'A-'
  elif percent >= float(87.0):
    return 'B+'
  elif percent >= float(83.0):
    return 'B'
  elif percent >= float(80.0):
    return 'B-'
  elif percent >= float(77.0):
    return 'C+'
  elif percent >= float(70.0):
    return 'C'
  elif percent >= float(60.0):
    return 'D'
  else:
    return 'F'
def run():
  percent = float(input("Enter your CMPSC 131 grade: "))
  print(f"Your letter grade for CMPSC 131 is {getLetterGrade(percent)}.")
if __name__ == '__main__':
  run()