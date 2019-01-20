def main(height):
    height.append(0)
    stack,maxArea=[-1],0
    for i in range(len(height)):
        while height[i]<height[stack[-1]]:
            h,w=height[stack.pop()],i-stack[-1]-1
            maxArea=max(maxArea,h*w)
        stack.append(i)
    return maxArea

if __name__ == '__main__':
    print(main([2,1,5,6,2,3]))