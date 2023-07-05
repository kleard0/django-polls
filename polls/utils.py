from polls.models import (Question)
from django.utils import timezone
from polls.models import Choice


def get_quantity_vote(question_id, choice_id):
    """
    Cette fonction retourne un entier égale à la quantité totale des votes d'une question dont l'id est passé en
    paramètre.
    """
    # 1 : contrôler que c'est bien un entier, où générer une erreur et informer l'utilisateur
    if not isinstance(question_id, int):
        raise ValueError("Question_id must be a integer, not an integer: " + str(type(question_id)))

    # 2 : contrôler que la cible existe, sinon informer l'utilisateur que la question n'existe pas.
    question = None
    try:
        question = Question.objects.get(id=question_id)
    except question.DoesNotExist:
        raise ValueError("Question with id " + str(question_id) + " doesn't exist.")

    # Récupérer les choix de la question
    choices_qs = Choice.objects.filter(question=question)
    total = 0
    for choice in list(choices_qs):
        total += choice.votes
    return total


def get_quantity_vote1(question_id):
    """
    Cette fonction retourne un entier égale à la quantité totale des votes du choix 1 de la question 1 dont l'id est
    passé en paramètre
    """
    # 1 : contrôler que c'est bien un entier, où générer une erreur et informer l'utilisateur

    if not isinstance(question_id, int):
        raise ValueError("Question_id must be a integer, not an integer: " + str(type(question_id)))

    # 2 : contrôler que la cible existe, sinon informer l'utilisateur que la question n'existe pas.
    question = None
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise ValueError("Question with id " + str(question_id) + " doesn't exist.")
    print(question.choices.first().vote)


def created_question(nquestion):
    """
    Cette fonction créer x question avec 3 choix chacune. Chaque choix aura le nom choix+q.pk+i(1,3)
    Chaque question aura le nom quest+1(1,x)
    """
    if not isinstance(nquestion, int):
        raise ValueError("Pas un int.")
    if nquestion < 0:
        raise ValueError("Le nombre de question doit etre supérieur à 0")
    for i in range(nquestion):
        q = Question(question_text="question_" + str(i), pub_date=timezone.now())
        q.save()
        for j in range(3):
            q.choice_set.create(choice_text="choix_" + str(q.pk) + "_" + str(i), vote=0)
