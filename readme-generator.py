import os

# --- 1. Entrada de Dados (Mantenha a mesma ordem nas duas listas!) ---
nomes_figuras = [
                    'line_example_sine_wave.png',
                    'line_example_axis_limit_sine_wave.png',
                    'line_example_axis_limit_invert_axis_sine__cosine_wave.png',
                    'correlation_heatmap_using_correlation_info.png',
                    'kde_histogram_one_variable.png',
                    'kde_histogram_compare.png',
                    'mix_predicted_vs_observed.png',
                    'scatter_example_sine_scatter.png',
                    'scatter_example_sine_scatter_with_cmap.png'
                ]
notebooks = [
                r'https://github.com/Pesquisa-UFCAT/plot_gallery/blob/main/charts-line/one_line_0.ipynb',
                r'https://github.com/Pesquisa-UFCAT/plot_gallery/blob/main/charts-line/one_line_1.ipynb',
                r'https://github.com/Pesquisa-UFCAT/plot_gallery/blob/main/charts-line/one_line_2.ipynb',
                r'https://github.com/Pesquisa-UFCAT/plot_gallery/blob/main/charts-heatmap/heatmap_0.ipynb',
                r'https://github.com/Pesquisa-UFCAT/plot_gallery/blob/main/charts-histogram/kde_histogram_0.ipynb',
                r'https://github.com/Pesquisa-UFCAT/plot_gallery/blob/main/charts-histogram/kde_histogram_1.ipynb',
                r'https://github.com/Pesquisa-UFCAT/plot_gallery/blob/main/charts-mix/mix_scatter_line_0.ipynb',
                r'https://github.com/Pesquisa-UFCAT/plot_gallery/blob/main/charts-scatter/scatter_0.ipynb',
                r'https://github.com/Pesquisa-UFCAT/plot_gallery/blob/main/charts-scatter/scatter_1.ipynb'
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
        
        descricao = os.path.splitext(nome_img)[0]
        descricao = descricao.replace('_', ' ').lower()
        
        # Escreve a linha
        linha = f"| <img src='{nome_img}' width='300'> | **{descricao}** | [See script]({link_url}) |\n"
        f.write(linha)

print("README.md gerado com sucesso!")