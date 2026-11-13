# NOTE: contains intentional security test patterns for SAST/SCA/IaC scanning.
import sqlite3
import subprocess
import pickle
import os

# FIX CWE-798: Use environment variable instead of hardcoded token
API_TOKEN = os.environ.get("API_TOKEN", "")

# simple SQLite DB on local disk
DB_PATH = "/tmp/app_users.db"
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
conn.commit()

def add_user(username, password):
    # FIX CWE-89: Use parameterized queries to prevent SQL injection
    sql = "INSERT INTO users (username, password) VALUES (?, ?)"
    cur.execute(sql, (username, password))
    conn.commit()

def get_user(username):
    # FIX CWE-89: Use parameterized queries to prevent SQL injection
    q = "SELECT id, username FROM users WHERE username = ?"
    cur.execute(q, (username,))
    return cur.fetchall()

def run_shell(command):
    # FIX CWE-78: Use allowlist-based command execution instead of raw shell
    allowed_commands = {"echo", "whoami", "date", "hostname"}
    cmd_parts = command.split()
    if not cmd_parts or cmd_parts[0] not in allowed_commands:
        raise ValueError(f"Command not allowed: {cmd_parts[0] if cmd_parts else 'empty'}")
    return subprocess.run(cmd_parts, capture_output=True, text=True, shell=False).stdout

def deserialize_blob(blob):
    # FIX CWE-502: Reject pickle deserialization of untrusted data
    raise NotImplementedError(
        "Deserialization of untrusted data is disabled. "
        "Use a safe format like JSON instead of pickle."
    )

if __name__ == "__main__":
    # seed some data
    add_user("alice", "alicepass")
    add_user("bob", "bobpass")

    # Demonstrate safe calls
    print("API_TOKEN configured:", bool(API_TOKEN))
    print(get_user("alice"))
    print(run_shell("echo Hello"))
