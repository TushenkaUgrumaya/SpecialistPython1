
def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y2 - y1) ** 2) ** 0.5

def can_triangle(p1, p2, p3):
    # a = distance(p1[0], p1[1], p2[0], p2[1])
    a = distance(*p1, *p2)
    b = distance(*p1, *p3)
    c = distance(*p2, *p3)
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c)/2
        s = (p*(p-a)*(p-b)*(p-c))**0.5
        p *=2
        return (s, p)



# Пример вызова функции
print(can_triangle((10, 12), (14, 15), (12, 12)))
