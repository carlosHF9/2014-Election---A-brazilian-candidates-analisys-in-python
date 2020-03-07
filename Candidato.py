from Bem import Bem
from Lista import Lista
from especial_tokenize import new_tokenize

class Candidato:
    def __init__(self, ano, sigla, descricao, nome, ID, numero_urna, CPF, nome_urna, numero_partido, sigla_partido, codigo_ocupacao, descricao_ocupacao, data_nascimento, sexo, grau_intrucao, estado_civil, uf_nascimento, municipio_nascimento, situacao_pos_pleito, situacao_candidatura,  cargo, codigo_cargo):
        self.__ano_eleicao = ano
        self.__sigla_uf = sigla
        self.__descricao = descricao
        self.__nome = nome

        self.__ID = ID
        self.__numero_urna = numero_urna
        self.__CPF = CPF
        self.__nome_urna = nome_urna

        self.__numero_partido = numero_partido
        self.__sigla_partido = sigla_partido
        self.__codigo_ocupacao = codigo_ocupacao
        self.__descricao_ocupacao = descricao_ocupacao


        self.__data_nascimento = data_nascimento
        self.__sexo = sexo
        self.__grau_intrucao = grau_intrucao
        self.__estado_civil = estado_civil
        
        self.__uf_nascimento = uf_nascimento
        self.__municipio_nascimento = municipio_nascimento
        self.__situacao_pos_pleito = situacao_pos_pleito
        self.__situacao_candidatura = situacao_candidatura

        self.__lista_bens = None
        self.__cargo = cargo
        self.__codigo_cargo = codigo_cargo
        self.__total_declarado = 0.0




        
    def __str__(self):
        return 'Nome: {} -- Número: {} -- Sigla: {}\nCargo: {}({}) Nascimento:{} ({})\nResumo dos bens:\n      -Total declarado: R${}\n      -Total por tipo de bem: R${}'.format(self.__nome_urna, self.__numero_urna, self.__sigla_partido, self.__cargo, self.__sigla_uf, self.__municipio_nascimento, self.__uf_nascimento, self.__total_declarado, 'None')



    def __repr__(self):
        return 'Nome: {} -- Número: {} -- Sigla: {}\nCargo: {}({}) Nascimento:{} ({})\nResumo dos bens:\n      -Total declarado: R${}\n      -Total por tipo de bem: R${}'.format(self.__nome_urna, self.__numero_urna, self.__sigla_partido, self.__cargo, self.__sigla_uf, self.__municipio_nascimento, self.__uf_nascimento, self.__total_declarado, 'None')
    


    def comparar(self, **kwargs):
        pass
    
    def getAno(self):
        return 'Ano de eleição: {}'.format(self.__ano_eleicao)
    
    def alterarAno(self, novo_ano):
        self.__ano_eleicao = novo_ano
        return 'O ano de eleição foi alterado para: {}'.format(self.__ano_eleicao)
    
    def getSiglaUF(self):
        return self.__sigla_partido
    
    def alterarSiglaUF(self, nova_sigla):
        self.__sigla_partido = nova_sigla


    def getDescricao(self):
        return self.__descricao
    
    def alterarDescricao(self, descricao):
        self.__descricao = descricao

    
    def getNome(self):
        return self.__nome
    
    def alterarNome(self, dados):
        self.__nome = dados

    
    def getID(self):
        return self.__ID
    
    def alterarID(self, dados):
        self.__ID = dados

    
    def getNumeroUrna(self):
        return self.__numero_urna 
    
    def alterarNumeroUrna(self, dados):
        self.__numero_urna = dados


    
    def getCPF(self):
        return self.__CPF


    
    def alterarCPF(self, dados):
        self.__CPF = dados

    
    def getNomeUrna(self):
        return self.__nome_urna


    
    def alterarNomeUrna(self, dados):
        self.__nome_urna = dados


    def getNumeroPartido(self):
        return self.__numero_partido


    def alterarNumeroPartido(self, dados):
        self.__numero_partido = dados


    def getSiglaPartido(self):
        return self.__sigla_partido


    def alterarSiglaPartido(self, dados):
        self.__sigla_partido = dados


    def getCodigoOcupacao(self):
        return self.__codigo_ocupacao


    def alterarCodigoOcupacao(self, dados):
        self.__codigo_ocupacao = dados


    def getDescricaoOcupacao(self):
        return self.__descricao_ocupacao
 
    
    def alterarNONE(self, dados):
        self.__descricao_ocupacao = dados


    def getDataNascimento(self):
        return self.__data_nascimento
        
    
    def alterarNONE(self, dados):
        self.__data_nascimento = dados


    def getSexo(self):
        return self.__sexo
    
    def alterarNONE(self, dados):
        self.__sexo = dados


    def getGrauInstrucao(self):
        return self.__grau_intrucao
        
    
    def alterarGrauInstrucao(self, dados):
        self.__grau_intrucao = dados


    def getEstadoCivil(self):
        return self.__estado_civil
    
    
    def alterarEstadoCivil(self, dados):
        self.__estado_civil = dados


    def getUfNascimento(self):
        return self.__uf_nascimento
        
    
    def alterarUfNascimento(self, dados):
        self.__uf_nascimento = dados


    def getMunicipioNascimento(self):
        return self.__municipio_nascimento
    
    def alterarMunicipioNascimento(self, dados):
        self.__municipio_nascimento = dados
    

    def getSituacaoPosPleito(self):
        return self.__situacao_pos_pleito
        
    
    def alterarSituacaoPosPleito(self, dados):
        self.__situacao_pos_pleito = dados


    def getSituacaoCandidatura(self):
        return self.__situacao_candidatura

    
    def alterarSituacaoCandidatura(self, dados):
        self.__situacao_candidatura = dados


    def getListaBens(self):
        return self.__lista_bens

    def alterarListaBens(self, dados):
        self.__lista_bens = dados

    



    def getCargo(self):
        return self.__cargo

    
    def alterarCargo(self, dados):
        self.__cargo = dados

    def getCodigoCargo(self):
        return self.__codigo_cargo

    
    def alterarCodigoCargo(self, dados):
        self.__codigo_cargo = dados

    def getTotalDeclarado(self):
        return self.__total_declarado

    def alterarTotalDeclarado(self, dados):
        self.__total_declarado += dados


    

    


    

     
         