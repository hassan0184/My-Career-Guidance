import os
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from django.http import HttpResponse
from .serializers import GoalSerializer
from .models import Goal
from user.models import Student
from django.template.loader import render_to_string
from weasyprint import HTML
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class GoalViewRelated(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GoalSerializer

    def get(self, request):
        """Get goals of user"""
        try:
          student =self.request.user
          user_obj=Student.objects.get(id=student.id)
          goal_obj =Goal.objects.filter(user=user_obj.id).first()
          temp_name = "general/templates/" 
          goal_template = str(user_obj.first_name) +"-"+str(user_obj.last_name) +"-"+"goal" + ".html"
          open(temp_name + goal_template, "w").write(render_to_string('goal.html', {'student_detail': user_obj,'goal_detail':goal_obj}))
          HTML(temp_name + goal_template).write_pdf(str(user_obj.first_name)+'.pdf')
          file_location = f'{user_obj.first_name}.pdf'
          with open(file_location, 'rb') as f:
            file_data = f.read()
          response = HttpResponse(file_data, content_type='application/pdf')
          response['Content-Disposition'] = 'attachment; filename="'+ user_obj.first_name +'".pdf'
          return response
        except Exception as e:
          return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        try:
          user_obj=request.user
          proffession=request.data.get('proffession')
          goal=request.data.get('goal')
          actions=request.data.get('actions')
          realistic=request.data.get('realistic')
          goal_obj=Goal.objects.create(user_id=user_obj.id,proffession=proffession, goal=goal,actions=actions,realistic=realistic)
          goal_obj.save()

          return Response(data={'success': True, 'Goals': goal_obj.goal}, status=status.HTTP_200_OK)
        except Exception as e:
          return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class GoalDetail(APIView):
    """
    Retrieve, update or delete a goal instance.
    """
    def get_object(self, pk):
        try:
            return Goal.objects.get(pk=pk)
        except Exception as e:
          return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        goal = self.get_object(pk)
        serializer = GoalSerializer(goal)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        goal = self.get_object(pk)
        serializer = GoalSerializer(goal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        goal = self.get_object(pk)
        goal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
