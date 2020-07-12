from __future__ import print_function


header = ["Cl", "LD", "LW", "RD", "RW"]


def unique_vals(rows, col):
    return set([row[col] for row in rows])



def class_counts(rows):
    counts = {}
    for row in rows:
        label = row[0]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts


class Question:

    def __init__(self, column, value):
        self.column = column
        self.value = value

    def match(self, example):
        val = example[self.column]
        return val == self.value

    def __repr__(self):
        condition = "=="
        return "Is %s %s %s?" % (
            header[self.column], condition, str(self.value))


def partition(rows, question):
    true_rows, false_rows = [], []
    for row in rows:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows, false_rows


def gini(rows):

    counts = class_counts(rows)
    impurity = 1
    for lbl in counts:
        prob_of_lbl = counts[lbl] / float(len(rows))
        impurity -= prob_of_lbl ** 2
    return impurity


def info_gain(left, right, current_uncertainty):
    p = float(len(left)) / (len(left) + len(right))
    return current_uncertainty - p * gini(left) - (1 - p) * gini(right)


def find_best_split(rows):
    best_gain = 0  
    best_question = None 
    current_uncertainty = gini(rows)
    n_features = len(rows[0]) - 1

    for col in range(n_features):

        values = set([row[col] for row in rows])

        for val in values:

            question = Question(col, val)

            true_rows, false_rows = partition(rows, question)

            if len(true_rows) == 0 or len(false_rows) == 0:
                continue

            gain = info_gain(true_rows, false_rows, current_uncertainty)

            if gain >= best_gain:
                best_gain, best_question = gain, question

    return best_gain, best_question


class Leaf:

    def __init__(self, rows):
        self.predictions = class_counts(rows)


class Decision_Node:

    def __init__(self,
                 question,
                 true_branch,
                 false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch


def build_tree(rows):
    gain, question = find_best_split(rows)

    if gain == 0:
        return Leaf(rows)

    true_rows, false_rows = partition(rows, question)

    true_branch = build_tree(true_rows)

    false_branch = build_tree(false_rows)

    return Decision_Node(question, true_branch, false_branch)


def print_tree(node, spacing=""):
    if isinstance(node, Leaf):
        print(spacing + "Predict", node.predictions)
        return

    print(spacing + str(node.question))

    print(spacing + '--> True:')
    print_tree(node.true_branch, spacing + "  ")

    print(spacing + '--> False:')
    print_tree(node.false_branch, spacing + "  ")


def classify(row, node):
    if isinstance(node, Leaf):
        return node.predictions

    if node.question.match(row):
        return classify(row, node.true_branch)
    else:
        return classify(row, node.false_branch)


def print_leaf(counts):
    total = sum(counts.values()) * 1.0
    probs = {}
    for lbl in counts.keys():
        probs[lbl] = str(int(counts[lbl] / total * 100)) + "%"
    return probs


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
    return ds


def readTestData():
    f = open("test.txt", "r")
    ds = []
    for line in f:
        values = line.strip('\n').split(',')
        ds.append(values)
    return ds

from math import floor
from random import shuffle

def splitData(lst, p):
    if p == 1:
        return lst, lst
    l = len(lst)
    l = floor(l * p)
    shuffle(lst)
    return lst[:l], lst[l:]


if __name__ == '__main__':
    training_data, testing_data = splitData(readData(), 0.8)
    my_tree = build_tree(training_data)

    print_tree(my_tree)

    for row in testing_data:
        print("Actual: %s. Predicted: %s" %
              (row[0], print_leaf(classify(row, my_tree))))
