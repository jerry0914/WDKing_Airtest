test_vers=$1
result=$2

if [ -z $test_vers ]; then
   echo "The version is Error"
   exit 1
fi

echo test_vers=$test_vers
echo result=$result

python3 -m process -version "$test_vers" -ftp_server '113.196.184.128' -ftp_username publish -ftp_password Qq111111 -upload_dir './export' -tg_token "7254965254:AAFxg1J_ffWJqMFcPxYnfaZ8s5DLSArreyw" -tg_chat_id -4563830402 -result $result
