"""

"""


def gen_pres(file_path):
    with open(file_path) as fp:
        for line in fp:
            yield (i for i in line.split(":")[1:3])


for line in gen_pres(file_path="/home/cjpenn/miscellaneous_code/Python/COURSES/COMP4320/ADVPY-with-mydemos/data/presidents.txt"):
    print(*line)
