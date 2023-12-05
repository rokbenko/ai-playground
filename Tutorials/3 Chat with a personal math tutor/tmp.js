const OpenAI = require("openai");
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

async function main() {
  const response = await openai.beta.assistants.del(
    "asst_895rXM9LIqodjOYVJcM7NsE1"
  );

  console.log(response);
}
main();
