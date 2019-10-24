from itertools import combinations
from string import ascii_uppercase
from collections import OrderedDict
from pdb import set_trace
import json


class Spook:
    def __init__(self, file):
        with open(file) as f:
            content = f.readlines()
        content = [x.strip() for x in content if len(x.strip()) > 4]
        self.buildTree(content)

    def getParity(self):
        for i in range(16, -1, -1):
            for j in self.stems[i]:
                node = self.leaves[j]
                if node.get("2", False):
                    node["3"] = i % 2 + 1
                    node["4"] = "2"
                else:
                    keys = [key for key in node]
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
            word = stack.pop()
            node = self.tree.get(word, None)
            if word in self.minTree:
                continue
            if node.get("4", None):
                if node["4"] == "2":
                    self.minTree[word] = [None]
                else:
                    letter = node["4"]
                    new_word = "".join(sorted(word + letter))
                    stack.append(new_word)
                    self.minTree[word] = [letter]
            else:
                keys = [key for key in node if key not in ["0", "1", "2", "3", "4"]]
                self.minTree[word] = []
                for key in keys:
                    new_word = "".join(sorted(word + key))
                    stack.append(new_word)
                    self.minTree[word].append(key)

        # stack = ["x"]
        # self.minTree = {}
        # while stack:
        #     key = stack.pop()
        #     if self.minTree.get(key, None):
        #         continue
        #     if self.tree[key].get("4", None):
        #         if self.tree[key]["4"] == "2":
        #             self.minTree[key] = [None]
        #         else:
        #             w = "".join(sorted(key + self.tree[key]["4"]))
        #             stack.append(w)
        #             self.minTree[key] = [w]
        #     else:
        #         self.minTree[key] = []
        #         for k in self.tree[key]:
        #             if k not in ["0", "1", "2", "3", "4"]:
        #                 w = "".join(sorted(key + k))
        #                 stack.append(w)
        #                 self.minTree[key].append(w)
        # for k in self.minTree:
        #     for j in k:
        #         w = "".join(sorted(k + j))
        #             if w and w not in minTree:
        #                 stack.append(w)

    def buildTree(self, content):
        content = {"".join(sorted(a)) for a in content}
        self.content = content
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
    try:
        for i in s.minTree:
            for j in s.minTree[i]:
                if j:
                    w = "".join(sorted(i + j))
                    if w not in s.minTree:
                        raise Exception(w)
    except Exception:
        pass
    set_trace()
