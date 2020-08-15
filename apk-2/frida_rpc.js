function callDYFun(url) {
    var result = null;
    Java.perform(function () {
        var ins = Java.use('com.ss.sys.ces.gg.tt$1').$new();

        var jsonObj = Java.use('org.json.JSONObject');
        var strClass = Java.use("java.lang.String");
        var map = Java.use("java.util.HashMap").$new();        
        
        var res = jsonObj.$new(ins.$new().a(url, map));

        console.log("url -> ", url)
        console.log("res -> ", strClass.valueOf(res))
        
        result = strClass.valueOf(res);
    });
    return result;
}

rpc.exports = {
    callsecretfunctionedy: callDYFun,
};