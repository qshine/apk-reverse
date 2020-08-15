import frida

from flask import Flask, jsonify, request


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

with open('frida_rpc.js') as f:
    jscode = f.read()


session = frida.get_usb_device().attach('com.ss.android.ugc.aweme')
script = session.create_script(jscode)
script.on('message', on_message)
script.load()


app = Flask(__name__)


@app.route('/test')
def hello_world():
    args = request.args['url_path']
    res = script.exports.callsecretfunctioneleme(args)
    return jsonify(res)


@app.route('/dy')
def dy_test():
    #浏览器访问不建议用get，会进行urlencode
    url = 'https://aweme-hl.snssdk.com/aweme/v2/comment/list/?aweme_id=6861027918886325507&cursor=0&count=20&address_book_access=2&gps_access=1&forward_page_type=1&os_api=23&device_type=Nexus%206P&device_platform=android&ssmix=a&iid=1319012797003741&manifest_version_code=670&dpi=560&js_sdk_version=1.16.3.5&uuid=867686020581318&version_code=670&app_name=aweme&version_name=6.7.0&ts=1597512806&openudid=848d1fd3a4902e98&device_id=2550465705552974&resolution=1440*2392&os_version=6.0.1&language=zh&device_brand=google&app_type=normal&ac=wifi&update_version_code=6702&aid=1128&channel=tengxun_new&_rticket=1597512810432'
    # url = request.args['url'] #
    res = script.exports.callsecretfunctionedy(url)
    return res


if __name__ == '__main__':
    app.run()