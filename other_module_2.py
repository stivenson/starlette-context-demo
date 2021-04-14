from starlette_context import context as current_request


def get_current_request_data_2():
    print(f'context in other module (2) layer: {current_request.data}')
    return current_request.data
