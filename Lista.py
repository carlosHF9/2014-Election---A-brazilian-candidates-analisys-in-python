from Node import Node

class Lista:
    def __init__(self):
        self.head = None
        self.size = 0


    def anexar(self, dados): #Anexando de forma duplamente encadeada
        ponteiro = self.head
        if ponteiro:
            while ponteiro.next:
                ponteiro = ponteiro.next
            ponteiro.next = Node(dados)
            ponteiro.next.previous = ponteiro.next
            self.size = self.size +1
        else:
            self.head = Node(dados)
            self.size = self.size +1




    def final(self):
        position = 0
        if self.head:
            ponteiro = self.head
            while ponteiro.next:
                ponteiro = ponteiro.next
                position = position + 1
        return position


    def index_exist(self, indice):
        position = 0
        conclusion = False
        ponteiro = self.head
        if ponteiro:
            while ponteiro.next:
                if indice == position:
                    conclusion = True
                ponteiro = ponteiro.next
                position = position +1
            if indice == position:
                conclusion = True
            return conclusion
        else:
            raise('Index out of range')

    def inserir(self, indice, dados):
        ponteiro = self.head
        position = 0
        if indice == position:
            lado_direito = ponteiro
            self.head = Node(dados)
            auxiliar = self.head
            auxiliar.next = lado_direito
            lado_direito.previous = auxiliar
            self.size = self.size +1

        elif indice == self.final():
            ponteiro = self.head 
            position = 0
            while ponteiro.next and position != self.final() -1:
                ponteiro = ponteiro.next
                position = position +1
            new = Node(dados)
            lado_esquerdo = ponteiro
            lado_direito = ponteiro.next
            lado_esquerdo.next = new
            lado_direito.previous = new
            new.previous = lado_esquerdo
            new.next = lado_direito
            self.size = self.size +1

        elif self.index_exist(indice):
            while ponteiro.next and position != indice-1:
                ponteiro = ponteiro.next
                position = position +1
            new = Node(dados)
            lado_esquerdo = ponteiro
            lado_direito = ponteiro.next
            lado_esquerdo.next = new
            lado_direito.previous = new
            new.next = lado_direito
            new.previous = lado_esquerdo
            self.size = self.size +1
        
        elif self.final() < indice:
            self.anexar(dados)

    def indice(self, dados):
        indice = 0
        indice_data = None
        ponteiro = self.head
        if ponteiro:
            while ponteiro.next:
                if ponteiro.data == dados and indice_data == None:
                    indice_data = indice
                    ponteiro = ponteiro.next
                    indice = indice +1
                if indice_data:
                    return indice_data
                else:
                    raise ValueError('This element is not in list')
            

        else:
            raise ValueError('This element is not in list')

    def getNode(self, posicao):
        position = 0
        ponteiro = self.head
        if ponteiro and posicao <= self.size -1:
            while position != posicao:
                ponteiro = ponteiro.next
                position += 1
            return ponteiro
        else:
            raise IndexError('List index out of range')
        


    def __getitem__(self, posicao):
        ponteiro = self.getNode(posicao)
        if ponteiro:
            return ponteiro.data
        else:
            raise IndexError('List index out of range')
    
    def __setitem__(self, posicao, data):
        ponteiro = self.getNode(posicao)
        if ponteiro:
            ponteiro.data = data
        else:
            raise IndexError('List index out of range') 
        

    
    def tamanho(self):
        return self.size

    def remover(self, indice):
        ponteiro = self.getNode(indice)
        if ponteiro.next != None and ponteiro.previous != None:
            ponteiro = self.getNode(indice -1)
            lado_esquerdo = ponteiro
            lado_direito = ponteiro.next.next
            ponteiro.next.previous = None
            ponteiro.next.next = None
            lado_esquerdo.next = lado_direito
            lado_direito.previous = lado_esquerdo


        elif ponteiro.next and ponteiro.previous == None:
            lado_direito = ponteiro.next
            ponteiro.next = None
            self.head = lado_direito
        elif ponteiro.next == None and ponteiro.previous:
            ponteiro = self.getNode(indice -1)
            ponteiro.next.previous = None
            ponteiro.next = None
    


    def __str__(self):
        if self.head:
            data = '['
            ponteiro = self.head
            while ponteiro.next:
                data = data+str(ponteiro.data)+', '
                ponteiro = ponteiro.next
            data = data+str(ponteiro.data)+']'
            return data      
        else:
            return str([])
    
    def __repr__(self):
        if self.head:
            data = '['
            ponteiro = self.head
            while ponteiro.next:
                data = data+str(ponteiro.data)+', '
                ponteiro = ponteiro.next
            data = data+str(ponteiro.data)+']'
            return data      
        else:
            return str([])

    def __iter__(self):

        def _ponteiro(i):
            while i is not None:
                yield i.data
                i = i.next

        return _ponteiro(self.head)






