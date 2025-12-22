import os

# --- 1. Entrada de Dados (Mantenha a mesma ordem nas duas listas!) ---

nomes_figuras = [
                    'Traditional-lineplot.png',
                    'Traditional-lineplot-with-axis-limit-control.png',
                    'Traditional-contourplot.png',
                    'Traditional-contourplot-With-Cmap.png'
                ]

notebooks = [
                r'https://github.com/Pesquisa-UFCAT/plot_gallery/blob/main/line%20charts/one_line_0.ipynb',
                r'https://github.com/Pesquisa-UFCAT/plot_gallery/blob/main/line%20charts/one_line_1.ipynb',
                r'https://github.com/Pesquisa-UFCAT/plot_gallery/blob/main/countour%20line%20charts/countour_line_0.ipynb',
                r'https://github.com/Pesquisa-UFCAT/plot_gallery/blob/main/countour%20line%20charts/countour_line_1.ipynb'
            ]

# (Opcional) Verificação de segurança para ver se não esqueceu nada
if len(nomes_figuras) != len(notebooks):
    print(f"ATENÇÃO: Você tem {len(nomes_figuras)} imagens e {len(notebooks)} links. As quantidades deveriam ser iguais!")

# --- 2. Gerar o README ---

with open('README.md', 'w', encoding='utf-8') as f:
    
    # Cabeçalho da Tabela
    f.write("# Gallery\n\n")
    f.write("| Image | Description | Notebook |\n")
    f.write("| :---: | :--- | :---: |\n")
    
    # O zip junta: (figura 1, link 1), depois (figura 2, link 2)...
    for nome_img, link_url in zip(nomes_figuras, notebooks):
        
        # Cria um título bonito baseado no nome do arquivo
        descricao = os.path.splitext(nome_img)[0]   # Tira o .png
        descricao = descricao.replace('_', ' ').title() # Tira underline e capitaliza
        
        # Escreve a linha
        linha = f"| <img src='{nome_img}' width='300'> | **{descricao}** | [See script]({link_url}) |\n"
        f.write(linha)

print("README.md gerado com sucesso!")