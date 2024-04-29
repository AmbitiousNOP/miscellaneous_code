; get systems current IP address

SECTION .data
error_msg: db "Propper usage: ./ip_retr <domain>", 0Ah
.error_len: equ $ - error_msg

prefix_msg: db "Your IP is: "
.prefix_len: equ $ - prefix_msg

new_line: db 0Ah
.new_line_len: equ $ - new_line


SECTION .text
global _start


_start:
	;---------------- pull the cmd args from the stack to registers
	pop rsi		; pops top of stack
	pop rsi		; pops argc
	pop rsi		; pops argv[1]
	cmp rsi, 0	; if rsi is 0 then user didnt pass argv[1]
	je no_args

	;--------------- store argv[1] in different registry
	mov r8, rsi

	;---------------- calc the length of the string
	xor rcx, rcx	; make rcx 0
	call calc_strlen	; run calc_strlen (pushes program position to stack for ret)

	;---------------- print the string with length buffer
	mov rax, 1	; write syscall
	mov rdi, 1	; file descriptior
	mov rsi, prefix_msg
	mov rdx, prefix_msg.prefix_len ; size of string
	syscall
	
	mov rax, 1
	mov rdi, 1
	mov rsi, r8
	mov rdx, r9
	syscall

	mov rax, 1
	mov rdi, 1
	mov rsi, new_line
	mov rdx, new_line.new_line_len
	syscall


	;---------------- syscall for program exit
	mov rax, 60
	mov rdi, 0
	syscall


calc_strlen:
	cmp byte[rsi + r9], 0	; compare if the string[i] is a null character (0)
	jz exitfromRoutine	; if zero jump to exit 
	inc r9			; increment rcx so we can get the next char in string
	jmp calc_strlen		; re-run this function

no_args:
	mov rax, 1 ; write syscall 
	mov rdi, 1 
	mov rsi, error_msg
	mov rdx, error_msg.error_len
	syscall

	mov rax, 60	; syscall for exit
	mov rdi, 1	; error code
	syscall

exitfromRoutine:
	ret	; pops stack to return to proper position in _start
