from lexico import Analisador
from sintatico import Parser

def main():
    entrada = """
    typo: perda data: 12/12/23 local: shoping rio poty relato: perdi minha carteira envolvidos: Joãl Gabriel Silva objetos: carteira
    """

    lexico = Analisador(entrada)
    tokens = lexico.tokenizar()

    for token in tokens:
        print(token)

    parser = Parser(tokens)
    ocorrencias = parser.parse()

    for i, ocorrencia in enumerate(ocorrencias, 1): 
        print(f"\nRegistro {i}:") 
        for chave, valor in ocorrencia.items():  
            print(f"{chave:>10}: {valor}")  

if __name__ == "__main__":
    main()