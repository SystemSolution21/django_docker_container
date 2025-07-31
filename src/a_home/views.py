import bleach
import markdown
from django.shortcuts import render

from .models import HomePageContent

# Define Markdown extensions as a constant for clarity and reusability.
MARKDOWN_EXTENSIONS = [
    "fenced_code",  # For GitHub-style code blocks (```)
    "tables",  # For data tables
    "admonition",  # For styled blocks (e.g., !!! note)
    "md_in_html",  # To parse Markdown inside HTML tags
]

# Define bleach whitelists as constants to keep the view logic clean.
ALLOWED_TAGS = [
    "p",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "strong",
    "b",
    "em",
    "i",
    "u",
    "strike",
    "s",
    "del",
    "ul",
    "ol",
    "li",
    "a",
    "br",
    "hr",
    "pre",
    "code",
    "blockquote",
    "table",
    "thead",
    "tbody",
    "tr",
    "th",
    "td",
    "div",
    "span",
    "img",
]
ALLOWED_ATTRIBUTES = {
    "*": ["class", "id", "markdown"],  # Allow class, id, and markdown on any tag
    "a": ["href", "title", "target"],
    "img": ["src", "alt", "title", "width", "height"],
}


def home_view(request):
    # This single query safely handles all cases:
    # 1. Finds the active content.
    # 2. If multiple are active, it picks the most recently created one.
    # 3. If none are active, it returns `None` without raising an error.
    page_content = (
        HomePageContent.objects.filter(is_active=True).order_by("-id").first()
    )

    if page_content:
        # 1. Convert Markdown to potentially unsafe HTML.
        unsafe_html = markdown.markdown(
            page_content.content, extensions=MARKDOWN_EXTENSIONS
        )

        # 2. Sanitize the HTML to prevent XSS, stripping any disallowed elements.
        html_content = bleach.clean(
            unsafe_html,
            tags=ALLOWED_TAGS,
            attributes=ALLOWED_ATTRIBUTES,
            strip=True,
        )
    else:
        # Set a default message if no content was found.
        html_content = "<h1>Welcome!</h1><p>No active home page content found. Please create one in the admin panel.</p>"

    return render(
        request=request,
        template_name="home.html",
        context={"readme_content": html_content},
    )
