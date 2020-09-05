Java.perform(function () {
    var MainActivity = Java.use('com.yaotong.crackme.MainActivity');
    
    MainActivity.securityCheck.overload(
        'java.lang.String'
    ).implementation = function (str) {
        console.log(str)
        // 直接在此处更改返回值为true来通过校验
        return true
    };
});