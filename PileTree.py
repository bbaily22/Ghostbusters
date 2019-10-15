from itertools import combinations
from string import ascii_uppercase
from collections import namedtuple, OrderedDict
from pdb import set_trace
import json


class PileTree:
    def __init__(self):
        with open(r"Scrabble.txt") as f:
            content = f.readlines()
        content = [x.strip() for x in content if len(x) > 4]
        self.buildTree(content)

    def buildTree(self, content):
        self.leaves = [{"0": "x", "1": 0}]
        content = {"".join(sorted(a)) for a in content}
        substrings = set([])
        for c in ["BEE", "MUG", "CRY", "DABBING", "GOLDEN", "NEXT"]:
            for i in range(len(c)):
                substrings.update(set(combinations(c, i + 1)))
        index = 1
        for s in substrings:
            w = "".join(sorted(s)) + "x"
            d = {"0": w, "1": index}
            if "".join(sorted(w)) in content:
                d.update({"2": True})
            self.leaves.append(d)
            index += 1
        Tree = namedtuple("MyTuple", [t["0"] for t in self.leaves])
        self.tree = Tree(*self.leaves)
        for k in self.tree:
            for a in ascii_uppercase:
                ka = "".join(sorted(k["0"] + a))
                if getattr(self.tree, ka, None):
                    getattr(self.tree, k["0"])[a] = getattr(self.tree, ka)["1"]
        with open("PileTree.txt", "w") as f:
            json.dump(self.tree, f)


if __name__ == "__main__":
    p = PileTree()

