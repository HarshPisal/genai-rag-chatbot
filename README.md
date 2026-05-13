# genai-rag-chatbot
AI-powered Retrieval-Augmented Generation (RAG) system for semantic document search and intelligent conversational question answering.

# Overview
This project is a Retrieval-Augmented Generation (RAG) based AI assistant that allows users to upload PDF documents and ask questions in natural language.

The system retrieves relevant document chunks using embeddings and vector similarity search, then sends contextual information to the LLM to generate accurate responses.

# Features
PDF document upload
Semantic search using embeddings
Retrieval-Augmented Generation (RAG)
FastAPI backend APIs
Vector database integration
Conversational AI workflow
Context-aware responses
Reduced hallucination using external knowledge retrieval

# Tech Stack
Component -	Technology
Language -	Python
Framework -	FastAPI
LLM Framework -	LangChain
Vector Database -	ChromaDB / FAISS
Embeddings -	OpenAI Embeddings
LLM -	GPT / Llama / Groq
PDF Loader -	PyPDF
Deployment -	Docker

# Architecture
1.User Query
2.Embedding Generation
3.Vector Similarity Search
4.Retrieve Relevant Chunks
5.Context Injection
6.LLM Response Generation

# Project Workflow
1.Upload PDF documents
2.Extract text from documents
3.Split text into chunks
4.Generate embeddings for chunks
5.Store embeddings in vector database
6.Convert user query into embeddings
7.Retrieve most relevant chunks
8.Send retrieved context to LLM
9.Generate contextual answer

# Why RAG?
Traditional LLMs may hallucinate because they rely only on pretrained knowledge.

RAG improves factual accuracy by retrieving external context dynamically before response generation.

# Benefits:
Better factual accuracy
Reduced hallucination
Domain-specific knowledge support
Real-time contextual retrieval

# Installation
pip install -r requirements.txt

Run FastAPI server:

uvicorn app.main:app --reload

# Future Enhancements
Multi-document support
AI agents and tool calling
Conversational memory
Hybrid search
Streaming responses
Authentication and RBAC
Cloud deployment

# Use Cases
Enterprise knowledge assistant

HR policy chatbot
Research assistant
Customer support automation
Internal documentation assistant

# Key Concepts Used
Generative AI
Retrieval-Augmented Generation (RAG)
Embeddings
Semantic Search
Vector Databases
Prompt Engineering
NLP
FastAPI APIs
LangChain Pipelines

# Author

Harsh Pisal
