import streamlit as st
from app.ui import display_ui
from models.jurors import run_juror_models
from models.judge_judy import judge_decision
from config.loaders import load_models, load_settings
from models.tracker import track_metrics
from models.logging import save_verdict

def main():
    st.set_page_config(page_title="TheJudge", layout="centered")
    st.title("⚖️ TheJudge")
    st.markdown("Choose your jurors, let Judge J.U.D.Y. deliver the verdict.")

    settings = load_settings()
    models = load_models()
    selected_models = st.multiselect("Choose your jurors", options=[m['name'] for m in models], default=[m['name'] for m in models[:4]])
    question = st.text_area("Enter your prompt/question")
    manual = st.toggle("Take the Gavel (Manual Mode)")

    if st.button("Submit"):
        with st.spinner("Deliberating..."):
            juror_responses = run_juror_models(question, selected_models)
            if manual:
                display_ui.manual_mode(juror_responses)
                save_verdict(question, juror_responses, winner="Manual", mode="manual")
            else:
                verdict = judge_decision(question, juror_responses)
                display_ui.judy_mode(verdict)
                save_verdict(question, juror_responses, verdict['winner'], verdict['reason'])
                track_metrics(verdict['winner'])

if __name__ == "__main__":
    main()
