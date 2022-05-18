def area_triangle(side1, side2, side3): 
    semi_pee = (side1 + side2 + side3) / 2 
    area = (semi_pee*(semi_pee-side1)*(semi_pee-side2)*(semi_pee-side3)) ** 0.5
    return area

area_tri = area_triangle(3,4,5)

print (f'The area of this triangle is: {area_tri}')