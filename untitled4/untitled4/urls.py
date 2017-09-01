from django.conf.urls import url
from agent.views import agentinfo, index

from django.contrib import admin
admin.autodiscover()

urlpatterns = (
    url(r'^admin/', admin.site.urls),
    url(r'^agentinfo$', agentinfo, name='agentinfo'),
    url(r'^$', index, name='index'),

)
