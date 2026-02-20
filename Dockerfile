FROM python:3.12-slim

# some optional metadata about the image
LABEL version="1.0"
LABEL maintainer="Jay Prajapati <jcprajapati9120@gmail.com>"
LABEL description="Dockerized Streamlit app for movie recommendation system"
LABEL repository="https://github.com/JayPrajapati09/Movie-Recommendation"

# set the working directory in the container
WORKDIR /app

# copy the requirements file into the container within /app folder
# COPY app.py /app/
COPY . .

# install the dependencies from the requirements file
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# expose the port that Streamlit will run on
EXPOSE 8501

# set the entry point to run the Streamlit app when the container starts
ENTRYPOINT ["streamlit", "run", "app.py"]
 