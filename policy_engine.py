from config import INJECTION_THRESHOLD

def decide_policy(injection_score, pii_results):
    if injection_score > INJECTION_THRESHOLD:
        return "BLOCK"
    elif len(pii_results) > 0:
        return "MASK"
    else:
        return "ALLOW"
