from django.urls import path
import translate.views as views

urlpatterns = [
    path('translate/', views.CompareTranslate.as_view(), name='api_translate'),
]
