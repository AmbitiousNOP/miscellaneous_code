#!/usr/bin/env python
from mpi4py import MPI


def main():
    comm = MPI.COMM_WORLD
    print(f'Inside rank {comm.Get_rank()})


if __name__ == '__main__':
    main()
