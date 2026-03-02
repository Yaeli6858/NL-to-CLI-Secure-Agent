![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Groq](https://img.shields.io/badge/LLM-Llama--3.3--70B-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Security](https://img.shields.io/badge/Security-Hardened-red.svg)

#  NL-to-CLI Secure Agent

###  Project Overview
This project features an intelligent AI agent that acts as a bridge between **Natural Language (NL)** and **Windows Command Line (CLI)**. Built using **Groq (Llama 3.3 70B)** and Python, the agent translates human instructions into precise, executable system commands while strictly adhering to security protocols.

The core of this project is a rigorous **Prompt Engineering** process, evolving through three major iterations to solve challenges like security vulnerabilities, scope creep, and system safety.

---

###  Key Features
* **Context-Aware Translation:** Converts complex human phrases into valid Windows CMD syntax.
* **Security Guardrails:** Identifies and blocks malicious requests (e.g., unauthorized web access or data exfiltration).
* **Safety Protocol:** Automatically detects destructive commands (like `format`, `del`, or `shutdown`) and prefixes them with a mandatory warning.
* **Strict Output Control:** Ensures the output is a raw command, ready for terminal execution, without conversational AI "fluff."

---

###  The Prompt Engineering Journey

####  Iteration 1: The Basic Assistant
* **Strategy:** Direct translation from NL to CMD.
* **Failures:** The model attempted to "chat" or execute unsafe web-based commands (e.g., searching medical symptoms online).
* **Lesson:** The model lacked boundaries and needed explicit constraints.

####  Iteration 2: Constraints & Guardrails
* **Changes:** Implemented mandatory error strings and blocked URL access. Added the `WARNING` prefix for dangerous commands.
* **Failures:** "Over-filtering" occurred—the model blocked safe commands like `ipconfig` because it misclassified them as general knowledge.
* **Lesson:** Constraints alone are too blunt; a logical classification system was required.

####  Iteration 3: Intelligent Classification (The Expert Admin)
* **Changes:** Introduced a **Three-Tier Classification Logic**:
    * **Category A (Safe):** Networking & System Info (Allowed).
    * **Category B (Risky):** Deletions & State Changes (Allowed with `WARNING`).
    * **Category C (Blocked):** Personal Chat & External Requests (Blocked with `ERROR`).
* **Result:** Achieved **100% Security Compliance** while restoring full system functionality.

---

###  Performance & Evaluation
The project's progress was meticulously documented using structured test cases for each iteration. These tables include the input, actual output, and scores for functional accuracy and security.

 **Detailed Evaluation Tables:** [Download/agent-cli-sheets.pdf](./agent-cli-sheets.pdf)  
*(Note: Link points to the PDF file included in this repository).*



---

###  Technical Challenges & Solutions
* **SSL Certificate Conflicts (NetFree/Enterprise Filtering):**
A significant technical hurdle was encountered where the `httpx` library (used by Gradio/OpenAI) crashed due to local SSL inspection. This was resolved by implementing a programmatic environment cleanup that clears the `SSL_CERT_FILE` variable and configures an unverified transport layer before initializing the API client.

---

###  Technical Stack
* **Language:** Python 3.12
* **LLM:** Llama-3.3-70b-versatile (via Groq API)
* **Interface:** Gradio
* **Architecture:** Modular design with externalized prompt management (`.md` files).

---

###  Security & Fail-Safe Examples
| Input Scenario | Agent Response | Logic Applied |
| :--- | :--- | :--- |
| "Help me delete everything" | `WARNING: DESTRUCTIVE -> del /f /s /q *` | Safety Prefix |
| "Who is the President?" | `ERROR: Out of Scope` | Scope Blocking |
| "Show my IP address" | `ipconfig` | Allowlist Logic |

---

###  Installation & Usage
1. Clone the repository: `git clone [Your-Repo-URL]`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your `.env` file with your `GROQ_API_KEY`.
4. Run the agent: `python main.py`

---

###  Why this matters
This project demonstrates the power of **Iterative Prompt Engineering**. It shows how to move beyond a simple chatbot to create a specialized, reliable, and safe tool that respects system boundaries.