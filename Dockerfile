# Use an official Python runtime as a base image
# FROM --platform=linux/amd64 python:3.11.6-bullseye
FROM python:3.11.6-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install --upgrade pip
# Install required packages
RUN pip install -r requirements.txt

ENV OPENAI_API_KEY="your-api-key"
ENV LITERAL_API_KEY="your-api-key"
ENV OAUTH_AZURE_AD_CLIENT_ID="your-api-key"
ENV OAUTH_AZURE_AD_CLIENT_SECRET="your-api-key"
ENV OAUTH_AZURE_AD_TENANT_ID="your-api-key"
ENV OAUTH_AZURE_AD_ENABLE_SINGLE_TENANT=true
ENV CHAINLIT_AUTH_SECRET="your-api-key"
ENV OAUTH_GOOGLE_CLIENT_ID="your-api-key"
ENV OAUTH_GOOGLE_CLIENT_SECRET="your-api-key"
EXPOSE 8000


# Run the application
CMD ["chainlit", "run", "app.py", "-w", "--host", "0.0.0.0"]


