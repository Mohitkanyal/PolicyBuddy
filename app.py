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
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🤝 PolicyBuddy+<br><span style='font-size: 1.2rem;'>Your GenAI Insurance Assistant</span></div>", unsafe_allow_html=True)

with st.expander("📥 Upload your Insurance Policy (PDF)", expanded=True):
    uploaded_file = st.file_uploader("Choose a policy file", type="pdf")
    policy_text = ""
    if uploaded_file:
        policy_text = extract_text_from_pdf(uploaded_file)
    if not is_valid_policy_text(policy_text):
        st.warning("⚠️ This PDF does not look like an insurance policy. Please check the file.")
    else:
        st.success("✅ Policy document uploaded and parsed!")


tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📄 Summary",
    "💬 Ask AI",
    "🔎 Verify Agent Claim",
    "🧪 Claim Simulator",
    "🚫 Exclusion Detector"
])

with tab1:
    st.subheader("📃 Generate a Policy Summary")
    if st.button("🧾 Generate Summary"):
        if policy_text:
            with st.spinner("Generating summary..."):
                summary = generate_summary(policy_text)
                st.info(summary)
        else:
            st.warning("Please upload a policy PDF first.")

with tab2:
    st.subheader("🤖 Ask a Question About Your Policy")
    user_question = st.text_input("What would you like to know?")
    if st.button("💡 Get Answer"):
        if user_question and policy_text:
            with st.spinner("Getting answer..."):
                answer = ask_question(policy_text, user_question)
                st.success(answer)
        else:
            st.warning("Upload the policy and enter your question.")

with tab3:
    st.subheader("🔍 Agent Explanation Verifier")
    agent_text = st.text_area("Paste what the agent told you about the policy")
    if st.button("🚨 Verify Explanation"):
        if agent_text and policy_text:
            with st.spinner("Verifying..."):
                result = verify_explanation(policy_text, agent_text)
                st.warning(result)
        else:
            st.warning("Please upload the policy and enter the agent’s explanation.")

with tab4:
    st.subheader("🧪 Claim Scenario Simulator")
    scenario = st.text_area("Describe your situation (e.g., dengue hospitalization claim)", key="scenario_input")
    if st.button("📊 Evaluate Claim"):
        if scenario and policy_text:
            with st.spinner("Evaluating claim scenario..."):
                result = simulate_claim(policy_text, scenario)
                st.info(result)
        else:
            st.warning("Please upload a policy and enter a scenario.")

with tab5:
    st.subheader("🚫 Exclusion Detector")
    if st.button("🔍 Analyze Exclusions"):
        if policy_text:
            with st.spinner("Scanning for exclusions..."):
                result = detect_exclusions(policy_text)
                st.warning(result)
        else:
            st.warning("Please upload a policy first.")
