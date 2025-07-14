version=$1
package_name=com.wudiking.wd_dev
activity_name=com.unity3d.player.UnityPlayerActivity

if [ -z $version ]; then
   echo "The version Error"
   exit 1
fi

# curl -O "https://rd1.alpha5d777.com/wdk/rd/app/android/$version/eg.apk"
#
adb uninstall "$package_name"
adb install ./eg.apk
adb shell am start -n $package_name/$activity_name

# rm ./eg.apk

echo 'run airtest'
# python3.11 -m airtest run ./Root.air --device Android:///emulator-5554 --log log/

echo 'export the report'
# python3.11 -m airtest report ./Root.air --log_root log/ --lang zh-TW --export export

# adb shell am force-stop "$package_name"
#python3 -m process.py -version "$version" -ftp_server '113.196.184.128' -ftp_username publish -ftp_password Qq111111 -upload_dir './export' -tg_token "7254965254:AAFxg1J_ffWJqMFcPxYnfaZ8s5DLSArreyw" -tg_chat_id -4563830402 -build_result $BUILD_RESULT
