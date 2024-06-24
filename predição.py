#arquivo da planilha pré-carregado na pasta junto com o código e arquivo .exe.
#o arquivo .exe é para aqueles que não utilizam python mas querem saber como o aplicativo funciona.
#eu ainda to me aperfeiçoando em python, mas consigo ver um caminho promissor, o código ainda é bem primitivo, não reparem na bagunça!!

import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox

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
    root = tk.Tk()
    root.withdraw() 
    
    nome_arquivo = filedialog.askopenfilename(title="Selecionar Arquivo Excel", filetypes=[("Excel Files", "*.xlsx;*.xls")])
    
    if nome_arquivo:
        df = carregar_dados_excel(nome_arquivo)
        
        if df is not None:
            numeros_previstos = analisar_e_prever(df)
            
            if numeros_previstos is not None:
                resultado_str = "Possível previsão dos próximos números:\n" + ', '.join(map(str, numeros_previstos))
                messagebox.showinfo("Resultado da Análise", resultado_str)



