# Federal Contract Compliance Co-Pilot 🤖📜

An AI-powered agentic system designed to analyze federal Request for Proposal (RFP) documents, extract key requirements, and identify compliance risks using Amazon Bedrock.

---

## 🎯 The Problem

Government and enterprise contracts, particularly RFPs, are often hundreds of pages long. Manually reviewing these documents to ensure full compliance is a tedious, time-consuming, and error-prone process. A single missed requirement can lead to a non-compliant proposal and a lost opportunity.

This project builds an "Analyst Co-Pilot" to automate this review process, saving time and reducing risk.

---

## ✨ Key Features

* **Interactive Q&A:** Ask questions about the RFP document in plain English.
* **Automated Requirements Extraction:** Automatically identifies and lists all mandatory requirements (clauses containing "shall," "must," etc.).
* **Risk Identification:** Flags potentially ambiguous or contradictory language that may require legal review.
* **Executive Summary:** Generates a concise summary of the document, highlighting key dates, deliverables, and sections.

---

## ⚙️ Tech Stack & Architecture

This project is built using a modern, scalable stack designed for building and deploying agentic AI applications.

* **Cloud & AI Services:**
    * **Amazon Bedrock:** Provides access to powerful foundation models (e.g., Anthropic's Claude 3).
    * **Amazon Titan Embeddings:** Used for generating vector representations of the document text.
* **Core Framework:**
    * **LangChain / LangGraph:** Used to build the core Retrieval-Augmented Generation (RAG) pipeline and orchestrate the multi-agent system.
* **Application & Deployment:**
    * **FastAPI:** Exposes the agent's functionality via a REST API.
    * **Poetry:** Manages Python dependencies and project packaging.
    * **Docker:** Containerizes the application for consistent and portable deployment.

---

## 🚀 Getting Started

### Prerequisites

* Python 3.10+
* Poetry installed
* An AWS account with configured credentials and access to Amazon Bedrock.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/antonio-zavaleta/Federal-Compliance-Copilot.git
    cd Federal-Compliance-Copilot
    ```

2.  **Install dependencies using Poetry:**
    ```bash
    poetry install
    ```

3.  **Run the application:**
    ```bash
    poetry run uvicorn use_case_contracts.main:app --reload
    ```

---

## Usage

Once the application is running, the API and its documentation will be available at `http://127.0.0.1:8000/docs`. You can interact with the endpoints directly from this interface.

<!-- (This section can be updated with `curl` examples as you build out the API). -->

---

## ⚖️ License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.
