#função para gravar dados no arquivo
def gerarListaOrdenada():
    quantidade = 101
    arquivo=open('crescente.txt','w')
 #gerar registro com os números
    for elemento in range(quantidade):
        arquivo.write(str(elemento)+';')
    arquivo.close()
 
def lerlistas():
    arquivo = open('crescente.txt','r')
    conteudo = arquivo.read()
    print(conteudo)


gerarListaOrdenada()
lerlistas()