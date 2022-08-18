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

