
print(__file__)
file=open("miku.pmd","rb")

def tell_pos():
    print("当前文件位置",file.tell())
def read_header():
    header_file_name=file.read(3)
    print("magic "+str(header_file_name))
    file.seek(3)
    print("当前文件位置",file.tell())
    version=file.read(24)
    #文件头结束
    print(version)
    file.seek(24)
    print(file.readline())
    # file.seek(4)
    # #model header
    # model_name=file.read(20).decode("shift-jis")
    # print(model_name)
read_header()
#print(file.read(4))
# tmp=file.read(1)
# print(tmp)