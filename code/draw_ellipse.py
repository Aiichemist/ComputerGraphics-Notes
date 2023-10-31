import matplotlib.pyplot as plt

# 中点算法
def MidPointEllipse(cx, cy, a, b):
    x = 0
    y = b
    d1 = (b * b) - (a * a * b) + (0.25 * a * a)
    dx = 2 * b * b * x
    dy = 2 * a * a * y
    points = []

    while dx < dy:
        # 将点加入列表，使用相对于(cx, cy)的坐标
        points.append((x + cx, y + cy))
        points.append((-x + cx, y + cy))
        points.append((x + cx, -y + cy))
        points.append((-x + cx, -y + cy))

        if d1 < 0:
            x += 1
            dx += 2 * b * b
            d1 = d1 + dx + (b * b)
        else:
            x += 1
            y -= 1
            dx += 2 * b * b
            dy -= 2 * a * a
            d1 = d1 + dx - dy + (b * b)

    d2 = ((b * b) * ((x + 0.5) ** 2)) + ((a * a) * ((y - 1) ** 2)) - (a * a * b * b)

    while y >= 0:
        # 将点加入列表，使用相对于(cx, cy)的坐标
        points.append((x + cx, y + cy))
        points.append((-x + cx, y + cy))
        points.append((x + cx, -y + cy))
        points.append((-x + cx, -y + cy))

        if d2 > 0:
            y -= 1
            dy -= 2 * a * a
            d2 = d2 + (a * a) - dy
        else:
            y -= 1
            x += 1
            dx += 2 * b * b
            dy -= 2 * a * a
            d2 = d2 + dx - dy + (a * a)

    return points

# Bresenham算法
def BresenhamEllipse(cx, cy, rx, ry):
    x = 0
    y = ry
    rx2 = rx * rx
    ry2 = ry * ry
    twoRx2 = 2 * rx2
    twoRy2 = 2 * ry2
    p = int(ry2 - rx2 * ry + 0.25 * rx2)

    points = []  # 用于保存椭圆上的点

    # 绘制第一象限
    while rx2 * (y - 0.5) > ry2 * (x + 1):
        points.append((x + cx, y + cy))
        points.append((-x + cx, y + cy))
        points.append((x + cx, -y + cy))
        points.append((-x + cx, -y + cy))

        if p < 0:
            p += ry2 * (2 * x + 3)
        else:
            p += ry2 * (2 * x + 3) + rx2 * (-2 * y + 2)
            y -= 1
        x += 1

    # 绘制第二象限
    p = int(ry2 * (x + 0.5) * (x + 0.5) + rx2 * (y - 1) * (y - 1) - rx2 * ry2)
    while y > 0:
        points.append((x + cx, y + cy))
        points.append((-x + cx, y + cy))
        points.append((x + cx, -y + cy))
        points.append((-x + cx, -y + cy))

        if p > 0:
            p += rx2 * (-2 * y + 3)
        else:
            p += rx2 * (-2 * y + 3) + ry2 * (2 * x + 2)
            x += 1
        y -= 1

    return points

def draw_ellipse(points):
    x = []
    y = []
    for i in points:
        x.append(i[0])
        y.append(i[1])
    # 设置坐标系X轴Y轴长度一致
    plt.axis('equal')
    # 绘制散点图
    plt.scatter(x, y, s=1)
    plt.show()

if __name__ == '__main__':
    cx, cy = map(int, input("请输入椭圆中心坐标(cx, cy): ").split())
    a, b = map(int, input("请输入椭圆长轴和短轴(a, b): ").split())
    points = MidPointEllipse(cx, cy, a, b)
    draw_ellipse(points)
    print("中点算法实现：")
    print(points)
    points = BresenhamEllipse(cx, cy, a, b)
    draw_ellipse(points)
    print("Bresenham算法实现：")
    print(points)