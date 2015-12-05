a1=0
a2=0
for line in open('a2.in'):
    l,w,h = list(map(int,line.split('x')))
    areas = l*w,w*h,h*l
    perims= l+w,w+h,h+l
    a1+=2*sum(areas) + min(areas)
    a2+=2*min(perims) + l*w*h
print(a1)
print(a2)
