from Node import Node
from math import log2, floor
from random import shuffle
from copy import deepcopy
from statistics import mean
from numpy import finfo


def majority(k):
    myMap = {}
    maximum = ('', 0)
    for n in k:
        if n in myMap:
            myMap[n] += 1
        else:
            myMap[n] = 1

        if myMap[n] > maximum[1]:
            maximum = (n, myMap[n])

    return maximum[0]


def entropy(ds: list):
    map = {"L": 0, "R": 0, "B": 0}
    for ex in ds:
        map[ex[0]] += 1
    entr = 0
    for val in map.values():
        if val == 0:
            entr += 0
        else:
            entr = entr - (val / len(ds)) * log2(val / len(ds))
    return entr


def IG(total, total_entr, a_vals: dict):
    aux = 0
    for val in a_vals.values():
        aux = aux + (len(val) / total) * entropy(val)

    gain = total_entr - aux
    return gain


def SplitInfo(total, total_entr, a_vals: dict):
    aux = 0
    for val in a_vals.values():
        if total == 0 or len(val) == 0:
            continue
        aux = aux - (len(val) / total) * log2(len(val) / total)

    return aux


def GainRatio(total, total_entr, a_vals: dict):
    ig = IG(total, total_entr, a_vals)
    split = SplitInfo(total, total_entr, a_vals)
    return ig / split


def sepAtr(ds: list, a: dict, n, total_entr):
    gains = {}
    for label, index in a.items():
        aux = {}
        for ex in ds:
            if ex[index] in aux:
                aux[ex[index]].append(ex)
            else:
                aux[ex[index]] = []
        gains[label] = GainRatio(n, total_entr, aux)

    max_lbl = ""
    max_val = -1
    for lbl, val in gains.items():
        if max_val < val:
            max_val = val
            max_lbl = lbl

    max_values = -1
    max_ind = 0

    for i in range(1, 5):
        ind = a[max_lbl]
        left, right = get_Dj(ds, i, ind)

        left_entr = entropy(left)
        right_entr = entropy(right)

        left_IG = (len(left) / n) * left_entr
        right_IG = (len(right) / n) * right_entr

        gain_val = total_entr - left_IG - right_IG

        if gain_val > max_values:
            max_values = gain_val
            max_ind = i

    return max_lbl, max_ind


def get_Dj(ds, val, index):
    left = []
    right = []
    for ex in ds:
        if ex[index] <= val:
            left.append(ex)
        else:
            right.append(ex)
    return left, right


def generate(ds: list, a: dict, n, total_entr):
    node = Node("")
    ok = True
    cls = ds[0][0]
    for ex in ds:
        if ex[0] != cls:
            ok = False
            break
    if ok:
        node.label = cls
        return node

    if len(a) == 0:
        node.label = majority([cl[0] for cl in ds])
        return node
    else:
        sep_atr, val = sepAtr(ds, a, len(ds), total_entr)
        node.label = sep_atr
        node.val = val

        djs_left, djs_right = get_Dj(ds, val, a[sep_atr])
        newAtr = deepcopy(a)
        newAtr.pop(sep_atr)

        subTree_left = generate(djs_left, newAtr, len(djs_left), total_entr)
        subTree_right = generate(djs_right, newAtr, len(djs_right), total_entr)

        node.left = subTree_left
        node.right = subTree_right
        node.children.append(subTree_left)
        node.children.append(subTree_right)

        # for val in range(1, 6):
        #     djs = list(get_Dj(ds, val, a[sep_atr]))
        #     if not djs:
        #         newN = Node("")
        #         newN.label = majority([cl[0] for cl in ds])
        #         node.children.append(newN)
        #     else:
        #         newAtr = deepcopy(a)
        #         newAtr.pop(sep_atr)
        #         subTree = generate(djs, newAtr, n, total_entr)
        #         node.children.append(subTree)

    return node


def readData():
    f = open("DECISION/balance-scale.data", "r")
    ds = []
    for line in f:
        values = line.strip('\n').split(',')
        values[1] = int(values[1])
        values[2] = int(values[2])
        values[3] = int(values[3])
        values[4] = int(values[4])
        ds.append(values)
    f.close()
    return ds


def splitData(lst, p):
    if p == 1:
        return lst, lst
    l = len(lst)
    l = floor(l * p)
    shuffle(lst)
    return lst[:l], lst[l:]


def predict(tree, row, a):
    if tree.label not in ['LW', 'RW', 'LD', 'RD']:
        return tree.label
    # pos = a[tree.label]
    # val = row[pos] - 1
    # return predict(tree.children[val], row, a)
    col = a[tree.label]
    if row[col] <= tree.val:
        return predict(tree.left, row, a)
    else:
        return predict(tree.right, row, a)


def main():
    ds = readData()
    training, test = splitData(ds, 1)
    total_entr = entropy(training)
    n = len(training)
    a = {"LD": 1, "LW": 2, "RD": 3, "RW": 4}
    tree = generate(training, a, n, total_entr)
    # print(tree)
    total = 0
    corr = 0
    for r in test:
        total += 1
        if r[0] == predict(tree, r, a):
            corr += 1
    print("The accuracy is: {:.2f}%".format(float(corr / total) * 100))


if __name__ == '__main__':
    main()
