# ===================================================================
# DOCKERFILE - Insurance Claims Dashboard
# ===================================================================
# 
# WHAT IS A DOCKERFILE?
# ---------------------
# A Dockerfile is like a recipe that tells Docker how to build your app
# into a "container" - a portable package that includes everything your
# app needs to run (Python, libraries, your code, etc.)
#
# Think of it like this:
# - Your computer might have Python 3.9, but your friend has Python 3.11
# - With Docker, both of you can run the EXACT same environment
# - This eliminates "it works on my machine!" problems
#
# HOW IT WORKS:
# -------------
# 1. Start with a base image (Python already installed)
# 2. Copy your code into the container
# 3. Install dependencies
# 4. Define how to run your app
#
# ===================================================================

# STEP 1: Start from Python base image
# -------------------------------------
# This is like saying "start with a computer that already has Python"
# python:3.11-slim is a lightweight version (smaller download)
FROM python:3.11-slim

# STEP 2: Set the working directory
# ----------------------------------
# This is like doing "cd /app" - all following commands run from here
WORKDIR /app

# STEP 3: Copy requirements first (for caching)
# -----------------------------------------------
# Docker caches each step. By copying requirements first, Docker can
# reuse the cached dependencies when only your code changes (not deps)
COPY requirements.txt .

# STEP 4: Install Python dependencies
# ------------------------------------
# --no-cache-dir: Don't store pip's cache (saves space in container)
RUN pip install --no-cache-dir -r requirements.txt

# STEP 5: Copy the rest of your application
# -------------------------------------------
# This copies all your code (app.py, src/, data/) into the container
COPY . .

# STEP 6: Expose the port Streamlit runs on
# -------------------------------------------
# EXPOSE doesn't actually publish the port, it's documentation
# The actual port is opened when you run the container with -p flag
EXPOSE 8501

# STEP 7: Health check (optional but recommended)
# -------------------------------------------------
# This tells Docker how to check if your app is healthy
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# STEP 8: Define how to run the app
# -----------------------------------
# This is the command that runs when the container starts
# --server.port: Which port to use
# --server.address: 0.0.0.0 means accept connections from anywhere
# --server.headless: Run without opening a browser
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]
