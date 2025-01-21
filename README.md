# Genius Python Game

Uma recriação simples do clássico jogo "Genius" usando Python. O objetivo do jogo é memorizar e repetir uma sequência de cores que cresce a cada rodada.

---

## Funcionalidades
- Apresenta sequências de cores para o jogador memorizar.
- Compara a entrada do jogador com a sequência gerada.
- Incrementa o nível e o desafio à medida que o jogador acerta.
- Fornece feedback claro sobre acertos e erros.
- Sistema de pontuação simples.

---

## Tecnologias Utilizadas
- **Python**
- **Biblioteca Padrão**: Uso de `random`, `time`, e `os` para funcionalidade e interação.

---

## Como Jogar
1. **Regras**:
   - As cores disponíveis são:
     - `vm`: vermelho
     - `az`: azul
     - `vd`: verde
     - `am`: amarelo
   - Digite as respostas separadas por espaços, seguindo o padrão exibido na tela.
     - Exemplo: `am am az az vd`

2. **Início**:
   - Execute o arquivo Python no terminal.
   - Memorize a sequência apresentada.
   - Digite a sequência corretamente para avançar de nível.

3. **Fim de Jogo**:
   - O jogo termina quando o jogador digita uma sequência incorreta.
   - Você pode optar por reiniciar o jogo ou encerrar.

---

## Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/genius-python-game.git

2. Acesse o diretório do projeto:
   ```bash
   cd genius-python-game

3. Execute o jogo:
   ```bash
   python genius.py
