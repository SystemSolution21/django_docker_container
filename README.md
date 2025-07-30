# Django Docker Container

This project is a **modern and well-structured for a Django web application**, designed to be developed and run inside a Docker container. It serves as an excellent starting point for building new applications, incorporating many current best practices.
<br>

## Core Technology Stack

* **Backend:** Django `5.2.4`
* **Language:** Python `3.13`
* **Package Management:** `uv`, a fast and modern Python package installer and resolver. Dependencies are locked in `uv.lock` for reproducible builds.
* **Containerization:** Docker and Docker Compose provide a consistent and isolated development environment.

<br>

## Key Features & Characteristics

**1.Container-First Design:** The entire setup is built around Docker. The `Dockerfile` is optimized for security (by creating a non-root `django` user) and reproducibility. The `docker-compose.yml` file orchestrates the application service, making it easy to start, stop, and manage.

**2.Excellent Development Workflow:**<br>
    **(a).Live Code Reloading:** The use of volumes in `docker-compose.yml` (`./src/:/app/`) means any changes make to source code on local machine are instantly reflected inside the running container without needing to rebuild the image.<br>
    **(b).Automatic Browser Refresh:** The inclusion of `django-browser-reload` in dependencies enhances the development experience by automatically refreshing web browser when a file is saved.<br>
    **(c).Dynamic Frontend with HTMX:** The project uses `django-htmx`, allowing to build modern, interactive user interfaces with the power of AJAX but without writing complex JavaScript.

**3.Robust User Authentication:** It integrates `django-allauth`, a comprehensive package that handles user registration, login, password management, and social account authentication right out of the box.

**4.Rich Content Management:** The homepage content is managed dynamically through the Django admin panel. By integrating `django-tinymce`, the `HomePageContent` model provides a full WYSIWYG (What You See Is What You Get) editor, allowing administrators to create and edit rich HTML content without writing any code.
