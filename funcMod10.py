

def mod10(numero):
   # print numero
   # print type(numero)
    numero = list(numero)
    acumulador = 0
    multAtual = 2
    resto = 0
    resultado =0
    resMulti = 0
    listaNumeros = []
    numeros = []
    while(len(numero) > 0):
        #print acumulador
        numAtual = int(numero.pop())
        resMulti = numAtual * multAtual
        #print str(numAtual)+' X '+str(multAtual)+' = '+str(resMulti)
        numeros = list(str(resMulti))
        listaNumeros += numeros
        if(multAtual == 2):
            multAtual = 1
        else:
            multAtual = 2

    #print listaNumeros

    while(len(listaNumeros) > 0):
        acumulador += int(listaNumeros.pop())
    resto = acumulador % 10
    #print 'resto = '+str(resto)
    if(resto == 0):
        return 0
    else:
        resultado = 10 - resto
        return resultado

##################################################################
#####Desenvolvido por Danilo da Silva Maciel - Aka(Dongutsi)######
##################################################################

##inicio
num = ''
while(num != '0'):
    num = raw_input("Entre com o numero a ger gerado o DV, ou zero(0) para sair\n")
    if(num == '0'):
        print 'Sair?'
        break
    if(num != ''):
        print 'O digito verificador eh: '+str(mod10(num))
    else:
        print 'Digite um numero valido!'
