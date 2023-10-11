import matplotlib.pyplot as plt

# DDA算法实现
def DDA(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    steps = max(abs(dx), abs(dy))  # 确定在哪个方向上有更多的步骤
    x = x0
    y = y0
    points = []  # 存储绘制的点
    for _ in range(steps + 1):
        points.append((round(x), round(y)))  # 四舍五入取整，将点添加到列表中
        x += dx / steps
        y += dy / steps
    return points

# 中点算法
def Midpoint(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    steep = dy > dx  # 判断是否需要交换 x 和 y 方向
    if steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1
    swapped = False  # 标记是否交换了起点和终点
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
        swapped = True
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    error = dx / 2.0
    y_step = 1 if y0 < y1 else -1
    y = y0
    points = []
    for x in range(x0, x1 + 1):
        if steep:
            points.append((y, x))
        else:
            points.append((x, y))
        error -= dy
        if error < 0:
            y += y_step
            error += dx
    if swapped:
        points.reverse()
    return points

# Breseham算法实现
def Bresenham(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    steep = abs(dy) > abs(dx)  # 判断是否需要交换 x 和 y 方向
    if steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1
    swapped = False  # 标记是否交换了起点和终点
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
        swapped = True
    dx = x1 - x0
    dy = y1 - y0
    dmax, dmin = (dx, dy) if abs(dx) > abs(dy) else (dy, dx)
    e = -dmax
    flag = 1 if dy > 0 else -1
    y = y0
    points = []
    for x in range(x0, x1 + 1):
        points.append((y, x) if steep else (x, y))
        e += 2 * dmin * flag
        if e >= 0:
            y += flag
            e -= 2 * dmax
    if swapped:
        points.reverse()
    return points

def draw_line(points):
    x = []
    y = []
    for point in points:
        x.append(point[0])
        y.append(point[1])
    plt.plot(x, y, color='r', linestyle='-', marker='o')
    plt.show()

if __name__ == '__main__':
    x0, y0 = map(int, input("请输入起点坐标(x0, y0): ").split())
    x1, y1 = map(int, input("请输入终点坐标(x1, y1): ").split())
    points = DDA(x0, y0, x1, y1)
    draw_line(points)
    print("DDA算法实现：")
    print(points)
    points = Midpoint(x0, y0, x1, y1)
    draw_line(points)
    print("中点算法实现：")
    print(points)
    points = Bresenham(x0, y0, x1, y1)
    draw_line(points)
    print("Bresenham算法实现：")
    print(points)
    plt.show()

