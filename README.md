# 🤝 PolicyBuddy+

An AI-powered assistant for insurance policyholders that helps demystify policy documents, verify agent claims, simulate claim scenarios, and detect potential exclusions. Powered by Mistral-7B via OpenRouter, Streamlit for UI, and PDF parsing with PyPDF2.

🔗 Live Demo: [Click to Try PolicyBuddy+](https://policybuddy-cxne44tuvzb4g6fkvwpb8w.streamlit.app/)
🔗 Video Demo: [Click to Open Demo Video](https://drive.google.com/file/d/11EK5IRJo0T3GpR-357F1d95AiwszkRDE/view)
---

## 📌 Problem Statement

Insurance policies are often complex and difficult for the average customer to understand. Many users rely on agents for interpretations, which can sometimes lead to misinformation, missed exclusions, or denied claims.

---

## 🎯 Key Features

✅ Upload & analyze any insurance policy in PDF format  
✅ AI-generated simplified summary in 6 points  
✅ Ask any question and get contextual answers from your policy  
✅ Verify if an agent’s explanation is misleading or incomplete  
✅ Simulate whether a user-described claim is likely to be accepted or rejected  
✅ Exclusion detector that flags risky terms or hidden limitations  

---

## 🧠 Tech Stack

- 🧠 GenAI Model: Mistral-7B (via OpenRouter API)
- 🖼️ UI: Streamlit
- 📄 PDF Parsing: PyPDF2
- 🌐 Backend: Python
- 🗃️ Deployment: Streamlit Community Cloud

---

## ⚙️ How to Run Locally

1. Clone this repository:
git clone https://github.com/MohitKanyal/policybuddy.git
cd policybuddy
2. Clone this repository:
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Create a .env file and add your OpenRouter key:
OPENROUTER_API_KEY=youropenrouterkey
5. Run the App
streamlit run app.py
