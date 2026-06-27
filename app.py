import streamlit as st
from utils.pdf_loader import extract_text_from_pdf
from utils.chunking import split_text_into_chunks
from utils.embeddings import (
    generate_embeddings,
    generate_query_embedding
)

from utils.vectorstore import (
    create_faiss_index,
    search_similar_chunks
)
from utils.rag import generate_answer

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="MediRAG",
    page_icon="🩺",
    layout="wide"
)

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.title("🩺 About MediRAG")

st.sidebar.info(
    """
MediRAG is an AI-powered Medical Report
Question Answering System that uses
Retrieval-Augmented Generation (RAG)
to provide accurate, context-aware
answers from uploaded medical reports.
"""
)

st.sidebar.success("✅ System Ready")

# ----------------------------
# Main Title
# ----------------------------
st.title("🩺 MediRAG")

st.subheader("AI-Powered Medical Report Question Answering System")

st.write(
    """
Upload your medical report in **PDF format**, ask questions in natural language,
and receive **context-aware AI-generated answers** using the
**Retrieval-Augmented Generation (RAG)** framework.
"""
)

st.divider()

# ----------------------------
# Upload Section
# ----------------------------
st.header("📂 Upload Medical Report")

uploaded_file = st.file_uploader(
    "Choose a PDF Medical Report",
    type=["pdf"]
)
question = ""

# ----------------------------
# PDF Text Extraction
# ----------------------------
tab1, tab2 = st.tabs(["🤖 AI Assistant", "📄 Processing Details"])

# -----------------------------
# AI Assistant Tab
# -----------------------------
with tab1:
    if uploaded_file is None:
        st.info("📄 Please upload a PDF medical report to begin.")
    else:

        if uploaded_file is not None:

            st.success(f"✅ Uploaded File: {uploaded_file.name}")

            extracted_text = extract_text_from_pdf(uploaded_file)
            chunks = split_text_into_chunks(extracted_text)
            embeddings = generate_embeddings(chunks)
            faiss_index = create_faiss_index(embeddings)

            st.header("❓ Ask Your Question")

            question = st.text_input("Enter your medical question")
# ----------------------------
# Button
# ----------------------------
            if st.button("🔍 Generate Answer"):

                if question.strip() == "":
                    st.warning("⚠ Please enter your medical question.")
                else:
                # Generate query embedding
                    query_embedding = generate_query_embedding(question)

                # Search similar chunks
                    retrieved_chunks = search_similar_chunks(
                        faiss_index,
                        query_embedding,
                        chunks
                    )

                    st.success("✅ Similarity Search Completed")

                    context = "\n\n".join(retrieved_chunks)

                    st.markdown("---")
                    st.header("🤖 AI Answer")

                    try:
                        with st.spinner("Generating AI Answer..."):
                            answer = generate_answer(
                                context, 
                                question
                                )

                        st.success(answer)

                    except Exception as e:
                        st.error("❌ Unable to generate the AI answer.")
                        st.exception(e)

                    st.markdown("---")
                    st.header("📑 Retrieved Context")

                    for i, chunk in enumerate(retrieved_chunks):
                        st.text_area(
                            f"Relevant Chunk {i+1}",
                            chunk,
                            height=150
                        )
# -----------------------------
# Processing Details Tab
# -----------------------------
with tab2:

    if uploaded_file is not None:

        st.header("📄 Extracted Medical Report")

        st.text_area(
            "Extracted Text",
            extracted_text,
            height=300
        )

        st.markdown("---")

        st.header("🧩 Text Chunks")

        st.write(f"Total Chunks Created: {len(chunks)}")

        for i, chunk in enumerate(chunks[:3]):
            st.subheader(f"Chunk {i+1}")
            st.text_area(
                f"Chunk {i+1}",
                chunk,
                height=150
            )

        st.markdown("---")

        st.header("🧠 Embedding Information")

        st.write(f"Total Embeddings Generated: {len(embeddings)}")
        st.write(f"Embedding Dimension: {len(embeddings[0])}")
        st.success("✅ Embeddings Generated Successfully")

        st.markdown("---")

        st.header("🗄️ FAISS Vector Database")

        st.write(f"Total Vectors Stored: {faiss_index.ntotal}")
        st.success("✅ FAISS Index Created Successfully")

        st.markdown("---")

        st.header("📊 Project Statistics")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("📄 Chunks", len(chunks))

        with col2:
            st.metric("🧠 Embeddings", len(embeddings))

        with col3:
            st.metric("🗄️ FAISS Vectors", faiss_index.ntotal)

if uploaded_file is not None:
    if st.button("🔄 Reset Application"):
        st.rerun()
    

st.divider()

# ----------------------------
# How It Works
# ----------------------------
with st.expander("📌 How MediRAG Works"):

    st.markdown("""
1. 📄 Upload a medical report (PDF)

2. 🔍 Ask a medical question

3. 🤖 The AI analyzes the uploaded report

4. 💡 A context-aware answer is generated using RAG
""")
st.divider()

st.caption(
    "© 2026 MediRAG | AI-Powered Medical Report Question Answering System | Python 3.11 • Streamlit • LangChain • FAISS • Groq"
)