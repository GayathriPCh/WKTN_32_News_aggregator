import google.generativeai as genai

def analyze_article(content):
    try:
        # Configure the API key
        api_key = 'AIzaSyBFnG0vbnM1V1hZJBWB5IwjyPakZRzjNIs'
        genai.configure(api_key=api_key)

        # Initialize the GenerativeModel
        model = genai.GenerativeModel('gemini-1.5-flash')  # Correct model name as per documentation

        # Create a prompt for analysis
        prompt = f"Identify and list tough or professional words, idioms, or phrases from the following text, and provide examples of how a Gen Z student might use them in daily life: {content}"

        # Generate content
        response = model.generate_content(prompt)
        
        # Return the generated text
        return response.text

    except Exception as e:
        print(f"An error occurred: {e}")
        return "Analysis could not be generated at this time."
