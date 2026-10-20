
import os
import sys
import shutil
import subprocess
from pathlib import Path
import tkinter as tk
from tkinter import messagebox


def resource_path(filename):
    """Find a bundled resource in development or a PyInstaller build."""
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
    return base / filename


def find_firefox():
    # Check the Windows PATH first.
    found = shutil.which("firefox") or shutil.which("firefox.exe")
    if found:
        return found

    # Common Windows installation locations.
    candidates = [
        Path(os.environ.get("PROGRAMFILES", r"C:\Program Files"))
        / "Mozilla Firefox" / "firefox.exe",
        Path(os.environ.get("PROGRAMFILES(X86)", r"C:\Program Files (x86)"))
        / "Mozilla Firefox" / "firefox.exe",
        Path(os.environ.get("LOCALAPPDATA", ""))
        / "Mozilla Firefox" / "firefox.exe",
    ]

    for candidate in candidates:
        if candidate.is_file():
            return str(candidate)

    return None


def main():
    homepage = resource_path("neon_gx_start.html")

    if not homepage.is_file():
        messagebox.showerror(
            "Neon GX",
            "The Neon GX start page could not be found."
        )
        return

    firefox = find_firefox()

    if not firefox:
        messagebox.showerror(
            "Neon GX - Firefox Required",
            "Mozilla Firefox was not found.\n\n"
            "Install Firefox from https://www.mozilla.org/firefox/ "
            "and then reopen Neon GX."
        )
        return

    try:
        subprocess.Popen([
            firefox,
            "--new-window",
            homepage.resolve().as_uri()
        ])
    except OSError as error:
        messagebox.showerror(
            "Neon GX",
            f"Firefox could not be started:\n{error}"
        )


if __name__ == "__main__":
    main()
