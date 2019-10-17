from itertools import combinations
from string import ascii_uppercase
from collections import OrderedDict
from pdb import set_trace
import json


class PileTree:
    def __init__(self):
        with open(r"Scrabble.txt") as f:
            content = f.readlines()
        content = [x.strip() for x in content if len(x) > 4]
        self.buildTree(content)

    def buildTree(self, content):
        content = {"".join(sorted(a)) for a in content}
        substrings = set([])
        for c in ["BEE", "MUG", "CRY", "DABBING", "GOLDEN", "NEXT"]:
            for i in range(len(c)):
                substrings.update(set(combinations(c, i + 1)))
        substrings = {"".join(sorted(s)) for s in substrings}
        index = 1
        self.leaves = [{"0": "x", "1": 0}]
        for s in substrings:
            w = "".join(sorted(s)) + "x"
            d = {"0": w, "1": index}
            if "".join(sorted(w)) in content:
                d.update({"2": True})
            self.leaves.append(d)
            index += 1
        self.tree = {s["0"]: s for s in self.leaves}
        for k in self.tree:
            for a in ascii_uppercase:
                ka = "".join(sorted(k + a))
                if ka in self.tree:
                    self.tree[k][a] = self.tree[ka]["1"]
        with open("PileTree.txt", "w") as f:
            json.dump(self.tree, f)


if __name__ == "__main__":
    p = PileTree()
    set_trace()

