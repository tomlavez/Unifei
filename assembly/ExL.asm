.data
# declara um array de 16 bytes (4 numeros)
A:	.space	16
# declara um array de 24 bytes (6 numeros)
B:	.space	24

.text
.globl main
main:
	
	# le o primeiro vetor
	jal	leituraA
	
	# le o segundo
	jal	leituraB
	
	# encontra elementos em comum
	jal	elementos_comum
	
	# move o resultado para a0
	move	$a0, $v0
	
	# Imprimir o resultado
   	li $v0, 1
   	syscall
	
	# Finaliza o programa
	li	$v0, 10
	syscall
	
.data
.text
leituraA:
	# declara variaveis
	li	$t0, 0	# i
	li	$t1, 4	# n
loopA:
	# Lê um inteiro
	li $v0, 5
	syscall
	
	# Aloca o valor no array
	sw	$v0, A($t0)
	
	# Move o i para a proxima posição
	addi	$t0, $t0, 4
	
	# contagem
	subi	$t1, $t1, 1
	
	# verifica se ja foram lidos os N numeros
	bgtz	$t1, loopA
	
	# return
	jr	$ra

.data
.text
leituraB:
	# declara variaveis
	li	$t0, 0	# i
	li	$t1, 6	# n
loopB:
	# Lê um inteiro
	li $v0, 5
	syscall
	
	# Aloca o valor no array
	sw	$v0, B($t0)
	
	# Move o i para a proxima posição
	addi	$t0, $t0, 4
	
	# contagem
	subi	$t1, $t1, 1
	
	# verifica se ja foram lidos os N numeros
	bgtz	$t1, loopB
	
	# return
	jr	$ra
	
.data
.text
elementos_comum:
	la	$t0, A	# endereço base de A
	li	$t2, 4	# tamanho de A
	li	$t4, 0	# contagem
loop_maior:
	blez	$t2, end_loop_common
	lw	$t5, 0($t0)	# carrega o elemento de A
	addi	$t0, $t0, 4	# move pro prox elemento de A
	subi	$t2, $t2, 1	# contabiliza
	
	la	$t1, B	# reinicia a base de B
	li	$t3, 6	# reinicia o tamanho de B
loop_menor:
	blez	$t3, loop_maior
	lw	$t6, 0($t1)	# carrega o elemento de B
	addi	$t1, $t1, 4	# move pro prox elemento de B
	subi	$t3, $t3, 1	# contabiliza
	
	beq	$t6, $t5, incremento_common
	j	loop_menor
incremento_common:
	addi	$t4, $t4, 1	# contagem = contagem + 1
	j	loop_maior
	
end_loop_common:
	move	$v0, $t4	
	jr	$ra	# retorna a contagem
	
	
	
	