import markdown
from django.shortcuts import render


def home_view(request):
    with open(file="README.md", mode="r", encoding="utf-8") as f:
        readme: str = f.read()
        html_readme: str = markdown.markdown(text=readme, extensions=["fenced_code"])
    return render(
        request=request,
        template_name="home.html",
        context={"readme_content": html_readme},
    )
