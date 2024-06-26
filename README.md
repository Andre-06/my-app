# Flask - Linguagem de Programação III
Repositório destinado para armazenar o contedúdo aprendido durante as aulas de LP3

---

## 🚀 Instalação

1. **Instalação do Poetry no Lab (Linux)**
    ````bash
        curl -sSL https://install.python-poetry.org | python3 - 
        export PATH="/home/estudante1/.local/bin:$PATH"
    ````
   
2. **Clone do repositório**
    ````bash
        git clone https://github.com/Andre-06/my-app.git
    ````     
   
3. **Instalação das dependências do projeto**
    ````bash
        poetry shell
        poetry install
    ````
   
4. **Execução do Flask**
    ````bash
        poetry run flask --app my_app/app.py run --debug
    ````
