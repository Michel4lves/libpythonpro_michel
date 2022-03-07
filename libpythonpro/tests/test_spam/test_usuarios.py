from libpythonpro.spam.modelos import Usuario


# Exemplo 2: Alto nível:
# Exemplificando a funcionalidade do pytest: fixture
# fixtures passadas para o módulo 'conftest'

def test_salvar_usuario(sessao):
    usuario = Usuario(nome='michel.alves')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='michel.alves'), Usuario(nome='carolina.alves')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()


# Exemplo 1: repetitivo:
# def test_salvar_usuario_1():
#     conexao = Conexao()
#     sessao = conexao.gerar_sessao()
#     usuario = Usuario(nome='michel.alves')
#     sessao.salvar(usuario)
#     assert isinstance(usuario.id, int)
#     sessao.roll_back()
#     sessao.fechar()
#     conexao.fechar()
#
#
# def test_listar_usuario_1():
#     conexao = Conexao()
#     sessao = conexao.gerar_sessao()
#     usuarios = [Usuario(nome='michel.alves'), Usuario(nome='carolina.alves')]
#     for usuario in usuarios:
#         sessao.salvar(usuario)
#     assert usuarios == sessao.listar()
#     sessao.roll_back()
#     sessao.fechar()
#     conexao.fechar()
