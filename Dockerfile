FROM python:3.13

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.2.10 /uv /uvx /usr/local/bin/

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV PATH="/app/.venv/bin:$PATH"

# Create a non-root user and group
RUN addgroup --system --gid 1001 django && \
    adduser --system --uid 1001 --ingroup django django

# Set work directory
WORKDIR /app

# Copy uv files
COPY uv.lock pyproject.toml ./

# Install dependencies
RUN uv sync --frozen --no-cache

# Copy project files
COPY ./src /app/

# Change ownership of the app directory to the non-root user
RUN chown -R django:django /app

# Switch to the non-root user
USER django

# Expose port
EXPOSE 8000

# Run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
