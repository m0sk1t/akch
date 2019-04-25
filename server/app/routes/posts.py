from sanic.response import text


async def retrieve_post(request, id):
    return text(id)
