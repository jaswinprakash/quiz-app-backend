from django.contrib import admin
from django.urls import path,include
from api.v1.questions import views

urlpatterns = [
    path('<int:id>/',views.view_questions,name="view_questions"),
    path('submit-answer/<int:id>/',views.submit_answer,name="submit_answer"),
]