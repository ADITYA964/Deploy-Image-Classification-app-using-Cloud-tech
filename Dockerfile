# ================= DockerFile Commands ===================

# We are importing an Ubuntu Operating system with 
# version of 22.04 for our virtual workspace to run in cloud.
FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
# To create python 3.9 environment.
RUN apt-get update \
    && apt-get install -y git python3-pip python3.9 

# Install dependencies to setup python environment.
RUN apt-get install ffmpeg libsm6 libxext6 -y

# We need to set the current working directory to 'app' folder
# which is present in Docker virtual space to run the application.
WORKDIR /app

# Copy the contents of files into the current working folder 'app'.
COPY requirements.txt ./requirements.txt
COPY config.prod.toml ./config.prod.toml
COPY credentials.prod.toml ./credentials.prod.toml

# Install python libraries for application execution purpose.
RUN pip3 install -r requirements.txt

# To setup Streamlit framework, we create 
# a folder called 'streamlit' inside 'app' folder.
RUN mkdir ~/.streamlit

# Store the configuration files inside 'streamlit' folder.
RUN cp config.prod.toml ~/.streamlit/config.prod.toml
RUN cp credentials.prod.toml ~/.streamlit/credentials.prod.toml

# Streamlit applications run on 
# 8501 so we expose a port at 8501.
EXPOSE 8501

# We copy any related files to 
# program into 'app' folder if needed. 
COPY . /app

# The starting point for running commands 
# before running python script.
ENTRYPOINT ["streamlit", "run"]

# Run the python script.
CMD ["app.py"]
