# Class 1 Setup Instructions: Windows

Complete this guide **before** the live class.
Using a Mac? Go to the [macOS setup guide](class-1-setup-mac.md).

**Time needed:** 35 to 50 minutes

**Checklist**

- [ ] 1. Create a GitHub account
- [ ] 2. Install Python
- [ ] 3. Install VS Code
- [ ] 4. Install GitHub Desktop
- [ ] 5. Get the course repository
- [ ] 6. Install Node.js and npm
- [ ] 7. Open it in VS Code and verify your setup

If you get stuck, jump to [Troubleshooting](#troubleshooting).
Steps 1 to 6 have a short video. Watch it first, then follow the written steps.

---

## 1. Create a GitHub account

🎥 **Watch this step (click the picture to play):**

<p align="center">
  <a href="https://www.youtube.com/watch?v=RnWDKWmaQ8s"><img src="https://img.youtube.com/vi/RnWDKWmaQ8s/hqdefault.jpg" alt="Step 1 video" width="480"></a>
</p>

1. Go to <https://github.com/signup>.
2. Sign up with your email, choose a username and verify your email.
3. Remember your username and password. You will need them in step 4.

---

## 2. Install Python

🎥 **Watch this step (click the picture to play):**

<p align="center">
  <a href="https://www.youtube.com/watch?v=lv5Vz80PG2w"><img src="https://img.youtube.com/vi/lv5Vz80PG2w/hqdefault.jpg" alt="Step 2 video" width="480"></a>
</p>

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

🎥 **Watch this step (click the picture to play):**

<p align="center">
  <a href="https://www.youtube.com/watch?v=TFF8B8AXkZY"><img src="https://img.youtube.com/vi/TFF8B8AXkZY/hqdefault.jpg" alt="Step 3 video" width="480"></a>
</p>

VS Code is the editor where you will write code.

1. Go to <https://code.visualstudio.com/> and download the Windows version.
2. Run the installer. Tick **"Add to PATH"** and **"Add 'Open with Code' action"** if offered.
3. Open VS Code.
4. Install the Python extension:
   - Click the **Extensions** icon in the left sidebar (four squares), or press `Ctrl+Shift+X`.
   - Search for **Python** and install the one published by **Microsoft**.

---

## 4. Install GitHub Desktop

🎥 **Watch this step (click the picture to play):**

<p align="center">
  <a href="https://www.youtube.com/watch?v=bk0WhIl7uFU"><img src="https://img.youtube.com/vi/bk0WhIl7uFU/hqdefault.jpg" alt="Step 4 video" width="480"></a>
</p>

GitHub Desktop lets you download and upload code without typing Git commands.

1. Go to <https://desktop.github.com/> and download the Windows version.
2. Run the installer. It opens GitHub Desktop automatically when done.
3. Click **Sign in to GitHub.com**. Log in with the account from step 1 and authorize the app.
4. When asked to configure Git, keep the name and email it suggests.

---

## 5. Get the course repository

🎥 **Watch this step (click the picture to play):**

<p align="center">
  <a href="https://www.youtube.com/watch?v=hL9fCjjwthE"><img src="https://img.youtube.com/vi/hL9fCjjwthE/hqdefault.jpg" alt="Step 5 video" width="480"></a>
</p>

You will make your **own copy** (a *fork*) of the course repo. Your work goes into your copy, and you can pull updates from the original.

1. Open the course repository in your browser: <https://github.com/ccunnect-tech/BFA>
2. Click **Fork** (top right), then **Create fork**.
3. Open **GitHub Desktop**.
4. Go to **File → Clone repository…**
5. On the **GitHub.com** tab, select **your fork** from the list.
6. Choose where to save it (for example, `Documents\course`). Remember this location.
7. Click **Clone**.
8. When asked *"How are you planning to use this fork?"*, choose **"To contribute to the parent project"**.

---

## 6. Install Node.js and npm

🎥 **Watch this step (click the picture to play):**

<p align="center">
  <a href="https://www.youtube.com/watch?v=Iqj8bUJweiU"><img src="https://img.youtube.com/vi/Iqj8bUJweiU/hqdefault.jpg" alt="Step 6 video" width="480"></a>
</p>

Node.js lets you run JavaScript on your computer. You will use it with React in later classes. `npm` is installed together with Node.js.

1. Go to <https://nodejs.org/> and click the **LTS** download button (not "Current").
2. Run the downloaded `.msi` file and follow the installer with the default options. Keep **Add to PATH** ticked.
3. **Close and reopen** VS Code and Command Prompt so they find the new install.
4. Check the install in Command Prompt:
   ```
   node --version
   npm --version
   ```
   Both should print a version number like `v22.x.x` and `10.x.x`.

---

## 7. Open it in VS Code and verify your setup

1. In GitHub Desktop, click **Open in Visual Studio Code** (or press `Ctrl+Shift+A`).
   If you don't see this button, in VS Code use **File → Open Folder…** and select the cloned folder.
2. If VS Code asks *"Do you trust the authors of this folder?"*, click **Yes, I trust the authors**.
3. Look at the **Explorer** panel on the left. You should see a file called `check_setup.py`. This is the file you will run.
4. Open the built-in terminal: **Terminal → New Terminal** (or `` Ctrl+` ``). A panel opens at the bottom of VS Code.
5. Type this command in the terminal and press **Enter**:
   ```
   python check_setup.py
   ```
6. You should see a checklist like this (version numbers will differ):
   ```
   Course setup doctor (...)
   --------------------------------------------------
   ✅ Python 3.x.x
   ✅ Visual Studio Code installed
   ✅ VS Code Python extension installed
   ✅ GitHub Desktop installed
   ✅ git version 2.x.x
   ✅ Node.js v22.x.x
   ✅ npm 10.x.x
   --------------------------------------------------
   Setup complete! You are ready for Class 1.
   ```
   A ✅ means good. A ⚠️ is optional (for example, Git in the terminal). Any ❌ line must be fixed, and the message tells you which step to redo.
7. If you see an error instead, check [Troubleshooting](#troubleshooting) and try again.

**Take a screenshot of this whole output and send it to the course group** so we know you are ready. All good after that.

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

### `node` or `npm` is "not recognized"
- Close VS Code and Command Prompt completely and open them again.
- If it still fails, re-run the Node.js installer and make sure **Add to PATH** is ticked.
### `npm` fails with "running scripts is disabled on this system"
- Open **PowerShell** and run `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`, then press `Y`. Reopen VS Code.

### VS Code doesn't show the Python version / "Select Interpreter"
- Press `Ctrl+Shift+P`, type **Python: Select Interpreter**, and pick the Python 3 version you installed.

### Still stuck?
Post in the course group with:
1. Your Windows version (10 or 11)
2. Which step you are on
3. The **full** error message or a screenshot

---

Setup done? See you in Class 1.
