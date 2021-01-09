"""

_|          _|  _|      _|  _|      _|  @Time : 2020.12.1 16:32
_|          _|    _|  _|      _|  _|    @Auth : Wang Xiangyu
_|    _|    _|      _|          _|      @File : baiduapi
  _|  _|  _|      _|  _|        _|      @IDE : PyCharm
    _|  _|      _|      _|      _|      @CODING : utf-8

"""

# apikey = 3s9UyhqzfBKf4uPh8cimvlYY
# secert key = rgUAdnuTIFjY1FxbRxMHL3Xv758rIEyO
# encoding:utf-8
import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=3s9UyhqzfBKf4uPh8cimvlYY&client_secret=rgUAdnuTIFjY1FxbRxMHL3Xv758rIEyO'
response = requests.get(host)
if response:
    print(response.json()['access_token'])

'''

{'refresh_token': '25.713e729c35ad3ce8ab7bedd00aaef694.315360000.1922172341.282335-23076233', 'expires_in': 2592000,
 'session_key': '9mzdX+3hD3O87sIocFMX2q+yhRWhnXnkWYtxEcnMR23y/ynRMIf7dBYf22HxLH1FYc4YGz8hk0F25JFPw6RpGNXVgYetog==',
 'access_token': '24.d75647247f587dd589a31765ded67223.2592000.1609404341.282335-23076233',
 'scope': 'public brain_all_scope easydl_mgr easydl_retail_mgr ai_custom_retail_image_stitch ai_custom_test_oversea easydl_pro_mgr wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test权限 vis-classify_flower lpq_开放 cop_helloScope ApsMis_fangdi_permission smartapp_snsapi_base smartapp_mapp_dev_manage iop_autocar oauth_tp_app smartapp_smart_game_openapi oauth_sessionkey smartapp_swanid_verify smartapp_opensource_openapi smartapp_opensource_recapi fake_face_detect_开放Scope vis-ocr_虚拟人物助理 idl-video_虚拟人物助理 smartapp_component smartapp_cserver_meta',
 'session_secret': 'edaccc67987f57027df6ced923a95e12'}

'''
