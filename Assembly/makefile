default: build

build: 
	nasm -f elf64 helloworld.asm
	ld helloworld.o -o helloworld

run:
	./helloworld

clean:
	rm -rf *.o helloworld
