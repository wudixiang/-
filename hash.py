import binascii

def myhash(x):
    str_16 = binascii.b2a_hex(x.encode('utf-8'))  # 字符串转16进制
    print('哈希值为：',str_16)
