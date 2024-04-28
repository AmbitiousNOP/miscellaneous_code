SECTION .rodata
msg: db 'Hello World!!!', 0Ah	; storing string in read only data section with new line

; assemble time constant.
; cacl len = string length. subtract addr of the start of the string from the current position ($).
.len: equ $ - msg

SECTION .text
global _start

_start: 
	; syscall: https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md
	mov rax, 1 ; write syscall 
	mov rdi, 1 
	mov rsi, msg
	mov rdx, msg.len
	syscall

	mov rax, 60 ; exit syscall
	mov rdi, 0 ; error code
	syscall


