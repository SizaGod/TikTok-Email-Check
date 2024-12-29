email = input("Enter Your Email : ")
import os
try:
  import requests
  import random
  import time,secrets,binascii,os,uuid
  from urllib.parse import urlencode
  from MedoSigner import Argus,Gorgon, md5,Ladon

except:
    os.system("pip install requests uuid MedoSigner pycryptodome")
    
import requests
import random
import time,secrets,binascii,os,uuid
from urllib.parse import urlencode
from MedoSigner import Argus,Gorgon, md5,Ladon    
 
def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 567753, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int =2, platform: int = 19, unix: int = None):
        x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload != None else None
        data=payload
        if not unix: unix = int(time.time())
        return Gorgon(params, unix, payload, cookie).get_value() | { "x-ladon"   : Ladon.encrypt(unix, license_id, aid),"x-argus"   : Argus.get_sign(params, x_ss_stub, unix,platform        = platform,aid             = aid,license_id      = license_id,sec_device_id   = sec_device_id,sdk_version     = sdk_version_str, sdk_version_int = sdk_version)}
        
secret = secrets.token_hex(16)        
tim = str(round(random.uniform(1.2, 1.6) * 100000000) * -1)
timr = str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632"
cc = str(uuid.uuid4())
op = str(binascii.hexlify(os.urandom(8)).decode())       
iid = str(random.randint(1, 10**19))
dev = str(random.randint(1, 10**19)) 
data = {
    'account_sdk_source': 'app',
    'multi_login': '1',
    'email': email,
    'mix_mode': '1'
}
cookies = {
    'passport_csrf_token': secret,
    'passport_csrf_token_default': secret,
}
m=sign(params='passport-sdk-version=19&iid='+iid+'&device_id='+dev+'&ac=mobile&channel=googleplay&aid=567753&app_name=tiktok_studio&version_code=320905&version_name=32.9.5&device_platform=android&os=android&ab_version=32.9.5&ssmix=a&device_type=Redmi%20Note%208%20Pro&device_brand=Redmi&language=ar&os_api=30&os_version=11&openudid='+op+'&manifest_version_code=320905&resolution=1080*2220&dpi=440&update_version_code=320905&_rticket='+timr+'&is_pad=0&app_type=normal&sys_region=EG&mcc_mnc=42103&timezone_name=Asia/Aden&app_language=ar&carrier_region=YE&ac2=lte&uoo=1&op_region=YE&timezone_offset=10800&build_number=32.9.5&host_abi=arm64-v8a&locale=ar&region=EG&ts='+tim+'&cdid='+cc+'&support_webview=1&cronet_version=5828ea06_2024-03-28&ttnet_version=4.2.137.58-tiktok&use_store_region_cookie=1',payload=urlencode(data),cookie=urlencode(cookies))

headers = {
'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'com.ss.android.tt.creator/320905 (Linux; U; Android 11; ar_EG; Redmi Note 8 Pro; Build/RP1A.200720.011; Cronet/TTNetVersion:5828ea06 2024-03-28 QuicVersion:68c84b0f 2024-02-29)','x-argus': m["x-argus"],
          'x-gorgon': m["x-gorgon"],
          'x-khronos': m["x-khronos"],
          'x-ladon': m["x-ladon"],}
response = requests.post(
    'https://api16-normal-no1a.tiktokv.eu/passport/user/check_email_registered?passport-sdk-version=19&iid='+iid+'&device_id='+dev+'&ac=mobile&channel=googleplay&aid=567753&app_name=tiktok_studio&version_code=320905&version_name=32.9.5&device_platform=android&os=android&ab_version=32.9.5&ssmix=a&device_type=Redmi%20Note%208%20Pro&device_brand=Redmi&language=ar&os_api=30&os_version=11&openudid='+op+'&manifest_version_code=320905&resolution=1080*2220&dpi=440&update_version_code=320905&_rticket='+timr+'&is_pad=0&app_type=normal&sys_region=EG&mcc_mnc=42103&timezone_name=Asia/Aden&app_language=ar&carrier_region=YE&ac2=lte&uoo=1&op_region=YE&timezone_offset=10800&build_number=32.9.5&host_abi=arm64-v8a&locale=ar&region=EG&ts='+tim+'&cdid='+cc+'&support_webview=1&cronet_version=5828ea06_2024-03-28&ttnet_version=4.2.137.58-tiktok&use_store_region_cookie=1',
    cookies=cookies,
    headers=headers,
    data=data,
)
print(response.text)
