# Class 1 Setup Instructions: Windows

Complete this guide **before** the live class.
Using a Mac? Go to the [macOS setup guide](class-1-setup-mac.md).

**Time needed:** 30 to 45 minutes

**Checklist**

- [ ] 1. Create a GitHub account
- [ ] 2. Install Python
- [ ] 3. Install VS Code
- [ ] 4. Install GitHub Desktop
- [ ] 5. Get the course repository
- [ ] 6. Open it in VS Code and verify your setup

If you get stuck, jump to [Troubleshooting](#troubleshooting).

---

## 1. Create a GitHub account

1. Go to <https://github.com/signup>.
2. Sign up with your email, choose a username and verify your email.
3. Remember your username and password. You will need them in step 4.

---

## 2. Install Python

1. Go to <https://www.python.org/downloads/> and click **Download Python 3.x**.
2. Open the downloaded `.exe` file.
3. **Important:** on the first screen, tick **"Add python.exe to PATH"** *before* clicking **Install Now**.
4. When the install finishes, click **Close**.
5. Open **Command Prompt** (press the Windows key, type `cmd`, press Enter).
6. Check the install:
   ```
   python --version
   ```
   You should see something like `Python 3.12.x`.

> If you see "Python was not found" or the Microsoft Store opens, see [Troubleshooting](#troubleshooting).

---

## 3. Install VS Code

VS Code is the editor where you will write code.

1. Go to <https://code.visualstudio.com/> and download the Windows version.
2. Run the installer. Tick **"Add to PATH"** and **"Add 'Open with Code' action"** if offered.
3. Open VS Code.
4. Install the Python extension:
   - Click the **Extensions** icon in the left sidebar (four squares), or press `Ctrl+Shift+X`.
   - Search for **Python** and install the one published by **Microsoft**.

---

## 4. Install GitHub Desktop

GitHub Desktop lets you download and upload code without typing Git commands.

1. Go to <https://desktop.github.com/> and download the Windows version.
2. Run the installer. It opens GitHub Desktop automatically when done.
3. Click **Sign in to GitHub.com**. Log in with the account from step 1 and authorize the app.
4. When asked to configure Git, keep the name and email it suggests.

---

## 5. Get the course repository

You will make your **own copy** (a *fork*) of the course repo. Your work goes into your copy, and you can pull updates from the original.

1. Open the course repository in your browser: `[ADD COURSE REPO URL HERE]`
2. Click **Fork** (top right), then **Create fork**.
3. Open **GitHub Desktop**.
4. Go to **File → Clone repository…**
5. On the **GitHub.com** tab, select **your fork** from the list.
6. Choose where to save it (for example, `Documents\course`). Remember this location.
7. Click **Clone**.
8. When asked *"How are you planning to use this fork?"*, choose **"To contribute to the parent project"**.

---

## 6. Open it in VS Code and verify your setup

1. In GitHub Desktop, click **Open in Visual Studio Code** (or press `Ctrl+Shift+A`).
   If you don't see this button, in VS Code use **File → Open Folder…** and select the cloned folder.
2. If VS Code asks *"Do you trust the authors of this folder?"*, click **Yes, I trust the authors**.
3. Open the built-in terminal: **Terminal → New Terminal** (or `` Ctrl+` ``).
4. Run the check script:
   ```
   python check_setup.py
   ```
5. You should see:
   ```
   Python version: 3.x.x
   Setup complete! You are ready for Class 1.
   ```

**Send a screenshot of this output to the course group** so we know you are ready.

---

## Troubleshooting

### "Python was not found" or the Microsoft Store opens
- You probably missed the **Add python.exe to PATH** checkbox. Re-run the Python installer, choose **Modify**, then **Next**, and tick **Add Python to environment variables**. Or uninstall and reinstall with the box ticked.
- Close and reopen the terminal afterwards.
- You can also try `py --version` or `py check_setup.py`.

### `python` works in Command Prompt but not in VS Code
- Close VS Code completely and reopen it. The terminal only picks up PATH changes after a restart.

### GitHub Desktop doesn't show my fork
- Make sure you completed the fork in step 5.2 and are signed in to the same account.
- In the clone window, click the refresh icon next to the repository list.

### VS Code doesn't show the Python version / "Select Interpreter"
- Press `Ctrl+Shift+P`, type **Python: Select Interpreter**, and pick the Python 3 version you installed.

### Still stuck?
Post in the course group with:
1. Your Windows version (10 or 11)
2. Which step you are on
3. The **full** error message or a screenshot

---

Setup done? See you in Class 1.
