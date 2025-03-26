#SToopId Flashcard maker
#if u do flashcard - Do it on paper


import  json

mode = input ("What mode do you want to enter? Teacher or Student?" )

class Teacher:
    @staticmethod #use a variable outside smthn else
    def flashcard_maker():
        try:
            with open ("flashcards.json", "r") as file:
                flashcards = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            flashcards = {}

        while True:
            a = input("do you want to make new flashcards? (yes/no):")
            if a.lower() == "yes":
                question = input ("what is your question?")
                answer = input ("what is the answer to the previous question?")
                flashcards[question] = answer 
                with open ("flashcards.json", "w") as file:
                    json.dump(flashcards, file, indent=4)
                print("flashcards are saved")
            elif a.lower() == "no":
                print ("WHY U LAZY")
                break
            else: 
                print ("Unknown input")
                

class Student:
    @staticmethod 
    def study_flashcards():
        streak = 0
        points = 0
        try:
            with open("flashcards.json", "r" ) as file:
                flashcards = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            flashcards = {}


        if not flashcards:
            print ("Your lazy teach made no flashcards for u")
        else:
            for question, answer in flashcards.items():
                print (f"Question: {question}")
                user_answer = input ("What is your answer?")
                if user_answer.lower() == answer.lower():
                    print ("Correct")
                    points += 1
                    streak += 1
                    print(points)
                else:
                    print (f"Wrong, the answer is {answer}")
                    streak = 0 
                if streak >= 3:
                    print ("You are on fire")
                    points = points + 2 
    


if mode.lower() == "teacher":
    Teacher.flashcard_maker()
elif mode.lower() == "student":
    Student.study_flashcards()
else:
    print("Unknown input")

    

