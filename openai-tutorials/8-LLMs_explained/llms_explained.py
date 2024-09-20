"""
This script uses the OpenAI API to create a chat completion with a specific prompt
and retrieves the log probabilities (`logprobs`) of the top tokens at each step of the response.

Key functionality includes:
- Initializing the OpenAI client with the API key from environment variables.
- Sending a system message and a user prompt ("Einstein") to generate a response from the GPT-4o-mini model.
- Retrieving the top 3 log probabilities (`top_logprobs`) for each token in the response.
- Iterating through the `logprobs` to display tokens and their corresponding top token alternatives and log probabilities.

Features:
- Model used: "gpt-4o-mini"
- Maximum tokens in completion: 50
- Stops generating the response at a period (`.`).
- Displays each token and the top 3 probable token alternatives along with their log probabilities.

Requires:
- OpenAI API client with an API key

Returns:
- Logs the tokens and their respective top 3 token alternatives, along with their log probabilities.
"""

# Imports
import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)


def main():
    # Create a chat completion
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. Use one short sentence per response.",
            },
            {"role": "user", "content": "Einstein"},
        ],
        logprobs=True,  # Necessary for top logprobs to work
        top_logprobs=5,  # Number of top logprobs to return
        stop="\n",
    )

    # Retrieve logprobs
    logprobs = completion.choices[0].logprobs.content

    # Iterate and display logprobs
    for logprob in logprobs:
        print(f'Chosen token: "{logprob.token}"')
        print("----------------------------------------")
        print(f"Top logprobs:")

        for idx, top_logprob in enumerate(logprob.top_logprobs, start=1):
            print(f'{idx}. Token: "{top_logprob.token}"')
            print(f"   Log probability: {top_logprob.logprob}")

        print("\n")


main()
