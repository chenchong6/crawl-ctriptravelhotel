# 携程酒店信息获取

>  本接口只提供 ___` eleven破解及持久化方案`___, 注:cookie未研究。
---

###可行性方案 
> 需要一台打开chrome的windows系统，chrome安装tampermonkey。
> 建立websocket长连接，python做服务端主动推送js到tampermonkey,tampermonkey解析返回eleven给服务端



---
###  程序入口
####  [ctrip_websockets.py](./ctrip_websockets.py)
> 参考[ctrip_websockets.py](./ctrip_websockets.py)
> 96行 

    if __name__ == '__main__':
        asyncio.get_event_loop().run_until_complete(websockets.serve(counter, '127.0.0.1', '8014'))
        asyncio.get_event_loop().run_forever()  
---
#### 注： ` 本文档只供研究使用` 