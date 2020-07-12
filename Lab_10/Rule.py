class FuzzyRule:
    def __init__(self, inputs, outputs):
        self.__ins = inputs
        self.__outs = outputs

    def evaluate(self, inputs):
        return [self.__outs, min(
            [inputs[descr_name][var_name]
             for descr_name, var_name in self.__ins.items()
             ])]
