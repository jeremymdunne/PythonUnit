"""


"""

class ValueWithUnits(float):
    def __init__(self, *args):
        if len(args) > 0:
            self.value = args[0]
        else:
            self.value = float('NaN')
        if len(args) > 1:
            self.unit = args[1]
        else:
            self.unit = ''

    def convert(self, target_unit):
        # this is going to be an interesting method

    def getValue(self):
        return self.value, self.unit
