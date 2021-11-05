import requests        #导入requests包
#
# # desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# # mobile user-agent
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
#
apps=["com.neutron.goldpay","com.neutron.pay","com.neutron.deloan","com.neutron.creditline","com.twentythree.extrarich"]
# # apps=["com.cashloan.timelyhelp", "com.jhfokcash.online", "com.jducas.hwellloan", "com.cas.hutydmog", "com.macalash.ikredit", "com.oncred.luckcas", "com.satisfy.stabilized", "com.goodloa.nblyds", "com.kotcalinsh.sixvest", "com.greatloann.zoigent", "com.easy.smiling", "com.rainbow.kasnkla", "com.live.forever.online", "com.mexi.mitomi", "com.de.bath", "com.aouceler.thb", "com.twentythree.extrarich", "com.louapn.sweet", "com.large.lljholsghj", "com.sabaidee.lowallet", "com.lebronjames.zhangchao", "com.soom.money", "com.neutron.goldpay", "com.neutron.pay", "com.furnish.veryrich", "com.dwyanewade.lightning", "com.neutron.deloan", "com.large.money.credit", "com.sorich.asgaghoie", "com.xxlyu.borrownow", "com.neutron.creditline", "com.lucky.a71loan"]
#
#
#
success = []
error = []
print("开始检测APP是否被下架..")
for uri in apps:
 URL = f"https://play.google.com/store/apps/details?id="+uri
 headers = {"user-agent": USER_AGENT}
 print("当前APP: "+uri)
 resp = requests.get(URL, headers=headers)
 if resp.text.find("sorry")==-1:
     success.append(uri)
 else :
     error.append(uri)
print("检测完毕，结果如下：")
print("正常APP ：")
print(success)
print("\n")
print("异常APP ：")
print(error)


# import requests        #导入requests包
#
# # desktop user-agent
# USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# # mobile user-agent
# MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
#
# # apps=["com.neutron.goldpay","com.neutron.pay","com.neutron.deloan"]
#
# URL = f"https://docs.qq.com/sheet/DSlVyeGZWWGtIQkpY?tab=BB08J2&_t=1626397892108"
#
# headers = {"user-agent": USER_AGENT}
#
# resp = requests.get(URL, headers=headers)
#
# print(resp.text)


##  2021年9月10日 异常APP ：  ['com.jhfokcash.online', 'com.jducas.hwellloan', 'com.goodloa.nblyds', 'com.kotcalinsh.sixvest', 'com.rainbow.kasnkla', 'com.live.forever.online', 'com.soom.money', 'com.neutron.goldpay', 'com.dwyanewade.lightning', 'com.large.money.credit', 'com.sorich.asgaghoie', 'com.xxlyu.borrownow', 'com.neutron.creditline', 'com.lucky.a71loan']



# with open("C:\\Users\\tunne\\Desktop\\66Loan描述.txt",  "r", encoding="utf-8") as f:
#     data = f.readlines()
#
# for item in data:
#     if data.index(item) % 2 != 0:
#         print(item,end="")


