
from django.conf import settings
from django.urls import path, re_path
from django.conf.urls import url

from products.views import (ProductListView,
                            ProductDetailSlugView,
                            )

urlpatterns = [
    path('', ProductListView.as_view()),
    re_path(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name= 'detail'),
]
