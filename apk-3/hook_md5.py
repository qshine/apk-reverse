# coding:utf-8


import frida, sys


def on_message(message, data):
    '''
    接收下面js代码中调用send函数后输出的日志
    :param message:
    :param data:
    :return:
    '''
    print(message)
    print(data)
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


jscode = """
// 打印堆栈
function printStack(){
    console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()))
}

// array 转 string
function array2string(array) {  
    var buffer = Java.array('byte', array);
    var result = "";
    // console.log(buffer.length)
    for(var i=0; i < buffer.length; ++i){
        result += (String.fromCharCode(buffer[i]));
    }
    return result;
}


Java.perform(function () {
    // 打印 md5 的入参
    var MessageDigest = Java.use('java.security.MessageDigest');

    MessageDigest.update.overload('[B').implementation = function (bytesarray) {
        console.log("origin: "+array2string(bytesarray));
        // 打印堆栈信息
        printStack(); 
        this.update(bytesarray);
    };

    MessageDigest.update.overload('byte').implementation = function (bytesarray) {
        console.log("origin: "+array2string(bytesarray))
        this.update(bytesarray)
    };

    MessageDigest.update.overload('java.nio.ByteBuffer').implementation = function (bytesarray) {
        console.log("origin: "+array2string(bytesarray))
        this.update(bytesarray)
    };

});
"""

# 获取指定app现在运行的进程, 参数是 包名
process = frida.get_usb_device().attach('com.iCitySuzhou.suzhou001')
script = process.create_script(jscode)
script.on('message', on_message)

print('[*] Running CTF')

# 将js代码注入进去
script.load()

sys.stdin.read()
