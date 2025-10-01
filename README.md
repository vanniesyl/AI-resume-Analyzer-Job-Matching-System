

# AI-Based Resume Classifier and Job Matching System

## Project Description

The **AI-Based Resume Classifier and Job Matching System** is an AI-powered tool designed to help match resumes to job descriptions. It evaluates the similarity between a candidate’s resume and a job posting by using natural language processing (NLP) techniques and machine learning algorithms. The system calculates a similarity score, identifies matching skills, and compares the candidate’s experience with the job’s requirements.

### Key Features:

* **Resume Parsing**: Extracts text from uploaded PDF resumes.
* **Job Description Parsing**: Analyzes job descriptions to extract key information.
* **Text Preprocessing**: Cleans and normalizes text from resumes and job descriptions.
* **Similarity Scoring**: Uses cosine similarity to calculate a match score between the resume and job description.
* **Skill Matching**: Identifies and compares skills between the resume and job requirements.
* **Experience Matching**: Compares years of experience from the resume with those required by the job description.
* **User Interface**: Built using Streamlit, allowing users to upload resumes and job descriptions for analysis.

## Project Requirements

To run this project, you will need the following:

* **Python 3.6 or higher**
* Required Python libraries (listed below)

### Required Libraries:

You can install all required libraries using the `requirements.txt` file:

```txt
streamlit
spacy
sklearn
PyPDF2
nltk
pyngrok
pandas
numpy
matplotlib
seaborn
```

To install the dependencies, run the following command in your terminal:

```bash
pip install -r requirements.txt
```

Alternatively, you can manually install the libraries by running:

```bash
pip install streamlit spacy sklearn PyPDF2 nltk pyngrok pandas numpy matplotlib seaborn
```

### Additional Setup:

1. **Download the SpaCy Language Model**:

   * To enable text processing, you need to download the SpaCy English language model:

   ```bash
   python -m spacy download en_core_web_sm
   ```

2. **Download NLTK Stopwords**:

   * You will need to download the stopwords dataset for text processing:

   ```python
   import nltk
   nltk.download('stopwords')
   ```

## How to Run the Project Locally

### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/vanniesyl/AI-resume-Analyzer-Job-Matching-System.git
cd AI-resume-Analyzer-Job-Matching-System
```

### Step 2: Install Dependencies

Install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```

### Step 3: Run the Streamlit Application

Start the Streamlit app with the following command:

```bash
streamlit run app.py
```

The app will start a local server and be available in your web browser at `http://localhost:8501`.

### Step 4: Interact with the App

1. **Upload Resume**: Upload your resume in PDF format.
2. **Enter Job Description**: Paste the job description into the provided text box.
3. **View Results**: The app will display a similarity score and highlight matching skills and experience.

---
