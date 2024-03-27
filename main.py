import random
import csv

FILE = "questions.csv"
SCORE = 10


def ask_question(questions: list, answer: str):
    """
    if we answer the question correctly, we return True else False
    :param questions: list
    :param answer: str
    :return: bool
    """
    try:
        result = int(input("numéro de la bonne réponse: "))  # entrée utilisateur
        if questions[result-1] == answer:
            print("bonne réponse", end='\n \n')
            return True
        else:
            print(f"mauvaise réponse, la bonne réponse était {answer}", end='\n \n')
            return False
    except:
        print(f"entrée invalide, vous devez saisir un entier entre 1 et {len(questions)}", end= '\n \n')


def get_questions():
    # fichier
    try:
        with open(FILE, "r") as file:
            lines = csv.reader(file, delimiter=';')
            lines = list(lines)
    except FileNotFoundError:
        print("impossible de trouver le fichier")
        return None
    return lines

def game(questions_array):
    score = 0
    answer_array = []
    # separer les réponses de questions_array des questions
    for i in range(len(questions_array)):
        new_question = []
        for j in range(len(questions_array[i]) - 1):
            new_question.append(questions_array[i][j + 1])
        answer_array.append(new_question)
        random.shuffle(answer_array[i])  # mélanger les réponses

    # poser les question
    for i in range(len(answer_array)):
        print(questions_array[i][0])  # afficher les questions
        for j in range(len(answer_array[i])):
            print(answer_array[i][j])
        if ask_question(questions=answer_array[i], answer=questions_array[i][-1]):  # poser la question, la réponse est toujours à la fin de la liste
            score += SCORE
    print(f"score final: {score}")


# point d'entrée
def main(num):
    questions_array = get_questions()
    questions_array = random.sample(questions_array, num)  # on mélange les questions
    game(questions_array)
    while True:
        if input("voulez vous rejouer: oui/non ") == "oui":
            game(questions_array)


# est ce qu'il y a un point d'entrée ?
if __name__ == "__main__":
    main(3)
