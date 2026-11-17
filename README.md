# BCG GenAI Financial Chatbot

An AI-powered chatbot built with Streamlit that answers queries about the financial performance of Apple, Microsoft, and Tesla. The chatbot utilizes a rule-based engine to deliver insights derived from historical financial data analysis (2023–2025).

## Supported Queries
The chatbot is currently programmed to answer the following specific questions based on the underlying data analysis:
* What is the total revenue?
* How has net income changed over the last year?
* Is there any relation in the data in Total Revenue and Total Liabilities?
* How has Cash Flow changed over 2023-2025?
* Has Total Assets increased or decreased?

## Features
* **Interactive UI:** A clean, modern chat interface built entirely in Python using Streamlit.
* **Data-Driven Insights:** Predefined responses covering Total Revenue, Net Income, Total Liabilities, Cash Flow, and Total Assets.
* **Automated Testing:** Integrated unit testing using `pytest` to ensure query logic remains accurate and functional.

## Project Structure
* `app.py`: The main Streamlit application containing the chatbot logic and user interface.
* `test_assistant.py`: The pytest suite for verifying the chatbot's responses.
* `requirements.txt`: The complete list of Python dependencies required to run the project.
* `financial_data_analysis.ipynb` / `.pdf` / `.html`: The original Jupyter Notebook and exported reports documenting the data analysis phase.
* `BCG Gen AI.xlsx` / `.csv`: The raw source datasets used for the analysis.

## Installation & Setup

1. **Activate the virtual environment:**
   Ensure you are operating within your isolated Python environment.
   ```bash
   source venv/bin/activate
   ```

2. **Install dependencies:**
   Install the required packages (Streamlit, Pytest, Pandas, etc.) from the requirements file.
   ```bash
   pip install -r requirements.txt
   ```

## Usage

**Running the Application**
Launch the Streamlit server to interact with the chatbot in your web browser.
```bash
streamlit run app.py
```

**Running the Tests**
Execute the test suite to verify the chatbot's logic and response accuracy.
```bash
pytest test_assistant.py
```


*Developed by [Rishabh Jaiswal](https://www.linkedin.com/in/rishabh93/) for the BCG GenAI Job Simulation.*