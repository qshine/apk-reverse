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


jscode = """
// perform是为了确保当前线程已连接到VM用的
Java.perform(function () {

    // Function to hook is defined here(Java.use是为了获取一个指向某个类的指针, 这个类就是要hook的类)
    var MainActivity = Java.use('com.droider.crackme0201.MainActivity');

    // Whenever button is clicked(hook MainActivity 中的 onClick方法吗, 参数要对应原函数中的参数)
    MainActivity.checkSN.implementation = function (x, y) {
        
        // Show a message to know that the function got called(输出日志)
        send('hook onClick start ...');

        console.log(x)
        console.log(y)
        console.log("=====")

        send('hook end !!!');

        return true
    };
});
"""

# 获取指定app现在运行的进程, 参数是 包名
process = frida.get_usb_device().attach('com.droider.crackme0201')
script = process.create_script(jscode)
script.on('message', on_message)

print('[*] Running CTF')

# 将js代码注入进去
script.load()

sys.stdin.read()
