version=$1

if [ -z $version ]; then
   echo "The version Error"
   exit 1
fi

curl -O "https://rd4.alpha5d777.com//APP/AndroidStore/$version/eg.apk"

adb uninstall "com.GanguTech.Invincible" 
adb install ./eg.apk 
adb shell am start -n com.GanguTech.Invincible/com.unity3d.player.UnityPlayerActivity

rm ./eg.apk

echo 'run airtest'
python3.11 -m airtest run ./Root.air --device Android:///emulator-5554 --log log/

echo 'export the report'
python3.11 -m airtest report ./Root.air --log_root log/ --lang zh-TW --export export

adb shell am force-stop "com.GanguTech.Invincible" 
#python3 -m process.py -version "$version" -ftp_server '113.196.184.128' -ftp_username publish -ftp_password Qq111111 -upload_dir './export' -tg_token "7254965254:AAFxg1J_ffWJqMFcPxYnfaZ8s5DLSArreyw" -tg_chat_id -4563830402 -build_result $BUILD_RESULT
