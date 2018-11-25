from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from dateutil.relativedelta import relativedelta
from datetime import date


class Consulta(models.Model):
    valor_imovel = models.FloatField(validators=[MinValueValidator(0.0)])
    taxa_juro = models.FloatField(validators=[MinValueValidator(0.0)])
    percentual_entrada = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    quantidade_parcelas = models.IntegerField(validators=[MinValueValidator(1)])
    data_inicial = models.DateField(auto_now_add=True)

    def __init__(self, data):
        super(Consulta, self).__init__()
        set_data_in_objects(self, data)
        self.data_inicial = date.today()

    @property
    def amortizacao(self):
        return self.valor_final / self.quantidade_parcelas

    @property
    def valor_final(self):
        return self.valor_imovel - (self.valor_imovel * (self.percentual_entrada/100))

    @property
    def valor_parcela(self):
        return self.amortizacao + (self.valor_final * self.taxa_porcentagem)

    @property
    def taxa_porcentagem(self):
        return self.taxa_juro/100

    @property
    def lista_parcelas(self):
        lista = []
        for i in range(self.quantidade_parcelas):
            obj = {}
            obj['data'] = self.data_inicial + relativedelta(months=+(i + 1))
            obj['valor'] = self.valor_parcela
            import ipdb; ipdb.set_trace()
            lista.append(obj)
        return lista



def set_data_in_objects(obj, data):
    for key, value in data.items():
        setattr(obj, key, value)