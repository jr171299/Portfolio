#CALCUALTE AVERAGE QUIZ GRADE 

#Asks the user for a numerical input out of 100 
print('Enter your score on Quiz 1:')
#Takes in user input, converts it in to an integer,stores it in the variable quiz1
quiz1 = int(input())

#Repeats the process for Quiz 2
print('Enter your score on Quiz2:')
quiz2 = int(input())

#Adds quiz1 and quiz2, divides by 2, then stores that value in a new variable average
average = (quiz1 + quiz2) / 2

#Converts average back to a string
average = str(average)

#Prints out the user's average quiz grade
print('Your average score is ' + average  + ' points.')
print()
