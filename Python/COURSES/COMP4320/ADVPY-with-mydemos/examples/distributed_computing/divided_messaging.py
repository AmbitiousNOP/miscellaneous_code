#!/usr/bin/env python
from mpi4py import MPI


def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    workers = comm.Get_size()

    data = list(range(1000000))

    slice = comm.scatter((data[n::workers] for n in range(workers)), root=0)
    total = sum(slice)
    result = comm.reduce(total, root=0)

    if rank == 0:
        print(result)


if __name__ == '__main__':
    main()
