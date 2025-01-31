from fastapi import FastAPI, HTTPException
from github_api import fetch_pr_files, post_github_comment
from ai_analysis import analyze_code_with_openai

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "OK"}

@app.post("/analyze_pr")
def analyze_pr(repo: str, pr_number: int):
    """
    Fetches PR details, analyzes the code using OpenAI, and comments on GitHub.
    """
    files = fetch_pr_files(repo, pr_number)
    comments = []
    for file in files:
        ai_feedback = analyze_code_with_openai(file['raw_url'])
        if ai_feedback:
            comments.append({
                "path": file['filename'],
                "position": 1,  # Change as needed
                "body": ai_feedback
            })
    
    for comment in comments:
        post_github_comment(repo, pr_number, comment)
    
    return {"status": "comments added"}
