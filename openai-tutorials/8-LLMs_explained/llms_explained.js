/**
 * This script uses the OpenAI API to create a chat completion with a specific prompt
 * and retrieves the log probabilities (`logprobs`) of the top tokens at each step of the response.
 *
 * Key functionality includes:
 * - Initializing the OpenAI client with the API key from environment variables.
 * - Sending a system message and a user prompt ("Einstein") to generate a response from the GPT-4o-mini model.
 * - Retrieving the top 3 log probabilities (`top_logprobs`) for each token in the response.
 * - Iterating through the `logprobs` to display tokens and their corresponding top token alternatives and log probabilities.
 *
 * Features:
 * - Model used: "gpt-4o-mini"
 * - Maximum tokens in completion: 50
 * - Stops generating the response at a period (`.`).
 * - Displays each token and the top 3 probable token alternatives along with their log probabilities.
 *
 * @async
 * @function main
 * @requires openai - OpenAI API client with an API key
 * @returns {Promise<void>} Logs the tokens and their respective top 3 token alternatives, along with their log probabilities.
 */

// Imports
const OpenAI = require("openai");

// Initialize OpenAI client
const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

async function main() {
  // Create a chat completion
  const completion = await client.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [
      {
        role: "system",
        content:
          "You are a helpful assistant. Use one short sentence per response.",
      },
      { role: "user", content: "Einstein" },
    ],
    logprobs: true, // Necessary for top logprobs to work
    top_logprobs: 5, // Number of top logprobs to return
    stop: "\n",
  });

  // Retrieve logprobs
  const logprobs = completion.choices[0].logprobs.content;

  // Iterate and display logprobs
  for (const logprob of logprobs) {
    console.log(`Chosen token: "${logprob.token}"`);
    console.log("----------------------------------------");
    console.log("Top logprobs:");

    logprob.top_logprobs.forEach((top_logprob, idx) => {
      console.log(`${idx + 1}. Token: "${top_logprob.token}"`);
      console.log(`   Log probability: ${top_logprob.logprob}`);
    });

    console.log("\n");
  }
}

main();
