from django.conf.urls import url,include
from . import views
app_name = 'app1'
urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
]