from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('detail/<int:id>/',views.hood_detail,name='details'),
    path('profile/',views.profile_page,name='profile'),
    path('submit_post/<int:hood_id>/',views.submit_post,name='submit_post'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)