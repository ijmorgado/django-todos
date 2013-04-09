from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

handler404 = 'todos_app.views.not_found_404'
handler500 = 'todos_app.views.internal_error_500'

urlpatterns = patterns('',
	url(r'^todos/', include('todos_app.urls',namespace='todos')),
	# Examples:
    # url(r'^$', 'TodosProject.views.home', name='home'),
    # url(r'^TodosProject/', include('TodosProject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)