conjunto1 = {"aluno1","aluno2","aluno3","aluno4","aluno5"}

conjunto2 = {"aluno11","aluno2","aluno3","aluno7","aluno9"}

uniao={}
uniao=conjunto1.union(conjunto2)
print(uniao)

print("")

intersecao={}
intersecao=conjunto1.intersection(conjunto2)
print(intersecao)

print("")


if "aluno1" in conjunto1:
    print("Aluno existe")
else:
    print("Aluno não existe")
    
    
