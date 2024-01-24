const { MilvusClient } = require("@zilliz/milvus2-sdk-node");

const milvusClient = new MilvusClient("localhost:19530");

async function main() {
  try {
    // List all collections
    const collections = await milvusClient.showCollections();
    console.log("List all collections:\n", collections);
  } catch (error) {
    console.error(error);
  }
}

main();
