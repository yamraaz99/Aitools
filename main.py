
# Set your OpenAI API key
openai.api_key = '<Replace with your API Key>'


def summarize_news(title, url):
    # You can customize the prompt based on your needs
    prompt = f"Summarize the news with title: '{title}' and URL: '{url}'"

    # Use the OpenAI GPT-3 engine to generate a summary
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150  # You can adjust the number of tokens as needed
    )

    summary = response['choices'][0]['text']
    return summary


def main():
    print("News Summarizer")
    print("Enter the title of the news:")
    news_title = input()
    print("Enter the URL of the news article:")
    news_url = input()

    if news_title and news_url:
        # Generate and display the news summary
        summary = summarize_news(news_title, news_url)
        print("\nSummary:")
        print(summary)
    else:
        print("Please enter both the title and URL of the news article.")


if __name__ == "__main__":
    main()
