# Sistema de Recrutamento Inteligente com IA e NLP

Bem-vindo ao projeto do **Sistema de Recrutamento Inteligente**, uma solução que utiliza **Inteligência Artificial (IA)** e **Processamento de Linguagem Natural (NLP)** para otimizar o processo de recrutamento, automatizando a análise de currículos e sugerindo os candidatos mais compatíveis com as vagas abertas.

## 🚀 Sobre o Projeto

Este projeto tem como objetivo **facilitar e acelerar o processo de seleção** de candidatos, aliviando a carga da equipe de Recursos Humanos e aumentando a precisão na correspondência entre candidatos e vagas.

### 🔹 Principais Funcionalidades

#### ✅ Coleta de Dados Automatizada
- Upload de currículos em formatos **PDF, DOCX ou TXT**.
- Cadastro de vagas com descrições detalhadas, requisitos e habilidades desejadas.

#### ✅ Processamento de Currículos com NLP
- Extração automática de informações chave dos currículos:
  - **Habilidades**
  - **Experiências Profissionais**
  - **Formação Acadêmica**
- Utilização de bibliotecas como **spaCy** e **NLTK** para o processamento.

#### ✅ Matching Inteligente
- Comparação dos perfis dos candidatos com as vagas disponíveis utilizando algoritmos de **Machine Learning**.
- Geração de um **ranking** dos candidatos mais compatíveis para cada vaga.

#### ✅ API para Integração
- Desenvolvimento de uma **API com FastAPI**.
- Endpoints para gerenciamento de candidatos, vagas e obtenção de correspondências.
- Possibilidade de **integração com outras plataformas e serviços**.


## 💻 Tecnologias Utilizadas

- **Linguagem de Programação:** Python
- **Framework Web:** FastAPI
- **Processamento de Linguagem Natural:** spaCy, NLTK
- **Machine Learning:** scikit-learn
- **Banco de Dados:** PostgreSQL
- **Servidor ASGI:** Uvicorn
- **Contêinerização (opcional):** Docker

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado em sua máquina:

- **Python 3.8+**
- **PostgreSQL**
- **Git** (para clonar o repositório)

## 🛠️ Como Executar o Projeto

### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/seu_usuario/recrutamento-inteligente.git
cd recrutamento-inteligente
```

### 2️⃣ Configurar o Ambiente Virtual
Crie e ative um ambiente virtual:
```bash
python3 -m venv venv
source venv/bin/activate  # No Windows, use venv\Scripts\activate
```

### 3️⃣ Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar o Banco de Dados PostgreSQL
Criar o Banco de Dados e Usuário:

Acesse o PostgreSQL:
```bash
sudo -i -u postgres
psql
```

Crie o banco de dados:
```sql
CREATE DATABASE recrutamento_db;
```

Crie o usuário (substitua `seu_usuario` e `sua_senha`):
```sql
CREATE USER seu_usuario WITH PASSWORD 'sua_senha';
```

Conceda permissões:
```sql
GRANT ALL PRIVILEGES ON DATABASE recrutamento_db TO seu_usuario;
\c recrutamento_db
ALTER SCHEMA public OWNER TO seu_usuario;
```

Saia do psql:
```sql
\q
```

Retorne ao seu usuário:
```bash
exit
```

### 5️⃣ Configurar as Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto com as seguintes informações:
```env
DATABASE_URL=postgresql://seu_usuario:sua_senha@localhost:5432/recrutamento_db
```
> Substitua `seu_usuario` e `sua_senha` pelas suas credenciais.

### 6️⃣ Inicializar o Banco de Dados
```bash
python -m scripts.init_db
```
Se tudo ocorrer bem, você verá:
```bash
Criando as tabelas no banco de dados...
Tabelas criadas com sucesso.
```

### 7️⃣ Iniciar a Aplicação
```bash
uvicorn app.main:app --reload
```
A aplicação estará disponível em [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 🚦 Como Testar o Sistema

### 🔹 Acessar a Documentação Interativa
Abra seu navegador e acesse: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Utilize o **Swagger UI** para interagir com os endpoints.

### 🔹 Testar o Cadastro de Candidatos
- **Endpoint:** `POST /candidatos/`
- Use o formulário para enviar um currículo de teste e preencher as informações solicitadas.

### 🔹 Testar o Cadastro de Vagas
- **Endpoint:** `POST /vagas/`
- Cadastre uma vaga fornecendo título, descrição, requisitos e habilidades desejadas.

### 🔹 Testar o Matching
- **Endpoint:** `GET /vagas/{vaga_id}/candidatos_recomendados/`
- Substitua `{vaga_id}` pelo ID da vaga cadastrada.
- Verifique se o sistema retorna os candidatos mais compatíveis.

## 🤝 Contribuindo com o Projeto

Contribuições são bem-vindas! Se você deseja melhorar este projeto, siga estas etapas:

1. Faça um **fork** do repositório.
2. Crie uma nova branch: `git checkout -b minha-feature`.
3. Commit suas mudanças: `git commit -m 'Minha nova feature'`.
4. Faça um push para a branch: `git push origin minha-feature`.
5. Abra um **Pull Request**.

## 📞 Contato

**Carlos Henrique**  
📧 Email: [ch.rodrigues098@gmail.com](ch.rodrigues098@gmail.com)  
🔗 LinkedIn: [https://www.linkedin.com/in/carlos-henrique-rodri/](https://www.linkedin.com/in/carlos-henrique-rodri/)
