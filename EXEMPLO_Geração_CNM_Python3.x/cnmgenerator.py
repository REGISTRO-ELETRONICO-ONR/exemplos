import stdnum.iso7064.mod_97_10

def calcMod97base10(num):
    digVerificador = stdnum.iso7064.mod_97_10.calc_check_digits(num)
    cnm = str(num) + str(digVerificador)
    cns = cnm[0:6]
    livro = cnm[6]
    matricula = cnm[7:14]
    matriculaCnm = cns + '.' + livro + '.' + matricula + '-' + digVerificador

    return matriculaCnm

def CnmGenerator(cns, livro, number):
    if livro == 2 or livro == 3:
        matricula = str(number).zfill(7)
        preCnm = cns + str(livro) + str(matricula)
        getCnm = calcMod97base10(preCnm)
        return getCnm
    else:
        return 'Erro: Livro informado não é válido'

