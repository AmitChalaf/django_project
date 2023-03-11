from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('<int:question_id>/', views.Detail.as_view(), name='detail'),
    path('<int:question_id>/vote', views.Vote.as_view(), name='vote'),
    path('newq/', views.NewQuestion.as_view(),name="newquestion"),
    path('newc/', views.NewChoice.as_view(),name="newchoice"),  
    path('register/', views.register, name='register'),      
    path('login/', views.LogInUser.as_view(), name='login'),      
    path('logout/', views.logUserOut, name='logout'),      
    path('api/questions/', views.question_list_api, name="questionlistapi"),
    path('api/question/<int:pk>/', views.question_api, name='question'),
    path('api/choices/', views.ChoiceListApi.as_view(), name='choices'),
    path('api/choice/<int:pk>/', views.choice_api, name='choice'),

]