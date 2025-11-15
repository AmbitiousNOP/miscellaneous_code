#!/usr/bin/env python
from mpi4py import MPI


def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    # Create a 4x4 "grid" of processes
    cartesian = comm.Create_cart(dims=(4, 4), periods=(False, False),
                                 reorder=True)
    coords = cartesian.Get_coords(rank)

    print(f'In 2D topology, {rank} handles {coords}')


if __name__ == '__main__':
    main()
