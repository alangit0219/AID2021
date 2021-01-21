"""
编写接口函数，从终端输入端口名称获取端口运行状态中的地址值

思路分析：
1. 根据输入的端口名称找到对应的段落
2. 在该段落中匹配address
"""

import re

def get_address(port):
    f = open('exc.txt')
    while True:
        data = ''
        for line in f:
            if line =='\n':
                break
            data += line
        #data為空說明到了文檔結尾
        if not data:
            break

        obj = re.match(port,data)   #匹配開始位置
        if obj:
            pattern = r"(\d{1,3}\.){3}\d{1,3}/\d+|Unknown"
            obj = re.search(pattern,data)
            return obj.group()
    return "沒有該端口"


if __name__ =='__main__':
    port = input("端口:")
    print(get_address(port))