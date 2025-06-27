import streamlit as st
from pdf_parser.extract_text import extract_text_from_pdf
from modules.summarizer import generate_summary
from modules.qa_bot import ask_question
from modules.verifier import verify_explanation
from modules.claim_simulator import simulate_claim
from modules.exclusion_detector import detect_exclusions
from modules.utils import is_valid_policy_text

st.set_page_config(page_title="PolicyBuddy+", page_icon="🤝", layout="centered")

st.markdown("""
    <style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .main-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
        color: #0A4D68;
    }
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🤝 PolicyBuddy+<br><span style='font-size: 1.2rem;'>Your GenAI Insurance Assistant</span></div>", unsafe_allow_html=True)

# Initialize session state for uploaded file
if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None

with st.expander("📥 Upload your Insurance Policy (PDF)", expanded=True):
    uploaded_file = st.file_uploader("Choose a policy file", type="pdf")
    if uploaded_file is not None:
        st.session_state.uploaded_file = uploaded_file

    # Try a sample demo file
    with open("data/sample_policy.pdf", "rb") as f:
        st.download_button("📄 Try a demo policy file", data=f, file_name="sample_policy.pdf", mime="application/pdf")

    # Clear uploaded file
    if st.button("🔄 Clear uploaded policy"):
        st.session_state.uploaded_file = None
        st.experimental_rerun()

    policy_text = ""
    if st.session_state.uploaded_file:
        policy_text = extract_text_from_pdf(st.session_state.uploaded_file)
        if not is_valid_policy_text(policy_text):
            st.warning("⚠️ This PDF does not look like an insurance policy. Please check the file.")
        else:
            st.success("✅ Policy document uploaded and parsed!")

# Tabs
tabs = st.tabs([
    "📄 Summary",
    "💬 Ask AI",
    "🔎 Verify Agent Claim",
    "🤪 Claim Simulator",
    "❌ Exclusion Detector"
])

# Tab 1: Summary
with tabs[0]:
    st.subheader("📃 Generate a Policy Summary")
    if st.button("🦾 Generate Summary"):
        if policy_text:
            with st.spinner("Generating summary..."):
                summary = generate_summary(policy_text)
                st.info(summary)
                st.caption("⚠️ This summary is AI-generated. Verify with your insurer.")
                if st.radio("Was this helpful?", ("👍 Yes", "👎 No"), horizontal=True):
                    st.write("✅ Thank you for your feedback!")
        else:
            st.warning("Please upload a policy PDF first.")

# Tab 2: Ask AI
with tabs[1]:
    st.subheader("🤖 Ask a Question About Your Policy")
    question = st.text_input("What would you like to know?")
    if st.button("💡 Get Answer"):
        if question and policy_text:
            with st.spinner("Thinking..."):
                answer = ask_question(policy_text, question)
                st.success(answer)
                st.caption("⚠️ AI-generated. Please cross-check with your provider.")
                if st.radio("Was this helpful?", ("👍 Yes", "👎 No"), horizontal=True):
                    st.write("✅ Thank you for your feedback!")
        else:
            st.warning("Upload the policy and enter your question.")

# Tab 3: Verify Agent Claim
with tabs[2]:
    st.subheader("🔍 Agent Explanation Verifier")
    agent_text = st.text_area("Paste what the agent told you about the policy")
    if st.button("🚨 Verify Explanation"):
        if agent_text and policy_text:
            with st.spinner("Verifying explanation..."):
                result = verify_explanation(policy_text, agent_text)
                st.warning(result)
                st.caption("⚠️ Cross-check with the insurer before decisions.")
                if st.radio("Was this helpful?", ("👍 Yes", "👎 No"), horizontal=True):
                    st.write("✅ Thank you for your feedback!")
        else:
            st.warning("Please upload the policy and agent explanation.")

# Tab 4: Claim Simulator
with tabs[3]:
    st.subheader("🤪 Claim Scenario Simulator")
    scenario = st.text_area("Describe your situation (e.g., dengue hospitalization)")
    if st.button("📊 Evaluate Claim"):
        if scenario and policy_text:
            with st.spinner("Analyzing your claim..."):
                result = simulate_claim(policy_text, scenario)
                st.info(result)
                st.caption("⚠️ This is AI-generated, please verify officially.")
                if st.radio("Was this helpful?", ("👍 Yes", "👎 No"), horizontal=True):
                    st.write("✅ Thank you for your feedback!")
        else:
            st.warning("Upload a policy and describe your scenario.")

# Tab 5: Exclusion Detector
with tabs[4]:
    st.subheader("❌ Exclusion Detector")
    if st.button("🔍 Analyze Exclusions"):
        if policy_text:
            with st.spinner("Scanning for exclusions..."):
                result = detect_exclusions(policy_text)
                st.warning(result)
                if st.radio("Was this helpful?", ("👍 Yes", "👎 No"), horizontal=True):
                    st.write("✅ Thank you for your feedback!")
        else:
            st.warning("Please upload a policy first.")

# Footer
st.markdown("""
---
📁 View on [GitHub](https://github.com/your-username/policybuddy) | © 2025 PolicyBuddy+ 
_Disclaimer: All responses are AI-generated. Verify with your insurer before making decisions._
""")
