from random import randrange


class GameTree:
    def buildTree(self, content):
        self.tree = {"0": ""}
        for a in content:
            head = self.tree
            for letter in a:
                if letter in head:
                    head = head[letter]
                else:
                    head[letter] = {"0": head["0"] + letter}
                    head = head[letter]
            if len(a) > 4:
                head["parity"] = (len(a) % 2) + 1
                head["FINAL"] = True

    def getParity(self, tree):
        if tree.get("parity"):
            return tree["parity"]
        keys = [*tree]
        keys.remove("0")
        if len(tree["0"]) % 2 == 0:
            for key in keys:
                if self.getParity(tree[key]) == 1:
                    tree["parity"] = 1
                    return 1
            tree["parity"] = 2
            return 2
        for key in keys:
            if self.getParity(tree[key]) == 2:
                tree["parity"] = 2
                return 2
        tree["parity"] = 1
        return 1

    def ai(self, t):
        ai_desired_outcome = (len(t["0"]) % 2) + 1
        r = [
            m
            for m in [*t]
            if m not in ["0", "parity", "FINAL"] and t[m].get("parity", None) == 2
        ]
        if r:
            letter = r[randrange(len(r))]
            t = t[letter]
            return letter, t

    def __init__(self):
        with open(r"/Users/benbaily/git/Ghostbusters/Scrabble.txt") as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        self.buildTree(content)
        self.getParity(self.tree)

    def mk_alt_tree(self, tree):
        g = GameTree()
        g.getParity(tree)
        g.tree = tree
        return g


if __name__ == "__main__":
    g = GameTree()
    t = g.tree
    while not t.get("FINAL", False):
        i = input(
            "The word is [{}]. Your move, type a capital letter, or 0 to challenge: ".format(
                t["0"]
            )
        )
        if i == "0":
            while not t.get("FINAL"):
                t = t[[*t][1]]
            print("I was thinking of [{}]. You lose!".format(t["0"]))
            t = g.tree
            break
        if not t.get(i, None) or i in ["0", "parity"]:
            print(
                "[{}{}] is not the prefix of any legal word. I challenge!".format(
                    t["0"], i
                )
            )
            break
        t = t[i]
        if t.get("FINAL"):
            print("You lose! You just spelled the word [{}]!".format(t["0"]))
            t = g.tree
            break
        print("After your addition, the word is now [{}]\n".format(t["0"]))
        letter, t = g.ai(t)
        if not letter:
            print("I lose! Whoops!\n")

        print(
            "I play the letter [{}]. The word now reads [{}]\n".format(letter, t["0"])
        )
    if t.get("FINAL"):
        print("I lose! Whoops!")
