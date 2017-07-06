import sys

project_root = sys.path[0]

if sys.argv[1] is not None:
    project_root = sys.argv[1]

config_gradle = r"config.gradle"
build_gradle = "build.gradle"
android_rex = r"\s*android\s*=\s*\[.*?\]"

dependency_pattern = r"\s*((?:(?:\w+C)|c)ompile)" \
                     r" *(?P<right>\(?'(?P<compony>(?:\w+\.)*\w+):" \
                     r"(?P<lib>[\w-]+):" \
                     r"(?P<ver>(?:\d+\.)*\d+)'\)?\s*)\n"

android_pattern = r"\s*" \
                  r"(?P<key>compileSdkVersion|buildToolsVersion|applicationId|minSdkVersion|" \
                  r"targetSdkVersion|versionCode|versionName)\s+(?P<value>[0-9a-zA-Z\.\"']+)"


replace_android = "rootProject.ext.android.%s"
replace_dependencies = "rootProject.ext.dependencies['%s']"


apply_from_config = "apply from: 'config.gradle'"

settings_gradle = r"settings.gradle"
module_pattern = r"':([\w-]+)'"