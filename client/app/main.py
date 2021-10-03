import asyncio
import aiohttp
from aiogqlc import GraphQLClient
# from itertools import islice
import pandas

# import json

from datetime import datetime
from typing import List

endpoint = "https://127.0.0.1:8000/credit_defaulter"

query = """
    query q1($x: [Behavior]) {
        getPredictions(x: $x) {
            ID
            default_payment_next_month
            score
            probability_0
            probability_1
            log_probability_0
            log_probability_1
        }
    }
    """
x_path = '.\\data\\default_of_credit_card_clients.parquet'
y_path = '.\\data\\default_of_credit_card_clients_y.parquet'

def load_data(filepath: str) -> List[dict]:
    df = pandas.read_parquet(filepath)
    x = df.to_dict(orient = 'records')
    return x

def make_chunks(seq: List, size: int):
  return [
    seq[i:i + size]
    for i in range(0, len(seq), size)
  ]

def prepare_variables(x: List[dict], batch_size: int = 0) -> List[dict]:
    chunked_variables = []
    if batch_size == 0 or batch_size is None:
        # no batching, dump all at once
        chunked_variables = [{'x': x}] # for k in x]
    elif batch_size == 1:
        # no batching, query one by one
        chunked_variables = [{'x': k} for k in x]
    else:
        # batching
        chunks = make_chunks(x, batch_size)
        chunked_variables = [{'x': k} for k in chunks]
    return chunked_variables

async def make_request(endpoint: str, query: str, variables: dict) -> str:
    async with aiohttp.ClientSession() as session:
        client = GraphQLClient(endpoint, session = session)
        response = await client.execute(query, variables)
        response_json = await response.json()
    return response_json

def save_data(y: List[dict], filepath: str):
    df = pandas.DataFrame(y)
    df.to_parquet(filepath, index = False, compression = None)
    return

def main():
    init = datetime.utcnow()

    x = load_data(x_path)
    chunked_variables = prepare_variables(x, batch_size = 5000)

    start = datetime.utcnow()
    print(f'Prepare requests: {start - init}')

    loop = asyncio.get_event_loop()
    multiple_requests = [make_request(endpoint, query, variables = chunk) for chunk in chunked_variables]
    response_jsons = loop.run_until_complete(asyncio.gather(*multiple_requests))

    end = datetime.utcnow()
    print(f'Requests-responses: {end - start}')
    y_list = []
    for response_json in response_jsons:
        y_list = response_json.get('data').get('getPredictions')
    save_data(y_list, y_path)

    finish = datetime.utcnow()
    print(f'Save responses: {finish - end}')
    return


if __name__ == "__main__":
    main()