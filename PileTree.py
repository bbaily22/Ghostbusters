# from GameTree import getParity
from string import ascii_uppercase


class PileTree:
    def __init__(self):
        with open(r"/Users/benbaily/git/Ghostbusters/Scrabble.txt") as f:
            content = f.readlines()
        content = [x.strip() for x in content if len(x) > 4]
        self.buildTree(content)
        # getParity(self.tree)

    def buildTree(self, content):
        self.tree = {"0": ""}
        # TODO initialize substrings by reading in from file
        for s in substrings:
            self.tree.update({s: {"0": s}})
        for k, v in self.tree.items():
            for a in ascii_uppercase:
                ka = "".join(sorted(k + a))
                if ka in self.tree:
                    self.tree[k][a] = self.tree[ka]


if __name__ == "__main__":
    p = PileTree()
    k = []
    for i in range(1, 17):
        k.append([n for n in p.tree.keys() if len(n) == k])
    import pdb

    pdb.set_trace()

