from aiohttp import web

from store import Store


routes = web.RouteTableDef()


@routes.get('/keys')
async def keys_list(request):
    ''' Getting list of all key-value pairs
    '''
    return web.json_response(Store().list())


@routes.post('/keys')
async def keys_create(request):
    ''' Create new key-value pair(s)
    '''
    Store().bulk_update(await request.json())
    return web.Response(text='OK', status=201)


@routes.post('/keys/clear')
async def clear_all(request):
    ''' Delete all items
    '''
    return web.Response(status=Store().clear())
