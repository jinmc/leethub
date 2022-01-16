class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        result = [[0] * len(img[0]) for _ in range(len(img))]
        directions=((0,0),(0,1),(0,-1),(-1,0),(1,0),(1,1),(-1,-1),(-1,1),(1,-1))
        # print(img)
        # print(img[1][1])
        # directions = ((0,0), (0,1), (1,0), (1,1))
        for i in range(len(img)):
            for j in range(len(img[0])):
                total=0
                count=0
                for x,y in directions:
                    newx = x+i
                    newy = y+j
                    # print("new", newx, newy, img[i][j])
                    if 0<=newx<len(img) and 0<=newy<len(img[0]):
                        total += img[newx][newy]
                        count += 1
                # print(total, count)
                result[i][j] = total//count
        return result
                

                    