from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # I believe you set the name variables here, and type it in the views folder later on. Also same goes for question_id variable in here
    # names here are used in the template html files (specificially in links to make them easier to manage and read)
    # ex: /polls/
    path("",views.IndexView.as_view(),name="index"),
    # ex: /polls/5/
    # path("<int:question_id>/",views.detail,name="detail"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail" ),
    # ex: /polls/5/results
    # path("<int:question_id>/results/",views.results,name="results"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results" ),
    # ex: /polls/5/vote
    path("<int:question_id>/vote/",views.vote,name="vote"),

]