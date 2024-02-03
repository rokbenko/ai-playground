import spacy
from pymilvus import connections, Collection, MilvusException

spacy_model = spacy.load('en_core_web_lg')

connections.connect(host="localhost", port="19530")

try:
    while True:
        user_input = input("Describe what movie would you like to watch (or type 'exit' to quit):\n")

        if user_input.lower() == 'exit':
            break

        user_input_doc = spacy_model(user_input)
        user_vector = user_input_doc.vector[:128].tolist()

        search_params = {
            "metric_type": "L2",
            "offset": 0,
            "ignore_growing": False,
            "params": {"nprobe": 10}
        }

        collection = Collection("Movies")

        similarity_search_result = collection.search(
            data=[user_vector],
            anns_field="vector",
            param=search_params,
            limit=3,
            output_fields=['description']
        )

        for idx, hit in enumerate(similarity_search_result[0]):
            score = hit.distance
            description = hit.entity.description
            print(f"{idx + 1}. {description} (distance: {score})")

except MilvusException as e:
    print(e)
finally:
    connections.disconnect(alias="localhost")
