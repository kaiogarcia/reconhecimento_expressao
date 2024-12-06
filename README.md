# RecognizeFace

**RecognizeFace** é uma aplicação de reconhecimento facial com detecção de emoções, desenvolvida utilizando Python, OpenCV e a biblioteca DeepFace. Este projeto é uma introdução prática ao uso de Visão Computacional e Machine Learning para identificar rostos e classificar emoções predominantes.

## 🚀 Funcionalidades

- **Detecção Facial:** Localiza rostos em imagens ou vídeos em tempo real usando o classificador Haar Cascade.
- **Análise de Emoções:** Identifica a emoção predominante entre felicidade, tristeza, surpresa, medo, raiva e neutra.
- **Interface Interativa:** Processa tanto imagens pré-carregadas quanto vídeos capturados em tempo real.

## 🛠️ Tecnologias Utilizadas

- **Python:** Linguagem de programação principal.
- **OpenCV:** Biblioteca para processamento de imagens e vídeos.
- **DeepFace:** Biblioteca para análise facial com modelos pré-treinados baseados em redes neurais.

## 📦 Como instalar e executar o projeto

### Pré-requisitos
Certifique-se de ter o seguinte instalado:
- Python 3.7 ou superior
- pip

### Passos para instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/kaiogarcia/reconhecimento_expressao.git
   cd RecognizeFace
   ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/MacOS
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

### Como executar

1. Execute o script principal:
   ```bash
   python recognize_your_face.py
   ```

2. Para encerrar a aplicação, pressione a tecla `q` na janela de vídeo.

## 📂 Estrutura do Projeto

```plaintext
RecognizeFace/
├── recognize_your_face.py     # Arquivo aplicação
├── recognize_your_face_2.py   # Arquivo da aplicação 2
├── requirements.txt           # Dependências do projeto
├── README.md                  # Documentação do projeto
```

## ⚙️ Como funciona

### 1️⃣ Detecção de Rostos
- A aplicação utiliza o classificador Haar Cascade para identificar rostos em imagens ou vídeos em tempo real.
- Rostos detectados são destacados com um retângulo verde.

### 2️⃣ Análise de Emoções
- Após a detecção, cada rosto é recortado e analisado pela biblioteca DeepFace.
- A emoção predominante é exibida acima do rosto detectado.

### 3️⃣ Interface Interativa
- Suporte para processamento de imagens estáticas e vídeo ao vivo.

## 🌟 Aplicações

Este projeto pode ser adaptado para diversos contextos:
- **Saúde Mental:** Monitoramento emocional em tempo real.
- **Educação:** Análise de engajamento de alunos em aulas remotas.
- **Comércio:** Avaliação de emoções durante interações com produtos.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias ou correções.

## 📸 Créditos

As imagens usadas para desenvolvimento foram retiradas de [Freepik](https://www.freepik.com/).

## 📜 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

💡 **Siga este repositório para acompanhar futuras atualizações!**
