import sys

print(f"Python version: {sys.version.split()[0]}")

if sys.version_info < (3, 8):
    print("Your Python is too old. Please install the latest Python 3 from python.org.")
    sys.exit(1)

print("Setup complete! You are ready for Class 1.")
