# Use a lightweight base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /home/data

# Copy the Python script and text files to the container
COPY script.py .
COPY IF.txt .
COPY AlwaysRememberUsThisWay.txt .

# Create an output directory inside the container
RUN mkdir -p /home/data/output

# Run the Python script
CMD ["python", "./script.py"]
