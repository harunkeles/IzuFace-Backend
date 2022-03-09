from asyncio.proactor_events import constants
from audioop import reverse
from http.client import HTTPResponse
import json
from posts.models import PostModel
from studentUsers.models import StudentExperiencesModel, StudentImageGalleryModel, StudentUserProfileModel
from .models import *
from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import AllUserSerializer, AuthUserSerializer, AuthUserSiteSettingsSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import obtain_auth_token


class AllUserListView(ListAPIView):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = AllUserSerializer

    def get(self,request, *args,**kwargs):
        main_list = []
        for user in self.User.objects.all():
            
            token, created = Token.objects.get_or_create(user = user)
            # We find the auth student user profile
            student = StudentUserProfileModel.objects.filter(user=user).first()

            # We find the image gallery of auth user
            auth_student_gallery = StudentImageGalleryModel.objects.filter(studentUser=student)
            auth_student_gallery_list = []
            if auth_student_gallery:
                index = 1
                for i in auth_student_gallery:
                    image_list = {
                            i.id : {
                                "image_url" : i.image.url,
                                "image_dec" : i.imageDec,
                            }
                        }
                    index += 1 
                    auth_student_gallery_list.append(image_list)

            # We find the image gallery of auth user
            auth_student_experiences = StudentExperiencesModel.objects.filter(studentUser=student)
            list_1 = []
            list_2 = []
            if auth_student_experiences:
                for i in auth_student_experiences:
                    if i.EXPERIENCE_INFO[0][0] == i.experienceInfo[0]:
                        experiences_list = {
                                i.id : {
                                    "company_name" : i.companyName,
                                    "company_dec" : i.experienceDesc,
                                    "started_date" : i.startedDate,
                                    "finished_date" : i.finishedDate,
                                },
                            }
                        list_1.append(experiences_list)

                    elif i.EXPERIENCE_INFO[1][0] == i.experienceInfo[0]:
                        experiences_list = {
                                i.id : {
                                    "company_name" : i.companyName,
                                    "company_dec" : i.experienceDesc,
                                    "started_date" : i.startedDate,
                                    "finished_date" : i.finishedDate,
                                },
                            }
                        list_2.append(experiences_list)


            # We find the following
            following_this_user =  self.User.objects.raw("Select * from studentUsers_studentuserprofilemodel_following where studentuserprofilemodel_id = %s",[user.id])
            following_list = []
            for i in range(len(list(following_this_user))):
                all_following_this_user = StudentUserProfileModel.objects.filter(id = following_this_user[i].user_id)
                print(all_following_this_user[0])
                following_list.append(all_following_this_user[0].id)

            # We find the followers count
            followers =  self.User.objects.raw("Select * from studentUsers_studentuserprofilemodel_following where user_id = %s",[user.id])
            followers_count = len(list(followers))

            
            one_dict = {
                'token': token.key,
                'user_id': user.pk,
                'email': user.email,
                'username':user.username,
                'first_name':user.first_name,
                'last_name':user.last_name,
                'is_active':user.is_active,
                'is_staff':user.is_staff,
                'is_superuser':user.is_superuser,
                'date_joined':user.date_joined,
                'last_login':user.last_login,
                'more_info': {
                    'user_status': 'student',
                    'studentId':student.studentId,
                    'backImage':student.backImage.url,
                    'profImage':student.profImage.url,
                    'departmentName':student.departmentName,
                    'smallDesc':student.smallDesc,
                    'bioDesc':student.bioDesc,
                    'departmentClass':student.departmentClass,
                    'phoneNumber':student.phoneNumber,
                    'adress':student.adress,
                    'birth_day':student.birth_day,
                    'studentUserSelfInfo':student.studentUserSelfInfo,
                    'instagram':student.instagram,
                    'twitter':student.twitter,
                    'github':student.github,
                    'linkedin':student.linkedin,
                    'facebook':student.facebook,
                    'whatsapp':student.whatsapp,
                    'studentUserSocialMedia':student.studentUserSocialMedia,
                    'following': following_list,
                    'followers': followers_count,
                },
                'student_galleries': auth_student_gallery_list,
                'student_experiences': {
                    "work_exp": list_1,
                    "intern_exp": list_2
                }
            }
            main_list.append(one_dict)

        return Response(main_list)




class AuthUserInfoView(RetrieveUpdateAPIView):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = AuthUserSerializer
    
    def get(self,request, url=None,*args,**kwargs):
        token, created = Token.objects.get_or_create(key = url)
        if url == token.key:
            user = token.user
            # We find the auth student user profile
            student = StudentUserProfileModel.objects.filter(user=user).first()

            # We find the image gallery of auth user
            auth_student_gallery = StudentImageGalleryModel.objects.filter(studentUser=student)
            auth_student_gallery_list = []
            if auth_student_gallery:
                index = 1
                for i in auth_student_gallery:
                    image_list = {
                            i.id : {
                                "image_url" : i.image.url,
                                "image_dec" : i.imageDec,
                            }
                        }
                    index += 1 
                    auth_student_gallery_list.append(image_list)


            # We find the image gallery of auth user
            auth_student_experiences = StudentExperiencesModel.objects.filter(studentUser=student)
            list_1 = []
            list_2 = []
            if auth_student_experiences:
                for i in auth_student_experiences:
                    if i.EXPERIENCE_INFO[0][0] == i.experienceInfo[0]:
                        experiences_list = {
                                i.id : {
                                    "company_name" : i.companyName,
                                    "company_dec" : i.experienceDesc,
                                    "started_date" : i.startedDate,
                                    "finished_date" : i.finishedDate,
                                },
                            }
                        list_1.append(experiences_list)

                    elif i.EXPERIENCE_INFO[1][0] == i.experienceInfo[0]:
                        experiences_list = {
                                i.id : {
                                    "company_name" : i.companyName,
                                    "company_dec" : i.experienceDesc,
                                    "started_date" : i.startedDate,
                                    "finished_date" : i.finishedDate,
                                },
                            }
                        list_2.append(experiences_list)


            # We find the posts-likes
            all_post_like_this_user =  StudentUserProfileModel.objects.raw("Select * from posts_postmodel_likes where user_id = %s",[user.id])
            like_list = []
            for i in range(len(list(all_post_like_this_user))):
                all_post_this_user =  PostModel.objects.filter(id = all_post_like_this_user[i].postmodel_id)
                for liked_post_id in range(len(list(all_post_this_user))):
                    like_list.append(all_post_this_user[liked_post_id].id)

            # We find the following
            following_this_user =  self.User.objects.raw("Select * from studentUsers_studentuserprofilemodel_following where studentuserprofilemodel_id = %s",[user.id])
            following_list = []
            for i in range(len(list(following_this_user))):
                all_following_this_user = StudentUserProfileModel.objects.filter(id = following_this_user[i].user_id)
                print(all_following_this_user[0])
                following_list.append(all_following_this_user[0].id)

             # We find the followers count
            followers =  self.User.objects.raw("Select * from studentUsers_studentuserprofilemodel_following where user_id = %s",[user.id])
            followers_count = len(list(followers))


        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username':user.username,
            'first_name':user.first_name,
            'last_name':user.last_name,
            'is_active':user.is_active,
            'is_staff':user.is_staff,
            'is_superuser':user.is_superuser,
            'date_joined':user.date_joined,
            'last_login':user.last_login,
            'more_info': {
                'user_status': 'student',
                'studentId':student.studentId,
                'backImage':student.backImage.url,
                'profImage':student.profImage.url,
                'departmentName':student.departmentName,
                'smallDesc':student.smallDesc,
                'bioDesc':student.bioDesc,
                'departmentClass':student.departmentClass,
                'phoneNumber':student.phoneNumber,
                'adress':student.adress,
                'birth_day':student.birth_day,
                'studentUserSelfInfo':student.studentUserSelfInfo,
                'instagram':student.instagram,
                'twitter':student.twitter,
                'github':student.github,
                'linkedin':student.linkedin,
                'facebook':student.facebook,
                'whatsapp':student.whatsapp,
                'studentUserSocialMedia':student.studentUserSocialMedia,
                'following': following_list,
                'followers': followers_count,
            },
            'student_galleries': auth_student_gallery_list,
            'student_experiences': {
                "work_exp": list_1,
                "intern_exp": list_2
            },
            'post_likes' : like_list,
        })



class AuthUserSiteSettingsView(RetrieveUpdateDestroyAPIView):
    queryset = AuthUserSiteSettingsModel.objects.all()
    serializer_class = AuthUserSiteSettingsSerializer

    def get(self,request, pk=None,*args,**kwargs):
        deger = AuthUserSiteSettingsModel.objects.filter(user=pk)
        return Response({
            "user_id" : deger[0].user.id,
            "username" : deger[0].user.username,
            "dark_theme" : deger[0].dark_theme
        })


    def patch(self, request, pk=None):
        item = AuthUserSiteSettingsModel.objects.filter(user=pk)
        serializer = AuthUserSiteSettingsSerializer(item[0], data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "id" : item[0].id,
                "user_id" : item[0].user.id,
                "username" : item[0].user.username,
                "dark_theme" : item[0].dark_theme
            })
        else:
            return Response({"status": "error", "data": serializer.errors})

