from GameTree import getParity


class PileTree:
    def __init__(self):
        with open(r"/Users/benbaily/git/Ghostbusters/Scrabble.txt") as f:
            content = f.readlines()
        content = [x.strip() for x in content if len(x) > 4]
        self.buildTree(content)
        getParity(self.tree)

    def buildTree(self, content):
        self.tree = {"0": ""}
        content = {"".join(sorted(x)) for x in content}
        maximal_words = get_max_words(content)
        for word in maximal_words:
            head = self.tree
            for letter in word:
                if letter in head:
                    head = head[letter]
                else:
                    head[letter] = {"0": head["0"] + letter}
                    tree[head[letter["0"]]] = head[letter]
