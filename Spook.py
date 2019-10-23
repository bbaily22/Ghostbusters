from itertools import combinations
from string import ascii_uppercase
from collections import OrderedDict
from pdb import set_trace
import json


class Spook:
    def __init__(self, file):
        with open(file) as f:
            content = f.readlines()
        content = [x.strip() for x in content if len(x) > 4]
        self.buildTree(content)

    def getParity(self):
        for i in range(16, -1, -1):
            for j in self.stems[i]:
                node = self.leaves[j]
                if node.get("2", False):
                    node["3"] = i % 2 + 1
                    node["4"] = "2"
                else:
                    keys = [*node]
                    keys.remove("0")
                    keys.remove("1")
                    if i % 2 == 0:
                        for key in keys:
                            if (
                                self.leaves[node[key]].get("3", None)
                                and self.leaves[node[key]]["3"] == 1
                            ):
                                node["3"] = 1
                                node["4"] = key
                                break
                        if not node.get("3", None):
                            node["3"] = 2
                            node["4"] = None
                    else:
                        for key in keys:
                            if (
                                self.leaves[node[key]].get("3", None)
                                and self.leaves[node[key]]["3"] == 2
                            ):
                                node["3"] = 2
                                node["4"] = key
                                break
                        if not node.get("3", None):
                            node["3"] = 1
                            node["4"] = None

    def minSolution(self):
        stack = ["x"]
        self.minTree = {}
        while stack:
            key = stack.pop()
            if self.minTree.get(key, None):
                continue
            if self.tree[key].get("4", None):
                if not self.tree[key]["4"] == "2":
                    w = "".join(sorted(key + self.tree[key]["4"]))
                    stack.append(w)
                    self.minTree[key] = [w]
            else:
                self.minTree[key] = []
                for k in [*self.tree[key]]:
                    if k not in ["0", "1", "2", "3", "4"]:
                        w = "".join(sorted(key + k))
                        stack.append(w)
                        self.minTree[key].append(w)

    def buildTree(self, content):
        content = {"".join(sorted(a)) for a in content}
        substrings = set([])
        for c in content:
            for i in range(len(c)):
                substrings.update(set(combinations(c, i + 1)))
        substrings = {"".join(sorted(s)) for s in substrings}
        index = 1
        self.stems = [[] for i in range(17)]
        self.leaves = [{"0": "x", "1": 0}]
        self.stems[0].append(0)
        for s in substrings:
            w = "".join(sorted(s)) + "x"
            d = {"0": w, "1": index, "2": "".join(sorted(s)) in content}
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
        self.minSolution()
        with open("Spook.txt", "w") as f:
            json.dump(self.minTree, f)


if __name__ == "__main__":
    s = Spook("Scrabble.txt")
    set_trace()

