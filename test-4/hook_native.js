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