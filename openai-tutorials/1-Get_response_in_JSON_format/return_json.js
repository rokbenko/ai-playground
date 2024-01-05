const OpenAI = require("openai");
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

async function main() {
  const completion = await openai.chat.completions.create({
    model: "gpt-4-1106-preview",
    messages: [
      {
        role: "system",
        content:
          "You are a helpful assistant. Your response should be in JSON format.",
      },
      { role: "user", content: "Hello!" },
    ],
    response_format: { type: "json_object" },
  });

  console.log(completion.choices[0].message.content);

  // Check if the OpenAI API response is a valid JSON
  const isJSON = (obj) => {
    try {
      JSON.parse(obj);
      return true;
    } catch (e) {
      return false;
    }
  };

  console.log(isJSON(completion.choices[0].message.content));
}

main();
