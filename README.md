# PyViewer
Um pequeno visualizador/copiador de imagens para navegar por uma pasta de imagens e copiar imagens selecionadas para outra pasta.

Problema: Quando lidamos com imagens geradas pelo Stable Diffusion, acabamos com uma grande quantidade de arquivos, separar manualmente as melhores imagens é trabalhoso, arrastando e soltando. 

Solução: Um pequeno script em Python que exibe as imagens de uma pasta, e copia a imagem corrente para uma pasta específica, ao apertar de um botão.

Modo de uso:

Para executar o programa, utilize a sintaxe:

python pyViewer.py <pasta_das_imagens> <pasta_de_saida>

Para avançar ou retroceder as imagens, use as setas. 

Para copiar a imagem corrente para a pasta de saída, aperte "C". Um breve bipe indicará o sucesso da operação.

Requisitos:

pip install keyboard Pillow
