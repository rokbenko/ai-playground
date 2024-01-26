import spacy
import json

nlp = spacy.load('en_core_web_lg')

descriptions = [
    "A pulse-pounding action film with explosive shootouts and high-octane chases",
    "An epic fantasy adventure set in a magical realm with mythical creatures and epic battles",
    "A gripping sci-fi thriller exploring the mysteries of outer space and extraterrestrial life",
    "A heartwarming family drama centered around love, loss, and the bonds that endure",
    "A mind-bending psychological thriller that keeps you on the edge of your seat",
    "A hilarious comedy filled with witty banter, slapstick humor, and outrageous antics",
    "A romantic escapade in the enchanting streets of Paris, weaving tales of love and destiny",
    "A spine-chilling horror story set in a haunted mansion with dark secrets lurking within",
    "A thought-provoking drama delving into the complexities of human relationships and morality",
    "A captivating mystery unfolding in a small town, where every resident has a hidden agenda"
]

description_vectors_list = []

for description in descriptions:
    doc = nlp(description)

    reduced_vector = doc.vector[:128].tolist()

    entry = {"vector": reduced_vector, "description": description}
    description_vectors_list.append(entry)

with open('dummy_data.json', 'w') as json_file:
    json.dump(description_vectors_list, json_file, indent=2)

print("JSON file created: dummy_data.json")
