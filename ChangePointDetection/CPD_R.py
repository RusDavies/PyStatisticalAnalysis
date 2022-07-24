
from rpy2.robjects import FloatVector
from rpy2.robjects.packages import importr

class CPD_R:
    def __init__(self):
        self.cpm = importr('cpm')

    @staticmethod
    def robj_to_dict(robj):
        return dict(zip(robj.names, map(list, robj)))

    def detectChanges(self, data, cpmType='GLR',  ARL0=2000, startup=20):
        data = FloatVector(data)
        result = self.cpm.processStream(data, cpmType='GLR',  ARL0=2000, startup=20)
        result = CPD_R.robj_to_dict(result)
        return result 