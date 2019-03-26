def main(height):
    water,i,j = 0,0,len(height)-1
    while i<j:
        h=min(height[i],height[j])
        water=max(water,(j-i)*h)
        while h>=height[i] and i<j: i+=1
        while h>=height[j] and i<j: j-=1
    return water 

if __name__ == '__main__':
    height = [1, 2, 3, 4, 3, 2, 1, 5]
    print(main(height))