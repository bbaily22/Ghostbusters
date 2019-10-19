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

    def getParity(self):
        print(node)
        for i in range(16,-1,-1):
            for j in self.stems[i]:
                if 

        if node.get("2"):
            return node["2"]
        keys = [*node]
        keys.remove("0")
        keys.remove("1")
        if len(node["0"]) % 2 == 0:
            for key in keys:
                if self.getParity(self.leaves[node[key]]) == 1:
                    node["parity"] = 1
                    return 1
            node["parity"] = 2
            return 2
        for key in keys:
            if self.getParity(self.leaves[node[key]]) == 2:
                node["parity"] = 2
                return 2
        node["parity"] = 1
        return 1

    def buildTree(self, content):
        content = {"".join(sorted(a)) for a in content}
        substrings = set([])
        for c in ["BEE", "MUG", "CRY", "DABBING", "GOLDEN", "NEXT"]:
            for i in range(len(c)):
                substrings.update(set(combinations(c, i + 1)))
        substrings = {"".join(sorted(s)) for s in substrings}
        index = 1
        self.stems = [[] for i in range(17)]
        self.leaves = [{"0": "x", "1": 0}]
        self.stems[0].append(0)
        for s in substrings:
            w = "".join(sorted(s)) + "x"
            d = {"0": w, "1": index}
            if "".join(sorted(w)) in content:
                d.update({"2": True})
            self.leaves.append(d)
            self.stems[len(s)].append(index)
            index += 1
        self.tree = {s["0"]: s for s in self.leaves}
        for k in self.tree:
            for a in ascii_uppercase:
                ka = "".join(sorted(k + a))
                if ka in self.tree:
                    self.tree[k][a] = self.tree[ka]["1"]
        self.getParity(self.tree["x"])
        with open("PileTree.txt", "w") as f:
            json.dump(self.tree, f)


if __name__ == "__main__":
    p = PileTree()
    set_trace()

