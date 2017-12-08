# -*- coding:utf-8 -*-


def read_txt_file():

    f = open("data.txt")

    lines = f.readlines()   # 读取全部内容 ，并以列表方式返回
    print lines

    for line in lines:  # 循环遍历行

        # 方法一：分割后存为list，然后用索引读取每一列
        a = line.split(",")
        print a
        print a[0], a[1], a[2], a[3], a[4], a[5]

        # 方法二：循环遍历行的每列
        for s in line.split(","):
            print s

    f.close()

if __name__ == "__main__":
    read_txt_file()
