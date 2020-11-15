import json
import re
import requests

macPlayLoad = {}
macLink="https://go.microsoft.com/fwlink/?linkid=2069147&platform=Mac&Consent=0&channel=Canary"
data = re.findall('(?<=data-whole-json=").+?(?=">)', requests.get("https://www.microsoft.com/zh-cn/edge/business/download").text)[0]
clearData = re.sub('&quot;', '"', data)
jsonData = json.loads(clearData)

# 0 -> Dev
# 1 -> Beta
# 2 -> Stable
# 3 -> EdgeUpdate
# 4 -> Policy

for product in jsonData:
    channel = product['Product']
    if channel == 'Dev':
        devData = product['Releases']
    elif channel == 'Beta':
        betaData = product['Releases']
    elif channel == 'Stable':
        stableData = product['Releases']

# 0 -> Windows arm64
# 1 -> Windows x86
# 2 -> Windows x64
# 3 -> MacOS x64

print(stableData,betaData,devData,)

# windowsArm64DevLocation =
# windowsArm64DevHash =
# windowsx86DevLocation =
# windowsx86DevHash =
# windowsx64DevLocation =
# windowsx64DevHash =
# macOSDevLocation =
# macOSDevLocation =
