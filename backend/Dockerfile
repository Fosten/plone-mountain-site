# syntax=docker/dockerfile:1
ARG PLONE_VERSION=6.0.13
FROM plone/plone-backend:${PLONE_VERSION}

LABEL maintainer="Brian Davis <info@lillymountain.com>" \
      org.label-schema.name="plone-mountain-site-backend" \
      org.label-schema.description="Plone Mountain Site backend image." \
      org.label-schema.vendor="Brian Davis"

# Add local code
COPY . .

# Install local requirements and fix permissions
RUN <<EOT
    ./bin/pip install mxdev
    mv requirements-docker.txt requirements.txt
    ./bin/mxdev -c mx.ini
    ./bin/pip install -r requirements-mxdev.txt
    chown -R plone: /app
EOT
