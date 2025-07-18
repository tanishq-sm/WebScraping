# WebScraping

This project automates data downloading from the India WRIS website using Selenium WebDriver integrated with a custom Brave browser user profile. It enables:

🔍 Automatic selection and deselection of stations via dropdown.

📥 Simulated button clicks to trigger data and metadata downloads.

⏳ Waits and delays for dynamic content handling.

🖱️ Uses pyautogui to handle native OS dialogs (like Save As windows) when needed.

🌐 Runs within a virtual environment for isolated package management.

The script uses a pre-signed-in Brave browser profile to maintain session state and avoid repeated logins. The setup also ensures compatibility with browser-based download behavior, where dialogs may appear only once per session.
