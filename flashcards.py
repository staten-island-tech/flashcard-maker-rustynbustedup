#SToopId Flashcard maker
#if u do flashcard - Do it on paper



import  json

mode = input ("What mode do you want to enter? Teacher or Student?")

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

class Student:
    

    

