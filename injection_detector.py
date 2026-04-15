import re
from config import INJECTION_PATTERNS

def detect_injection(text):
    text = text.lower()
    score = 0

    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, text):
            score += 1

    # Normalize score
    return score / len(INJECTION_PATTERNS)
