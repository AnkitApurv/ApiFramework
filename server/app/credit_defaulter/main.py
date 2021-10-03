from fastapi.routing import APIRouter

from ariadne import make_executable_schema, load_schema_from_path, gql, QueryType
from ariadne.asgi import GraphQL
import pandas

from app.credit_defaulter import ml_model

from typing import List

type_defs = load_schema_from_path(r'.\app\credit_defaulter\schema.graphql')
type_defs = gql(type_defs)

query = QueryType()

@query.field('getPrediction')
async def resolve_getPrediction(_, info, x: dict) -> dict:
    y = await do_work([x])
    return y[0]

@query.field('getPredictions')
async def resolve_getPredictions(_, info, x: List[dict]) -> List[dict]:
    y = await do_work(x)
    return y

schema = make_executable_schema(type_defs, [query])
app = GraphQL(schema, debug = True)

credit_defaulter = APIRouter()
credit_defaulter.add_route(path = '/credit_defaulter', endpoint = app)


async def do_work(x: List[dict]) -> List[dict]:
    df_x = pandas.DataFrame(x)
    df_y = await ml_model.run(df_x)
    y = df_y.to_dict(orient = 'records')
    return y