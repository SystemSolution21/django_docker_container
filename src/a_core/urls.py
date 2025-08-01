"""
URL configuration for a_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from a_users.views import profile_view

urlpatterns = [
    # Django admin
    path("admin/", admin.site.urls),
    # Third-party apps
    path("accounts/", include("allauth.urls")),
    path("tinymce/", include("tinymce.urls")),
    # My apps
    path("profile/", include("a_users.urls")),
    path("@<username>/", profile_view, name="profile"),
    path("", include("a_home.urls")),  # Keep this last
]

# Only for development: serve media files and enable browser reload
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]
