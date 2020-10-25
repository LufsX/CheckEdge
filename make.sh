curl -s https://www.microsoft.com/zh-cn/edge/business/download | grep -o 'data-whole-json=".*">' | sed "s|&quot;|\"|g" | sed "s|data-whole-json=\"||g" | sed "s|\">||g" | jq >1.json
