def remove_repetidos(lista):
	l = []
	for i in lista:
		if i not in l:
			l.append(i)
	l.sort()
	return l

def existe_caminho(l,e,s):
	meu_set=set(l)
	if e > s:
		maior = e
		menor = s
	else:
		maior = s
		menor = e
	f=[]
	for i in range(menor,maior+1):
		f.append(i)
	meu_set2= set(f)
	cont=0
	for i in range(len(f)):
		if f[i] in meu_set.intersection(meu_set2):
			cont+=1
	if cont == len(f):
		return True 
	else:
		return False
		
def dijkstra_path(dic, origem, fim):
	controle = { }
	distanciaAtual = { }
	noAtual = { }
	naoVisitados = []
	atual = origem
	noAtual[atual] = 0
	for vertice in dic.keys():
		naoVisitados.append(vertice)    
		distanciaAtual[vertice] = float('inf') 
	distanciaAtual[atual] = [0,origem] 
	naoVisitados.remove(atual)
	while naoVisitados:
		for vizinho, peso in dic[atual].items():
			pesoCalc = peso + noAtual[atual]
			if distanciaAtual[vizinho] == float("inf") or distanciaAtual[vizinho][0] > pesoCalc:
				distanciaAtual[vizinho] = [pesoCalc,atual]
				controle[vizinho] = pesoCalc
		if controle == {} : break    
		minVizinho = min(controle.items(), key=lambda x: x[1])
		atual=minVizinho[0]
		noAtual[atual] = minVizinho[1]
		naoVisitados.remove(atual)
		del controle[atual]
	return distanciaAtual[fim][0]

dic={}
t=int(input())
caso=1
while t > 0: 
	n,m,s,e= input().split(" ")
	n=int(n)
	m=int(m)
	s=int(s)
	e=int(e)
	t-= 1
	l=[]
	l2=[]
	for i in range(m):
		a,b,d= input().split(" ")
		a=int(a)
		b=int(b)
		d=int(d)
		l.append(a)
		l.append(b)
		if a < b:
			c=a,b,d
		else:
			c=b,a,d
		l2.append(c)
	lista = remove_repetidos(l)
	for i in range(len(lista)):
		dic[lista[i]]={}
		for j in range(len(l2)):
			if l2[j][0] == lista[i]:
				dic[lista[i]][l2[j][1]]=l2[j][2]
	if m < 1 or existe_caminho(lista,e,s) == False:
		print("Case #%d: unreachable\n" % (caso))
		caso+=1
	else:
		if e > s:
			print("Case #{}: {}\n".format(caso,dijkstra_path(dic, s, e)))
			caso+=1
		else:
			print("Case #%{}: {}\n".format(caso,dijkstra_path(dic, e, s)))
			caso+=1

