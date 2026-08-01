# pyrefly: ignore [missing-import]
import streamlit as st

from agents.research_agent import ResearchAgent

st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🤖",
    layout="wide"
)

# ----------------------------
# Session State
# ----------------------------

if "agent" not in st.session_state:
    st.session_state.agent = ResearchAgent()

if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------------------
# Sidebar
# ----------------------------

with st.sidebar:

    st.title("🔍 AI Research Agent")

    st.markdown("""
This application demonstrates an **AI Research Agent**


The agent performs:

- Multi-step reasoning
- Tool calling
- Web search
- Session memory
""")

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []
        st.session_state.agent = ResearchAgent()

        st.rerun()

# ----------------------------
# Main Page
# ----------------------------

st.title("🤖 AI Research Agent")

st.write(
    "Ask any research question."
)

# ----------------------------
# Display Chat History
# ----------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# ----------------------------
# Chat Input
# ----------------------------

question = st.chat_input(
    "Ask a research question..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Researching..."):

            answer = st.session_state.agent.ask(question)

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )