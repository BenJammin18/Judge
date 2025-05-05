# TheJudge v1

Welcome to TheJudge — an AI courtroom where multiple LLMs (jurors) argue over your prompt, and Judge J.U.D.Y. delivers the verdict.

## Features
- Choose your jurors (2–10)
- Auto-judging with Judge J.U.D.Y.
- Manual override ("Take the Gavel")
- Retrial option if you disagree
- Thumbs up/down feedback for the judge
- FastAPI + Streamlit hybrid with API-only mode
- Helm chart + Docker support

See `roadmap.md` for what's coming next.

## Usage
```bash
make docker-local   # build for Docker Desktop
make dev            # run Streamlit locally
make deploy-eks     # deploy to EKS via Helm
```
