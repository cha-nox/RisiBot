# Getting official Python image
FROM python:3.13-alpine

# Defining the working directory
WORKDIR /

# Keeping Package Installer for Python up to date
RUN python3 -m pip install --upgrade pip

# Installing Python dependencies into the container
RUN python3 -m pip install --no-cache-dir discord virtualenv

# Creating the virtual environment
RUN python3 -m venv venv

# Copying the application itself into the container
COPY . .

# Defining the running command
CMD ["python3", "-m", "index.py"]