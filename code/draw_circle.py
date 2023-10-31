import matplotlib.pyplot as plt

# 中点算法
def MidPointCircle(cx, cy, r):
    x1 = 0
    y1 = r
    d = 1 - r
    points = []  # 用于保存圆上的点

    while x1 <= y1:
        # 将点加入列表，使用相对于(cx, cy)的坐标
        points.append((x1 + cx, y1 + cy))
        points.append((-x1 + cx, y1 + cy))
        points.append((x1 + cx, -y1 + cy))
        points.append((-x1 + cx, -y1 + cy))
        points.append((y1 + cx, x1 + cy))
        points.append((-y1 + cx, x1 + cy))
        points.append((y1 + cx, -x1 + cy))
        points.append((-y1 + cx, -x1 + cy))

        if d < 0:
            d += 2 * x1 + 3
        else:
            d += 2 * (x1 - y1) + 5
            y1 -= 1
        x1 += 1

    return points

# Bresenham算法
def BresenhamCircle(cx, cy, r):
    x = 0
    y = r
    d = 3 - 2 * r
    points = []  # 用于保存圆上的点

    while x <= y:
        # 将点加入列表，使用相对于(cx, cy)的坐标
        points.append((x + cx, y + cy))
        points.append((-x + cx, y + cy))
        points.append((x + cx, -y + cy))
        points.append((-x + cx, -y + cy))
        points.append((y + cx, x + cy))
        points.append((-y + cx, x + cy))
        points.append((y + cx, -x + cy))
        points.append((-y + cx, -x + cy))

        if d < 0:
            d += 4 * x + 6
        else:
            d += 4 * (x - y) + 10
            y -= 1
        x += 1

    return points

def draw_circle(points):
    x = []
    y = []
    for i in points:
        x.append(i[0])
        y.append(i[1])
    # 设置坐标系X轴Y轴长度一致
    plt.axis('equal')
    plt.scatter(x, y, s=1)
    plt.show()

if __name__ == '__main__':
    cx, cy = map(int, input("请输入圆心坐标(cx, cy): ").split())
    r = int(input("请输入圆的半径: "))
    points = MidPointCircle(cx, cy, r)
    draw_circle(points)
    print("中点算法实现：")
    print(points)
    points = BresenhamCircle(cx, cy, r)
    draw_circle(points)
    print("Bresenham算法实现：")
    print(points)