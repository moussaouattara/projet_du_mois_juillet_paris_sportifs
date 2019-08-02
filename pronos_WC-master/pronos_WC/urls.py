from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin
from pronos_WC.apps.football.views import JoueurClassementView, MatchView, MatchOldView, MyPronosticsView, add_pronostic
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pronos_WC.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Statics pages
    url(r'^$', TemplateView.as_view(template_name='static-pages/home.html'), name='home'),
    url(r'^error/404.html', TemplateView.as_view(template_name='404.html'), name='error-404'),
    url(r'^error/500.html', TemplateView.as_view(template_name='500.html'), name='error-500'),

    # Apps
    url(r'^classement.html$', JoueurClassementView.as_view(), name='classement'),
    url(r'^match.html$', MatchView.as_view(), name='match'),
    url(r'^resultat.html$', MatchOldView.as_view(), name='resultat'),
    url(r'^pronostics.html$', MyPronosticsView.as_view(), name='pronostics'),
    url(r'^pronostic/add$', add_pronostic, name='pronos_WC_create_pronostic'),

    # Media
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'login.html'},
        name='pronos_WC_login'),
    url(r'^logout/$', 'logout', {'next_page': '/'}, name='pronos_WC_logout'),
)
