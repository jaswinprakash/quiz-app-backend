from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view


from questions.models import Question
from api.v1.questions.serializers import QuestionSerializer


@api_view(["GET"])
def view_questions(request,id):
        question = get_object_or_404(Question, id=id)
        print(question)
        serializers=QuestionSerializer(instance=question)
        response_data={
            "status_code":6000,
            "data":serializers.data
        }
        return Response(response_data)
 
@api_view(["POST"])
def submit_answer(request, id):
    question = get_object_or_404(Question, id=id)
    selected_choice = request.POST.get('choice')

    if selected_choice == question.correct_answer:
        # Correct answer
        score = request.session.get('score', 0) + 1  # Get the current score from session and increment it by 1
        request.session['score'] = score  # Update the score in the session
        response_data = {
            "status_code": 6000,
            "message": "Correct answer",
            "score": score
        }
        return Response(response_data)
    else:
        # Incorrect answer
        score = request.session.get('score', 0)  # Get the current score from session
        response_data = {
            "status_code": 6001,
            "message": "Incorrect answer",
            "score": score
        }
        return Response(response_data)

     
        