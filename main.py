import google.generativeai as genai

# Set your Gemini API key
genai.configure(api_key="YOUR_API_KEY")

def summarize_news(title, url):
    # Initialize the Gemini model
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Prepare the input prompt
    prompt = f"You are an Expert news agent.You never miss any valuable point to cover.Your task is to provide only valuable insights from a whole news article with the title: '{title}' and the URL: '{url}'. Provide a concise insight without missing key points."

    # Generate the response using Gemini
    response = model.generate_content(prompt)
    
    # Extract and return the response text
    return response.text.strip()

def main():
    print("News Summarizer")
    print("Enter the title of the news:")
    news_title = input().strip()
    print("Enter the URL of the news article:")
    news_url = input().strip()

    if news_title and news_url:
        try:
            # Generate and display the news summary
            summary = summarize_news(news_title, news_url)
            print("\nSummary:")
            print(summary)
        except Exception as e:
            print("\nAn error occurred while summarizing the news:")
            print(e)
    else:
        print("Please provide both the title and URL of the news article.")

if __name__ == "__main__":
    main()
