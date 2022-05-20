def area_triangle(side1, side2, side3): 
    semi_perimeter = (side1 + side2 + side3) / 2 
    area = (semi_perimeter*(semi_perimeter-side1)*(semi_perimeter-side2)*(semi_perimeter-side3)) ** 0.5
    return area


print ("The area of the triangle is:",(area_triangle(3, 4, 5)))