from flask import Flask, request, render_template_string
import time

from injection_detector import detect_injection
from presidio_module import analyze_pii, anonymize_pii
from policy_engine import decide_policy

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>LLM Security Gateway</title>
</head>
<body style="font-family: Arial; padding: 40px;">
    <h2>🔐 LLM Security Gateway</h2>
    
    <form method="POST">
        <textarea name="input_text" rows="5" cols="60" placeholder="Enter text here..."></textarea><br><br>
        <button type="submit">Analyze</button>
    </form>

    {% if result %}
        <h3>Result:</h3>
        <p><b>Decision:</b> {{ result.decision }}</p>
        <p><b>Output:</b> {{ result.output }}</p>
        <p><b>Injection Score:</b> {{ result.score }}</p>
        <p><b>Latency:</b> {{ result.latency }} seconds</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        user_input = request.form.get("input_text")

        start = time.time()

        # Step 1: Injection Detection
        injection_score = detect_injection(user_input)

        # Step 2: PII Detection
        pii_results = analyze_pii(user_input)

        # Step 3: Policy Decision
        decision = decide_policy(injection_score, pii_results)

        # Step 4: Output Handling
        if decision == "BLOCK":
            output = "Request blocked due to security risk."
        elif decision == "MASK":
            output = anonymize_pii(user_input, pii_results)
        else:
            output = user_input

        latency = round(time.time() - start, 4)

        result = {
            "decision": decision,
            "output": output,
            "score": round(injection_score, 2),
            "latency": latency
        }

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)
