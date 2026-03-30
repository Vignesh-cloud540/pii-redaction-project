import re

def mask_pii(text):

    # Email
    text = re.sub(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", "[EMAIL]", text)

    # Phone
    text = re.sub(r"\b\d{10}\b", "[PHONE]", text)

    # Aadhaar
    text = re.sub(r"\b\d{12}\b", "[AADHAAR]", text)

    # Name (fixed)
    text = re.sub(r"(my name is|name is|my name is)\s+[A-Za-z]+", r"\1 [NAME]", text, flags=re.IGNORECASE)

    return text