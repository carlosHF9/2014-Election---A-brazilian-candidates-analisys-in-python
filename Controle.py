from remover_ponto_virgula import remover_virgula
from Lista import Lista
from Bem import Bem
from Candidato import Candidato
from especial_tokenize import new_tokenize

class Controle:
    def __init__(self, caminho_panilha):
        self.__lista_candidatos = None
        self.__bens = {}
        self.__lista_candidatos = Lista()
        arquivo_2 = open(caminho_panilha+'\\bem_candidato_2014\\bem_candidato_2014_PE.csv', 'r')


        for linhas in arquivo_2:
            tokenizado = new_tokenize(linhas)
            try:
                self.__bens[tokenizado[11]].anexar(Bem(tokenizado[6], tokenizado[14], tokenizado[15], tokenizado[16]))
            except:
                self.__bens[tokenizado[11]] = Lista()
                self.__bens[tokenizado[11]].anexar(Bem(tokenizado[6], tokenizado[14], tokenizado[15], tokenizado[16]))
        arquivo_2.close()



        arquivo = open(caminho_panilha+'\\consulta_cand_2014\\consulta_cand_2014_PE.csv', 'r')
        for linhas in arquivo:
            tokenizado = new_tokenize(linhas)
            self.__lista_candidatos.anexar(Candidato(tokenizado[2], tokenizado[10], tokenizado[14], tokenizado[17], tokenizado[15], tokenizado[16], tokenizado[20], tokenizado[18], tokenizado[27], tokenizado[28], tokenizado[13], tokenizado[14], tokenizado[38], tokenizado[42], tokenizado[44], tokenizado[46], tokenizado[35], tokenizado[37], tokenizado[54], tokenizado[53], tokenizado[14], tokenizado[13]))
        self.__lista_candidatos.remover(0)



        for candidatos in self.__lista_candidatos:
            try:
                candidatos.alterarListaBens(self.__bens[candidatos.getID()])
            except:
                candidatos.alterarListaBens(None)

            if candidatos.getListaBens():
                for bens in candidatos.getListaBens():
                    if bens is not None:
                        try:
                            candidatos.alterarTotalDeclarado(float(remover_virgula(bens.getValorBem())))
                        except:
                            pass
                    else:
                        pass
    def getLista(self):
        return self.__lista_candidatos
    








        








                











        def getBens(self):
            return self.__bens

        def getListaCandidatos(self):
            return self.__lista_candidatos







        """arquivo = open(caminho_panilha+'\\consulta_cand_2014\\consulta_cand_2014_BRASIL.csv', 'r')

        for linhas in arquivo:
            tokenizado = new_tokenize(linhas)
            self.__lista_candidatos.anexar(Candidato(tokenizado[2], tokenizado[10], tokenizado[14], tokenizado[17], tokenizado[15], tokenizado[16], tokenizado[20], tokenizado[18], tokenizado[27], tokenizado[28], tokenizado[49], tokenizado[50], tokenizado[38], tokenizado[42],tokenizado[44],tokenizado[46],tokenizado[35],tokenizado[37], None, tokenizado[2],tokenizado[23], None, tokenizado[14], tokenizado[13]))
        arquivo.close()""

    def getCandidatos(self):
        return self.__lista_candidatos"""





        



                                                                                                                                                                                                                                                                                                                                                                                                                                                                      #    [2][10][14][17][15][16][20][18][27][28][49][50][38][42][44][46][35][37][x][23][outro arquivo][14][13]




        
        
        

        