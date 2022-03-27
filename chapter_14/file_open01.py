fout = open("oops.txt", "wt")
print("Oops, I create a file.", file=fout)
fout.close()

poem_contents = """
나 보기가 역겨워 가실 때에는
말 없이 고이 보내드리오리다.
"""

with open("poem.txt", "wt") as poem:
    poem.write(poem_contents)

