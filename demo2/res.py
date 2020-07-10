# coding:utf-8


import frida, sys


def on_message(message, data):
    '''
    接收下面js代码中调用send函数后输出的日志
    :param message:
    :param data:
    :return:
    '''
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


# with open('demo.js') as f:
#     jscode = f.read()

jscode = """
Java.perform(function () {

    var MainActivity = Java.use('d.f');
    
    send('====')

    MainActivity.a.implementation = function (x, y) {
        
        send('hook onClick start ...');

        this.a(x, y);

        send('hook end !!!');

    };
});
"""

# 获取指定app现在运行的进程, 参数是 包名
process = frida.get_usb_device().attach('com.loco.example.OkHttp3SSLPinning')
script = process.create_script(jscode)
script.on('message', on_message)

print('[*] Running CTF')

# 将js代码注入进去
script.load()

sys.stdin.read()
