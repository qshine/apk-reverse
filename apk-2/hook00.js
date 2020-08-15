Java.perform(function () {
    var MainActivity = Java.use('com.ss.sys.ces.gg.tt$1');

    var strClass = Java.use("java.lang.String");

    MainActivity.a.overload('java.lang.String', 'java.util.Map').implementation = function (a1, a2) {
        var res = this.a(a1, a2);

        console.log("a1 ->", a1)
        console.log("a2 ->", strClass.valueOf(a2))
        console.log("res ->", strClass.valueOf(res));

        return res;
    };
});