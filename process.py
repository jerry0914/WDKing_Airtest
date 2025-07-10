
import requests 
import ftplib
import os
import logging
import sys


if( len(sys.argv ) == 1 ):
    sys.exit(0)

#預設值
uploadFolder = './airtest/export'
ftp_server = '172.31.129.22'
ftp_username = 'publish'
ftp_password = 'Qq111111'
ftp_remote_folder = 'Airtest'

for i in range(1,len(sys.argv)):
    if( sys.argv[i] == "-version" ):
        version = sys.argv[i+1]
    if( sys.argv[i] == "-ftp_server" ):
        ftp_server = sys.argv[i+1]
    if( sys.argv[i] == "-ftp_username" ):
        ftp_username = sys.argv[i+1]
    if( sys.argv[i] == "-ftp_password" ):
        ftp_password = sys.argv[i+1]
    if( sys.argv[i] == "-upload_dir" ):
        uploadFolder = sys.argv[i+1]
    if( sys.argv[i] == "-tg_token" ):
        token = sys.argv[i+1]
    if( sys.argv[i] == "-tg_chat_id" ):
        _chat_id_to_group = sys.argv[i+1]


#logging.info('build result：' + build_result )

open_url = 'https://rd1.alpha5d777.com/Airtest/' + version + "/log.html"

#正常頻道
token = "7392888956:AAHfVl52OW-k8R7gAndS5UIcht9mTHaGNUk"
_chat_id_to_group = -4288190230

logging.basicConfig(level=logging.DEBUG)
logging.info("version = " + version)
logging.info("ftp_server = " + ftp_server)
logging.info("ftp_username = " + ftp_username)
logging.info("upload_dir = " + uploadFolder)
logging.info("tg_token = " + token)
logging.info("tg_chat_id = " + str(_chat_id_to_group))

def SendMessageToTG( token, _chat_id_to_group, text ):
    method = "sendMessage"
    
    response = requests.post(
        url=f'https://api.telegram.org/bot{token}/{method}',
        data={
            'chat_id': _chat_id_to_group,
            'text': text,
#            'parse_mode': 'HTML'  # Ensuring HTML parsing mode
        }
    ).json()



def startUpload(server, username, password, path, targetDir):
    print('上傳資料夾：' + path + " 到 " + server + "/" + targetDir)
    targetFtp = ftplib.FTP(server, username, password)
    
    try:
        targetFtp.cwd(targetDir)  # 切換到指定的遠端資料夾
    except ftplib.error_perm:
        targetFtp.mkd(targetDir)  # 如果資料夾不存在，則建立資料夾
        targetFtp.cwd(targetDir)  # 切換到新建立的資料夾

    uploadFolder(targetFtp, path)
    targetFtp.quit()  # 結束FTP連線


def uploadFolder(targetFtp, path):
    files = os.listdir(path)
    os.chdir(path)


    log_message = '上傳中...' + path
    print(log_message)


    for f in files:
        local_path = os.path.join(path, f)
        if os.path.isfile(local_path):
            with open(f, 'rb') as fh:
                targetFtp.storbinary('STOR %s' % f, fh)
        elif os.path.isdir(local_path):
            try:
                targetFtp.mkd(f)  # 嘗試建立遠端資料夾
            except ftplib.error_perm:
                pass  # 如果資料夾已存在，忽略錯誤
            targetFtp.cwd(f)
            uploadFolder(targetFtp, local_path)
            targetFtp.cwd('..')  # 返回上層目錄

    os.chdir('..')



# Upload the file to the FTP server
# 取得目前工作目錄
current_path = os.getcwd()

# 印出目前工作目錄
print("目前工作目錄:", current_path)
# Upload the file to the FTP server
startUpload(ftp_server, ftp_username, ftp_password, current_path + "/export/Root.log", ftp_remote_folder + "/" + version)

# Prepare the message to send
text = "版本：" + version + "\nAirtst執行完畢，請檢視測試資訊: " + open_url
SendMessageToTG(token, _chat_id_to_group, text)



