from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from backend.models import Question, QuestionLink
from backend.serializers import QuestionSerializer, QuestionLinkSerializer
from backend.controller import questionlinkcontroller


@csrf_exempt
@api_view(['GET', 'POST'])
def question_list(request):
    """
    List all questions, or create a new one
    """
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def question_detail(request, id):
    """
    View, edit or delete a Question
    """
    try:
        question = Question.objects.get(id=id)
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET'])
def question_outgoing_links_list(request, id):
    """
    View the links whose source is the given Question
    """
    serializer_context = {'request': request}
    try:
        question = Question.objects.get(id=id)
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    question_links = questionlinkcontroller.get_by_source(question)
    serializer = QuestionLinkSerializer(
        question_links, many=True, context=serializer_context)
    return Response(serializer.data)


@csrf_exempt
@api_view(['GET'])
def question_linked_questions(request, id):
    """
    View the Questions linked to the given Question
    """
    serializer_context = {'request': request}
    try:
        question = Question.objects.get(id=id)
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    question_links = questionlinkcontroller.get_by_source(question)
    questions = [q.target for q in question_links]
    serializer = QuestionSerializer(
        questions, many=True, context=serializer_context)
    return Response(serializer.data)


@csrf_exempt
@api_view(['GET', 'POST'])
def question_link_list(request):
    """
    List all question_links, or create a new one
    """
    serializer_context = {'request': request}
    if request.method == 'GET':
        question_links = QuestionLink.objects.all()
        serializer = QuestionLinkSerializer(
            question_links, many=True, context=serializer_context)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = QuestionLinkSerializer(
            data=request.data, context=serializer_context)
        if serializer.is_valid():
            link = serializer.create(serializer.validated_data)
            link = questionlinkcontroller.create_link(
                link.source, link.target)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def question_link_detail(request, id):
    """
    View, edit or delete a QuestionLink
    """
    serializer_context = {'request': request}
    try:
        question_link = QuestionLink.objects.get(id=id)
    except QuestionLink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuestionLinkSerializer(
            question_link, context=serializer_context)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = QuestionLinkSerializer(
            question_link, data=request.data, context=serializer_context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        question_link.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
