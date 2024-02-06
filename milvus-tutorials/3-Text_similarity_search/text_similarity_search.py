import spacy
from pymilvus import connections, Collection, MilvusException

# Load the spaCy model for English language
spacy_model = spacy.load('en_core_web_lg')

# Connect to Milvus server
connections.connect(host="localhost", port="19530")

try:
    while True:
        # Get user input for movie description or exit
        user_input = input("\nDescribe what movie would you like to watch (or type 'exit' to quit):\n")

        # Exit loop if user types 'exit'
        if user_input.lower() == 'exit':
            break

        # Process user input using spaCy model to get embedding vector
        user_input_doc = spacy_model(user_input)
        user_vector = user_input_doc.vector[:128].tolist()

        # Define search parameters for similarity search
        search_params = {
            "metric_type": "L2",
            "offset": 0,
            "ignore_growing": False,
            "params": {"nprobe": 10}
        }

        # Connect to the Milvus collection named "Movies"
        collection = Collection("Movies")

        # Perform similarity search using Milvus
        similarity_search_result = collection.search(
            data=[user_vector],
            anns_field="vector",
            param=search_params,
            limit=3,
            output_fields=['description']
        )

        # Display search results to the user
        for idx, hit in enumerate(similarity_search_result[0]):
            score = hit.distance
            description = hit.entity.description
            print(f"{idx + 1}. {description} (distance: {score})")

except MilvusException as e:
    # Handle Milvus exceptions
    print(e)
finally:
    # Disconnect from Milvus server
    connections.disconnect(alias="localhost")