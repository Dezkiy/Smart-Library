# Contributing

Thank you for considering contributing to the Smart Library project! 🎉  
We welcome pull requests from everyone. Please read the following guidelines before you begin.

---

## 🔧 Project Setup Instructions

### Prerequisites
- Python 3.11+
- Poetry (or pip)
- Git

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/smart-library.git
    cd smart-library
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    .\venv\Scripts\activate   # Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run tests to confirm setup:
    ```bash
    pytest
    ```

---

## 🧹 Coding Standards

- Follow PEP8 conventions.
- Use descriptive variable and function names.
- Run all tests before submitting a PR:
    ```bash
    pytest
    ```

- Recommended tools:
    - `flake8` for linting
    - `black` or `autopep8` for formatting

---

## 📌 How to Contribute

1. **Fork this repository**.

2. **Pick an issue** labeled `good-first-issue` or discuss a new feature in the issues tab.

3. **Create a new branch**:
    ```bash
    git checkout -b feature/your-feature-name
    ```

4. **Write your code**, add/modify tests, and commit changes:
    ```bash
    git add .
    git commit -m "Add feature: description"
    ```

5. **Push to your fork** and submit a **Pull Request** to the `main` branch.

6. Provide a **clear PR description** including:
    - What was added/changed
    - How to test it
    - Related issue numbers (e.g., Closes #5)

---

## 🙌 Code of Conduct

Please respect other contributors.

---

Happy coding! 💻📚  
