# FROM ubuntu:16.04
FROM python:2.7-wheezy
RUN apt-get update && apt-get install -y

# Set the working directory to /app
WORKDIR /usr/src/Falsy

# Copy the current directory contents into the container at /app
COPY . /usr/src/Falsy

# Install any needed packages specified in requirements.txt
RUN pip install  -r requirements.txt

ENV TCM_API_host = 0.0.0.0
ENV TCM_DB_host = 0.0.0.0

EXPOSE 8089

# Run app.py when the container launches
CMD ["python", "app.py"]
