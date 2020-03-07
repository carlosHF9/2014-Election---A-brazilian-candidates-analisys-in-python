class Bem:
    def __init__(self, codigo_tipo_bem, descricao_tipo_bem, descricao_detalhada_bem, valor_bem):
        self.__codigo_tipo_bem = codigo_tipo_bem
        self.__descricao_tipo_bem = descricao_tipo_bem
        self.__descricao_detalhada_bem = descricao_detalhada_bem
        self.__valor_bem = valor_bem
    
    def __str__(self):
        return '{} -- {} -- {} Descrição: {}'.format(self.__codigo_tipo_bem, self.__descricao_tipo_bem, self.__valor_bem, self.__descricao_detalhada_bem)

    def __repr__(self):
        return '{} -- {} -- {} Descrição: {}'.format(self.__codigo_tipo_bem, self.__descricao_tipo_bem, self.__valor_bem, self.__descricao_detalhada_bem)
    
    def getCodigoBem(self):
        return self.__codigo_tipo_bem
    
    def alterarCodigoBem(self, dados):
        self.__codigo_tipo_bem = dados
    
    def getDescricaoTipoBem(self):
        return self.__descricao_tipo_bem
    
    def alterarDescricaoTipoBem(self, dados):
        self.__descricao_tipo_bem = dados
    
    def getDescricaoDetalhadaBem(self):
        return self.__descricao_detalhada_bem
    
    def alterarDescricaoDetalhadaBem(self, dados):
        self.__descricao_detalhada_bem = dados

    def getValorBem(self):
        return self.__valor_bem
    
    def alterarValorBem(self, dados):
        self.__valor_bem = dados
    
    def compararBens(self, codigo_tipo_bem, descricao_tipo_bem, descricao_detalhada_bem, valor_bem):
        pass
    
    

    