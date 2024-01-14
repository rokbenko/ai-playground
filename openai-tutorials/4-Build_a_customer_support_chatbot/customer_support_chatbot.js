const OpenAI = require("openai");
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});
const fs = require("fs");

async function main() {
  // Step 1: Upload a File with an "assistants" purpose
  const myFile = await openai.files.create({
    file: fs.createReadStream("knowledge.txt"),
    purpose: "assistants",
  });
  console.log("This is the file object: ", myFile, "\n");

  // Step 2: Create an Assistant
  const myAssistant = await openai.beta.assistants.create({
    model: "gpt-3.5-turbo-1106",
    instructions:
      "You are a customer support chatbot. Use your knowledge base to best respond to customer queries.",
    name: "Customer Support Chatbot",
    tools: [{ type: "retrieval" }],
  });
  console.log("This is the assistant object: ", myAssistant, "\n");

  // Step 3: Create a Thread
  const myThread = await openai.beta.threads.create();
  console.log("This is the thread object: ", myThread, "\n");

  // Step 4: Add a Message to a Thread
  const myThreadMessage = await openai.beta.threads.messages.create(
    (thread_id = myThread.id),
    {
      role: "user",
      content: "What can I buy in your online store?",
      file_ids: [myFile.id],
    }
  );
  console.log("This is the message object: ", myThreadMessage, "\n");

  // Step 5: Run the Assistant
  const myRun = await openai.beta.threads.runs.create(
    (thread_id = myThread.id),
    {
      assistant_id: myAssistant.id,
      instructions: "Please address the user as Rok Benko.",
    }
  );
  console.log("This is the run object: ", myRun, "\n");

  // Step 6: Periodically retrieve the Run to check on its status to see if it has moved to completed
  const retrieveRun = async () => {
    let keepRetrievingRun;

    while (myRun.status === "queued" || myRun.status === "in_progress") {
      keepRetrievingRun = await openai.beta.threads.runs.retrieve(
        (thread_id = myThread.id),
        (run_id = myRun.id)
      );
      console.log(`Run status: ${keepRetrievingRun.status}`);

      if (keepRetrievingRun.status === "completed") {
        console.log("\n");

        // Step 7: Retrieve the Messages added by the Assistant to the Thread
        const allMessages = await openai.beta.threads.messages.list(
          (thread_id = myThread.id)
        );

        console.log(
          "------------------------------------------------------------ \n"
        );

        console.log("User: ", myThreadMessage.content[0].text.value);
        console.log("Assistant: ", allMessages.data[0].content[0].text.value);

        break;
      } else if (
        keepRetrievingRun.status === "queued" ||
        keepRetrievingRun.status === "in_progress"
      ) {
        // pass
      } else {
        console.log(`Run status: ${keepRetrievingRun.status}`);
        break;
      }
    }
  };
  retrieveRun();
}

main();
