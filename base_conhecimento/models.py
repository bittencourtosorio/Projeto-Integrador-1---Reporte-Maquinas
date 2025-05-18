from django.db import models

class Defeito(models.Model):#responsavel por criar o modelo Defeito
    maquina = models.CharField(max_length=100, db_index=True)
    descricao = models.TextField(max_length=250, null = False, blank = False)
    solucao = models.TextField(max_length=250, null=False, blank=False)
    causa_possivel = models.TextField(max_length=250)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:#responsavel por criar a classe Meta para definir o nome da tabela no banco de dados
        db_table = 'Defeito'

    def __str__(self):#responsavel por criar o metodo __str__ para retornar uma string representando o objeto Defeito
        return f"{self.maquina}: {self.descricao} | solucao: {self.solucao} | causa_possivel: {self.causa_possivel}"

    @classmethod
    def buscar_por_maquina(cls, nome_maquina):#responsavel por criar o metodo buscar_por_maquina para buscar os defeitos pelo nome da maquina
        return cls.objects.filter(maquina__icontains=nome_maquina)
