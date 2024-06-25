.data
# declara um array de 24 bytes (6 numeros)
array:	.space	24
.text
.globl main
main:
	# Chama a função de leitura
	jal	leitura

	# imprime o maior valor
	jal	maior
	
	# move o maior para a0
	move	$a0, $v0
	
	# imprime o maior
	li	$v0, 1
	syscall
	
	# Finaliza o programa
	li $v0, 10
	syscall
.data
.text
leitura:
	# declara variaveis
	li $t0, 0	# i
	li $t1, 6	# n
loop:
	# Lê um inteiro
	li $v0, 5
	syscall
	
	# Aloca o valor no array
	sw	$v0, array($t0)
	
	# Move o i para a proxima posição
	addi	$t0, $t0, 4
	
	# contagem
	subi	$t1, $t1, 1
	
	# verifica se ja foram lidos os N numeros
	blez	$t1, end_loop
	j	loop
end_loop:
	# return
	jr	$ra
	
.data
.text
maior:
	# declara variaveis
	li	$t0, 0	# i
	li	$t1, 6	# n
	
	# Le o primeiro valor, aloca em t2
	lw	$t2, array
	
	# Define como maior
	add	$t3, $zero, $t0
	
loop_maior:
	# Move o i para a proxima posição
	addi	$t0, $t0, 4
	
	# Contabiliza
	subi	$t1, $t1, 1

	# checagem se ja verificou todos os numeros
	blez	$t1, fim_maior
	
	# Le o valor
	lw	$t2, array($t0)
	
	# Se for menor, volta pro começo do loop
	blt	$t2, $t3, loop_maior
	
	# Atualiza o maior
	move	$t3, $t2
	
	# volta pro loop
	j	loop_maior
fim_maior:
	# move o maior para v0
	move	$v0, $t3
	jr	$ra
	
	