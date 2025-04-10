class Parser:
    def __init__(self, tokens):
        self.tokens = tokens  
        self.posicao = 0 
        self.ocorrencias = []  

    def parse(self):
        while self.posicao < len(self.tokens): 
            self.ocorrencias.append(self.parse_registro())  
        return self.ocorrencias  

    def parse_registro(self):
        registro = {} 

        self.consumir('PALAVRA_CHAVE', 'tipo:')
        registro['tipo'] = self.consumir('NATUREZA')['valor']  

        self.consumir('PALAVRA_CHAVE', 'data:') 
        registro['data'] = self.consumir('DATA_HORA')['valor']

        self.consumir('PALAVRA_CHAVE', 'local:') 
        registro['local'] = self.parse_texto()

        self.consumir('PALAVRA_CHAVE', 'relato:') 
        registro['relato'] = self.parse_texto()  

        self.consumir('PALAVRA_CHAVE', 'envolvidos:')  
        registro['envolvidos'] = self.parse_texto()

        self.consumir('PALAVRA_CHAVE', 'objetos:')  
        registro['objetos'] = self.parse_texto() 

        return registro  

    def parse_texto(self): 
        textos = []  
        while (self.posicao < len(self.tokens) and 
               self.tokens[self.posicao]['tipo'] != 'PALAVRA_CHAVE'): 
            textos.append(self.tokens[self.posicao]['valor']) 
            self.posicao += 1  
        return ' '.join(textos) 

    def consumir(self, tipo, valor=None):
        if self.posicao >= len(self.tokens): 
            raise ValueError(f"Fim inesperado dos tokens. Esperava: {tipo}/{valor}")
        
        token = self.tokens[self.posicao]    
        if token['tipo'] != tipo or (valor is not None and token['valor'] != valor):
            raise ValueError(f"Token inesperado. Esperava: {tipo}/{valor}, encontrou: {token['tipo']}/{token['valor']}")
        
        self.posicao += 1  
        return token 