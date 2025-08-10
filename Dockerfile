# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY pyproject.toml .
RUN pip install --no-cache-dir streamlit pandas plotly numpy

# Copy application code
COPY . .

# Create data directory with proper permissions
RUN mkdir -p /app/data && chmod 755 /app/data

# Expose port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/_stcore/health || exit 1

# Run the application
CMD ["streamlit", "run", "app.py", "--server.port=5000", "--server.address=0.0.0.0", "--server.headless=true"]