from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User


from questions.models import Question
from api.v1.questions.serializers import QuestionSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def view_questions(request):
    category = request.GET.get('category')
    questions = Question.objects.filter(category__name=category)
    
    if questions.exists():
        serializer = QuestionSerializer(questions, many=True)
        user = User.objects.get(username=request.user.username)
        response_data = {
            "status_code": 6000,
            "data": serializer.data,
            "first_name": user.first_name
        }
        return Response(response_data)
    else:
        response_data = {
            "status_code": 6001,
            "message": "Questions not found in that category"
        }
        return Response(response_data)
 
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def submit_answer(request, id):
    question = get_object_or_404(Question, id=id)
    selected_choice = request.POST.get('choice')
    print(selected_choice)

    if selected_choice == question.correct_answer:
        score = request.session.get('score', 0) + 1
        request.session['score'] = score
        response_data = {
            "status_code": 6000,
            "message": "Correct answer",
            "score": score
        }
        return Response(response_data)
    else:
        score = request.session.get('score', 0)
        response_data = {
            "status_code": 6001,
            "message": "Incorrect answer",
            "score": score
        }
        return Response(response_data)
    
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def handlefetch(request):
    first_name = request.user.first_name
    
    response_data = {
        "first_name": first_name,
    }
    return Response(response_data)