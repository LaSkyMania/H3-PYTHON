from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime

start_time = datetime.now()

app = FastAPI()
@app.get("/date")
def read_date():
    now = datetime.now()
    return {"date": now.strftime("%Y-%m-%d")}

@app.get("/heure")
def read_heure():
    now = datetime.now()
    return {"heure": now.strftime("%H:%M:%S")}

@app.get("/status", response_class=HTMLResponse)
def read_status():
    now = datetime.now()
    return f"""
    <html>
        <head>
            <title>Service Status</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: #f0f2f5;
                    color: #333;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                    margin: 0;
                }}
                .container {{
                    background: white;
                    padding: 40px;
                    border-radius: 12px;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                    text-align: center;
                    max-width: 400px;
                }}
                h1 {{
                    margin-bottom: 24px;
                    color: #2c3e50;
                }}
                p {{
                    margin: 8px 0;
                    font-size: 1.1em;
                }}
                .footer {{
                    margin-top: 20px;
                    font-size: 0.9em;
                    color: #888;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 Service Status</h1>
                <p><strong>Launch Time:</strong><br>{start_time.strftime('%Y-%m-%d %H:%M:%S')}</p>
                <p><strong>Current Time:</strong><br>{now.strftime('%Y-%m-%d %H:%M:%S')}</p>
                <div class="footer">FastAPI Monitoring</div>
            </div>
        </body>
    </html>
    """