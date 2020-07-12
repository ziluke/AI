class FuzzySystem:
    def __init__(self, rules):
        self.__in_descr = {}
        self.__out_descr = None
        self.__rules = rules

    def add_description(self, name, descr, out=False):
        if out:
            if self.__out_descr is None:
                self.__out_descr = descr
            else:
                raise ValueError("System already has an output!")
        else:
            self.__in_descr[name] = descr

    def compute(self, inputs):
        fuzzy_vals = self.__compute_descr(inputs)
        rule_vals = self.__compute_rules(fuzzy_vals)

        fuzzy_outs = [(list(descr[0].values())[0], descr[1]) for descr in rule_vals]

        w_total = 0
        w_sum = 0

        print("Inputs: {}\n".format(inputs))
        print("Fuzzy values: {}\n".format(fuzzy_vals))
        print("Fuzzy rules: {}\n".format(rule_vals))
        print("Fuzzy outs: {}\n".format(fuzzy_outs))

        for var in fuzzy_outs:
            w_sum += var[1]
            x = self.__out_descr.defuzzify(*var)
            w_total += x * var[1]

        return w_total / w_sum

    def __compute_descr(self, inputs):
        return {
            name: self.__in_descr[name].fuzzify(inputs[name]) for name, _ in inputs.items()
        }

    def __compute_rules(self, fuzzy_vals):
        aux = []
        for rule in self.__rules:
            val = rule.evaluate(fuzzy_vals)
            if val[1] != 0:
                aux.append(val)
        return aux
