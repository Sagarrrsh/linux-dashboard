FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y 
ansible 
openssh-client 
sshpass 
&& rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p 
/app/data/reports 
/app/data/inventory 
/app/logs 
/app/vault-keys

EXPOSE 5000

CMD ["python", "app.py"]
