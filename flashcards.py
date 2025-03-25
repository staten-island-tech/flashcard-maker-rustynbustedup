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
            

