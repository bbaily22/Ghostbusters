from itertools import combinations
from string import ascii_uppercase
from collections import OrderedDict
from pdb import set_trace
import json


class Spook:
    def __init__(self):
        with open(r"Scrabble.txt") as f:
            content = f.readlines()
        content = [x.strip() for x in content if len(x) > 4]
        self.buildTree(content)

    def getParity(self):
        for i in range(16, -1, -1):
            for j in self.stems[i]:
                node = self.leaves[j]
                if node.get("2", False):
                    node["3"] = i % 2 + 1
                else:
                    keys = [*node]
                    keys.remove("0")
                    keys.remove("1")
                    if i % 2 == 0:
                        for key in keys:
                            if self.leaves[node[key]].get("3", None) and self.leaves[node[key]]["3"] == 1:
                                node["3"] = 1
                                break
                        node["3"] = 2
                    else: 
                        for key in keys:
                            if self.leaves[node[key]].get("3", None) and self.leaves[node[key]]["3"] == 2:
                                node["3"] = 2
                                break
                        node["3"] = 1


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
        self.getParity()
        with open("Spook.txt", "w") as f:
            json.dump(self.tree, f)


if __name__ == "__main__":
    p = Spook()
    set_trace()

