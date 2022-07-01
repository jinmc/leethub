class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        # print(boxTypes)
        
        output = 0
        while truckSize > 0 and boxTypes:
            this_box = boxTypes.pop(0)
            if this_box[0] >= truckSize:
                output += truckSize * this_box[1]
                truckSize = 0
            else:
                output += this_box[0] * this_box[1]
                truckSize -= this_box[0]
            # print(output)
        return output
            