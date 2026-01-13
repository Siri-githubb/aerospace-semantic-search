# Aerospace Semantic Document Search Engine

## Overview
This project implements a semantic search engine for aerospace engineering documents. It enables natural language search over technical PDF reports related to turbine blade thermal fatigue and low-cycle fatigue, going beyond traditional keyword-based search.

## Problem Statement
Aerospace engineering reports are typically long, highly technical, and often available only as scanned PDFs. Searching these documents using keyword-based methods is inefficient and may fail to retrieve relevant information due to differences in terminology. This project addresses this limitation by applying natural language processing techniques to retrieve conceptually relevant sections from such documents.

## Approach
The system follows an end-to-end NLP pipeline. Text is extracted from aerospace PDF documents and split into sentence-aware chunks with overlap to preserve context. Each chunk is converted into a dense vector embedding using a transformer-based sentence embedding model. These embeddings are indexed using FAISS to enable fast semantic similarity search. Search results include the source document name and page number, allowing verification in the original report.

## Key Features
- Semantic, meaning-based search over aerospace engineering documents  
- Handles noisy OCR text from scanned technical reports  
- Uses transformer-based sentence embeddings  
- Fast similarity search using FAISS  
- Page-level traceability to the original documents  

## Technologies Used
- Python  
- Natural Language Processing (NLTK)  
- Sentence Transformers  
- FAISS  
- pdfplumber  
- NumPy  

## Input Data
The project expects aerospace PDF documents to be placed in the `data/pdfs/` directory. PDF files are not included in this repository due to file size and licensing considerations. Users can add their own aerospace engineering PDFs locally before running the pipeline.

The `data/` directory contains raw PDFs, extracted text, text chunks, and FAISS index files. These files are generated locally and are excluded from version control using `.gitignore`.

## How to Run
Install the required dependencies using the requirements file. Place aerospace PDF documents inside the `data/pdfs/` directory. Run the scripts in sequence to extract text, create chunks, generate embeddings, and perform semantic search. The search script prompts the user to enter a natural language query.

 
