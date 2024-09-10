FROM python:3.10-slim-buster

# Install system dependencies for OpenCV and other packages
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /flask-app

COPY requirements.txt requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

# Install Gunicorn
RUN pip install gunicorn

# Use Gunicorn to serve the app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
