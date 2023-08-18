from django.shortcuts import render

# Create your views here.

# below are written by @firat
from django.http import HttpResponse
# we added below for voting
# ----
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Choice
# ----
from .models import Question
# from django.template import loader
from django.shortcuts import render
# lets now consider the case of 404 errors
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views import generic

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     # before it was like below
#     # output = ", ".join([q.question_text for q in latest_question_list])
#     # return HttpResponse(output)
#     # Then I can also do like below after importing loader from django.template
#     # template = loader.get_template("polls/index.html")
#     # context = {"latest_question_list":latest_question_list,}
#     # return HttpResponse(template.render(context,request))
#     # But even better way to do this which is shown belo
#     context = {"latest_question_list":latest_question_list,}
#     # The render() function takes the request object as its first argument, 
#     # a template name as its second argument and a dictionary as its optional third argument. 
#     # It returns an HttpResponse object of the given template rendered with the given context.
#     return render(request,'polls/index.html',context)

# def detail(request,question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404
#     # return render(request,"polls/detail.html",{"question":question})
#     # new method with shortcut
#     # question = get_object_or_404(Question.objects.get(pk=question_id))
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})

# # below is to show after someone votes
# def results(request,question_id):
#     # response = "You are looking at the results for question %s."
#     # return HttpResponse(response %question_id)
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request,"polls/results.html",{"question":question,})


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request,question_id):
    # return HttpResponse("You are voting on question %s"%question_id)
    # let's identify the question or get a 404 error 
    question = get_object_or_404(Question,pk=question_id)
    try:
        # request.POST is a dictionary-like object that lets you access submitted data by key name. In this case, request.POST['choice'] returns the ID of the selected choice, as a string. request.POST values are always strings.
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
        # request.POST['choice'] will raise KeyError if choice wasn’t provided in POST data. The above code checks for KeyError and redisplays the question form with an error message if choice isn’t given.
    except(KeyError,Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question":question,
                "error_message":"You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

        # After incrementing the choice count, the code returns an HttpResponseRedirect rather than a normal HttpResponse. HttpResponseRedirect takes a single argument: the URL to which the user will be redirected (see the following point for how we construct the URL in this case).
        # We are using the reverse() function in the HttpResponseRedirect constructor in this example. 
        # This function helps avoid having to hardcode a URL in the view function. 
        # It is given the name of the view that we want to pass control to and the variable portion of the URL pattern that points to that view. 
        # In this case, using the URLconf we set up in Tutorial 3, this reverse() call will return a string like.
        # "/polls/3/results/"
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

    





