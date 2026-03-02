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

#### 🟢 Iteration 1: The Basic Assistant
* **Strategy:** Direct translation from NL to CMD.
* **Failures:** The model attempted to "chat" or execute unsafe web-based commands (e.g., searching medical symptoms online).
* **Lesson:** The model lacked boundaries and needed explicit constraints.

#### 🟡 Iteration 2: Constraints & Guardrails
* **Changes:** Implemented mandatory error strings and blocked URL access. Added the `WARNING` prefix for dangerous commands.
* **Failures:** "Over-filtering" occurred—the model blocked safe commands like `ipconfig` because it misclassified them as general knowledge.
* **Lesson:** Constraints alone are too blunt; a logical classification system was required.

#### 🔴 Iteration 3: Intelligent Classification (The Expert Admin)
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

### 🛡️ Enterprise & Filtered Environments (NetFree/SSL Fix)
In environments with strict SSL inspection (like **NetFree** or corporate firewalls), Python's `httpx` and `openai` libraries often crash due to certificate validation errors. 

To solve this, I implemented a custom transport layer that bypasses local certificate conflicts without compromising the application's logic.

**The Solution:**
Add this snippet before initializing your API client:

```python
import os
import httpx

# Clear local SSL cert conflicts
if "SSL_CERT_FILE" in os.environ:
    del os.environ["SSL_CERT_FILE"]

# Initialize client with unverified transport for restricted environments
client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
    http_client=httpx.Client(verify=False)
)
```

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


1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Yaeli6858/NL-to-CLI-Secure-Agent](https://github.com/Yaeli6858/NL-to-CLI-Secure-Agent)
   cd NL-to-CLI-Secure-Agent
   ```
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your `.env` file with your `GROQ_API_KEY`.
4. Run the agent: `python main.py`

---

### 💡 Why this matters
This project demonstrates the power of **Iterative Prompt Engineering**. It shows how to move beyond a simple chatbot to create a specialized, reliable, and safe tool that respects system boundaries.