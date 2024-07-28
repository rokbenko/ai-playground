const { VertexAI } = require("@google-cloud/vertexai");

const projectId = "xxxxxxxxxxxxxxxxxxx";
const location = "us-central1";

const vertexAI = new VertexAI({ project: projectId, location: location });

async function run() {
  const model = vertexAI.preview.getGenerativeModel({ model: "gemini-pro" });
  const request = {
    contents: [{ role: "user", parts: [{ text: "Say hi" }] }],
  };
  const result = await model.generateContent(request);
  const response = await result.response;

  console.log(response.candidates[0].content.parts[0].text);
}

run();
