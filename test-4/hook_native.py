import frida, sys


# 接受下面js代码中send出来的内容, 也可以在js中直接用consule.log
def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


jscode = """
// 找到libc的基地址
var base_address = Module.findBaseAddress('libc.so')
console.log('base_address: ' + base_address)

// 获取dlopen函数的地址
var mod_address = Module.findExportByName('libc.so', 'dlopen')
console.log('mod_address: ' + mod_address)

// 返回module对象
var lib_module = Process.findModuleByAddress(base_address)
console.log('lib_module: ' + lib_module.name)

// 开始hook, 传入mod_address内存地址. 针对dlopen函数
Interceptor.attach(mod_address, {
    // args是dlopen函数的参数, 可能有一个或多个
    onEnter: function(args){
        console.log("open("+Memory.readUtf8String(args[0])+", "+args[1]+")")
    },
    onLeave: function(retval){
        console.log("retval: " + retval)
    }

})
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


"""
2117
[*] Running CTF
base_address: 0xb72ae000
mod_address: 0xb7778221
lib_module: libc.so
open(/data/app/com.yaotong.crackme-1/lib/arm/libcrackme.so, 0x0)
retval: 0x0
open(libc.so, 0x0)
retval: 0xb774fe5c
open(libc.so, 0x0)
retval: 0xb774fe5c
open(libz.so, 0x0)
retval: 0xb6110004
open(libc.so, 0x0)
retval: 0xb774fe5c
open(libc.so, 0x0)
retval: 0xb774fe5c
open(/system/lib/hw/gralloc.x86.so, 0x0)
retval: 0xb2fa7664
open(/system/lib/egl/libEGL_emulation.so, 0x0)
retval: 0xb2fa7e5c
open(/system/lib/egl/libGLESv1_CM_emulation.so, 0x0)
retval: 0xb26d6004
open(/system/lib/egl/libGLESv2_emulation.so, 0x0)
retval: 0xb26d619c
open(/system/lib/egl/libGLESv1_CM_emulation.so, 0x0)
retval: 0xb26d6004
open(/system/lib/egl/libGLESv2_emulation.so, 0x0)
retval: 0xb26d619c
open(/system/lib/libEGL.so, 0x0)
retval: 0xb76b17fc
open(/system/lib/libGLESv2.so, 0x0)
retval: 0xb76b1b2c
open(/system/lib/libGLESv1_CM.so, 0x0)
retval: 0xb76b1994
"""