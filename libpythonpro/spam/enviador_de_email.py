class Enviador:

    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'O Email {remetente} não é válido, tente novamente.')
        return remetente


class EmailInvalido(Exception):
    pass
