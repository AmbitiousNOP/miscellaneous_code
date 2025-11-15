#!/usr/bin/env python

def main():
    
    areas = [2.345, 5.676, 4,345, 8.456]
    
    result = list(map(round, areas, range(1, len(areas))))
    
    print(result)
    print(areas)
    
    print (  list(map(round, areas, range(1, 4))) )
    
if __name__ == "__main__":
    main()