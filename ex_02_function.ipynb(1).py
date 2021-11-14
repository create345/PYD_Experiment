# -*- coding: 使用图乘法计算在单一集中荷载作用下的悬臂梁挠度与转角
def squire(F,x1):#面积
    ω=x1**2*F*1/2#ω为集中荷载F作用在x1处产生的弯矩图的面积
    return ω
print("集中荷载F作用在x1处产生的弯矩图的面积是{}".format(sq(12,3)))
print("_"*50)
def co(F,x1,x2):#co为centroid ordinate 形心纵坐标
    ω=x1**2*F*1/2#ω为集中荷载F作用在x1处产生的弯矩图的面积
    M1=x2#M1为单位力作用在x2处产生的最大弯矩
    Yc1=x2-1/3*x1#Yc1为ω的形心在单位力产生弯矩图中的纵坐标
    Yc2=1-x1/3*x2#Yc2为ω的形心在单位弯矩产生弯矩图中的纵坐标
    return Yc1,Yc2
print("ω的形心在单位力和单位弯矩产生弯矩图中的纵坐标是{}".format(co(12,3,6)))
print("_"*50)
def dmm(F,x1,x2,E,I):#dmm为Diagrammatic Multiplication Method 图乘法
    ω=x1**2*F*1/2#ω为集中荷载F作用在x1处产生的弯矩图的面积
    M1=x2#M1为单位力作用在x2处产生的最大弯矩
    Yc1=x2-1/3*x1#Yc1为ω的形心在单位力产生弯矩图中的纵坐标
    Yc2=1-x1/3*x2#Yc2为ω的形心在单位弯矩产生弯矩图中的纵坐标
    Δ=ω*Yc1/E/I#Δ为x2位置处的挠度
    θ=ω*Yc2/E/I#θ为x2位置处的转角
    return Δ,θ
print("挠度和转角分别是{}".format(dmm(12,3,6,1,2)))
    
