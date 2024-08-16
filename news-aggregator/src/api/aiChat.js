import Groq from "groq-sdk";

const groq = new Groq({ apiKey: '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' ,dangerouslyAllowBrowser: true});

export async function getGroqChatCompletion(prompt) {
    const fullPrompt = `Your name is Buzz.This is currently 2024. Keep in mind you are a cool news discusser/debater and answer me like a real human for this: ${prompt}`;

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


