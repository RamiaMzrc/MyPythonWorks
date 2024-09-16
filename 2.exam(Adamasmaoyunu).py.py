Name= input("Enter name:")

print("Hello,"+ Name +" time to play hangman")

answer="FreePalestine"

yoursanswer_string=""

lives=10

while lives>0:
	letter_left=0 
	for letter in answer:
		if letter in yoursanswer_string:
			print(letter)
		else :
			print("-")
			letter_left=+1

	if letter_left==0:
		print("you won!!!")
		break		
	value=input("Enter value..")
	yoursanswer_string+= value		
	if value not in answer:
		lives-=1
		print("Wrong word!")
		print(f"You have {lives} left")
		if lives==0:
			print("Game Over!!!")
	
