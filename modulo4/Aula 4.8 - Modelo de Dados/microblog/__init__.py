#Incluindo o import do LoginManager no início do arquivo
from flask_login import LoginManager

# Após instanciar o objeto principal da aplicação, instancie e crie uma chave
# da sua aplicação (se ainda não tinha criado acompanhando a apostila
app =  Flask(__name__)
#...
login = LoginManager(app)
app.config['SECRET_KEY'] = "PD12345678"

