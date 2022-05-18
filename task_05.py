def area_triangle(side1, side2, side3): 
    semiperimeter = (side1 + side2 + side3) / 2 
    area = (semiperimeter*(semiperimeter-side1)*(semiperimeter-side2)*(semiperimeter-side3)) ** 0.5
    return area

area_tri = area_triangle(3,4,5)

print (f'The area of this triangle is: {area_tri}')