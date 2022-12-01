from pathlib import Path

root = Path(__file__).parent.parent
csv = Path(root, "CubeMain.csv")
txt = Path(r"C:\Program Files (x86)\Diablo II\ProjectD2\data\global\excel\CubeMain.txt")

with open(csv.absolute(), "r") as f:
    raw = f.read()
# with open(txt.absolute(), "w") as f:
#     f.write(raw)
print(csv)
