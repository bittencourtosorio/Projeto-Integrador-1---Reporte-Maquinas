from django.shortcuts import render, redirect #responsavel por renderizar as paginas e redirecionar para outras paginas
from .models import Defeito #responsavel por importar o modelo Defeito
from django.db.models import Q #responsavel por importar o Q para fazer consultas mais complexas
from django.core.paginator import Paginator #responsavel por importar o Paginator para fazer a paginação dos resultados
from django.contrib import messages #responsavel por importar o messages para mostrar mensagens de sucesso ou erro


def base_conhecimento (request):
    if request.method == 'GET': #responsavel por carregar a página inicial
        return render(request, 'base_conhecimento.html')
    
    if request.method == "POST":#responsavel por receber os dados do formulario e salvar no banco de dados
        try:
            maquina = request.POST.get("maquina","").strip()
            descricao = request.POST.get("descricao","").strip()
            solucao = request.POST.get("solucao","").strip()
            causa_possivel = request.POST.get('causa_possivel')
        
            if maquina and descricao and solucao:# verifica se os campos obrigatorios foram preenchidos
                Defeito.objects.create(maquina=maquina, 
                                       descricao=descricao, 
                                       solucao=solucao, 
                                       causa_possivel=causa_possivel
                                       )
                messages.success(request, "Registro salvo com sucesso!")
                return redirect('base_conhecimento')
            else:
                messages.error(request, "Preencha todos os campos obrigatórios!")
        except Exception as e:
            messages.error(request, f"Erro ao salvar: {str(e)}")
                
    defeitos = Defeito.objects.all().order_by('-id') #responsavel por listar todos os defeitos cadastrados no banco de dados
    return render(request, "base_conhecimento.html", {"defeitos": defeitos})#responsavel por renderizar a pagina inicial com os defeitos cadastrados
            
                
def buscar_defeito(request):#responsavel por buscar os defeitos no banco de dados
    query = request.GET.get('q', '').strip()#responsavel por receber a query da busca
    page = request.GET.get('page', 1)#responsavel por receber o numero da pagina atual

    if query:
        # Busca em múltiplos campos
        resultados = Defeito.objects.filter(
            Q(maquina__icontains=query) | 
            Q(descricao__icontains=query) |
            Q(solucao__icontains=query)
        ).distinct().order_by('-id') #responsavel por fazer a busca no banco de dados utilizando o Q para fazer consultas mais complexas
    else:
        resultados = Defeito.objects.none()#responsavel por criar uma query vazia para evitar erro caso a busca não retorne resultados
    
    paginator = Paginator(resultados, 10)  # 10 itens por página
    resultados_paginados = paginator.get_page(page)
    
    return render(request, "base_conhecimento.html", {
        'resultados': resultados_paginados,
        'query': query
        })#responsavel por renderizar a pagina de busca