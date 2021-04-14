from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.requests import Request
from starlette.responses import JSONResponse

from starlette_context import context, plugins
from starlette_context.middleware import RawContextMiddleware

from other_module import get_current_request_data
import uuid

middleware = [
    Middleware(
        RawContextMiddleware,
        plugins=(
            plugins.RequestIdPlugin(),
            plugins.CorrelationIdPlugin()
        )
    )
]

app = Starlette(middleware=middleware)


@app.route("/")
async def index(request: Request):
    context.data["bussines_transation_id"] = str(uuid.uuid1())
    print(f'context in route layer: {context.data}')
    return JSONResponse(get_current_request_data())
