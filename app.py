from flask import Flask, jsonify

app = Flask(__name__)

channels = [
    {
        "id": 1,
        "name": "Canal A",
        "stream_url": "http://example.com/canal_a.m3u8"
    },
    {
        "id": 2,
        "name": "Canal B",
        "stream_url": "http://example.com/canal_b.m3u8"
    }
]

@app.route("/")
def home():
    return jsonify({"status": "online"})

@app.route("/channels")
def get_channels():
    return jsonify(channels)

@app.route("/play/<int:id>")
def play(id):
    for c in channels:
        if c["id"] == id:
            return jsonify(c)

    return jsonify({"erro": "Canal não encontrado"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
