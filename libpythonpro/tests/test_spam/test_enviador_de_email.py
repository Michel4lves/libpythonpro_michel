import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    carteiro = Enviador()
    assert carteiro is not None


@pytest.mark.parametrize(
    'remetente',
    ['michelsalntosa@gmail.com', 'michelsalves@yahoo.com.br']
)
def test_remetente(remetente):
    carteiro = Enviador()
    resultado = carteiro.enviar(
        remetente,                          # remetente
        'michel4lves.python@gmail.com',     # destinatário
        'Curso Dev Pro',                    # assunto
        'Curso poderia ser bem melhor...'   # corpo
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'michelsalves']
)
def test_remetente_invalido(remetente):
    carteiro = Enviador()
    with pytest.raises(EmailInvalido):
        carteiro.enviar(
            remetente,                          # remetente
            'michel4lves.python@gmail.com',     # destinatário
            'Curso Dev Pro',                    # assunto
            'Curso poderia ser bem melhor...'   # corpo
        )
