# Use the official Python image as a base
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script to the container
COPY age_calculator.py .

# Command to run the Python script
CMD ["python", "age_calculator.py"]

