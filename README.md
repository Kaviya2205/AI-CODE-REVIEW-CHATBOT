# AI-Powered Code Review Bot

An automated PR review system using FastAPI, OpenAI, and GitHub Actions.

## Setup
1. Clone the repo
2. Set `GITHUB_TOKEN` and `OPENAI_API_KEY` in `.env` or GitHub Secrets
3. Run `uvicorn main:app --reload`
4. Trigger PR analysis via GitHub Actions

## Features
- Automated PR comments
- AI-based code analysis
- GitHub Actions integration
