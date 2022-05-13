def triangle_area(side1, side2, side3): 
    semiperimeter = side1 + side2 + side3 / 2 
    area = (side1*(semiperimeter-side1)*(semiperimeter-side2)*(semiperimeter-side3)) ** 0.5
    return area

area_tri = triangle_area(6,5,5)

print (f'The area of this triangle is: {area_tri}')

#double check formula before submitting