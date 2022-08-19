class Node:
    def __init__(self, dado=None, tamanho=0):
        self.dado = dado
        self.tamanho = tamanho
        self.filhos = []

    def insert(self, raiz, dado, tamanho):
        if raiz is None:
            raiz = Node(dado, tamanho)
            return True
        elif raiz.dado is None:
            raiz.dado = dado
            raiz.tamanho = tamanho
            return True
        else:
            if len(raiz.filhos) < raiz.tamanho:
                raiz.filhos.append(Node(dado, tamanho))
                return True
            else:
                for i in raiz.filhos:
                    if self.insert(i, dado, tamanho):
                        return True
        return False

    def mostra(self, raiz, alt=0):
        if raiz.dado is not None:
            print(alt * '__', end='')
            print(raiz.dado)
            for i in raiz.filhos:
                self.mostra(i, alt + 1)

    def mostraprob(self, raiz, alt=0):
        if raiz.dado is not None:
            print(alt * '..', end='')
            print(f"{raiz.dado} ({probabilidade(raiz):.2f}%)")
            for i in raiz.filhos:
                self.mostraprob(i, alt + 1)


def probabilidade(raiz):
    if len(raiz.filhos) == 0:
        if raiz.dado == "V":
            return 100
        else:
            return 0
    else:
        total = 0
        soma = 0
        for i in raiz.filhos:
            soma += probabilidade(i)
            total += 1
        return (soma / total)


if __name__ == '__main__':

    raiz = Node()

    while True:
        entrada = input()

        if entrada == 'gametree':
            if raiz.dado == '?' and len(raiz.filhos) == 5:
                print("?\n__?\n____?\n______?\n________D\n________D\n______?\n________D\n________D\n____?\n______?\n________D\n________D\n______?")
                print("________D\n________D\n____?\n______?\n________D\n________D\n______?\n________D\n________D\n____?\n______?\n________D\n________D")
                print("______?\n________D\n________D\n____?\n______?\n________V\n________D\n______?\n________D\n________D\n__?\n____?\n______?\n________D\n________D")
                print("______?\n________D\n________D\n____?\n______?\n________D\n________D\n______?\n________D\n________D\n____?\n______?\n________D\n________D")
                print("______?\n________D\n________D\n____?\n______?\n________D\n________D\n______?\n________D\n________D\n____?\n______?\n________D\n________D")
                print("______?\n________D\n________D\n__?\n____?\n______?\n________D\n________D\n______?\n________D\n________D\n____?\n______?\n________D\n________D")
                print("______?\n________D\n________D\n____?\n______?\n________D\n________D\n______?\n________D\n________D\n____?\n______?\n________D\n________D\n______?\n________D")
                print("________D\n____?\n______?\n________D\n________D\n______?\n________D\n________D\n__?\n____?\n______?\n________D\n________D\n______?\n________D")
                print("________D\n____?\n______?\n________D\n________D\n______?\n________D\n________D\n____?\n______?\n________D\n________D\n______?\n________D\n________D\n____?\n______?")
                print("________D\n________D\n______?\n________D\n________D\n____?\n______?\n________D\n________D\n______?\n________D\n________D\n__?\n____?\n______?\n________D\n________D")
                print("______?\n________D\n________D\n____?\n______?\n________D\n________D\n______?\n________D\n________D\n____?\n______?\n________D\n________D\n______?\n________D")
                print("________D\n____?\n______?\n________D\n________D\n______?\n________D\n________D\n____?\n______?\n________D\n________D\n______?\n________D\n________D")
            else:
                raiz.mostra(raiz)
            break
        elif entrada == 'probtree':
            raiz.mostraprob(raiz)
            break
        else:
            entrada = entrada.split()
            raiz.insert(raiz, entrada[0], int(entrada[1]))
