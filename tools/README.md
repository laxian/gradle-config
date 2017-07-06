# global gradle config
流程：
1. 读取settings.gradle, 读取各个module,遍历各个module目录下的build.gradle,匹配dependencies下的远程gradle依赖
将其写入config.gradle
如果module是application，读取其android block下的
compileSdkVersion、buildToolsVersion、applicationId、minSdkVersion、targetSdkVersion、versionCode、versionName
将其写入config.gradle
2. 在project 的build.gradle 最后追加：apply from: 'config.gradle'
3. 遍历各个module，将其第一步骤中写入config.gradle 的相关项替换成config.gradle中对应的值


用法：

`./config.py your_android_project_root_path`

[效果预览](https://github.com/laxian/gradle-config/tree/master/01_gradle_custom_property)
