#Generate random 32bit codes combo of digits 0-9 and cap. Ls. A-F
#Writes to file










import string
import random
import secrets
alpha = string.ascii_uppercase[:7]
alpha += string.digits
def generate():
	value = ""
	for i in range(32):
		value += secrets.choice(alpha)
	return value

def user_in():
	try:
		return int(input("How many codes are desired: \n"))
	except Exception as e:
		print("Only interger values accepted. \n")
		return user_in()
def main():
    iterations = user_in()
    codes = []
    with open("Generated codes.txt", "w") as f:
        for reps in range(iterations):
            number = generate()
            codes.append(number+"\n")
        f.writelines(codes)
#        print(f"These are the generated codes \n{codes}")
    with open("generated codes.txt", "r") as f:
        print(f"These are the generated codes \n{f.read()}")
main()
        
                
