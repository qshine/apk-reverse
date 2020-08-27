Java.perform(function () {
    var MainActivity = Java.use('com.yaotong.crackme.MainActivity');
    
    MainActivity.securityCheck.overload(
        'java.lang.String'
    ).implementation = function (str) {
        console.log(str)
        return true
    };
});