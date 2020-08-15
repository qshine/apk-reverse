Java.perform(function () {
    var ins = Java.use('com.ss.sys.ces.gg.tt$1').$new();
    var strClass = Java.use("java.lang.String");

    var url = 'https://aweme-hl.snssdk.com/aweme/v2/comment/list/?aweme_id=6859265638045748487&cursor=0&count=20&address_book_access=2&gps_access=1&forward_page_type=1&os_api=23&device_type=Nexus%206P&device_platform=android&ssmix=a&iid=1319012797003741&manifest_version_code=670&dpi=560&js_sdk_version=1.16.3.5&uuid=867686020581318&version_code=670&app_name=aweme&version_name=6.7.0&ts=1597510237&openudid=848d1fd3a4902e98&device_id=2550465705552974&resolution=1440*2392&os_version=6.0.1&language=zh&device_brand=google&app_type=normal&ac=wifi&update_version_code=6702&aid=1128&channel=tengxun_new&_rticket=1597510239678'

    var map = Java.use('java.util.HashMap').$new()
    var res = ins.a(url, map)

    console.log("url -> ", url)
    console.log("res -> ", strClass.valueOf(res))

});