section .text
global _start

_start:
	;---------------- pull the cmd args from the stack to registers
	pop rsi
	pop rsi
	pop rsi
	
	;---------------- calc the length of the string
	xor rcx, rcx		; make rcx 0
	call calc_strlen	; run calc_strlen (pushes program position to stack for ret)

	;---------------- print the string with length buffer
	mov rax, 1	; write syscall
	mov rdi, 1	; file descriptior
	mov rdx, rcx ; size of string
	syscall

	;---------------- syscall for program exit
	mov rax, 60
	mov rdi, 0
	syscall

calc_strlen:
	cmp byte[rsi + rcx], 0	; compare if the string[i] is a null character (0)
	jz exitfromRoutine	; if zero jump to exit 
	inc rcx			; increment rcx so we can get the next char in string
	jmp calc_strlen		; re-run this function



exitfromRoutine:
	ret	; pops stack to return to proper position in _start
