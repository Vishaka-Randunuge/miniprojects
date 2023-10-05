print("Welcome to my quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay lets play now!")
score = 0

answer = input("What is the name of the school Harry Potter attends? ")
if answer.lower() == "hogwarts":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer is: Hogwarts")

answer = input("Who is Harry Potter's best friend? ")
if answer.lower() == "ron weasley":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer is: Ron Weasley")

answer = input("What is the name of Harry Potter's pet owl? ")
if answer.lower() == "hedwig":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer is: Hedwig")

answer = input("Who is the dark wizard and main antagonist in the series? ")
if answer.lower() == "lord voldemort":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer is: Lord Voldemort")

answer = input("What is the name of the sport played on broomsticks in the wizarding world? ")
if answer.lower() == "quidditch":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer is: Quidditch")

answer = input("What is the name of the train that takes students to Hogwarts? ")
if answer.lower() == "hogwarts express":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer is: Hogwarts Express")

answer = input("What is the name of the magical sport played on flying broomsticks with four balls? ")
if answer.lower() == "quidditch":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer is: Quidditch")

answer = input("Who is the headmaster of Hogwarts throughout most of the series? ")
if answer.lower() == "albus dumbledore":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer is: Albus Dumbledore")

print ("you got " + str(score) + " questions correct!")
print ("you got " + str((score/8)*100) + " %")
