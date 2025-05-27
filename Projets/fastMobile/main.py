from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI()

LOG_FILE = "actions.log"

def log_action(action: str, angle: float = None):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    angle_str = f"{angle:.2f}" if angle is not None else ""
    with open(LOG_FILE, "a") as file:
        file.write(f"{now};{action};{angle_str};\n")

@app.post("/gauche")
def tourner_gauche(angle: float = Query(..., ge=3.0, le=10.0)):
    log_action("gauche", angle)
    return {"direction": "gauche", "angle": angle}

@app.post("/droite")
def tourner_droite(angle: float = Query(..., ge=3.0, le=10.0)):
    log_action("droite", angle)
    return {"direction": "droite", "angle": angle}

@app.post("/avant")
def aller_avant():
    log_action("avant")
    return {"action": "avant"}

@app.post("/arriere")
def aller_arriere():
    log_action("arriere")
    return {"action": "arriere"}

@app.get("/status", response_class=HTMLResponse)
def status():
    status_info = "En ligne"

    try:
        with open(LOG_FILE, "r") as f:
            logs = f.readlines()
    except FileNotFoundError:
        logs = []

    log_rows = ""
    for line in logs[::-1]:  # les plus récents en haut
        dt, action, angle, *_ = line.strip().split(";")
        angle_display = f"{angle}°" if angle else "-"
        log_rows += f"""
            <tr>
                <td>{dt}</td>
                <td>{action}</td>
                <td>{angle_display}</td>
            </tr>
        """

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Status du Robot</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f9f9f9;
                padding: 20px;
            }}
            h1 {{
                color: #333;
            }}
            .status {{
                font-size: 1.2em;
                margin-bottom: 20px;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                background: white;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }}
            th, td {{
                padding: 10px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }}
            th {{
                background-color: #4CAF50;
                color: white;
            }}
            tr:hover {{background-color: #f1f1f1;}}
        </style>
    </head>
    <body>
        <h1>Status du Robot</h1>
        <div class="status">🟢 Statut : <strong>{status_info}</strong></div>
        <h2>📋 Historique des actions</h2>
        <table>
            <tr>
                <th>Date / Heure</th>
                <th>Action</th>
                <th>Angle</th>
            </tr>
            {log_rows}
        </table>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)