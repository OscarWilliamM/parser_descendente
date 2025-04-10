import re 

class Analisador:
    def __init__(self, entrada):
        self.entrada = entrada 
        self.posicao = 0  
        self.tokens = []  
        self.palavras_chave = ['tipo:', 'data:', 'local:', 'relato:', 'envolvidos:', 'objetos:']
        self.natureza = ['furto', 'roubo', 'perda', 'ameaça', 'acidente', 'estelionato']

    def tokenizar(self):
        while self.posicao < len(self.entrada):
            caracter = self.entrada[self.posicao]  
                
            if caracter.isspace():
                self.posicao += 1 
                continue 
            
            palavra_chave_encontrada = next(
                (pc for pc in self.palavras_chave if self.entrada.startswith(pc, self.posicao)),      
                None 
            )
            
            if palavra_chave_encontrada: 
                self.tokens.append({ 
                    'tipo': 'PALAVRA_CHAVE',  
                    'valor': palavra_chave_encontrada  
                })
                self.posicao += len(palavra_chave_encontrada)
                continue  

            natureza_encontrada = next(
                (n for n in self.natureza if self.entrada.startswith(n, self.posicao)), 
                None 
            )

            if natureza_encontrada:
                self.tokens.append({
                    'tipo': 'NATUREZA', 
                    'valor': natureza_encontrada  
                })
                self.posicao += len(natureza_encontrada)
                continue 

            padrao_data = re.match( 
                r'\d{2}/\d{2}/\d{2,4}(?: \d{2}:\d{2})?',  
                self.entrada[self.posicao:]  
            )
            if padrao_data:
                self.tokens.append({
                    'tipo': 'DATA_HORA',  
                    'valor': padrao_data.group()  
                })
                self.posicao += padrao_data.end()
                continue 

            texto = ''
            while (self.posicao < len(self.entrada) and  
                   not any(self.entrada.startswith(pc, self.posicao) for pc in self.palavras_chave) and 
                   not self.entrada[self.posicao].isspace()):  
                texto += self.entrada[self.posicao]  
                self.posicao += 1  

            if texto:
                self.tokens.append({
                    'tipo': 'TEXTO',  
                    'valor': texto 
                })

        return self.tokens