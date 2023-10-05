print("Welcome to my quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay lets play now!")
score = 0

answer = input("What does CPU mean? ")
if answer == "central processing unit":
    print("correct")
    score += 1
else:
    print("Incorrect!")
    print("the correct answer is : central processing unit")

answer = input("What does GPU stand for? ")
if answer == "graphics processing unit":
    print("correct")
    score += 1
else:
    print("Incorrect!")
    print("the correct answer is : graphics processing unit")

answer = input("What does RAM mean? ")
if answer == "random access memory":
    print("correct")
    score += 1
else:
    print("Incorrect!")
    print("the correct answer is : random access memory")

answer = input("What does PSU mean? ")
if answer == "power supply unit":
    print("correct")
    score += 1
else:
    print("Incorrect!")
    print("the correct answer is : power supply unit")

print ("you got " + str(score) + " questions correct!")
print ("you got " + str((score/4)*100) + " %")