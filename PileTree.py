from GameTree import getParity


class PileTree:
    def __init__(self):
        with open(r"/Users/benbaily/git/Ghostbusters/Scrabble.txt") as f:
            content = f.readlines()
        content = [x.strip() for x in content if len(x) > 4]
        content = {"".join(sorted(x)) for x in content}
        self.buildTree(content)
        getParity(self.tree)

