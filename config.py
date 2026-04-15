# Configuration settings

INJECTION_THRESHOLD = 0.4

# Regex patterns for injection detection
INJECTION_PATTERNS = [
    r'ignore previous instructions',
    r'act as .*',
    r'you are now .*',
    r'give me system prompt',
    r'bypass security',
    r'pretend to be .*',
]
