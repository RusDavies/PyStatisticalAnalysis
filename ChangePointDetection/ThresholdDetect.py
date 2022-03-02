
import numpy as np

class ThresholdDetect:
    def detectChanges(self, data:np.array, threshold=None):
        if (not threshold):
            (dmax, dmin) = (max(data), min(data))
            threshold = ((dmax - dmin) / 2) + dmin

        changePoints = []
        previous_index = -1
        for index in data.index:
            if (previous_index >= 0):
                if (((data[index] > threshold) and (data[previous_index] < threshold)) or  ((data[index] < threshold) and (data[previous_index] > threshold))):
                    changePoints.append(index)
            previous_index = index
        
        return changePoints