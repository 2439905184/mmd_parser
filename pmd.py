import struct
print(__file__)
file=open("gumi.pmd","rb")

def tell_pos():
    print("当前文件位置",file.tell())
def read_header():
    header_magic=file.read(3)
    print(header_magic)
    if header_magic.decode()!="Pmd":
        print("不是pmd文件")
        return
    else:
        print("Loading pmd")
    print("当前文件位置",file.tell())
    version_info=file.read(4)
    print(version_info)
    f=struct.unpack('<f',version_info)[0]
    print("Version:",f)
def read_model_header():
    model_name=file.read(20)
    print("modelName:",model_name)
    comment=file.read(256)
    #print("comment:",comment)
    #c=struct.unpack('c',model_name)
    #print(c)
    
    #print("模型名称：",model_name.decode("Shift-JIS"))
#读取顶点
def read_vertex():
    #x y z 位置
    x_pos=file.read(4)
    y_pos=file.read(4)
    z_pos=file.read(4)
    x_pos_float=struct.unpack('f',x_pos)[0]
    y_pos_float=struct.unpack('f',y_pos)[0]
    z_pos_float=struct.unpack('f',z_pos)[0]
    print("位置:",x_pos_float,y_pos_float,z_pos_float)
    #x y z 法线
    x_normal=file.read(4)
    y_normal=file.read(4)
    z_normal=file.read(4)
    x_normal_float=struct.unpack("f",x_normal)[0]
    y_normal_float=struct.unpack("f",y_normal)[0]
    z_normal_float=struct.unpack("f",z_normal)[0]
    print("法线:",x_normal_float,y_normal_float,z_normal_float)
    #uv 顶点纹理坐标
    u=file.read(4)
    v=file.read(4)
    u_float=struct.unpack("f",u)[0]
    v_float=struct.unpack("f",v)[0]
    print("纹理坐标:",u_float,v_float)
    #骨骼索引
    bone0=file.read(2)
    bone1=file.read(2)
    #骨骼0权重
    bone0_weight=file.read(1)
    print("权重",bone0_weight)
    #边缘标记 确定是否在顶点周围画线
    edge_flag=file.read(1)
    print("边缘标记",edge_flag)
#索引信息
def read_index():
    vertex_id=file.read(2)
    #unsigned short
    vertex_id_short=struct.unpack("H",vertex_id)[0]
    print("索引信息",vertex_id_short)
#材质信息
def read_material():
    #漫反射
    R_diffuse=file.read(4)
    G_diffuse=file.read(4)
    B_diffuse=file.read(4)
    A_diffuse=file.read(4)
    R=struct.unpack("f",R_diffuse)[0]
    G=struct.unpack("f",G_diffuse)[0]
    B=struct.unpack("f",B_diffuse)[0]
    A=struct.unpack("f",A_diffuse)[0]
    print("漫反射颜色",R,G,B,A)
    #镜面度
    mirrow_value=file.read(4)
    mirrow_R=file.read(4)
    mirrow_G=file.read(4)
    mirrow_B=file.read(4)
    #环境度
    ambient_R=file.read(4)
    ambient_G=file.read(4)
    ambient_B=file.read(4)
    #toon
    toon_number=file.read(1)
    edge_flag=file.read(1)
    long_value=file.read(4)
    #材质名称
    file_name=file.read(20)
    print("toon材质",file_name)
    
#骨骼信息
def read_bone():
    bone_name=file.read(20)
    bone_parent_index=file.read(2)
    short_bone_parent_index=struct.unpack("h",bone_parent_index)[0]
    bone_type=file.read(1)
    target_bone=file.read(2)
    bone_x=file.read(4)
    bone_y=file.read(4)
    bone_z=file.read(4)
    char_bone_type=struct.unpack('c',bone_type)[0]
    #shift-jis
    print("骨骼名称",bone_name)
    print("骨骼parent",short_bone_parent_index)
    print("targetbone:",char_bone_type)
    #未写完
    file.close()
read_header()
read_model_header()
read_vertex()
read_index()
read_material()
read_bone()
#print(file.read(4))
# tmp=file.read(1)
# print(tmp)
