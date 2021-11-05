import json
jsonFalse= '{"app_version": "1.3", "channel": "1", "sign": "716bfdd9a802e6a43f337b8c9856de50", "appversion": "1.3",; "uuid": "6fb8e21c-1be1-3c8c-8820-fa874ccb44bc", "version": "1.0", "pkg_name": "com.neutron.thaimoney",; "self_mobile": "017629047816", "account_id": "017629047816", "user_id": "2202110191609493512675",; "record": [{"last_time": "1630894000616", "other_mobile": "16675190404", "other_name": "Jack"},; {"last_time": "1635659335375", "other_mobile": "13728687014", "other_name": "Jimmy"}],; "imei": "6fb8e21c-1be1-3c8c-8820-fa874ccb44bc", "timestamp": "1636076179063"}'

jsonTrue='{"user_id":"2202110191609493512675","uuid":"ab859b90-3d54-11ec-9d61-ff9b4f64c258","self_mobile":"017629047816","account_id":"017629047816","record":[{"other_name":"Jack","other_mobile":"16675190404","last_time":"0"},{"other_name":"Jimmy","other_mobile":"137 2868 7014","last_time":"0"}],"app_version":"1.0.0","appversion":"1.0.0","version":"1.0","channel":"1","imei":"ab859b90-3d54-11ec-9d61-ff9b4f64c258","timestamp":"1636076560010","pkg_name":"com.neutron.richmoney","sign":"test"}'



{"app_version":"1.3","channel":"1","sign":"127c15f2611b09fbdeabaafdffc9cc23",
 "appversion":"1.3","uuid":"6fb8e21c-1be1-3c8c-8820-fa874ccb44bc","version":"1.0",
 "pkg_name":"com.neutron.thaimoney","self_mobile":"017629047816","account_id":"017629047816",
 "user_id":"2202110191609493512675","record":[{"last_time":"1630894000616","other_mobile":
    "16675190404","other_name":"Jack"},{"last_time":"1635659335375","other_mobile":
    "13728687014","other_name":"Jimmy"}],"imei":"6fb8e21c-1be1-3c8c-8820-fa874ccb44bc","timestamp":"1636077729734"}

{"user_id":"2202110191609493512675","uuid":"ab859b90-3d54-11ec-9d61-ff9b4f64c258",
 "self_mobile":"017629047816","account_id":"017629047816",
 "record":[{"other_name":"Jack","other_mobile":"16675190404","last_time":"0"},{"other_name":"Jimmy","other_mobile":"137 2868 7014","last_time":"0"}]
    ,"app_version":"1.0.0","appversion":"1.0.0","version":"1.0","channel":"1",
 "imei":"ab859b90-3d54-11ec-9d61-ff9b4f64c258","timestamp":"1636076560010",
 "pkg_name":"com.neutron.richmoney","sign":"test"}





dict = json.loads(s=jsonTrue)
dict2 = json.loads(s=jsonFalse)

for i in dict.keys():
    if i in dict2 == False:
        print("不存在 key " + i)

    else :
        print("取值比对 dict  "+i+"   "+str(dict[i])+"  --  "+str(dict2[i]) )
        if str(dict2[i])=="" or str(dict2[i])=="null":
            print("========= 缺少數據  "+i+"  "+str(dict2[i]))
