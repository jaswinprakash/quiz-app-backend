from django.urls import path
from api.v1.questions import views

urlpatterns = [
    path('',views.view_questions,name="view_questions"),
    path('submit-answer/<int:id>/',views.submit_answer,name="submit_answer"),
    path('handlefetch/',views.handlefetch,name="handlefetch"),
]