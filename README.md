# Calculator API

## Overview:
The Calculator API is a web application built with Python using Django as the web framework. It enables users to upload CSV files containing mathematical operations and returns calculated results. The application also maintains logs of requests and their corresponding results, accessible through an admin interface.

## Features:
File Upload and Processing:

- Users can upload CSV files containing mathematical operations (addition, subtraction, multiplication, division).

- The API processes the file, performs calculations based on the provided operations, and returns the final result.

Error Handling:

- The API includes robust error handling for various scenarios, such as unsupported file formats, division by zero, and invalid data formats.

Request Logging:

- Each file upload is logged with details including the user, file name, and request date, enabling easy tracking of calculations.

Admin Interface:

- An admin UI allows users to browse through request logs and calculation results, providing insights into the operations performed through the API.

User-Friendly Home Page:

- The application features a simple web interface where users can upload their CSV files for processing.

## Technologies Used:
- Python: The primary programming language used for developing the application.

- Django: The web framework used for developing the application.

- SQLite: The database used for storing request logs and calculation results.

- HTML/CSS/JavaScript: Used for creating the user interface, styling the application, and enabling client-side interactivity.

- CSV File Handling: The API processes CSV files for mathematical operations, ensuring easy input format for users.

## Structure

API Endpoints:

- /api/upload/: Endpoint for uploading CSV files.

- /api/admin/: Endpoint for accessing the admin interface.
