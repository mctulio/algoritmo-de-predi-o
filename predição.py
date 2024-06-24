#arquivo da planilha pré-carregado na pasta junto com o código e arquivo .exe.
#o arquivo .exe é para aqueles que não utilizam python mas querem saber como o aplicativo funciona.




import pandas as pd
import numpy as np


def carregar_dados_excel(nome_arquivo):
    try:
        
        df = pd.read_excel(nome_arquivo, usecols=["concurso", "data", "bola 1", "bola 2", "bola 3", "bola 4", "bola 5", "bola 6"])
        return df
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao carregar a planilha: {e}")
        return None


def analisar_e_prever(df):
    try:
        
        colunas_bolas = ["bola 1", "bola 2", "bola 3", "bola 4", "bola 5", "bola 6"]
        numeros_sorteados = df[colunas_bolas].values.flatten().tolist()
        
        
        numeros_flat = [int(numero) for numero in numeros_sorteados if pd.notna(numero)]
        
        
        contagem_numeros = np.bincount(numeros_flat, minlength=61)[1:]
        
        
        numeros_sugeridos = np.argsort(contagem_numeros)[::-1][:6] + 1
        
        return numeros_sugeridos
    
    except Exception as e:
        print(f"Erro ao analisar os dados: {e}")
        return None


if __name__ == "__main__":
    nome_arquivo = "nome_do_arquivo.xlsx"
    #Caso não consiga carregar o arquivo ou retornar um erro, utilize o parametro "r" antes das aspas do caminho do arquivo.
    
    df = carregar_dados_excel(nome_arquivo)
    if df is not None:
        numeros_previstos = analisar_e_prever(df)
        
        if numeros_previstos is not None:
            print("Possível previsão dos próximos números:")
            print(', '.join(map(str, numeros_previstos)))
