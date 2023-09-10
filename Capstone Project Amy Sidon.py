"""
Author: Amy Sidon
Program: Capstone Project
Due Date: May 9, 2021
"""
def main():
    
    greetings()
    
#1. Create a list of user names using a WHILE loop (30 points)
    import random
    x = input("Press enter to proceed: ")
    list = []
    while x == '':
        first_name = input("\nPlease enter first name: ") 
        last_name = input("Please enter last name: ")
        age = (int(input("Please enter age: ")))
        num = random.randint(age, 99) #Generates random number to add to the end of the username
        username = first_name[-1] + last_name[0:4] + str(num) #Uses LAST letter of first name and FIRST FOUR letters of last name to create user name
        x = input("Type 'exit' to leave or press enter to proceed:")
        list.append(username)
 
    print("\nThe user name list is displayed below")
    print(list)
#2. Ask user to check if user name is in the list, if user input is wrong, keep trying. (10 points)    
    while True:
        askUser = input("\nEnter a user name to check: ")
        for username in list:
            if askUser == username:
                print("Yes, it is in the list")
                break
            elif askUser == "":
                print("")
                break
        else:
            print("No, it is not in the list")
        if askUser == "":
            break
            
        
#3. Write the user name list to a file named username.text (5 points)
    file = open("username.txt","w")
    file.write(username)
    file.close()

#4. Calculate the average of test scores (15 points)
    intList = []
    theSum = 0
    numTests = int(input("Enter the number of tests:"))
    for i in range(1,numTests +1):
        numOfScore = int(input("Enter score:"))
        intList.append(numOfScore)
        theSum += numOfScore
        average = theSum / numTests
    print("The average is %0.1f"%averageTestScore(theSum, numTests))
    letter(average)

    goodbye()

def averageTestScore(theSum, numTests):
    return (theSum//numTests)
  
#5. Calculate Letter Grades (15 points)
def letter(average):
    if average <=100 and average >= 90:
        print("The letter grade is A")
    elif average <=89 and average >= 80:
        print("The letter grade is B")
    elif average <=79 and average >= 70:
        print("The letter grade is C")
    elif average <=69 and average >= 60:
        print("The letter grade is D")
    elif average <=59 and average >= 0:
        print("The letter grade is F")
    return average
#6. Greeting message
def greetings():
    print("Welcome to Amy Sidon's username creater and test score averages checker")
    print("This program allows you to create usernames by entering first name, last name, and age.")
    print("Next you will be able to check if usernames are in use.")
    print("Then you can do averages of test scores that will return the value and letter grade.")
    print("Press <Enter> for the section you wish to skip or you are finished with")
#6. Good-bye message
def goodbye():
    print("\nYou have reached the end of this program,")
    print("your username will appear in a text file.")
    print("\nGoodbye")

if __name__=="__main__":
    main()
