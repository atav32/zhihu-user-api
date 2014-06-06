from django.conf.urls import url, patterns, include
from django.contrib.auth.models import User, Group
from django.contrib import admin
from rest_framework import viewsets, routers
from zhihuUser.models import ZhihuUser
from search.views import SearchPageView


# ViewSets define the view behavior.
class ZhihuUserViewSet(viewsets.ModelViewSet):
    model = ZhihuUser


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'api', ZhihuUserViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^search/', SearchPageView.as_view(), name='search_page'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
