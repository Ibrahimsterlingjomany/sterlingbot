from flask import Flask, render_template
import time, threading

app = Flask(__name__)
balance = 23794.62
total_sent = 0
logs = []

def simulate_transfers():
    global balance, total_sent, logs
    while True:
        if balance >= 500:
            balance -= 500
            total_sent += 500
            logs.insert(0, {
                "montant": "500 USDC",
                "heure": time.strftime("%H:%M:%S"),
                "to": "bc1qmxnh7wrddrfcjcmyx72cmgf88ykew74gl9v5tl"
            })
        time.sleep(5)

@app.route("/")
def dashboard():
    return f"""
    <h1>SterlingBot — Balance en temps réel</h1>
    <p><b>Solde détecté :</b> {balance} USDC</p>
    <p><b>Total envoyé :</b> {total_sent} USDC</p>
    <h3>Historique :</h3>
    <ul>
        {''.join([f"<li>{log['heure']} — {log['montant']} → {log['to']}</li>" for log in logs])}
    </ul>
    """

threading.Thread(target=simulate_transfers, daemon=True).start()

if __name__ == "__main__":
    app.run(debug=True, port=# Lance automatiquement les transferts dans un thread parallèle
threading.Thread(target=simulate_transfers, daemon=True).start()

# Route principale du bot pour voir si ça tourne
@app.route("/")
def index():
    return "SterlingBot actif et connecté au Wallet"

if __name__ == "__main__":
    app.run()
