.data

	equilatero:	.asciiz "equilatero"
	isosceles:	.asciiz "isosceles"
	escaleno:	.asciiz "escaleno"

.text
.globl main

main:
#Leitura do valor do primeiro lado
	li $v0, 5
	syscall
	
	move $t0, $v0

#Leitura do valor do segundo lado
	li $v0, 5
	syscall
	
	move $t1, $v0
	
#Leitura do valor do terceiro lado
	li $v0, 5
	syscall
	
	move $t2, $v0
	
#Checagem equilatero
if1:
	bne $t0, $t1, else1	#Se os lados forem diferentes, não é equilatero
	bne $t0, $t2, else1	
	
	li $v0, 4
	la $a0, equilatero
	syscall
	
	j end_if
else1:
	beq $t0, $t1, else2
	beq $t1, $t2, else2
	beq $t2, $t0, else2
	
	li $v0, 4
	la $a0, escaleno
	syscall
	
	j end_if
else2:
	li $v0, 4
	la $a0, isosceles
	syscall
end_if:
	