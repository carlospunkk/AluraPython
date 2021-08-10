#Para isso, preciso armazenar os números dos contatos. A princípio, podemos pensar em usar uma lista:
#Telefones=['92954166','98543762','89275345','87453264']

#teste
#print(Telefones)
#print()

#saida ['92954166', '98543762', '89275345', '87453264']

#Precisamos, de algum modo, conectar os telefones a seus respectivos contatos. 
# Já conhecemos um tipo que pode nos ajudar com isso [a tupla]
'''contato = ('Carlos','92954166')'''

#Para não precisarmos de uma variável para cada contato, 
# podemos colocá-los direto em uma lista de contatos:
#contatos_lista=[('carlos , 92954166'),('richard ','98543762 '),('Lucas','89275345'),('Paloma','87453264')]
#Ok! Se quisermos acessar o número de telefone do Richard, podemos fazer:
#print(contatos_lista[1][0])
#print()

'''Mapeando contatos com um dicionário'''
#Esse tipo de estrutura é muito utilizado em diversas linguagens de programação (mas normalmente tem outro nome, 
# como [array associativo](https://pt.wikipedia.org/wiki/Vetor_associativo).
#  Com ela, conseguimos ter um comportamento parecido com o de dicionários.
#Bem, vamos falar para o Python criar um desses dicionários para a gente. No Python, usamos chaves ({}) para construir nossos dicionários
# . Neste caso, falamos para o Python, que a chave 
# 'carlos' possuí (:) o valor 1234-5678 como seu telefone:

#dict - de fato um dicionário. Mas será que vamos ter que redigitar todos os dados de contatos 
# que já colocamos em nossa lista de contatos? Também podemos criar um dicionário usando sua 
# função construtora dict() e passando, como parâmetro, uma lista de tuplas, como em nosso caso:
contatos_lista=[('carlos' , '92954166'),('richard ','98543762 '),('Lucas','89275345'),('Paloma','87453264')]
contato = dict(contatos_lista)
#print(contato['carlos'])#acessei o telefone do Carlos 

'''Método GET()'''
#Os dicionários possuem um método específico para busca de valores, o get(), 
# no qual podemos passar como parâmetros a chave que queremos e um valor padrão 
# para retornar caso essa chave não seja encontrada:
print(contato.get('carlos','contato não encontrado'))#se caso não encontrar o telefone do carlos aparece a mensagem 'contato não encontrado' se caso aparecer aparece o numero de telefone dele. 
print(contato.get('joão','contato não encontrado'))

'''Também podemos verificar se um contato está em nosso 
    dicionário através da palavra chave in:'''
    #print('Yan' in contato)# existe yan em contato / se sim aparece true 
    #print('53435346' in contato)# da mesma forma com o valor pode ser feita essa busca mas lembrando de usar o .values()
    #print('53435346' in contato.values())#dessa forma aparece valor true
    #Acontece que o in, usado dessa forma, verifica apenas as chaves do dicionário, 
    # não os valores. Para obtermos valores, 
    # podemos usar o método values():
