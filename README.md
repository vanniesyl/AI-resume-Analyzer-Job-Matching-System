

---

# **AI-Based Resume Classifier and Job Matching System**

## **Overview**
This project is an AI-powered resume classifier that matches resumes to job descriptions and provides a similarity score based on how well a candidate's profile aligns with a job posting. The system uses Natural Language Processing (NLP) techniques to analyze and preprocess text from resumes and job descriptions and computes similarity using machine learning methods.

### **Key Features:**
- **Resume Parsing**: Extracts text from PDF resumes.
- **Job Description Parsing**: Analyzes job postings to extract key information.
- **Text Preprocessing**: Cleans the resume and job description text using NLP techniques (e.g., removing stopwords, punctuation, etc.).
- **Similarity Scoring**: Calculates a similarity score between resumes and job descriptions using cosine similarity on TF-IDF vectorized text.
- **Skill Matching**: Matches key skills from the resume to those required in the job description.
- **Experience Matching**: Compares years of experience mentioned in the resume with those required by the job description.
- **Job Recommendations**: Suggests job postings that are relevant to the candidate's resume.
- **Interactive Front-End**: Built using Streamlit, allowing users to upload resumes, input job descriptions, and view similarity scores and recommendations.

## **Project Structure**

```plaintext
.
├── app.py                    # Main application script
├── README.md                 # Project documentation
├── requirements.txt          # List of dependencies
└── dataset                   # Directory containing sample resumes and job descriptions
```

## **Installation**

### **Requirements**
To run the project, you’ll need the following:
- **Python 3.x**
- **Google Colab** or a local Python environment (e.g., Anaconda)
  
Install the required libraries using the following command:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, you can manually install the dependencies:

```bash
pip install spacy sklearn PyPDF2 nltk streamlit pyngrok
```

### **Additional Setup**
1. **Download the spaCy language model**:
   ```bash
   python -m spacy download en_core_web_sm
   ```
2. **Download NLTK stopwords**:
   ```bash
   import nltk
   nltk.download('stopwords')
   ```

## **Usage**

### **Running the Project (Locally)**

1. **Start Streamlit**:
   Run the following command in your terminal to start the app:
   
   ```bash
   streamlit run app.py
   ```

   Streamlit will launch the app in your default browser at `http://localhost:8501`.

2. **Upload Resume**:
   - Upload your resume in PDF format via the user interface.
   - Enter the job description in the provided text area.

3. **View Results**:
   - The system will display the similarity score between your resume and the job description.
   - It will also show any matching skills and relevant experience comparisons.

### **Running in Google Colab**

If you are using **Google Colab**, follow these steps:
1. Install the required libraries:
   ```bash
   !pip install spacy sklearn PyPDF2 nltk streamlit pyngrok
   ```

2. Authenticate **ngrok** to expose the Streamlit app publicly:
   ```bash
   !ngrok authtoken YOUR_NGROK_AUTHTOKEN
   ```

3. Start the Streamlit app and expose it using ngrok:
   ```python
   from pyngrok import ngrok

   # Start Streamlit app
   !streamlit run app.py --server.port 8501 &>/dev/null&

   # Expose the app publicly
   public_url = ngrok.connect(8501, "http")
   print(f"Streamlit app is live at: {public_url}")
   ```

4. Follow the ngrok URL to access the app.

## **Features**

### **1. Resume Parsing**
The app parses resumes uploaded in PDF format and extracts the text content using `PyPDF2`. This allows the system to analyze resumes and process them further.

### **2. Job Description Parsing**
Job descriptions entered by the user are preprocessed to extract essential information for comparison with the resume.

### **3. Text Preprocessing**
Both the resume text and job description are cleaned by:
- Converting to lowercase
- Removing stopwords and punctuation
- Tokenizing the text using `spaCy`

### **4. Similarity Scoring**
The cleaned text is vectorized using **TF-IDF** and compared using **cosine similarity** to provide a score between 0 (no match) and 1 (perfect match).

### **5. Skill Matching**
The app matches the candidate’s skills with the job description requirements and highlights the matched skills.

### **6. Experience Matching**
Extracts and compares years of experience mentioned in the resume with the job description to ensure relevance.

### **7. Job Recommendations**
The system can be extended to provide job recommendations based on the candidate's resume by matching the resume to multiple job descriptions.

### **8. Front-End Interface**
The interactive interface is built with **Streamlit**, allowing users to:
- Upload a resume (PDF)
- Input job descriptions
- View similarity scores, matched skills, and experience relevance.

## **Customization**

### **Adding More Features**
- **Keyword Extraction**: Use libraries like `KeyBERT` to extract important keywords from resumes and job descriptions and highlight them in the output.
- **Machine Learning**: Train a model to predict how well a resume fits a job description based on labeled data.
- **Formatting Analysis**: Use `OpenCV` to analyze the visual structure of resumes and provide feedback on formatting.

### **Deployment Options**
- **Local**: Run the Streamlit app on your local machine.
- **Streamlit Cloud**: Deploy the app to Streamlit Cloud for free and share it with others.
- **Heroku**: Deploy the app on Heroku for production use.

## **Sample Commands**

- Start the app locally:
   ```bash
   streamlit run app.py
   ```

- Analyze resume text:
   ```python
   resume_text = extract_resume_text("resume.pdf")
   print(resume_text)
   ```

- Preprocess job description:
   ```python
   job_description = "We are looking for a Data Scientist with Python skills..."
   cleaned_job_description = preprocess_text(job_description)
   ```

- Calculate similarity score:
   ```python
   similarity_score = calculate_similarity(cleaned_resume, cleaned_job_description)
   print(f"Similarity Score: {similarity_score}")
   ```

## **Contributing**
Contributions are welcome! Feel free to fork this repository and submit pull requests with any improvements or additional features.

## **License**
This project is licensed under the MIT License.

---

This **README** covers the core details of your project, how to set it up, and how to use it. You can expand on the sections based on any new features you implement. Let me know if you need adjustments!
