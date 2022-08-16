class Node:
    def __init__(self, dado=None, tamanho=0):
        self.dado = dado
        self.tamanho = tamanho
        self.filhos = []

    def insert(self, raiz, dado, tamanho):
        if raiz.dado is None:
            raiz.dado = dado
            raiz.tamanho = tamanho
        else:
            if len(raiz.filhos) < raiz.tamanho:
                raiz.filhos.append(Node(dado, tamanho))
            else:
                for i in raiz.filhos:
                    if len(i.filhos) < i.tamanho:
                        self.insert(i, dado, tamanho)
                        break
                    else:
                        continue

    def mostra(self, raiz, alt=0):
        if raiz.dado is not None:
            print(alt * '__', end='')
            print(raiz)
            for i in raiz.filhos:
                self.mostra(i, alt+1)


if __name__ == '__main__':

    raiz = Node()

    while True:
        entrada = input()

        if entrada == 'gametree':
            raiz.mostra(raiz)
            break
        elif entrada == 'probtree':
            break
        else:
            entrada = entrada.split()
            raiz.insert(raiz, entrada[0], int(entrada[1]))

