# Web API implementation Architecture

This project is meant to explore achieving following objectives:

1. Implementation's public interface must be easy to use and document. (GraphQL's schema docs)
2. Fast in speed and low on resource usage. (implemented via async execution approach, request batching and GraphQL)
3. Modular, scalable: implementing various APIs in the same server web interface should be trivial. (ToDo via gRPC connecting server and API endpoints)

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

## Reasons for speed improvement: impact % (in order of impact):

1. Batching requests and responses (possible in baseline, but somewhat more difficult, GraphQL makes this easy): 60 %
2. Async execution approach (needs both client and server to be modified to use this approach): 20 %
3. Use of efficient data exchange standards (JSON instead of XML): 20 %

Further speed-up is possible in new implementation: estimated impact % (in order of impact):

1. Flexibility of sending and receiving only the necessary data: will vary case-by-case, ~20-30%
