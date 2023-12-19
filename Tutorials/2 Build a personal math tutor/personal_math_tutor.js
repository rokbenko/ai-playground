const OpenAI = require("openai");
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

async function main() {
  // Step 1: Create an Assistant
  const myAssistant = await openai.beta.assistants.create({
    model: "gpt-4",
    instructions:
      "You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
    name: "Math Tutor",
    tools: [{ type: "code_interpreter" }],
  });
  console.log("This is the assistant object: ", myAssistant, "\n");

  // Step 2: Create a Thread
  const myThread = await openai.beta.threads.create();
  console.log("This is the thread object: ", myThread, "\n");

  // Step 3: Add a Message to a Thread
  const myThreadMessage = await openai.beta.threads.messages.create(
    (thread_id = myThread.id),
    {
      role: "user",
      content: "I need to solve the equation `3x + 11 = 14`. Can you help me?",
    }
  );
  console.log("This is the message object: ", myThreadMessage, "\n");

  // Step 4: Run the Assistant
  const myRun = await openai.beta.threads.runs.create(
    (thread_id = myThread.id),
    {
      assistant_id: myAssistant.id,
      instructions: "Please address the user as Rok Benko.",
    }
  );
  console.log("This is the run object: ", myRun, "\n");

  // Step 5: Periodically retrieve the Run to check on its status to see if it has moved to completed
  const retrieveRun = async () => {
    let keepRetrievingRun;
  
    while (myRun.status === "in_progress") {
      keepRetrievingRun = await openai.beta.threads.runs.retrieve(
        (thread_id = myThread.id),
        (run_id = myRun.id)
      );
  
      console.log(`Run status: ${keepRetrievingRun.status}`);
  
      if (keepRetrievingRun.status === "completed") {
        console.log("\n");
        break;
      } else {
        console.log(`Run status: ${keepRetrievingRun.status}`);
        break;
      }
    }
  };
  
  retrieveRun();

  // Step 6: Retrieve the Messages added by the Assistant to the Thread
  const waitForAssistantMessage = async () => {
    await retrieveRun();

    const allMessages = await openai.beta.threads.messages.list(
      (thread_id = myThread.id)
    );

    console.log(
      "------------------------------------------------------------ \n"
    );

    console.log("User: ", myThreadMessage.content[0].text.value);
    console.log("Assistant: ", allMessages.data[0].content[0].text.value);
  };
  waitForAssistantMessage();
}

main();
