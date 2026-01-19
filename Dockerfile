# =============================================================================
# DOCKERFILE - Insurance Claims Dashboard
# =============================================================================
#
# OVERVIEW
# --------
# This Dockerfile defines the container image for the Insurance Dashboard.
# It packages the Streamlit application with all its dependencies.
#
# WHAT IS A DOCKER CONTAINER?
# ---------------------------
# A container is a lightweight, standalone package that includes:
#   - Application code
#   - Runtime environment (Python)
#   - System libraries and dependencies
#   - Configuration files
#
# Containers ensure the application runs the same way in:
#   - Local development
#   - CI/CD testing
#   - Production deployment
#
# DOCKERFILE INSTRUCTIONS
# -----------------------
# Each instruction creates a new layer in the image:
#
#   FROM      - Base image to start from
#   WORKDIR   - Set the working directory
#   COPY      - Copy files into the container
#   RUN       - Execute commands during build
#   EXPOSE    - Document which port the app uses
#   CMD       - Command to run when container starts
#
# BUILD AND RUN COMMANDS
# ----------------------
# Build the image:
#   docker build -t insurance-dashboard .
#
# Run the container:
#   docker run -p 8501:8501 insurance-dashboard
#
# Access the application:
#   http://localhost:8501
#
# =============================================================================

# -----------------------------------------------------------------------------
# STAGE 1: BASE IMAGE
# -----------------------------------------------------------------------------
# Using Python 3.11 slim variant for smaller image size.
# The slim variant excludes development tools not needed at runtime.
# 
# Image size comparison:
#   python:3.11        ~1GB
#   python:3.11-slim   ~150MB
# -----------------------------------------------------------------------------
FROM python:3.11-slim

# -----------------------------------------------------------------------------
# METADATA LABELS
# -----------------------------------------------------------------------------
# Labels provide metadata about the image for documentation and tooling.
# -----------------------------------------------------------------------------
LABEL maintainer="Insurance Dashboard Team"
LABEL version="1.0"
LABEL description="Streamlit dashboard for insurance claims analytics"

# -----------------------------------------------------------------------------
# WORKING DIRECTORY
# -----------------------------------------------------------------------------
# Sets the working directory inside the container.
# All subsequent commands run from this directory.
# -----------------------------------------------------------------------------
WORKDIR /app

# -----------------------------------------------------------------------------
# INSTALL SYSTEM DEPENDENCIES
# -----------------------------------------------------------------------------
# Install curl for health checks.
# Clean up apt cache to reduce image size.
# -----------------------------------------------------------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------------------------------------------------------
# COPY REQUIREMENTS FIRST (LAYER CACHING OPTIMIZATION)
# -----------------------------------------------------------------------------
# Docker caches each layer. By copying requirements.txt first and installing
# dependencies before copying application code, we can reuse the cached
# dependencies layer when only application code changes.
#
# This significantly speeds up builds during development.
# -----------------------------------------------------------------------------
COPY requirements.txt .

# -----------------------------------------------------------------------------
# INSTALL PYTHON DEPENDENCIES
# -----------------------------------------------------------------------------
# --no-cache-dir: Do not store pip's cache (saves space)
# --upgrade pip: Ensure latest pip version for security and compatibility
# -----------------------------------------------------------------------------
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# -----------------------------------------------------------------------------
# COPY APPLICATION CODE
# -----------------------------------------------------------------------------
# Copy all application files into the container.
# The .dockerignore file excludes unnecessary files from the build context.
# -----------------------------------------------------------------------------
COPY . .

# -----------------------------------------------------------------------------
# EXPOSE PORT
# -----------------------------------------------------------------------------
# Documents that the container listens on port 8501.
# This is informational only; actual port binding happens at runtime with -p.
#
# Streamlit's default port is 8501.
# -----------------------------------------------------------------------------
EXPOSE 8501

# -----------------------------------------------------------------------------
# HEALTH CHECK
# -----------------------------------------------------------------------------
# Defines how Docker determines if the container is healthy.
# Streamlit exposes a health endpoint at /_stcore/health
#
# Parameters:
#   --interval: How often to run the check (30 seconds)
#   --timeout: Maximum time to wait for response (10 seconds)
#   --start-period: Grace period before starting checks (5 seconds)
#   --retries: Number of failures before marking unhealthy (3)
# -----------------------------------------------------------------------------
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# -----------------------------------------------------------------------------
# CONTAINER STARTUP COMMAND
# -----------------------------------------------------------------------------
# Command executed when the container starts.
#
# Streamlit configuration:
#   --server.port=8501           Port to run on
#   --server.address=0.0.0.0     Accept connections from any IP (required for Docker)
#   --server.headless=true       Run without browser (server mode)
#   --browser.gatherUsageStats=false   Disable telemetry
# -----------------------------------------------------------------------------
CMD ["streamlit", "run", "app.py", \
     "--server.port=8501", \
     "--server.address=0.0.0.0", \
     "--server.headless=true", \
     "--browser.gatherUsageStats=false"]
