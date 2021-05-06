from src.celular import Celular
from src.acessorios.carregador import Carregador
from src.acessorios.fone_de_ouvido import Fone_de_ouvido

print('-=' * 20)

celular1 = Celular(Carregador())
celular1.plugar_acessorio()

print('-=' * 20)

celular2 = Celular(Fone_de_ouvido())
celular2.plugar_acessorio()

print('-=' * 20)
