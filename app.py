import os

equipamentos = [{"nome":"Halteres", "Categoria":"Peso Livre","ativo": True},
    {"nome":"Esteira", "Categoria":"Cardio","ativo": False},
    {"nome":"Bicicleta Ergométrica", "Categoria":"Cardio","ativo": True}]

def mostra_titulo():
    print("""
██████╗░███████╗██╗░██████╗  ░██████╗░██╗░░░██╗███╗░░░███╗
██╔══██╗██╔════╝██║██╔════╝  ██╔════╝░╚██╗░██╔╝████╗░████║
██████╔╝█████╗░░██║╚█████╗░  ██║░░██╗░░╚████╔╝░██╔████╔██║
██╔══██╗██╔══╝░░██║░╚═══██╗  ██║░░╚██╗░░╚██╔╝░░██║╚██╔╝██║
██║░░██║███████╗██║██████╔╝  ╚██████╔╝░░░██║░░░██║░╚═╝░██║
╚═╝░░╚═╝╚══════╝╚═╝╚═════╝░  ░╚═════╝░░░░╚═╝░░░╚═╝░░░░░╚═╝""")

def mostra_escolhas():
    print("1. Cadastrar Alunos")
    print("2. Listar Alunos")
    print("3. Ativar Alunos")
    print("4. Sair")

def escolhe_opcao():

    def exibir_subtitulo(texto):
        os.system("cls")
        print(texto)
        print(" ")

    def retorna_menu():
        input(" Digite uma tecla para voltar ao menu principal ")
        main()

    def cadastrar_equipamentos():
        exibir_subtitulo("Cadastrar Equipamentos")
        nome_equipamento = input(" Digite o nome do equipamento que deseja cadastrar ")
        categoria_equipamento = input(" Digite a categoria do equipamento ")
        ativo = input(" O equipamento está ativo? (s/n) ").strip().lower() == 's'
        equipamentos.append({"nome": nome_equipamento, "Categoria": categoria_equipamento, "ativo": ativo})
        print(f" O equipamento {nome_equipamento} foi cadastrado com sucesso\n")

        retorna_menu()

    def listar_equipamentos():
        exibir_subtitulo("Lista de Equipamentos Cadastrados")
        for equipamento in equipamentos:
            nome_equipamento = equipamento["nome"]
            categoria_equipamento = equipamento["Categoria"]
            ativo = "Ativo" if equipamento["ativo"] else "Inativo"
            print(f" - {nome_equipamento} | {categoria_equipamento} | {ativo}")

        retorna_menu()

    def ativar_equipamentos():
        exibir_subtitulo("Ativar Equipamentos")
        nome_equipamento = input(" Digite o nome do equipamento que deseja ativar ")
        encontrado = False
        for equipamento in equipamentos:
            if equipamento["nome"].lower() == nome_equipamento.lower():
                if equipamento["ativo"]:
                    print(f"O equipamento {nome_equipamento} já está ativo.")
                else:
                    equipamento["ativo"] = True
                    print(f"O equipamento {nome_equipamento} foi ativado com sucesso.")
                encontrado = True
                break
        if not encontrado:
            print(f"O equipamento {nome_equipamento} não foi encontrado.")
        retorna_menu()

    def finalizar_programa():
        os.system("cls") 
        print("Finalizando o programa\n") 

    def opcao_invalida():
        print("Essa opção não é válida")
        input("Aperte qualquer tecla para voltar")
        main()  

    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_equipamentos()
        elif opcao_escolhida == 2:
            listar_equipamentos()
        elif opcao_escolhida == 3:
            ativar_equipamentos()
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    mostra_titulo()
    mostra_escolhas()
    escolhe_opcao()

if __name__ == "__main__":
    main()
