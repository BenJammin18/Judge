import streamlit as st

class display_ui:
    @staticmethod
    def manual_mode(responses):
        st.subheader("Manual Mode: Review Juror Responses")
        for model, response in responses.items():
            st.markdown(f"**{model}**: {response}")

    @staticmethod
    def judy_mode(verdict):
        st.subheader("Judge J.U.D.Y.'s Verdict")
        st.success(f"**{verdict['winner']}** wins the argument.")
        st.caption(f"Reason: {verdict['reason']}")
