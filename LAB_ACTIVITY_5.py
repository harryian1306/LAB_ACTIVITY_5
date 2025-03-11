assign_grade = int(input("What is your grade?"))
if assign_grade >= 101:
	print("Invalid score! Please enter a value between 0 and 100.")
elif assign_grade >= 90:
	print("Wow!!! You got an A. congratulations!")
elif assign_grade >= 80:
	print("You got a B. Not bad.")
elif assign_grade >= 70:
	print("Uhhh, you got a C. Better study more!")
elif assign_grade >= 60:
	print("Oh no, you got a D!")
elif assign_grade >= 0:
	print("I'm so sorry, but you got an F.")
else:
	print("Invalid score! Please enter a value between 0 and 100.")
