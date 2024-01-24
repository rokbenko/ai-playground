from pymilvus import connections, utility, MilvusException

connections.connect(host="localhost", port="19530")

try:
    # List all collections
    collections = utility.list_collections()
    print(f"List all collections:\n", collections)
except MilvusException as e:
    print(e)
