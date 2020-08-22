from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('content.urls')),
    path('', include('identity.urls')),
    
    path('mesajlar/', include('pinax.messages.urls', namespace='pinax_messages')),
    path('begeniler/', include('pinax.likes.urls', namespace='pinax_likes')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
