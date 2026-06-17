from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import csv
import subprocess
from datetime import datetime

app = Flask(**name**)

BASE_DIR = os.path.dirname(os.path.abspath(**file**))

REPORT_PATH = os.path.join(
BASE_DIR,
"data",
"reports",
"latest_report.csv"
)

INVENTORY_PATH = os.path.join(
BASE_DIR,
"data",
"inventory",
"ansible_hosts"
)

PLAYBOOK_PATH = os.path.join(
BASE_DIR,
"collect.yml"
)

PRIVATE_KEY = os.path.join(
BASE_DIR,
"vault-keys",
"ec2-key.pem"
)

def load_servers():
servers = []

```
if not os.path.exists(REPORT_PATH):
    return servers

with open(REPORT_PATH, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        servers.append(row)

return servers
```

@app.route("/")
def dashboard():

```
servers = load_servers()

total_servers = len(servers)

online_servers = len(
    [s for s in servers if s["Status"].lower() == "online"]
)

offline_servers = total_servers - online_servers

health_score = 0

if total_servers > 0:
    health_score = round(
        (online_servers / total_servers) * 100,
        2
    )

return render_template(
    "dashboard.html",
    servers=servers,
    total_servers=total_servers,
    online_servers=online_servers,
    offline_servers=offline_servers,
    health_score=health_score,
    last_scan=datetime.now().strftime("%d-%b-%Y %H:%M")
)
```

@app.route("/submit-ips", methods=["POST"])
def submit_ips():

```
ip_data = request.form.get("ip_list", "")

hosts = [
    ip.strip()
    for ip in ip_data.splitlines()
    if ip.strip()
]

if not hosts:
    return redirect(url_for("dashboard"))

with open(INVENTORY_PATH, "w") as file:

    file.write("[targets]\n")

    for host in hosts:
        file.write(f"{host}\n")

env = os.environ.copy()

env["ANSIBLE_HOST_KEY_CHECKING"] = "False"

subprocess.run(
    [
        "ansible-playbook",
        "-i",
        INVENTORY_PATH,
        "-u",
        "root",
        f"--private-key={PRIVATE_KEY}",
        PLAYBOOK_PATH
    ],
    env=env
)

return redirect(url_for("dashboard"))
```

@app.route("/server/<hostname>")
def server_detail(hostname):

```
servers = load_servers()

for server in servers:

    if server["Hostname"].lower() == hostname.lower():

        return render_template(
            "server_detail.html",
            server=server
        )

return "Server not found", 404
```

@app.route("/search")
def search_server():

```
search_term = request.args.get(
    "q",
    ""
).strip().lower()

servers = load_servers()

filtered = []

for server in servers:

    hostname = server["Hostname"].lower()

    if search_term in hostname:
        filtered.append(server)

return {
    "results": filtered
}
```

@app.route("/download")
def download_report():

```
if not os.path.exists(REPORT_PATH):
    return "No report available.", 404

return send_file(
    REPORT_PATH,
    as_attachment=True,
    download_name="linux_audit_report.csv"
)
```

if **name** == "**main**":
app.run(
host="0.0.0.0",
port=5000,
debug=True
)
