from .serializers import UserCreateSerializer, CreateAccessSerializer
from django.shortcuts import render, redirect
from .models import Student, StudentGroup, Task, Thread, Ticket, FAQ, Course, Group, UserAccess
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
import pandas as pd 
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Q
# Create your views here.


class getUser(APIView):

    def get(self, request):
        user=request.user
        serializer = UserCreateSerializer(user)
        return Response(serializer.data)
    

class login(APIView):

    def get(self, request):
        if(not request.user.id):
            response = redirect('http://localhost:8000/microsoft/to-auth-redirect/?next=/login')
            return response
        else:
            if(UserAccess.objects.all().filter(Q(email=request.user.email))): #check if work
                refresh = RefreshToken.for_user(request.user)

                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            else:
                return Response({'unsuccessful':'unsuccessful'})
    
class createClass(APIView):

    def post(self, request):
        excel_file = request.FILES['excel_file']
        df= pd.read_excel(excel_file,header=None)
        course_code=df.iloc[2][0].split()[1]
        class_type=df.iloc[3][0].split()[2]
        [current_course, created]=Course.objects.get_or_create(code=course_code,name=course_code)

        i=0
        tempgroup=''
        while(i<len(df)):
            if(isinstance(df.iloc[i][0], str) and df.iloc[i][0].startswith('Class Group:')):
                [tempgroup,created]=Group.objects.get_or_create(code=df.iloc[i][0].split()[2],type=class_type,course_code=current_course)
            if(isinstance(df.iloc[i][0], str) and df.iloc[i][0].startswith('No.')):
                i+=1
                while(i<len(df) and not pd.isna(df.iloc[i][0])):
                    value=df.iloc[i]
                    student_type='Exchange'
                    program_year=None
                    
                    if('Exchange' not in value[2]):
                        program_year=value[2].split()[0]
                        student_type=value[2].split()[1]
                    [student, created]=Student.objects.get_or_create(
                        VMS=value[5],
                        name=value[1],
                        program_year=program_year,
                        student_type=student_type,
                        course_type=value[3],
                        nationality=value[4]
                        )
                    StudentGroup.objects.get_or_create(
                        group=tempgroup,
                        student=student
                    )
                    i+=1
            i+=1
        return Response({'success':'success'})
    
class createAccess(APIView):

    def post(self, request):
        # serializer = CreateAccessSerializer(data=request.data)
        [access,created]=UserAccess.objects.get_or_create(email=request.data['email'], access=request.data['access'])
        #need send email
        if(created):
            return Response({'success':'created and emailed'})
        else:
            return Response({'success':'already created, emailed again'})
