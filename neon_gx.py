
import os
import subprocess
import sys
from pathlib import Path

APP_NAME = "Neon GX"

def find_firefox():
    if sys.platform == "win32":
        candidates = [
            Path(os.environ.get("PROGRAMFILES", "C:/Program Files"))
            / "Mozilla Firefox" / "firefox.exe",
            Path(os.environ.get("PROGRAMFILES(X86)", "C:/Program Files (x86)"))
            / "Mozilla Firefox" / "firefox.exe",
            Path(os.environ.get("LOCALAPPDATA", ""))
            / "Mozilla Firefox" / "firefox.exe",
        ]
    elif sys.platform == "darwin":
        candidates = [
            Path("/Applications/Firefox.app/Contents/MacOS/firefox")
        ]
    else:
        candidates = [
            Path("/usr/bin/firefox"),
            Path("/usr/bin/firefox-esr"),
        ]

    for path in candidates:
        if path.is_file():
            return str(path)

    import shutil
    return shutil.which("firefox") or shutil.which("firefox-esr")


def main():
    firefox = find_firefox()

    if not firefox:
        print("Firefox is not installed or could not be located.")
        input("Press Enter to exit...")
        return

    # Keep the custom start page beside this script.
    homepage = Path(__file__).resolve().parent / "neon_gx_start.html"

    if not homepage.exists():
        print(f"Start page not found: {homepage}")
        input("Press Enter to exit...")
        return

    subprocess.Popen([
        firefox,
        "--new-window",
        homepage.resolve().as_uri()
    ])


if __name__ == "__main__":
    main()
