from django.http import HttpRequest, JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ..models import Question, Choice
from ..serializers import QuestionSerializer, ChoiceSerializers
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin


@csrf_exempt
def question_list_api(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return JsonResponse(serializer.data, safe=False)
    

@csrf_exempt
def question_api(request, pk):
    question = Question.objects.get(id=pk)

    if request.method == "GET":
        serializer = QuestionSerializer(question)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = QuestionSerializer(question,data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data ,status = status.HTTP_201_CREATED)
        else:
            return JsonResponse(status.HTTP_406_NOT_ACCEPTABLE)
        
# class ChoiceListApi(generics.ListCreateAPIView):
#     queryset = Choice.objects.all()
#     serializer_class = ChoiceSerializers

class ChoiceListApi(CreateModelMixin, ListModelMixin, generics.GenericAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# class ChoiceListApi(APIView):
#     def post(self, request):
#         data = JSONParser().parse(request)
#         serializer = ChoiceSerializers(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return HttpResponse(status.HTTP_400_BAD_REQUEST)
    
#     def get(self, request):
#         choices = Choice.objects.all()
#         serializer = ChoiceSerializers(choices, many=True)
#         return JsonResponse(serializer.data, safe=False)
