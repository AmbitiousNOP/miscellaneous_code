#!/usr/bin/env python
from mpi4py import MPI


def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    workers = comm.Get_size()

    if rank == 0:
        data = list(range(1000000))

        for n in range(1, workers):
            comm.send(data[n::workers], dest=n)

        result = 0
        for n in range(1, workers):
            result += comm.recv(source=n)
        print(result)
    else:
        data = comm.recv(source=0)
        total = sum(data)
        comm.send(total, dest=0)


if __name__ == '__main__':
    main()
