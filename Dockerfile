# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and text file into the container
COPY prog.py unfiltered.txt /app/

# Install any dependencies required by the Python script
RUN pip install nltk  # Install NLTK if necessary
RUN python -m nltk.downloader stopwords

# Run the Python script when the container launches
CMD ["python", "prog.py"]
