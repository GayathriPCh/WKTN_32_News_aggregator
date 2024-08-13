import google.generativeai as genai

# Configure the API key
api_key = 'AIzaSyBFnG0vbnM1V1hZJBWB5IwjyPakZRzjNIs'
genai.configure(api_key=api_key)

def analyze_article(content):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Analyze this article content and list any tough or professional words, idioms or phrases used. Provide examples of a cool GenZ student using them in their daily life."
        response = model.generate_content(prompt)
        
        return response.text

    except Exception as e:
        print(f"An error occurred: {e}")
        return "Analysis could not be generated at this time."
