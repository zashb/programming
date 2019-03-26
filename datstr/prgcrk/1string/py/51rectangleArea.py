def main(A,B,C,D,E,F,G,H):
    # left=max(A,E)
    # right=max(min(C,G), left)
    # bottom = max(B,F)
    # top = max(min(D,H), bottom)
    # return (C-A)*(D-B) - (right-left)*(top-bottom) + (G-E)*(H-F)
    
    overlap = max(min(C,G)-max(A,E), 0)*max(min(D,H)-max(B,F), 0)
    return (A-C)*(B-D) + (E-G)*(F-H) - overlap

if __name__ == '__main__':
    print(main(-3,0,3,4,0,-1,9,2))