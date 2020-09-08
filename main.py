# Author: Evelyn Moore eim5178@psu.edu
# Collaborator:
# Collaborator:
# Collaborator:
# Section:
# Breakout: 
def getLetterGrade():
  percent = float(input("Enter your CMPSC 131 grade: "))
  if percent >= float(93.0):
    print("Your letter grade for CMPSC 131 is A.")
  elif percent >= float(90.0):
    print("Your letter grade for CMPSC 131 is A-.")
  elif percent >= float(87.0):
    print("Your letter grade for CMPSC 131 is B+.")
  elif percent >= float(83.0):
    print("Your letter grade for CMPSC 131 is B.")
  elif percent >= float(80.0):
    print("Your letter grade for CMPSC 131 is B-.")
  elif percent >= float(77.0):
    print("Your letter grade for CMPSC 131 is C+.")
  elif percent >= float(70.0):
    print("Your letter grade for CMPSC 131 is C.")
  elif percent >= float(60.0):
    print("Your letter grade for CMPSC 131 is D.")
  else:
    print("Your letter grade for CMPSC 131 is F.")

if __name__ == '__main__':
    getLetterGrade()