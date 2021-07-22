from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import conexao
from django.contrib.auth.models import User

__login = True

con = conexao.conectar()
# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def cad_user(request):
    return render(request, 'cad_user.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def hoteis(request):
    return render(request, 'hoteis.html')

def reserva(request):
    return render(request, 'reserva.html')  

def insere_cliente(request):
    nome = request.POST.get('nome')
    idade = request.POST.get('idade')
    telefone = request.POST.get('telefone')
    cpf = request.POST.get('cpf')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    with con.cursor() as inserir:
        sql = 'insert into tbcliente(nome, idade, telefone, cpf, email, senha) values(%s, %s, %s, %s, %s, %s)'
        inserir.execute(sql, (nome, idade, telefone, cpf, email, senha))
        con.commit()
    return render(request, 'cad_user.html')

def insere_reserva(request):
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    telefone = request.POST.get('telefone')
    hotel = request.POST.get('hotel')
    checkin = request.POST.get('checkin')
    checkout = request.POST.get('checkout')
    qtd_quartos = request.POST.get('qtd_quartos')


    with con.cursor() as inserir:
        sql = 'insert into tbreserva(nome, cpf, telefone, hotel, checkin, checkout, qtd_quartos) ' \
              'values(%s, %s, %s, %s, %s, %s, %s)'
        inserir.execute(sql, (nome, cpf, telefone, hotel, checkin, checkout, qtd_quartos))
        con.commit()
    return render(request, 'reserva.html')


def cliente(request):
    if __login == True:
        with con.cursor() as selecionar:
            sql = 'select * from tbcliente'
            selecionar.execute(sql)
            dados = selecionar.fetchall()
        return render(request, 'cliente.html', {'clientes':dados})
    else:
        return render(request, 'cliente.html')

def hoteis_reservados(request):
    if __login == True:
        with con.cursor() as selecionar:
            sql = 'select * from tbreserva'
            selecionar.execute(sql)
            dados = selecionar.fetchall()
        return render(request, 'hoteis_reservados.html', {'hoteis':dados})
    else:
        return render(request, 'hoteis_reservados.html')

def deleta_cliente(request, id):
    if __login == True:
        with con.cursor() as deletar:
            sql = 'DELETE FROM tbcliente WHERE id = %s'
            deletar.execute(sql, id)
            con.commit()
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')

def deleta_reserva(request, id):
    if __login == True:
        with con.cursor() as deletar:
            sql = 'DELETE FROM tbreserva WHERE id = %s'
            deletar.execute(sql, id)
            con.commit()
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')
