from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Django Admin
    path("admin/", admin.site.urls),

    # Users / Authentication
    path("users/", include("users.urls")),

    # Homepage and main user routes
    path("", include("users.urls")),

    # Movies
    path("movies/", include("movies.urls")),
]


# Serve media files during local development
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
