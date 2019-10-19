if __name__ == "__main__":
    with open(r"/Users/benbaily/git/Ghostbusters/Scrabble.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content if len(x) > 4]
    content = {"".join(sorted(x)) for x in content}
    count = 0
    for c in content:
        count += 2 ** len(c)
        count -= 1
    print(count)

