from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter

from account.views import UsersViewSet, StatusViewSet
from core import settings
from parsing.views import *

router = DefaultRouter()

router.register('product_title', ProductTitleViewSet)
router.register('results', ResultsViewSet)
router.register('users', UsersViewSet)
router.register('accounts/status', StatusViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title='Stack API',
        default_version='v1',
        description='Test description',
    ),
    public=True,
)

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('docs/', schema_view.with_ui()),
    path('admin/', admin.site.urls),
    path('accounts/', include("account.urls")),
    path('all_parse/', AllParseAPIView.as_view()),
    path('count_status/', CountStatusAPIView.as_view()),
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
