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
    var MainActivity = Java.use('com.example.seccon2015.rock_paper_scissors.MainActivity');

    // Whenever button is clicked(hook MainActivity 中的 onClick方法吗, 参数要对应原函数中的参数)
    MainActivity.onClick.implementation = function (v) {
        // Show a message to know that the function got called(输出日志)
        send('hook onClick start ...');

        // Call the original onClick handler(调用原始的 onClick 方法)
        this.onClick(v);
        
        send('hook end !!!');

        // Set our values after running the original onClick handler(更改我们要的值)
        this.m.value = 0;
        this.n.value = 1;
        this.cnt.value = 99;

        send('change the value success ...')

        // Log to the console that it's done, and we should have the flag!
        console.log('Done:' + JSON.stringify(this.cnt));
    };
});
"""

# 获取指定app现在运行的进程, 参数是 包名
process = frida.get_usb_device().attach('com.example.seccon2015.rock_paper_scissors')
script = process.create_script(jscode)
script.on('message', on_message)

print('[*] Running CTF')

# 将js代码注入进去
script.load()

sys.stdin.read()
