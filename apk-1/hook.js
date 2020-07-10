// sign

Java.perform(function () {
    var MainActivity = Java.use('d.g.b.a.n.a.a');
    
    MainActivity.a.overload(
        'java.util.Map',
        'java.lang.String'
    ).implementation = function (map,str) {

        console.log(1111);
        console.log(map)    // 参数
        console.log(str)    // http method

        var response = MainActivity.a.call(this,map,str);
        console.log(response)

        console.log(2222);
        return response
    };


    var MainActivity1 = Java.use('com.smzdm.client.base.utils.Ka');
    
    MainActivity1.a.overload(
        'java.lang.String'
    ).implementation = function (str) {

        console.log(3333);
        console.log(str)    

        var response = MainActivity1.a.call(this,str);
        console.log("sign: " + response)

        console.log(4444);
        return response
    };
});