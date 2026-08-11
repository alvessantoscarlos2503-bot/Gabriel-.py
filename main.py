nome = input("Digite seu nome: ").strip()
idade = int(input("Digite sua idade: "))
idade_minima = 14

print ("\--- VERIFICAÇÃO DE ACESSO ---")

if idade >= idade_minima:
    print(f"{nome}, seu acesso á oficina foi liberado.")
    print("Vcoê já possui idade mínima exigida.")
else:
    anos_faltantes = idade_minma - idade
    print(f"{nome}, seu acesso ainda não foi liberado.")
    print(f"Faltam {anos_faltantes} anos(s) para atingir a idade mínima.")