该apk为阿里测试程序

### 直接通过命令行执行
```sh
frida -U --no-pause com.yaotong.crackme -l hook_java.js
```

### 通过py脚本执行
```
python hook_java.py
```

### hook启动时的onCreate方法
```
python hook_oncreate.py
```

### hook native方法
```
python hook_native.py
```


### 拿出so文件
```
apktool d AliCrackme.apk
```