import os
import shutil


pasta_alvo = os.path.expanduser("~/Downloads")


categorias = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Compactados": [".zip", ".rar", ".7z"],
    "Programas": [".exe", ".msi", ".dmg"]
}

def organizar_pasta():
    for arquivo in os.listdir(pasta_alvo):
        caminho_completo = os.path.join(pasta_alvo, arquivo)

        if os.path.isdir(caminho_completo):
            continue


        _, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower()

        
        pasta_destino = None
        for categoria, extensoes_permitidas in categorias.items():
            if extensao in extensoes_permitidas:
                pasta_destino = os.path.join(pasta_alvo, categoria)
                break

       
        if not pasta_destino and extensao:
            pasta_destino = os.path.join(pasta_alvo, "Outros")

       
        if pasta_destino:
            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)
            
            caminho_novo = os.path.join(pasta_destino, arquivo)
            shutil.move(caminho_completo, caminho_novo)
            print(f"Movido: {arquivo} -> {pasta_destino}")

if __name__ == "__main__":
    organizar_pasta()
    print("Pasta organizada com sucesso!")