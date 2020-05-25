// ==UserScript==
// @name         get_eleven
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://hotels.ctrip.com/hotel/*
// @grant        none
// ==/UserScript==

(function() {
    var mess = document.getElementById("mess");
    if(window.WebSocket){
        ws = new WebSocket('ws://127.0.0.1:8014/');
        ws.onopen = function(e){
            console.log("连接服务器成功");
            ws.send(JSON.stringify({'id':'2'}));
        }
        ws.onclose = function(e){
            console.log("服务器关闭");
        }
        ws.onerror = function(){
            console.log("连接出错");
        }
        ws.onmessage = function(e){

            var data = JSON.parse(e.data);
            console.log(data);

            if (data['id']==1){data1=data['reason'];
                               magicid = data['magicid'];
                               console.log(data);
            try{g = eval(data1);}catch(e){1}finally{ws.send(JSON.stringify({'id':'3','magicid':magicid,'eleven':window.p?window.p[0]:'null'}))}};
        };
        //if(window.p){ws.send('111111111111111');};
        //return;
    };
})();