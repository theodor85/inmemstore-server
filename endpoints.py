from aiohttp import web

from storage import Storage


routes = web.RouteTableDef()


@routes.get('/keys')
async def keys_list(request):
    ''' Getting list of all key-value pairs
    '''
    return web.json_response(Storage().list())


@routes.get('/key')
async def one_item(request):
    ''' Getting chosen values
    '''
    body = await request.json()
    key = body[0]
    value, status_code = Storage().get_value(key)
    return web.Response(status=status_code, text=value)


@routes.post('/keys')
async def keys_create(request):
    ''' Create new key-value pair(s)
    '''
    return web.Response(status=Storage().bulk_update(await request.json()))


@routes.delete('/keys')
async def keys_delete(request):
    ''' Delete chosen values
    '''
    result, status_code = Storage().delete(await request.json())
    return web.json_response(result, status=status_code)


@routes.post('/keys/clear')
async def clear_all(request):
    ''' Delete all items
    '''
    return web.Response(status=Storage().clear())
