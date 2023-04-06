"""
Jogo do NIM
"""


def ler_opcao_de_jogo():
    """
    funcao que ler a opcao do jogo
    """
    try:
        return int(input("""Bem-vindo ao jogo do NIM! Escolha:\n\n
1 - para jogar uma partida isolada
2 - para jogar um campeonato """))
    except ValueError:
        return None
    except TypeError:
        return None


def ler_dado(msg):
    """
    Funcao que ler um dado
    """
    try:
        return int(input(msg))
    except ValueError:
        return None
    except TypeError:
        return None


def verificar_validade_da_opcao_de_entrada(valor):
    """
    Função que verifica a validade da opcao 
    """
    if valor is not None and (valor == 1 or valor == 2):
        return True
    return False


def verificar_validade_da_entrada(valor):
    """
    funcao que verifica a validade da entrada
    """
    if valor is not None and valor > 0:
        return True
    return False


def verificar_inicio_da_partida(total, limite):
    """
    verifica inicio da partida
    """
    if (total % (limite+1)) == 0:
        return True
    return False


def imprimir_quantidade_de_pecas_restantes(total, retiradas):
    """
    funcao que imprime a quantidade de pecas restantes
    """
    if total - retiradas > 1:
        imprimir_mensagem(
            f"Agora restam {total - retiradas} peças no tabuleiro.")
    else:
        imprimir_mensagem("Agora resta apenas uma peça no tabuleiro.")


def computador_escolhe_jogada(total, retiradas):
    """
    Funcao computador escolhe jogada
    """
    # retorno: devolver o numero de pecas removidas da jogada
    removidas = 0  # pecas a serem removidas
    if total > 1:
        if total > retiradas:
            removidas = retiradas
        else:
            removidas = total
        imprimir_mensagem(f"\nO computador tirou {removidas} peças.")
    elif total == 1:
        if total == retiradas:
            removidas = retiradas
        else:
            removidas = total
        imprimir_mensagem("\nO computador tirou uma peça.")
    return removidas


def usuario_escolhe_jogada(total, limite):
    """
    funcao em que o usuario escolhe a jogada
    """
    retiradas = ler_dado("\nQuantas peças você vai tirar? ")
    while retiradas > limite:
        imprimir_mensagem("\nOops! Jogada inválida! Tente de novo.")
        retiradas = ler_dado("\nQuantas peças você vai tirar? ")

    removidas = 0  # pecas a serem removidas
    if total > 1:
        if total > retiradas:
            removidas = retiradas
        else:
            removidas = total
        imprimir_mensagem(f"\nvoce tirou {removidas} peças.")
    elif total == 1:
        if total == retiradas:
            removidas = retiradas
        else:
            removidas = total
        imprimir_mensagem("\nvoce tirou uma peça.")
    return removidas


def partida():
    """
    funcao que dá a partida do jogo
    """
    quem_jogou = ""
    # ler o numero de pecas inicial
    total = ler_dado("\nQuantas peças? ")
    while not verificar_validade_da_entrada(total):
        total = ler_dado("\nQuantas peças? ")
        # ler o numero maximo de pecas

    removidas = ler_dado("Limite de peças por jogada? ")
    while not verificar_validade_da_entrada(removidas):
        removidas = ler_dado("Limite de peças por jogada? ")

    if verificar_inicio_da_partida(total, removidas):
        imprimir_mensagem("\nVocê começa!")
    else:
        imprimir_mensagem("\nComputador começa!")

    while total > 0:
        # decide quem inicia o jogo
        if verificar_inicio_da_partida(total, removidas):
            # recebe o numero de pecas removidas da jogada
            n_pecas_removidas = usuario_escolhe_jogada(total, removidas)
            quem_jogou = "usuario"
        else:
            n_pecas_removidas = computador_escolhe_jogada(total, removidas)
            quem_jogou = "computador"

        if total - n_pecas_removidas > 0:
            imprimir_quantidade_de_pecas_restantes(total, n_pecas_removidas)

        # atualiza o valor de n de acordo com o numero de pecas removidas
        total -= n_pecas_removidas

    # verificar se o jogo acabou quando n == 0
    if quem_jogou == "computador":
        imprimir_mensagem("Fim do jogo! O computador ganhou!")
    else:
        imprimir_mensagem("Fim do jogo! você ganhou!")
    return quem_jogou


def formatar_mensagem_da_rodada(i):
    """
    funcao para formatar mensagem da rodada.
    """
    return f'\n**** Rodada {i} ****'


def campeonato():
    """
    funcao que faz a chamada da funcao formatar a mensagem da rodada.
    """
    contabiliza_vitorias_computador = 0
    for i in range(3):
        imprimir_mensagem(formatar_mensagem_da_rodada(i+1))
        quem_jogou = partida()
        if quem_jogou == "computador":
            contabiliza_vitorias_computador += 1
    return contabiliza_vitorias_computador


def formatar_mensagem_da_opcao(opcao):
    """
    funcao que formata a mensagem da opcao
    """
    if opcao == 1:
        msg = "um partida isolada"
    else:
        msg = "um campeonato"
    return f'\nVocê escolheu {msg}!'


def formatar_memsagem_final(total, vitorias):
    """
    funcao que formata a mensagem final do programa
    """
    return f'\nPlacar: Você {total - vitorias} X {vitorias} Computador'


def imprimir_mensagem(msg):
    """
    imprimir mensagem
    """
    print(msg)


def main():
    """
    funcao principal 
    """
    vitorias = 0
    opcao = ler_opcao_de_jogo()
    while not verificar_validade_da_opcao_de_entrada(opcao):
        opcao = ler_opcao_de_jogo()
    imprimir_mensagem(formatar_mensagem_da_opcao(opcao))
    if opcao == 1:
        total = 1
        quem_jogou = partida()
        if quem_jogou == "computador":
            vitorias += 1
    else:
        total = 3
        vitorias += campeonato()
        imprimir_mensagem("\n**** Final do campeonato ****")
    imprimir_mensagem(formatar_memsagem_final(total, vitorias))


if __name__ == "__main__":
    main()
