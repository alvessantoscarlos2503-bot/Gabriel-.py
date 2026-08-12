nome = input("Digite o nome do aluno:).strip()
nota1 = float(input("Digite a primeira nota: ").replace(",", "."))
nota2 = float(input("Digite a segunda nota: ").replace(",","."))

media = (nota1 + nota2) / 2
          
if media >= 7:
             situacao = "Aprova"
elif media >= 5:
             situcao = "Recuperação"
else:
             situcao = "Reprovado"
            
print("\n--- RESULTADO ESCOLAR ---")
prin(f"Aluno: {nome})
print(f"Média: {media: .1f}")
print(f"Situação: {situcao}")
     