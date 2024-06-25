.data
	
	sim:		.asciiz "sim"
	nao:		.asciiz	"nao"
	
.text
.globl main

main:
#Leitura da idade
	li	$v0, 5		#Leitura de inteiro
	syscall
	
	move	$t0, $v0	#Aloca a idade em t0

#Leitura do tempo de serviço
	li	$v0, 5		#Leitura de inteiro
	syscall
	
	move	$t1, $v0	#Aloca o tempo de serviço em t1
	
#Condições
if1:
	slti	$t2, $t0, 65	#Se idade for maior que 65, t2 = 0
	beq	$t2, $zero, then
if2:
	slti	$t2, $t1, 35	#Se tempo de serviço for maior que 35, t2 = 0
	beq	$t2, $zero, then
if3:
	slti	$t2, $t0, 60	#Se idade for maior que 60, t2 = 0
	beq	$t2, $zero, if4	#Se a idade for maior, vai pro if do tempo de serviço
	j	else		#Se for menor, vai pro else
if4:
	slti	$t2, $t1, 30	#Se tempo de serviço for maior que 30, t2 = 0
	beq	$t2, $zero, then
	j	else
#Resposta negativa
else:
	li	$v0, 4
	la	$a0, nao
	syscall
	j	end_if
#Resposta positiva
then:
	li	$v0, 4
	la	$a0, sim
	syscall

end_if:
