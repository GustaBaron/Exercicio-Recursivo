cpf = input("Insira seu CPF")


if "." in cpf:

    cpf.replace(".", "")

elif "-" in cpf:

    cpf.replace("-", "")

if not cpf.isdigit() or len(cpf) != 11:

    raise ValueError("informe seu CPF corretamento:")


cpf_lista = 0


for i in cpf:

    cpf_lista.append(int(i))


primeiro_v, segundo_v = cpf_lista[-2], cpf_lista[-1]


print(primeiro_v)

print(segundo_v)


calculo1 = sum([x * y for x, y in (zip(range(10, 1, -1), cpf_lista[:10]))]) % 11

calculo2 = sum([x * y for x, y in (zip(range(11, 1, -1), cpf_lista[:10]))]) % 11


verificar_pri_dig = 11 - calculo1 if 11 - calculo1 < 10 else 0

verificar_seg_dig = 11 - calculo2 if 11 - calculo2 < 10 else 0


if verificar_pri_dig == cpf_lista[-2] and verificar_seg_dig == cpf_lista[-1]:

    print("CPF Válido")

else:

    print("O CPF informado é Inválido")
