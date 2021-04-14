from starlette_context import context as current_request
from other_module_2 import get_current_request_data_2


def get_current_request_data():
    print(f'context in other module layer: {current_request.data}')
    return get_current_request_data_2()
