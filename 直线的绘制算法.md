## 数值微分DDA算法
DDA算法是计算机图形学中最简单的绘制直线算法。其主要思想是由直线公式 $y = kx + b$ 推导出来的。  

我们已知直线段两个端点$P_0(x_0,y_0)$和$P_1(x_1,y_1)$，就能求出 $k$ 和 $b$ 。

在 $k$，$b$ 均求出的条件下，只要知道一个 $x$ 值，我们就能计算出一个 $y$ 值。如果 $x$ 的步进为$1$（$x$每次加$1$，即$x = x +1$），那么 $y$ 的步进就为 $k+b$；同样知道一个 $y$ 值也能计算出 $x$ 值，此时 $y$ 的步进为 $1$，$x$ 的步进为 $\dfrac{1-b}{k}$。根据计算出的 $x$ 值和 $y$ 值，向下取整，得到坐标 $(x’,y’)$，并在 $(x’,y’)$ 处绘制直线段上的一点。

为进一步简化计算，通常可令 $b$ 取 $0$，将起点看作 $(0,0)$。设当前点为 $(x_i, y_i)$ 则用DDA算法求解$(x_{i+1}，y_{i+1})$的计算公式可以概括为：

$$x_{i+1}=x_i+xStep\tag{1}$$
$$y_{i+1}=y_i+yStep\tag{2}$$

我们一般通过计算 $Δx$ 和 $Δy$ 来确定 $xStep$ 和 $yStep$：

- 如果 $Δx > Δy$ ，说明$x$轴的最大差值大于$y$轴的最大差值，$x$轴方向为步进的主方向，$xStep = 1$，$yStep = k$；
- 如果 $Δy> Δx$，说明$y$轴的最大差值大于$x$轴的最大差值，$y$轴方向为步进的主方向，$yStep = 1$，$xStep = \dfrac{1}{k}$。

根据这个公式，就能通过$(x_i，y_i)$迭代计算出$(x_{i+1}、y_{i+1})$，然后在坐标系中绘制计算出的$(x,y)$坐标点。

```python
def DDA(x0, y0, x1, y1):  
    dx = x1 - x0  
    dy = y1 - y0  
    steps = max(abs(dx), abs(dy))  # 确定步进主方向  
    x = x0  
    y = y0  
    points = []  # 存储绘制的点  
    for _ in range(steps + 1):  
        points.append((round(x), round(y)))  # 四舍五入取点
        x += dx / steps  
        y += dy / steps  
    return points
```

## 中点算法
```python
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
```

## Bresenham算法
Bresenham算法也是一种计算机图形学中常见的绘制直线的算法，其本质思想也是步进的思想，但由于避免了浮点运算，相当于DDA算法的一种改进算法。

设直线的斜率为$k$，当$|k| <=1$时，$x$方向为主步进方向；当$|k| >1$时，$y$方向为主步进方向。现以$|k| <1$时为例，推导Bresenham算法的原理。

图中绘制了一条直线，蓝色点表示该直线上的点，红色点表示光栅下绘制的点。  
假设当前点是$(x_i,y_i)$
- 如果$int(y_i+0.5) = y_i$，则在点$(x_i, round(y_i))$处绘制.  
- 如果$int(y_i+0.5)=yi+1$，则在点$(x_i, round(y_i)+1)$处绘制。

上述逻辑可简述为：当x方向是主要步进方向时，以每一小格的中点为界，如果当前的yi在中点(图中红色短线)下方，则y取round($y_i$); 如果当前的$y_i$在中点上方，则y取round($y_i$)+1。

改进后的Bresenham算法：
```python
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
```
