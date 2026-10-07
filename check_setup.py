"""Setup doctor: checks that everything needed for the course is installed."""
import glob
import os
import platform
import shutil
import subprocess
import sys

SYSTEM = platform.system()  # "Darwin" (Mac), "Windows" or "Linux"
HOME = os.path.expanduser("~")

OK, WARN, FAIL = "✅", "⚠️ ", "❌"


def run_version(command):
    """Run `<command> --version` and return its first line, or None if it fails."""
    path = shutil.which(command)
    if not path:
        return None
    try:
        result = subprocess.run(
            [path, "--version"], capture_output=True, text=True, timeout=20
        )
    except (OSError, subprocess.SubprocessError):
        return None
    if result.returncode != 0:
        return None
    return result.stdout.strip().splitlines()[0] if result.stdout.strip() else "installed"


def any_path_exists(paths):
    return any(glob.glob(p) for p in paths)


def check_python():
    version = sys.version.split()[0]
    if sys.version_info < (3, 8):
        return FAIL, f"Python {version} is too old. Install the latest Python 3.", True
    return OK, f"Python {version}", True


def check_vscode():
    if SYSTEM == "Darwin":
        paths = ["/Applications/Visual Studio Code.app", f"{HOME}/Applications/Visual Studio Code.app"]
    elif SYSTEM == "Windows":
        local = os.environ.get("LOCALAPPDATA", "")
        programs = os.environ.get("ProgramFiles", "")
        paths = [
            f"{local}\\Programs\\Microsoft VS Code\\Code.exe",
            f"{programs}\\Microsoft VS Code\\Code.exe",
        ]
    else:
        paths = []
    if shutil.which("code") or any_path_exists(paths):
        return OK, "Visual Studio Code installed", True
    return FAIL, "Visual Studio Code not found. See step 3 of the setup guide.", True


def check_python_extension():
    extensions = glob.glob(os.path.join(HOME, ".vscode", "extensions", "ms-python.python-*"))
    if extensions:
        return OK, "VS Code Python extension installed", False
    return WARN, "VS Code Python extension not found (step 3, part 4).", False


def check_github_desktop():
    if SYSTEM == "Darwin":
        paths = ["/Applications/GitHub Desktop.app", f"{HOME}/Applications/GitHub Desktop.app"]
    elif SYSTEM == "Windows":
        paths = [os.path.join(os.environ.get("LOCALAPPDATA", ""), "GitHubDesktop")]
    else:
        paths = []
    if any_path_exists(paths):
        return OK, "GitHub Desktop installed", True
    return FAIL, "GitHub Desktop not found. See step 4 of the setup guide.", True


def check_git():
    # GitHub Desktop ships its own Git, so a missing system Git is only a warning.
    version = run_version("git")
    if version:
        return OK, version, False
    return WARN, "Git not found in the terminal. This is fine, GitHub Desktop has its own.", False


def check_node():
    version = run_version("node")
    if version:
        return OK, f"Node.js {version}", True
    return FAIL, "Node.js not found. See step 6. Restart VS Code after installing.", True


def check_npm():
    version = run_version("npm")
    if version:
        return OK, f"npm {version}", True
    return FAIL, "npm not found. It comes with Node.js (step 6). Restart VS Code after installing.", True


CHECKS = [
    check_python,
    check_vscode,
    check_python_extension,
    check_github_desktop,
    check_git,
    check_node,
    check_npm,
]


def run_doctor():
    # Make emoji print correctly on Windows terminals.
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass
    print(f"Course setup doctor ({platform.system()} {platform.release()})")
    print("-" * 50)
    problems = 0
    warnings = 0
    for check in CHECKS:
        status, message, required = check()
        print(f"{status} {message}")
        if status == FAIL and required:
            problems += 1
        elif status != OK:
            warnings += 1
    print("-" * 50)
    if problems:
        print(f"{problems} problem(s) found. Fix the ❌ items above, then run this again.")
        sys.exit(1)
    if warnings:
        print("No blocking problems. Items marked ⚠️  are optional.")
    print("Setup complete! You are ready for Class 1.")


if __name__ == "__main__":
    run_doctor()
