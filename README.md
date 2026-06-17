linux-audit-dashboard/
│
├── app.py
├── collect.yml
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── server_detail.html
│   └── history.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       ├── dashboard.js
│       └── search.js
│
├── vault-keys/
│   └── ec2-key.pem
│
├── data/
│   ├── reports/
│   │   ├── latest_report.csv
│   │   └── scan_*.csv
│   │
│   └── inventory/
│       └── ansible_hosts
│
└── logs/
    └── audit.log 

ssh admin@10.68.2.135
