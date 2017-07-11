from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from authapp import views as auth_views
from school import views as school_views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', auth_views.UserViewSet)
router.register(r'groups', auth_views.GroupViewSet)
router.register(r'schools', school_views.SchoolViewSet)
router.register(r'students', school_views.StudentViewSet)
router.register(r'activities', school_views.ActivityViewSet)
router.register(r'assignments', school_views.AssignmentViewSet)

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    # url(r'^api/', include('school.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
