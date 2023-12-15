# Select the base image
FROM  python:3.10

# Set the working directory
WORKDIR /code


RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*


# Copy the requirements file
COPY ./requirements.txt /code/requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./API_SP.POP.TOTL_DS2_en_csv_v2_6224560.csv /code/API_SP.POP.TOTL_DS2_en_csv_v2_6224560.csv

COPY ./main.py /code/main.py

# Expose the port
EXPOSE 8501

# Run the container
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
