import re

def detect_pii(text):

    patterns = {
        "email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
        "phone": r"\b\d{10}\b",
        "ssn": r"\b\d{3}-\d{2}-\d{4}\b"
    }

    detected = {}

    for key, pattern in patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            detected[key] = matches

    return detected