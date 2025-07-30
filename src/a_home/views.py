from django.shortcuts import render

from .models import HomePageContent


def home_view(request):
    # This single query safely handles all cases:
    # 1. Finds the active content.
    # 2. If multiple are active, it picks the most recently created one.
    # 3. If none are active, it returns `None` without raising an error.
    page_content = (
        HomePageContent.objects.filter(is_active=True).order_by("-id").first()
    )

    if page_content:
        # The content from TinyMCE is already HTML, so no conversion is needed.
        html_content = page_content.content
    else:
        # Set a default message if no content was found.
        html_content = "<h1>Welcome!</h1><p>No active home page content found. Please create one in the admin panel.</p>"

    return render(
        request=request,
        template_name="home.html",
        context={"readme_content": html_content},
    )
