from Atividade import Familia
class Principal:

    if __name__ == '__main__':

        PaideRoberto = Familia("Reginaldo")
        FilhadeCristina = Familia("Carol")

        Roberto = Familia("Roberto")
        Cristina = Familia("Cristina")

        Roberto.Casar(Cristina.getNome())
        Cristina.Casar(Roberto.getNome())

        print("-----------------------------")

        PaideRoberto.Casar(FilhadeCristina.getNome())
        FilhadeCristina.Casar(PaideRoberto.getNome())

        print("-----------------------------")

        FilhadeCristina.setIdentidade("madrasta")
        FilhadeCristina.Identificar(Roberto.getNome())

        Roberto.setIdentidade("pai")
        Roberto.Identificar(FilhadeCristina.getNome())

        PaideRoberto.setIdentidade("genro")
        PaideRoberto.Identificar(Cristina.getNome())

        Cristina.setIdentidade("sogra")
        Cristina.Identificar(PaideRoberto.getNome())

        print("-----------------------------")

        FilhodeRoberto = Familia("Robertinho")
        FilhodeRoberto.Nascer(Roberto.getNome(),Cristina.getNome())

        FilhodeRoberto.setIdentidade("irmão")
        FilhodeRoberto.Identificar(FilhadeCristina.getNome())

        FilhadeCristina.setIdentidade("avó")
        FilhadeCristina.Identificar(FilhodeRoberto.getNome())

        print("-----------------------------")

        FilhodoPaideRoberto = Familia("Romer")
        FilhodoPaideRoberto.Nascer(PaideRoberto.getNome(),FilhadeCristina.getNome())

        FilhodoPaideRoberto.setIdentidade("irmão")
        FilhodoPaideRoberto.Identificar(Roberto.getNome())

        Cristina.setIdentidade("avó")
        Cristina.Identificar(FilhodoPaideRoberto.getNome())

        Roberto.setIdentidade("avô")
        Roberto.Identificar(FilhodoPaideRoberto.getNome())

        Roberto.Identificar(Roberto.getNome())





















