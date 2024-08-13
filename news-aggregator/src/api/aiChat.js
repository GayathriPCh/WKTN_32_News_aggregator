import Groq from "groq-sdk";

const groq = new Groq({ apiKey: '' ,dangerouslyAllowBrowser: true});

export async function getGroqChatCompletion(prompt) {
    const fullPrompt = `Keep in mind you are a cool news discusser/debater and answer me for this: ${prompt}`;

  return groq.chat.completions.create({
    messages: [
      {
        role: "user",
        content: fullPrompt,
      },
    ],
    model: "llama3-8b-8192",
    "temperature": 0.7,
    "max_tokens": 1024,
    "top_p": 1,
    "stream": false,
    "stop": null
  });
}


