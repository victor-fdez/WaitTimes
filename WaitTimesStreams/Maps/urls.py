from django.conf.urls import patterns, url

urlpatterns = patterns('Maps.views',
	url('^current_location/', 'current_location'),
)	
