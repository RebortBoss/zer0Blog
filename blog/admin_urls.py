from django.conf.urls import url,include

from blog.admin_views import PostView, DeletePost

urlpatterns = [
    url(r'^admin/', include([
        url(r'^$', PostView.as_view(), name='index'),
        url(r'^delete/(?P<pk>[0-9]+)$', DeletePost.as_view())
    ])),
]