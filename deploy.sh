#!/bin/bash

# Fitness Tracker Deployment Script
echo "🏋️ Deploying Fitness Tracker App..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    print_error "Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    print_error "Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Create necessary directories
print_status "Creating directories..."
mkdir -p data ssl

# Set permissions for data directory
chmod 755 data

# Stop existing containers
print_status "Stopping existing containers..."
docker-compose down

# Build and start containers
print_status "Building and starting containers..."
docker-compose up -d --build

# Wait for services to be ready
print_status "Waiting for services to start..."
sleep 10

# Check if the app is running
if curl -f http://localhost:5000/_stcore/health &> /dev/null; then
    print_status "✅ Fitness Tracker is running successfully!"
    print_status "🌐 Access your app at: http://localhost:5000"
else
    print_warning "App might still be starting. Check logs with: docker-compose logs -f"
fi

# Show running containers
print_status "Running containers:"
docker-compose ps

print_status "Deployment complete! 🎉"
print_status ""
print_status "Commands you can use:"
print_status "  📊 View logs: docker-compose logs -f"
print_status "  🔄 Restart: docker-compose restart"
print_status "  🛑 Stop: docker-compose down"
print_status "  📁 Backup data: tar -czf backup-$(date +%Y%m%d).tar.gz data/"