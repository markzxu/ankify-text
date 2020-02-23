import argparse

def process(of, lines, n=3):
    for i, l in enumerate(lines):
        if l == "" or i == 0: continue
        of.write("<br>".join(lines[max(0, i - n):i]) + 
                "<br>{{c1::" + l + "}}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--infile", type=str)
    parser.add_argument("--outfile", type=str)
    parser.add_argument("--n", type=int, default=3)
    args = parser.parse_args()
    with open(args.outfile, "w") as of:
        lines = [line.strip() for line in open(args.infile, 'r').readlines()]
        process(of, lines, args.n)

