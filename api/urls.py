from rest_framework import routers
from . import views
from django.urls import include, re_path

router = routers.SimpleRouter()
router.register(r'builds', views.BuildViewSet)

urlpatterns = [
    re_path(r'', include(router.urls)),
    re_path('pipeline-image', views.pipeline_from_github_api_endpoint),
    re_path('ga-version', views.ga_version),
    re_path('branch/', views.branch_data, name='branch_data_view'),
    re_path('test', views.test)
]
