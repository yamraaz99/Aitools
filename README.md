
## News Summarizer

### Description  
**News Summarizer** is a Python application that summarizes news articles based on the given title and URL using the **Google Gemini API**. It extracts concise and valuable insights, ensuring that no key points are missed.

### Features  
- Integrates the **Gemini API** (`gemini-1.5-flash`) for generating high-quality, AI-powered news summaries.  
- Provides **valuable insights** and **key points** from long news articles.  
- Easy to use — input a news title and its corresponding URL, and receive a clean summary.  

---

### Installation  

#### Prerequisites  
- Python 3.8 or higher  
- Google Generative AI SDK (`google-generativeai`)  

#### Steps  
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/news-summarizer.git
   cd news-summarizer
   ```

2. Install the required dependencies:
   ```bash
   pip install google-generativeai
   ```

3. Set up your **Gemini API Key**:
   - Replace `YOUR_API_KEY` in the code with your actual API key:
     ```python
     genai.configure(api_key="YOUR_API_KEY")
     ```

---

### Usage  

Run the program:  
```bash
python main.py
```

Follow the prompts:  
1. **Enter the title** of the news article.  
2. **Enter the URL** of the news article.  

**Example Input**:
```
Enter the title of the news:
Gukesh Wins 2024 FIDE World Championship

Enter the URL of the news article:
https://example.com
```

**Example Output**:
```
Summary:
Indian Grandmaster Gukesh clinched the 2024 FIDE World Championship title with a commanding performance, highlighting his dominance and strategic brilliance in chess.
```

---

### Code Overview  

#### Main Script  
- **`summarize_news(title, url)`**:
   - Calls the **Gemini API** with a customized prompt to generate concise and valuable insights.  
   - Model used: **`gemini-1.5-flash`**.  
- **`main()`**:
   - Takes user input for title and URL.  
   - Displays the generated summary.  

---

### API Configuration  

This project uses the **Google Gemini API**. To get started:  
1. Obtain your API key from [Google AI Studio](https://makersuite.google.com/).  
2. Replace the placeholder in the code:  
   ```python
   genai.configure(api_key="YOUR_API_KEY")
   ```

---

### Dependencies  
- Python 3.8+  
- `google-generativeai` (Google Generative AI SDK)

---

### License  
This project is licensed under the **MIT License**.

---
