from django.contrib import admin
from django.urls import path,include
from api.v1.questions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/questions/',include("api.v1.questions.urls")),
    path('api/v1/auth/', include("api.v1.auth.urls")),
    path('api/v1/handlefetch/', views.handlefetch, name="handlefetch"),
]