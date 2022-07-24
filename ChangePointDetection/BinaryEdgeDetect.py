
import numpy as np

class BinaryEdgeDetect:
    def detectChanges(self, data:np.array):

        changePoints = []
        previous_index = -1
        for index in data.index:
            if (previous_index >= 0):
                change = abs(data[index] - data[previous_index])
                if(change):
                    changePoints.append(index)
            previous_index = index

        return changePoints