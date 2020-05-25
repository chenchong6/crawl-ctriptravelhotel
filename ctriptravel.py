import aiohttp, time, asyncio, re
from ctrip_js import return_cascode, return_oceanjs


class Crip_travel():

    def __init__(self):

        self.headers = {'referer': 'https://hotels.ctrip.com/hotel/shanghai2',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

    async def _AjaxHotelList(self, eleven, magicid):  # post发送城市数据
        async with aiohttp.ClientSession() as session:
            url = 'https://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx'
            headers = {'referer': 'https://hotels.ctrip.com/hotel/shanghai2',
                       'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
                       'cookie': 'magicid={0}; ASP.NET_SessionId=qopmys5bdx1tcuefiqbvuss3; _abtest_userid=dd979348-5b22-4378-9f0a-346c0c810914; _RGUID=4d486f42-dbea-4a62-a32b-54ed9a0a0d2b; _RSG=YfawRBqR8r4hqW2QsELhCA; _RDG=282208da972f2f20473357b45a83edc30c; hoteluuid=GPDNupOpPHXnuadM; OID_ForOnlineHotel=15900464739423xqvpu1590046478135102032; _RF1=58.240.196.6; MKT_CKID=1590046480560.5oazh.d8gw; MKT_CKID_LMT=1590046480560; _ga=GA1.2.1823403917.1590046481; _gid=GA1.2.1240194812.1590046481; MKT_Pagesource=PC; _bfi=p1%3D102002%26p2%3D102002%26v1%3D12%26v2%3D11; _jzqco=%7C%7C%7C%7C1590046480679%7C1.2067621633.1590046480576.1590047212708.1590047336397.1590047212708.1590047336397.undefined.0.0.12.12; __zpspc=9.1.1590046480.1590047336.12%234%7C%7C%7C%7C%7C%23; appFloatCnt=11; hoteluuidkeys=9F4Ea5inhed7EQDW7YTYzoYGdEzYcY7SehcE9GjshWMYoYsmjOqrBNrNOWQY9YpGjPXyQ5j4nJ5YFYsQj5DI70Imqj7YSYTUv9trB7ylqjt1vQze6OeDcjH5y5Y4YTDvZmvoFYhnwlLjcfe5tiUAYGYcYpYtYDHvloeznYGXioUYbYsYUYGYnSE5cKB8w6FiakRFbjGr1bYtPJ0Qy5r8kYLOWcPv8Fxfme1bY7dxpMxN1YzbitgwmsjUkESpJTaWM0jcroHJqgiPMwF6vLsRn7jZlYa5jarMnyFOiSmwZtRfbEXsjgqxQnxOZEQzElTEZhWU3etkwh8E8zjbcecSiMpYXqrhTebGeamx1biUXilDx74WkQj4be1Lw9dKGBwn9ibURXfjq5ePpEkPym3vTQil5EU6yB8vhDKmUEDPKc7wGdiLpR3tjlrdOYkNJzTyHrg5jAqep5jDBKczjhfwPzxM3xsSxLqxoUEBgEmNEGDWtledGwBMESsjbDeckiB0Y36rDaE58yscvZNidTEZ5y4Qv40K3zW5bE16jN8eQfxGDjHrTtEPtWTXe3oj0DYDNjX0xh8xTLxnhxLoEQzEaXEG5WzmekSw4OEkmj3peb6iqzYq4r7Le71eAbY6tEtlwQUWzqiHHKlLEmtEOgEL1WBXelSwDHEaQjnseqzic0YX6rdUe4aeD9ElcYZUElTwLgWcPi0YNYb1YM3iB9i8Tihtj0YOYHkwAdJaGydHwQSJA6j9tv4BvBYfYlMR8gJ9cvFmWBoWp4EhGyMtETLR1cyzAvXSW54whYgYUtjcNYSmJU3WZQvBZEn7RbdEmBYHsvQQx3gYUmvcdEbNyBqrUYTY8dRBSJT3vf9WPFWT6EDow1tEdsy91iqnvBlEz9YSY7YBqjUtwSkvdm; _bfa=1.1590046473942.3xqvpu.1.1590046473942.1590046473942.1.13; _bfs=1.13; hotelhst=2012709687'.format(
                           magicid)}
            data = {
                '__VIEWSTATEGENERATOR': 'DB1FBB6D',
                'cityName': '%E4%B8%8A%E6%B5%B7',
                'StartTime': '2020-05-18',
                'DepTime': '2020-05-19',
                'RoomGuestCount': '1,1,0',
                'txtkeyword': '',
                'Resource': '',
                'Room': '',
                'Paymentterm': '',
                'BRev': '',
                'Minstate': '',
                'PromoteType': '',
                'PromoteDate': '',
                'operationtype': 'NEWHOTELORDER',
                'PromoteStartDate': '',
                'PromoteEndDate': '',
                'OrderID': '',
                'RoomNum': '',
                'IsOnlyAirHotel': 'F',
                'cityId': '2',
                'cityPY': 'shanghai',
                'cityCode': '021',
                'cityLat': '31.2363508011',
                'cityLng': '121.4802384079',
                'positionArea': '',
                'positionId': '',
                'hotelposition': '',
                'keyword': '',
                'hotelId': '',
                'htlPageView': '0',
                'hotelType': 'F',
                'hasPKGHotel': 'F',
                'requestTravelMoney': 'F',
                'isusergiftcard': 'F',
                'useFG': 'F',
                'HotelEquipment': '',
                'priceRange': '-2',
                'hotelBrandId': '',
                'promotion': 'F',
                'prepay': 'F',
                'IsCanReserve': 'F',
                'OrderBy': '99',
                'OrderType': '',
                'k1': '',
                'k2': '',
                'CorpPayType': '',
                'viewType': '',
                'checkIn': '2020-05-18',
                'checkOut': '2020-05-19',
                'DealSale': '',
                'ulogin': '',
                'hidTestLat': '0%7C0',
                'AllHotelIds': '',
                'psid': '',
                'isfromlist': 'T',
                'ubt_price_key': 'htl_search_noresult_promotion',
                'showwindow': '',
                'defaultcoupon': '',
                'isHuaZhu': 'False',
                'hotelPriceLow': '',
                'unBookHotelTraceCode': '',
                'showTipFlg': '',
                'traceAdContextId': '',
                'allianceid': '0',
                'sid': '0',
                'pyramidHotels': '',
                'hotelIds': '',
                'markType': '0',
                'page': '1',
                'zone': '',
                'location': '',
                'type': '',
                'brand': '',
                'group': '',
                'feature': '',
                'equip': '',
                'bed': '',
                'breakfast': '',
                'other': '',
                'star': '',
                'sl': '',
                's': '',
                'l': '',
                'price': '',
                'a': '0',
                'keywordLat': '',
                'keywordLon': '',
                'contrast': '0',
                'PaymentType': '',
                'CtripService': '',
                'promotionf': '',
                'allpoint': '',
                'page_id_forlog': '102032',
                'contyped': '0',
                'productcode': '',
                'eleven': eleven
            }
            async with session.post(url, timeout=30, headers=headers, data=data) as res:
                text = await res.text()
                print(text)

    async def _oceanball(self):
        '''
        : 获取加密eleven的resposne，url为加密
        :param:
        :return:
        '''
        cas_code = return_cascode()
        url = 'https://hotels.ctrip.com/domestic/cas/oceanball?callback={0}&_={1}'.format(cas_code, int(
            round(time.time() * 1000)))
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=30, headers=self.headers) as res:
                magicid = str(res.cookies)
                pat = re.compile(r'magicid=(.*?);')
                magicid = pat.findall(magicid)[0] if pat.findall(magicid) else ValueError
                text = await res.text()
                diff_flag = None
                if '_unknown_' in text:
                    diff_flag = '_unknown_'
                elif '_bot_' in text:
                    diff_flag = '_bot_'
                elif '_human_' in text:
                    diff_flag = '_human_'
                if diff_flag and magicid is not ValueError:
                    return (return_oceanjs(text, diff_flag), magicid,)

                # mycollection.update_one({'id': 1}, {'$set': {'js': encrypted_str, 'id': 1}})


if __name__ == '__main__':
    c = Crip_travel()
    asyncio.get_event_loop().run_until_complete(c._oceanball(1))
