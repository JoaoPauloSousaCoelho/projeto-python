from cesar.cesar import encripta


def test_encripta_eduardo_retorna():
    assert encripta('Eduardo') == 'rqhneqb'


def test_encripta_deve_retornar_minusculo():
    assert encripta('A').islower()


def test_encripta_deve_preservar_os_espacos():
    resultado = encripta('e a')
    assert resultado[1] == ' '
