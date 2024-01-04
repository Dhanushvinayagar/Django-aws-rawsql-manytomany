from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.db import connection

from .models import *
from .serializers import *


# import boto3

# service = 'cognito-idp'
# aws_client = boto3.client(service,
#     aws_access_key_id = "<access_id>",
#     aws_secret_access_key = "<access_key>",
#     region_name =  '<region i.e Stockholm>'
# )
# access_token= "<token>"

# import random

# srp_a = random.getrandbits(1024)

# @api_view (['GET'])
def getKey(request):
#     if request.method == 'GET':

#         # ======================aws kms key========================================================
#         # key="<arn_key>"
#         # secret_text = "abcdefgh"
#         # cipher_text = kms_client.encrypt(
#         #     KeyId = key,
#         #     Plaintext=secret_text.encode(),
#         #     EncryptionAlgorithm='RSAES_OAEP_SHA_1'
#         # )['CiphertextBlob']

#         # print("Encrpytion***************************",cipher_text)

#         # text = kms_client.decrypt(
#         #     KeyId=key,
#         #     CiphertextBlob=cipher_text,
#         #     EncryptionAlgorithm='RSAES_OAEP_SHA_1'
#         # )['Plaintext']
#         # text=text.decode('utf-8')
#         # print("TEXT**************************",text)

#         # response = kms_client.list_resource_tags(KeyId=key)
#         # print(response['Tags'])


#         # ==================================aws cognito user pool role=====================================

#         response = aws_client.initiate_auth(
#             AuthFlow='USER_PASSWORD_AUTH',
#             AuthParameters={
#                 'USERNAME': '<username>', 
#                 'PASSWORD': '<password>'
#             },
#             ClientId='<client id>',
#         )
        
#         user_attributes = aws_client.get_user(
#            AccessToken = response.get("AuthenticationResult")["AccessToken"]
#         )
#         # print(user_attributes.get("UserAttributes"))
#         # for i in user_attributes.get("UserAttributes"):
#         #     if i.get("Name") == "profile":
#         #         print("\n\n\n\n\n\n\n\n===============>",i["Value"])



#         # ===================================identity pool===========================================
        
#         iam_client = boto3.client('iam')

#         cognito_identity = user_attributes
#         print(cognito_identity)
#         groups = [attr['Value'] for attr in cognito_identity['UserAttributes'] if attr['Name'] == 'custom:groups']

    
#         def get_role_name_for_groups(groups):
#             print(groups)
#             if 'AdminGroup' in groups:
#                 return 'AdminRole'
#             elif 'UserRole' in groups:
#                 return 'UserRole'
#             else:
#                 return 'DefaultRole'
#         role_name = get_role_name_for_groups(groups)
#         print("************************************************************************************************************************************************************",role_name)

#         role_arn = f'arn:aws:iam::your-account-id:role/{role_name}'
#         # assume_role_response = iam_client.assume_role(RoleArn=role_arn, RoleSessionName='session-name')

#         print(role_arn)
        return Response({"key":"value"})


@api_view (['GET','POST'])
def home(request):

    if request.method== 'GET':
        datas = Employee.objects.all()
        obj = EmployeeSerializer(datas,many=True)
        return Response(obj.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = EmployeeSerializer(data = data)
        if serializer.is_valid():
            serializer.save()

        datas = Employee.objects.all()
        obj = EmployeeSerializer(datas,many=True)
        return Response({'Post method':serializer.data})
 
@api_view (['PATCH','PUT','DELETE'])

def detailsupdate(request,pk):

    emp = Employee.objects.get(pk=pk)

    if request.method == 'PUT':
        data = request.data
        serializer = EmployeeSerializer(emp , data = data)
        if serializer.is_valid():
            serializer.save()
    
    elif request.method == 'PATCH':
        data = request.data
        serializer = EmployeeSerializer(emp ,data = data,partial=True)
        if serializer.is_valid():
            serializer.save()

    
    elif request.method == 'DELETE':
        emp.delete()
    
    datas = Employee.objects.all()
    obj = EmployeeSerializer(datas,many=True)
    return Response({'api':obj.data})

# Big H
class TableApi(APIView):

    def get(self,request):
        data = TableDb.objects.all()
        obj = TableSerializer(data,many=True)
        return Response({"class get":obj.data})
    
    def post(self,request):
        serializer = TableSerializer(data=request.data)
    
        if serializer.is_valid():
            serializer.save()
        data = TableDb.objects.all()
        obj = TableSerializer(data,many=True)
        return Response(obj.data)
    
    def put(self,request,pk):
        instance = TableDb.objects.get(id=pk)
        if instance is not None:
            serializer = TableSerializer(instance,data = request.data)
            if serializer.is_valid():
                serializer.save()
        data = TableDb.objects.all()
        obj = TableSerializer(data,many=True)
        return Response(obj.data)
    
    def patch(self,request,pk):
        instance = TableDb.objects.get(id=pk)
        if instance:
            serializer = TableSerializer(instance , data = request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
        data = TableDb.objects.all()
        obj = TableSerializer(data,many=True)
        return Response(obj.data)        
    
    def delete(self,request,pk):
        instance = TableDb.objects.get(id=pk)
        if instance:
            instance.delete()
        data = TableDb.objects.all()
        obj = TableSerializer(data,many=True)
        return Response(obj.data)         


class RoleApi(APIView):

    def get(self,request):
        data = UserRole.objects.all()
        obj = RoleSerializer(data,many=True)
        return Response({"class get":obj.data})
    
    # def get(self,request,pk):
    #     data = UserRole.objects.get(id=pk)
    #     obj = RoleSerializer(data)
    #     return Response({"class get":obj.data})
    
    def post(self,request):
        serializer = RoleSerializer(data=request.data)
    
        if serializer.is_valid():
            serializer.save()
        data = UserRole.objects.all()
        obj = RoleSerializer(data,many=True)
        return Response(obj.data)
    
    def put(self,request,pk):
        instance = UserRole.objects.get(id=pk)
        if instance is not None:
            serializer = RoleSerializer(instance,data = request.data)
            if serializer.is_valid():
                serializer.save()
        data = UserRole.objects.all()
        obj = RoleSerializer(data,many=True)
        return Response(obj.data)
    
    def patch(self,request,pk):
        instance = UserRole.objects.get(id=pk)
        if instance:
            serializer = RoleSerializer(instance , data = request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
        data = UserRole.objects.all()
        obj = RoleSerializer(data,many=True)
        return Response(obj.data)        
    
    def delete(self,request,pk):
        instance = UserRole.objects.get(id=pk)
        if instance:
            instance.delete()
        data = UserRole.objects.all()
        obj = RoleSerializer(data,many=True)
        return Response(obj.data)         


# Big U 
class PersonaApi(APIView):
    def get(self,request):
        data = PersonaDb.objects.all()
        orderdict = PersonaSerializer(data,many=True)

        # django_queries.log file will stroe the raw query of this file
        connection.force_debug_cursor = True
        connection.force_debug_cursor = False

        # execcuting raw query in django
        raw_data = PersonaDb.objects.raw('SELECT id, persona_name , persona_code,persona_description from app_PersonaDb where id=1 LIMIT 1')[0]
        print("**********************************************************")
        print(raw_data)
        print("**********************************************************")
        return Response(orderdict.data)



@api_view (['GET'])
def employeedetails(request):
    if request.method == 'GET':
        raw_data = PersonaDb.objects.raw('SELECT id, persona_name , persona_code,persona_description from app_PersonaDb')
        print(raw_data)
        for i in raw_data:
            print(i)
        return Response({"res":"Success"})