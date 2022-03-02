# libpythonpro_michel
Módulo para exemplificar construção de projetos Python no curso Pytools. 
Nesse curso é tentado ensinar como contribuir com projetos de código aberto.
Pórém a didática é muito ruim.

Link para o curso: [Dev Pro](https://plataforma.dev.pro.br/)

![workflow](https://github.com/michel4lves/libpythonpro-michel/actions/workflows/main.yml/badge.svg)
[![Updates](https://pyup.io/repos/github/Michel4lves/libpythonpro_michel/shield.svg)](https://pyup.io/repos/github/Michel4lves/libpythonpro/)
[![Python 3](https://pyup.io/repos/github/Michel4lves/libpythonpro_michel/python-3-shield.svg)](https://pyup.io/repos/github/Michel4lves/libpythonpro/)

Suportada versão 3 de python.

Github Actions funcionando.

Tópicos a serem abordados:
1. Git;
2. Virtualenv;
3. Pip.

Para instalar:

consolecls

    py -3 -m venv .venv
    .venv\Scripts\activate
    .venv\Scripts\python.exe -m pip install --upgrade pip
    pip install -r requirements-dev.txt

Para conferir qualidade de código:

console

    flake8

