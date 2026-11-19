import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
db = sqlite3.connect(":memory:", check_same_thread=False)
db.execute("CREATE TABLE users (id INTEGER, name TEXT)")
db.execute("INSERT INTO users VALUES (1, 'alice'), (2, 'bob')")


@app.after_request
def security_headers(resp):
    resp.headers["Content-Security-Policy"] = "default-src 'self'"
    resp.headers["X-Content-Type-Options"] = "nosniff"
    resp.headers["X-Frame-Options"] = "DENY"
    return resp


@app.get("/user")
def user():
    name = request.args.get("name", "")
    # UNSAFE (Semgrep will flag): db.execute(f"SELECT * FROM users WHERE name = '{name}'")
    rows = db.execute("SELECT * FROM users WHERE name = ?", (name,)).fetchall()
    return jsonify(rows)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
