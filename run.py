#!/usr/bin/env python3
"""
CascadeGuard AI Runner
Starts the FastAPI backend and serves the interactive live dashboard.
"""
import uvicorn
import webbrowser
import sys
import time
import threading

def open_browser():
    time.sleep(1.2)
    webbrowser.open("http://127.0.0.1:8000")

if __name__ == "__main__":
    print("=" * 70)
    print("  CASCADEGUARD AI -- SRE FAILURE PREDICTION & RECOVERY RUNTIME")
    print("=" * 70)
    print("  Starting dashboard at: http://127.0.0.1:8000")
    print("  Press Ctrl+C to stop.")
    print("=" * 70)

    # Launch browser automatically if requested or standard
    if "--no-browser" not in sys.argv:
        threading.Thread(target=open_browser, daemon=True).start()

    uvicorn.run("backend.app.main:app", host="127.0.0.1", port=8000, reload=False)
