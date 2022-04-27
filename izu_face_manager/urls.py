
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from izu_face_manager.views import RegisterView, UserLogout, UserSignin


urlpatterns = [
    # Rest_Framework base url
    path('api-auth/',include('rest_framework.urls')),

    # My_Api(s)
    path('api/v0/all-endpoints/',include('apiApp.urls')),
    path('api/v0/posts/',include('posts.api.urls')),
    path('api/v0/news/',include('news.api.urls'), name='post-api'),
    path('api/v0/discussions/',include('discussions.api.urls'), name='discussions-api'),
    path('api/v0/student-user/',include('studentUsers.api.urls'), name='student-user-api'),
    path('api/v0/appointments/',include('appointments.api.urls'), name='appointments-api'),

    # Side urls
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserSignin.as_view(), name='userSignin'),
    path('logout/', UserLogout.as_view(), name='userLogout'),
    path('', include('mainPage.urls')),
    path('std/', include('studentUsers.urls')),
    path('news/', include('news.urls')),
    path('posts/', include('posts.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
