class Pessoa:
    tamanho_cpf = 11

    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    def valida_cpf(self):
        if (len(self.cpf) == __class__.tamanho_cpf):
            return True
        else:
            return False


pe = Pessoa("00000000001", "Ruby")
print(f"Esse é True ou False: {pe.valida_cpf()}")

pe = Pessoa("0000000000", "Cristal")
print(f"Esse é True ou False: {pe.valida_cpf()}")
