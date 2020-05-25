import execjs, re

js1 = '''
function e(e) {
    var t = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"], a = "CAS", o = 0
    for (; o < e; o++) {
        var i = Math.ceil(51 * Math.random()); a += t[i]
    }
    return a
}
function getCallback() {
    return e(15);

}
'''


def return_cascode():
    return execjs.compile(js1).call('getCallback')  # call方法传入调用的方法名称、参数1、参数2


def return_oceanjs(a_str: str, diff: str):
    '''
    :param a_str: response.text 加密后js
    :param diff:  加密js判断特征
    :return:
    '''
    pat = re.compile(r',i={0}(.*?)\(h\);'.format(diff))
    b = pat.findall(a_str)
    pat1 = 'i={1}{0}(h);'.format(b[0], diff)
    # print(pat1)
    b = a_str.rfind(pat1)
    c1 = a_str[:b]
    c2 = a_str[b:]
    c3 = c2.replace(pat1, pat1 + '''                        if (e == 5698 || e == 5706) {
                            g = [function (e) {
                                var a = "";
                                i = !0;
                                try {
                                    a = e()
                                } catch (o) {
                                    $.ajax("/domestic/cas/image/bi", {
                                        method: $.AJAX_METHOD_POST,
                                        cache: !1,
                                        context: {value: "11-" + encodeURIComponent(o.stack || o)}
                                    })
                                } finally {
                                    try{t(a);}catch (e) {
                                        1
                                    }finally {
                                        1
                                    }
                                }
                            }];
                        };
                        if (e==77){console.log('777777777777777',g,window.p=g)};
                        console.log(e, '=', i, '=', h._unknown_d4dfa, '=', '_unknown_b98ba', '=', g,'=',window.p);''')
    result = c1 + c3
    return result
