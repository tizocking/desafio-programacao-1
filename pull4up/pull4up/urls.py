from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from formparser import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', views.index, name='index')
)
