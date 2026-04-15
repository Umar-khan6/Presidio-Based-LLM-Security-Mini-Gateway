from presidio_analyzer import AnalyzerEngine, PatternRecognizer, Pattern
from presidio_anonymizer import AnonymizerEngine

# Initialize engines
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

# -------------------------------
# Custom API Key Recognizer
# -------------------------------
api_pattern = Pattern(
    name="api_key_pattern",
    regex=r'api_[A-Za-z0-9]{16,}',
    score=0.8
)

api_recognizer = PatternRecognizer(
    supported_entity="API_KEY",
    patterns=[api_pattern]
)

analyzer.registry.add_recognizer(api_recognizer)

# -------------------------------
# Analyze PII
# -------------------------------
def analyze_pii(text):
    results = analyzer.analyze(text=text, language='en')
    return results

# -------------------------------
# Anonymize PII
# -------------------------------
def anonymize_pii(text, results):
    anonymized = anonymizer.anonymize(
        text=text,
        analyzer_results=results
    )
    return anonymized.text
