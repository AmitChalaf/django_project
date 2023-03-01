from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic,View
from django.urls import reverse
from django.utils import timezone
from .models import Question, Choice
from .forms import QuestionForm, ChoiceForm, UserForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list':latest_question_list}
#     return render(request, 'polls/index.html',context)

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question' : question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html' ,{'question': question})


class Index(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """return the last five published"""
        return Question.objects.order_by('-pub_date')
        # [:5]



class Detail(generic.DetailView):
    # model = Question
    # template_name = 'polls/detail.html'
    
    def get(self, request, question_id):
        question = get_object_or_404(Question, pk = question_id)
        return render(request=request, template_name='polls/detail.html', context={'question':question})

# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'



class NewQuestion(View):
    def post(self, request):
        form = QuestionForm(request.POST)
        if form.is_valid():
            question_text = form.cleaned_data['question_text']
            pub_date = form.cleaned_data['pub_date']
            q = Question(question_text, pub_date)
            q.save()
            # Question.objects.create(question_text = question_text, pub_date = pub_date)
            
            return HttpResponseRedirect(reverse('polls:index'))

        else:
            message = 'failed validation'
            return render(request=request, template_name='polls/question_form.html', context={'form':form, 'message':message})


    def get(self, request):
        form = QuestionForm()
        return render(request=request, template_name='polls/question_form.html', context={'form':form})

class NewChoice(View):
    def post(self, request):
        form = ChoiceForm(request.POST)
        if form.is_valid():
            # choice_text = form.cleaned_data['choice_text']
            # votes = form.cleaned_data['votes']
            # question = form.cleaned_data['question']
            # Choice.objects.create(choice_text=choice_text, votes=votes, question=question)
            form.save()
            return HttpResponseRedirect(reverse('polls:index'))

    def get(self, request):
        form = ChoiceForm()
        return render(request=request, template_name='polls/choice_form.html', context={'form':form})
       
class Vote(View):
    def post(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        choice = question.choice_set.get(pk=request.POST['choice'])
        choice.votes = choice.votes +1
        choice.save()
        return HttpResponseRedirect(reverse('polls:detail', args=(question_id,)))
    
    def get(self, request, question_id):
        return HttpResponse('this is a get request')

@login_required()
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('polls:index'))
        else:
            return HttpResponseRedirect(reverse('polls:register'))
    else:
        form = UserForm()
        return render(request=request, template_name="polls/registration.html", context={'form':form})


class LogInUser(View):
    def get(self, request):
        form = LoginForm()
        return render(request=request, template_name="polls/login.html", context={'form':form})

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('polls:index'))
        else:
            return HttpResponseRedirect(reverse('polls:login'))



def logUserOut(request):
    logout(request)
    return HttpResponseRedirect(reverse('polls:login'))