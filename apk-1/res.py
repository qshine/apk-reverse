import frida, sys


# 接受下面js代码中send出来的内容, 也可以在js中直接用consule.log
def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


with open('hook.js') as f:
    jscode = f.read()

# 获取指定app当前运行的进程
process = frida.get_usb_device().attach('com.smzdm.client.android')
# 注入js代码
script = process.create_script(jscode)
script.on('message', on_message)
print('[*] Running CTF')
script.load()

# 输出日志
sys.stdin.read()