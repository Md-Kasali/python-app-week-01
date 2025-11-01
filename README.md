# Simple Python Web Application

A minimal Flask web application that displays a static page.

## ⚠️ Troubleshooting Exercise

**This repository contains several Linux troubleshooting issues that you need to fix before the application will run!**

See `ISSUES.md` for details on the problems you need to solve.

## Setup

1. Create a virtual environment (recommended):
```bash
python3 -m venv venv
# Or:
python -m venv venv
```

2. Activate the virtual environment:
```bash
# On Linux/Mac:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
# Or on some Linux systems:
pip3 install -r requirements.txt
```

**Note**: After activating the virtual environment, your command prompt should show `(venv)` prefix, indicating the virtual environment is active. To deactivate later, simply run `deactivate`.

## Running the Application

Once you've fixed the issues, run the application with:
```bash
python app.py
# Or:
python3 app.py
```

Alternatively, you can use the shell script:
```bash
./run.sh
```

The application will start on `http://localhost:5000` (or `http://0.0.0.0:5000`).

Open your web browser and navigate to the URL above to see the static page.

