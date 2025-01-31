import requests
from config import OPENAI_API_KEY

def analyze_code_with_openai(code_url: str) -> str:
    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}"}
    file_content = requests.get(code_url).text
    data = {"model": "gpt-4", "prompt": f"Analyze this code:\n{file_content}", "max_tokens": 100}
    response = requests.post("https://api.openai.com/v1/completions", json=data, headers=headers)
    if response.status_code == 200:
        return response.json().get("choices", [{}])[0].get("text", "No feedback")
    return "Failed to analyze code"
