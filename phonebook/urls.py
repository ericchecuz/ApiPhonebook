
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, views
from .phonebook import views
router = routers.DefaultRouter()
router.register(r'phonebook', views.PhonebookViewSet)
router.register(r'contacts', views.ContactsViewSet)

urlpatterns = [
    # path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('phonebook/', include('phonebook.phonebook.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
