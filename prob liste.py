lista1=[1,6,8,90,34,2,9,5,4,7]
print("Lista initiala: ", lista1)
lista2=sorted(lista1)
print("Lista sortata in ordine crescatoare: ",lista2)
lista3=sorted(lista1,reverse=True)
print( "Lista in ordine descrescatoare: ",lista3)
print( "Numarul de cifre din lista: ", len(lista1))
print( "Numarul maxim, minim din lista: " ,max(lista1),min(lista1),sep="\n")
lista4=lista1+[111]
print( "Lista +111: " ,lista4)
lista5=lista1
lista5.insert(1, 222)
print(  "Lista cu nr 222 inserat pe pozitia 1: ", lista5)