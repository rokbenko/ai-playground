# #1 Milvus Standalone starter

## Short description

Python and Node.js examples on how to install Milvus Standalone using Docker, connect to a Milvus server and list all collections.

<br>

## Working example in Python

If you run `milvus_standalone.py`, you should get the following response:

> List all collections:
> []

Environment:

- Windows `10`
- Python `3.12.1`
- Milvus Python SDK `2.3.6`

<br>

## Working example in Node.js

If you run `milvus_standalone.js`, you should get the following response:

> List all collections:  
> {
> collection_names: [],  
>  collection_ids: [],  
>  created_timestamps: [],  
>  created_utc_timestamps: [],
> inMemory_percentages: [],
> query_service_available: [],
> status: {
> error_code: 'Success',
> reason: '',
> code: 0,
> retriable: false,
> detail: ''
> },
> data: []
> }

Environment:

- Windows `10`
- Node.js `21.2.0`
- Milvus Node.js SDK `2.3.5`
