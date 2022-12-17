# Video Status Cutter
![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=VERSÃO1.0&color=GREEN&style=for-the-badge) ![Script](https://img.shields.io/static/v1?label=type&message=Script&color=blue&style=for-the-badge)

## 📑 Descrição

O Video Status Cutter é um script em python criado por __Paulo Kaedo__, utilizando ferramentas da biblioteca moviePy, com a finalidade de a partir de um vídeo em mp4 e a definição de um offset de corte, dividir esse vídeos em diversas partes, que podem ser utilizados para postar em redes sociais que possuam a funcionalidade de storys. 

A ideia desse software se deu a que as vezes é necessário a postagem de um vídeo em status do Whatsapp, porém com a limitação de tempo de 30 segundos para vídeos nessa ferramenta, torna um trabalho custoso o corte manual dentro da própria interface de storys do whatsapp. Assim, o Video Status Cutter possibilita a divisão de vídeos enormes em poucos minutos.


## :hammer: Funcionalidades do projeto

- Cortar vídeos a partir de um offset determinado.

## :wrench: Tecnologias utilizadas

- Python 3.9.6
- VS Code

## 📥 Instalação

```bash
$ pip install -r requirements.txt
```
## ⚙ Configuração

Na pasta raiz do script é possível encontrar um arquivo __config.json__. Nele duas variáveis devem ser preenchidas:
  - __video_path__: O caminho do vídeo que se encontra. __DEVE SER UTILIZADO PADRÃO LINUX__. _Ex: C:/Program Files/meu_video.mp4_
  - __cut_offset__: O tamanho de cada clipe __EM SEGUNDOS__ que será gerado a partir do vídeo. Se o valor for deixado 0, o padrão será de 5 segundos.

## 💻 Rodando a Aplicação

```bash
$ python main.py
```

## 📰 Changelog

[Ver histórico de alterações do projeto.](https://github.com/PauloKaedo/video-status-cutter/blob/main/CHANGELOG.MD)



