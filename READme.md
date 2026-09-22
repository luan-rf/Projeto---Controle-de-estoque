# Sistema de Gestão de Estoque

Um sistema simples de gerenciamento de estoque com interface gráfica desenvolvida em Python (Tkinter) e banco de dados SQLite. Este aplicativo permite cadastrar, buscar, deletar e registrar o consumo de insumos, garantindo que não haja duplicidades e validando os dados inseridos pelo usuário.

## 🚀 Funcionalidades

* **Adicionar Insumo:** Registra novos produtos no banco de dados. Valida se o produto já existe para evitar duplicatas.
* **Procurar Insumo:** Busca os detalhes de um produto (quantidade, lote, etc.) pelo nome.
* **Registrar Uso (Consumir):** Subtrai a quantidade especificada do estoque atual, com validação para impedir que o estoque fique negativo.
* **Deletar Insumo:** Remove o cadastro completo de um item do banco de dados.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Tkinter:** Para a interface gráfica (GUI).
* **SQLite3:** Para armazenamento e persistência dos dados localmente.

## ⚙️ Pré-requisitos e Execução

Para rodar a aplicação em sua máquina, siga os passos:

1. Clone o repositório ou baixe os arquivos fonte.
2. Certifique-se de ter o Python instalado. O Tkinter e o SQLite3 são bibliotecas padrão do Python, não sendo necessária instalação adicional.
3. É obrigatório ter as imagens de background e dos botões (`background.png`, `img0.png`, etc.) na mesma raiz do arquivo principal.
4. Crie a estrutura de pastas para o banco de dados. O sistema espera que exista uma pasta `db` contendo o arquivo `db/estoque.db` na raiz do projeto.

Execute o arquivo principal:
```bash
python main.py
```

## 📁 Estrutura de Diretórios Recomendada

```text
/
├── main.py
├── background.png
├── img0.png
├── img1.png
├── img2.png
├── img3.png
├── img_textBox0.png
├── img_textBox1.png
├── img_textBox2.png
├── img_textBox3.png
├── img_textBox4.png
├── db/
│   └── estoque.db
├── README.md
└── .gitignore
```