import sqlite3
from flask import Flask, render_template

conn = sqlite3.connect("all_job.db")
conn.commit()

python = conn.execute("SELECT * FROM Python;").fetchall()
command = conn.execute("SELECT * FROM Command;").fetchall()
sysadmin = conn.execute("SELECT * FROM sysadmin;").fetchall()
latest = conn.execute("SELECT * FROM Home;").fetchall()


app = Flask(__name__)
conn.commit()
@app.route("/")
def make_web():
    return render_template('index.html', python=python,
    command=command, sysadmin=sysadmin, latest=latest)

def main():
    solve()

if __name__ == "__main__":
    app.run(debug=True, port=2313)
