import pprint
class Node:
    def __init__(self, label):
        self.label = label
        self.val = 0
        self.children = []
        self.left = None
        self.right = None
    # def print(self):
    #     return str(pprint.pprint(self.children))
        
    def pprint_tree(self, node, file=None, _prefix="", _last=True):
        print(_prefix, "`- " if _last else "|- ",node.label+": "+str(node.val), sep="", file=file)
        _prefix += "   " if _last else "|  "
        child_count = len(node.children)
        for i, child in enumerate(node.children):
            _last = i == (child_count - 1)
            self.pprint_tree(child, file, _prefix, _last)

    def __str__(self):   
        self.pprint_tree(self)
        return ""
