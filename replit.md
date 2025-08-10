# Fitness Progress Tracker

## Overview

This is a Streamlit-based fitness tracking application designed to help users monitor their 7-day fat-loss workout and Indian diet plan. The application provides comprehensive tracking capabilities for body metrics, workout completion, diet adherence, and progress analytics. It follows a structured 7-day plan targeting 2,000-2,200 kcal/day with specific macro distributions (P: 170-180g, C: 180-200g, F: 55-65g) and includes detailed workout routines for different muscle groups.

**Recent Updates (January 2025):** Enhanced with Progressive Web App (PWA) capabilities and mobile-first design optimizations for iOS devices. The app now features touch-friendly interfaces, installation prompts, offline functionality, and responsive layouts optimized for iPhone usage.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Framework**: Streamlit web application with multi-page architecture
- **Page Structure**: Main dashboard (`app.py`) with dedicated pages for weekly entry, progress analytics, and plan overview
- **UI Components**: Sidebar navigation, tabbed interfaces, metrics displays, and interactive charts
- **Layout**: Wide layout with responsive columns and expandable sidebar for navigation
- **PWA Features**: Progressive Web App capabilities with manifest.json, service worker, offline support, and mobile installation prompts
- **Mobile Design**: Touch-friendly interfaces, enhanced CSS styling, haptic feedback, and iOS-optimized layouts

### Backend Architecture
- **Data Layer**: CSV-based file storage system managed through `DataManager` class
- **Business Logic**: Separated into utility modules for data management, analytics, and workout plan definitions
- **Core Modules**:
  - `DataManager`: Handles all data persistence and retrieval operations
  - `Analytics`: Provides data analysis and visualization capabilities
  - `workout_plans.py`: Contains structured workout and diet plan definitions

### Data Storage Solutions
- **Storage Type**: Local CSV files for simplicity and portability
- **Data Categories**:
  - Body metrics (weight, fat percentage, muscle mass, body measurements)
  - Workout data (completion tracking, exercise progress, intensity ratings)
  - Diet data (adherence scores, calorie estimates, meal compliance)
- **Data Directory**: Organized under `/data` folder with automatic initialization
- **Schema Design**: Structured with date/week tracking for temporal analysis

### Analytics and Visualization
- **Charting Library**: Plotly for interactive visualizations
- **Chart Types**: Line charts for progress tracking, trend analysis with polynomial fitting
- **Metrics Calculation**: Progress statistics, compliance rates, and goal tracking
- **Real-time Updates**: Dynamic data loading and chart generation based on user entries

### Application Flow
- **Navigation**: Sidebar-based navigation with quick stats display
- **Data Entry**: Structured forms with validation for daily metric input
- **Progress Tracking**: Automated compliance calculations and trend analysis
- **Plan Reference**: Static display of workout routines and diet plans for user guidance

## External Dependencies

### Python Libraries
- **Streamlit**: Web application framework for the user interface
- **Pandas**: Data manipulation and analysis for CSV operations
- **Plotly**: Interactive charting and visualization library
- **NumPy**: Numerical computations for trend analysis and statistics
- **datetime**: Built-in Python module for date/time handling

### Data Dependencies
- **Local File System**: CSV files stored locally for data persistence
- **Static Plan Data**: Hardcoded workout and diet plans based on the attached 7-day master plan
- **No External APIs**: Self-contained application without external service dependencies

### Development Dependencies
- Standard Python environment with ability to install packages via pip
- File system write permissions for data storage
- Web browser for Streamlit interface access