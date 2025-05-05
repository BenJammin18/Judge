FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install streamlit pyyaml
CMD ["streamlit", "run", "app/main.py"]
