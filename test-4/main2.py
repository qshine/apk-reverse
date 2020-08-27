import frida, sys


# 接受下面js代码中send出来的内容, 也可以在js中直接用consule.log
def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


jscode = """
Java.perform(function () {
    var MainActivity = Java.use('com.yaotong.crackme.MainActivity');
    
    MainActivity.onCreate.overload('android.os.Bundle').implementation = function (v) {
        console.log(v);
        // 输出证明成功hook住了该方法
        console.log('now is in onCreate ...')
        this.onCreate(v);
    };
});
"""

# app也必须先启动
device = frida.get_usb_device()
# 找到进程号
pid = device.spawn(['com.yaotong.crackme'])

print(pid)

# attach到进程号
process = device.attach(pid)
script = process.create_script(jscode)
script.on('message', on_message)
print('[*] Running CTF')
script.load()

# 直接重启程序, 重启阶段就能hook到onCreate方法
device.resume(pid)

# 输出日志
sys.stdin.read()

