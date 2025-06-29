# 📊 Projeto Prático – Coleta de Dados com YouTube API + MongoDB

Este projeto tem como objetivo demonstrar a integração entre **fontes de dados externas** (YouTube) e **bancos de dados NoSQL**, usando Python, a biblioteca `youtool` e o banco MongoDB.

A proposta é extrair informações do canal **Manual do Mundo** como:
- Comentários dos vídeos
- Transcrições automáticas

Esses dados são armazenados em um banco de dados **MongoDB local** e podem ser consultados para análise posterior.

---

## 🛠️ Tecnologias Utilizadas

| Ferramenta       | Finalidade                            |
|------------------|----------------------------------------|
| Python           | Lógica de programação e scripts        |
| MongoDB          | Banco de dados NoSQL local             |
| youtool          | Biblioteca para acessar a API do YouTube |
| dotenv           | Leitura de variáveis do arquivo `.env` |

---

## 🧱 Estrutura do Projeto

youtube-nosql/
├── src/ # Scripts principais
│ ├── fetch_data.py # Coleta dados do YouTube
│ ├── insert_to_mongo.py# Insere os dados no MongoDB
│ └── query_data.py # Consulta os dados do MongoDB
├── data/ # Exportação dos dados
│ └── export.json
├── youtool/ # Biblioteca embutida
├── .env # Chave da API do YouTube (não versionada)
├── demo.gif # Demonstração do projeto
└── README.md

![Demonstração](demo.gif)
