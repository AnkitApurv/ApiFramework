# Web API implementation Architecture

This project is meant to explore achieving following objectives:

1. A low approach to implementing APIs.
2. Implementation's public interface must be easy to use and document. (GraphQL's schema docs)
3. Fast and low on resource usage. (implemented via asyncio, request batching and GraphQL)
4. Modular: to implement various APIs in the same server web interface. (ToDo via gRPC connecting server and API endpoints)

## Test results

See client and server RunLog.md for more details

[Dataset](https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients)

Timing results: New Implementation\
Prepare requests: 00.680105 seconds\
Requests-responses: 10.244659 seconds\
Save responses: 00.021846 seconds

Timing results: Baseline\
Prepare requests: 01 minutes 13.537498 seconds\
Requests-responses: 07 minutes 57.877159 seconds\
Save responses: 01 minutes 10.876450 seconds

Total time taken:\
Baseline: 622.27 seconds\
New implementation: 10.94 seconds

Speedup: __56.88 times__