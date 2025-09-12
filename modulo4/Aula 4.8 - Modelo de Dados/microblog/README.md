# Microblog

Este é um projeto exemplo de **Microblog em Flask**, incluindo:
- Autenticação com Flask-Login
- Cadastro de usuários com foto e bio
- CRUD de posts (com timestamp)
- Templates com HTML + CSS simples

## Instalação

1. Clone ou extraia este repositório:
   ```bash
   unzip microblog.zip
   cd microblog
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Inicialize o banco de dados (SQLite):
   ```bash
   flask shell
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```

5. Rode a aplicação:
   ```bash
   flask run
   ```

6. Acesse em: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Estrutura do Projeto

```
microblog/
|-- .flaskenv
|-- flask_env/
|-- app/
|   |-- __init__.py
|   |-- alquimias.py
|   |-- routes.py
|   |-- templates/
|   |   |-- base.html
|   |   |-- index.html
|   |   |-- login.html
|   |   |-- cadastro.html
|   |   |-- post.html
|   |-- models/
|   |   |-- models.py
|-- microblog.py
|-- instance/
|   |-- microblog.db
|-- requirements.txt
|-- README.md
```

---
Projeto didático baseado no Mega Tutorial de Flask (Miguel Grinberg).
