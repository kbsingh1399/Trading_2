# OMNI headless cloud runtime — multi-stage, minimal, non-root.
# Build:  docker build -f deploy/Dockerfile -t omni-headless:latest .
# Run:    docker compose -f deploy/docker-compose.yml up -d
FROM python:3.11-slim AS builder
WORKDIR /app
COPY deploy/requirements-headless.txt .
RUN pip wheel --no-cache-dir --wheel-dir /wheels -r requirements-headless.txt

FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/app
WORKDIR /app
# runtime deps only; wheels copied from the builder stage
COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir --no-index /wheels/*.whl && rm -rf /wheels
# application code (tests and data stay out of the image)
COPY Terminal /app/Terminal
COPY deploy/requirements-headless.txt /app/deploy/requirements-headless.txt
# non-root, no shell for the service user
RUN useradd --create-home --shell /usr/sbin/nologin omni && mkdir -p /app/Data && chown -R omni:omni /app
USER omni
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=5s --start-period=30s --retries=3 \
  CMD ["python", "-c", "import sys,urllib.request; sys.exit(0 if urllib.request.urlopen('http://127.0.0.1:8080/healthz', timeout=3).status == 200 else 1)"]
CMD ["python", "-m", "Terminal.Headless"]
