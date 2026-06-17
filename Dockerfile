FROM python:3.11-slim

# Install Ansible dependencies
RUN apt-get update && apt-get install -y \
    openssh-client \
    sshpass \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create required directories
RUN mkdir -p data/reports data/inventory vault-keys logs

EXPOSE 5000

CMD ["python", "app.py"]
