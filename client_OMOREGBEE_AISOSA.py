import tkinter as tk
import urllib.request
import json

SERVER_URL = "http://localhost:8000/welcome"

def send_name():
    name = entry.get().strip()
    if not name:
        output.config(text="Name required.")
        return

    data = json.dumps({"name": name}).encode("utf-8")
    req = urllib.request.Request(
        SERVER_URL,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(req) as resp:
            body = resp.read().decode("utf-8")
            parsed = json.loads(body)
            output.config(text=parsed.get("message"))
    except Exception as e:
        output.config(text=f"Error: {e}")

root = tk.Tk()
root.title("Distributed Systems Client")
root.geometry("500x300")  # width x height in pixels

tk.Label(root, text="Enter name:", font=("Arial", 14)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)

tk.Button(root, text="Send", font=("Arial", 12), command=send_name).pack(pady=10)

output = tk.Label(root, text="", font=("Arial", 12), wraplength=450, justify="center")
output.pack(pady=20)

root.mainloop()
