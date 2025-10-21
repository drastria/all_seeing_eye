All Seeing Eye is a sophisticated Python-based surveillance tool, engineered to scan designated global zones, acquire target endpoints from unsecured camera feeds, and establish direct visual access for real-time monitoring across the globe

## Legal disclaimer:
Usage of All Seeing Eye for accessing restricted or private feeds without authorization is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

![All Seeing Eye](https://github.com/user-attachments/assets/14420f44-ca46-441b-bc06-61b4f62ceac4)

### Features
- Dynamic Zone Scanning : Scans and enumerates target zones (countries)
- Headless Target Acquisition : Utilizes a headless Chromium instance to acquire feed data undetected
- Isolated Viewport Interface : Launches a sandboxed, UI-less render window for direct feed monitoring
- SSL/TLS Override Protocol : Bypasses invalid certificate warnings to establish connections with misconfigured `HTTP` endpoints
- Core Component Verification : Verifies all required components are present at runtime

### Usage:
```
git clone https://github.com/drastria/all_seeing_eye
cd all_seeing_eye
python all_seeing.py
```

### Install requirements (selenium and webdriver-manager):

```
cd all_seeing_eye
pip install -r requirements.txt
```

### How it works?

The script initializes a headless Selenium instance to perform data acquisition from a protected API endpoint. Once a target vector is selected, it injects a secondary, sandboxed instance of the Chromium engine

Using --app and --ignore-certificate-errors flags, it establishes a direct, low-level connection to the target's stream, bypassing standard browser security protocols to render the feed

### Donate!
Support the authors:

[![Donate using Trakteer](https://new.trakteer.id/_assets/v11/f005987b6b7970f1696c6a8e2306d192f63a03ae.png)](https://trakteer.id/drastria/gift)
