#-*- coding:utf-8 -*-

file_path_text = "./test_txt.txt"
file_path_binary = "./test_binary.txt"


def open_file():
    pass


def encode_text(encoding="utf-8", file_path="./test_txt.txt"):

    with open(file=file_path, mode="r", encoding=encoding) as f:
        content = f.read()

    print(content)
    return content


def encode_binary(file_path="./test_binary.txt"):

    with open(file=file_path, mode="rb") as f:
        content = f.read()

    print(content)
    return content


def decode_text(encoding="utf-8", file_path="./test_txt.txt"):

    with open(file=file_path, mode="w", encoding=encoding) as f:
        f.write("HELLO WORLD\n")
        f.write("你好，世界！")


def decode_binary(file_path="./test_binary.txt"):

    with open(file=file_path, mode="wb") as f:
        f.write("HELLO WORLD\n".encode("utf-8"))
        f.write("你好，世界！".encode("utf-8"))


if __name__ == '__main__':
    import os
    if os.path.exists(file_path_text):
        os.remove(file_path_text)
    if os.path.exists(file_path_binary):
        os.remove(file_path_binary)

# 1 测试文本模式"w"写入，文本模式 "r"读取
#   必须知道文本是什么编码形式，否则无法读取/读取错误
#   1) decode_text()
#      encode_text()
    # 文本
#   2) decode_text(encoding="GBK")
#      encode_text(encoding="GBK")
    # OK

#   3) decode_text()
#      encode_text(encoding="GBK")

    # txt: HELLO WORLD你好，世界！
    # console: HELLO WORLD浣犲ソ锛屼笘鐣岋紒

#   4) decode_text(encoding="GBK")
#      encode_text()
    # txt: HELLO WORLD��ã����磡
    # console: ERROR UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc4 in position 11: invalid continuation byte

#  结论：
#       1)
#
#
#
    # write
    # decode_text(encoding="GBK")
    decode_text(encoding="utf-8")
    decode_binary()
    # read
    content = encode_text(file_path=file_path_binary)
    print(content.encode("utf-8"))
    content = encode_binary(file_path=file_path_text)
    print(content.decode("utf-8"))
    content = encode_binary()
    print(content.decode("utf-8"))

    # print(b'\xe4\xbd\xa0'.decode("utf-8"))
    # print(b'\xc4\xe3'.decode("GBK"))