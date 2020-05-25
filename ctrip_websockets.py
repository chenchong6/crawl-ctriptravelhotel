import asyncio
import websockets, json
from dbconfig import mycollection
from websocket import create_connection
from ctriptravel import Crip_travel

USERS = set()

num = 1


# 注册列表内客户端推送
async def notify_users(unique_user):
    c = Crip_travel()
    if unique_user.get('id') == '2':

        if USERS:
            js, magicid = await c._oceanball()
            await asyncio.wait([user.send(json.dumps({'id': 1, 'reason': js, 'magicid': magicid})) for user in USERS])

        else:
            await asyncio.wait([user.send(json.dumps({'id': 0, 'reason': '请求ctrip无数据'})) for user in USERS])
            return
    elif unique_user.get('id') == '3':
        if USERS:
            eleven = unique_user.get('eleven')
            magicid = unique_user.get('magicid')
            await c._AjaxHotelList(eleven,magicid)
            js, magicid = await c._oceanball()
            await asyncio.wait([user.send(json.dumps({'id': 1, 'reason': js, 'magicid': magicid})) for user in USERS])


# 注册用户
async def register(websocket):
    async for message in websocket:
        unique_user = json.loads(message)
        if unique_user.get('id') == '2':  # 第一次建连接
            USERS.add(websocket)
            await notify_users(unique_user)
        elif unique_user.get('id') == '3':

            USERS.add(websocket)
            await notify_users(unique_user)

        # elif unique_user.get('id') == '1':
        #     USERS1.add(websocket)
        #     if USERS2:
        #         await notify_users(unique_user)
        #     else:
        #         await asyncio.wait(
        #             [user.send(json.dumps({'id': 0, 'reason': 'tamper脚本未建里webscket连接'})) for user in USERS1])


async def counter(websocket, path):
    await register(websocket)
    # try:
    # async for message in websocket:
    # except Exception:
    #     print(Exception)
    # finally:
    #     await unregister(websocket)


# 接收客户端消息并处理，这里只是简单把客户端发来的返回回去
async def recv_msg(websocket):
    print(websocket)
    while True:
        recv_text = await websocket.recv()
        print(websocket.cookie)
        recv_dict = json.loads(recv_text)
        astr = ''
        if recv_dict['id'] == '1':
            astr = recv_dict.get('astr')
            # await websocket.send(col['js'])
        elif recv_dict['id'] == '2' and astr:
            await websocket.send(astr)
        else:
            print(recv_text, '=====')
        print(astr)


# 服务器端主逻辑
async def main_logic(websocket, path):
    # await check_permit(websocket)
    await recv_msg(websocket)


# ----------------------------------------------------------------------------

# 客户端逻辑
def client_websocket(astr: str):
    ws = create_connection("ws://127.0.0.1:8014")
    ws.send(astr)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(websockets.serve(counter, '127.0.0.1', '8014'))
    asyncio.get_event_loop().run_forever()
