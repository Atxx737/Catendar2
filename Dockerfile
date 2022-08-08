# The image you are going to inherit your Dockerfile from
FROM python:3.10.6-alpine
# upgrade pip
RUN python -m venv venv
RUN pip install --upgrade pip

#fix error: install pandas
RUN apk add --no-cache --update \
    python3 python3-dev gcc \
    gfortran musl-dev g++ \
    libffi-dev openssl-dev \
    libxml2 libxml2-dev \
    libxslt libxslt-dev \
    libjpeg-turbo-dev zlib-dev
# Necessary, so Docker doesn't buffer the output and that you can see the output 
# of your application (e.g., Django logs) in real-time.
ENV PYTHONUNBUFFERED 1
# Make a directory in your Docker image, which you can use to store your source code
RUN mkdir /catendar
# Set the /Catendar directory as the working directory
WORKDIR /catendar
# Copies from your local machine's current directory to the Catendar folder 
# in the Docker image
COPY . .
# Copy the requirements.txt file adjacent to the Dockerfile 
# to your Docker image
COPY ./requirements.txt /requirements.txt
# Install the requirements.txt file in Docker image
RUN pip install -r /requirements.txt
# maybe run port 5453 for postgress
RUN apk add --update postgresql-client jpeg-dev
RUN apk add --update --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
# Create a user that can run your container
RUN adduser -D user
USER user