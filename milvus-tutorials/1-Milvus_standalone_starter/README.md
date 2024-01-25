# #1 Milvus Standalone starter

## Short description

Python and Node.js examples on how to install Milvus Standalone using Docker, connect to a Milvus server and list all collections.

<br>

## Working example in Python

If you run `milvus_standalone.py`, you should get the following response:

> List all collections: <br>
> []

Environment:

- Windows `10`
- Python `3.12.1`
- Milvus Python SDK `2.3.6`

<br>

## Working example in Node.js

If you run `milvus_standalone.js`, you should get the following response:

> List all collections: <br>
> { <br>
> &nbsp;&nbsp;&nbsp;&nbsp;collection_names: [], <br>
> &nbsp;&nbsp;&nbsp;&nbsp;collection_ids: [], <br>
> &nbsp;&nbsp;&nbsp;&nbsp;created_timestamps: [], <br> 
> &nbsp;&nbsp;&nbsp;&nbsp;created_utc_timestamps: [], <br>
> &nbsp;&nbsp;&nbsp;&nbsp;inMemory_percentages: [], <br>
> &nbsp;&nbsp;&nbsp;&nbsp;query_service_available: [], <br>
> &nbsp;&nbsp;&nbsp;&nbsp;status: { <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;error_code: 'Success', <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reason: '', <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;code: 0, <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;retriable: false, <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;detail: '' <br>
> &nbsp;&nbsp;&nbsp;&nbsp;}, <br>
> &nbsp;&nbsp;&nbsp;&nbsp;data: [] <br>
> }

Environment:

- Windows `10`
- Node.js `21.2.0`
- Milvus Node.js SDK `2.3.5`
