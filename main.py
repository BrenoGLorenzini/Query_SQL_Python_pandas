import csv
import sqlite3
import pandas as pd

""" 
-- FUNÇÕES --

! qtde = quantidade !

Relação de todos os usuários por departamento em ordem alfabética. 
= ordem_alfabetica()

Relação de todos os chamados por grau de prioridade de atendimento (baixa, normal ou alta). 
= prioridade()

usuário que abriu mais chamados e em que quantidade.
= qtde_chamados_usuario()

Quantidade de chamados por departamento.
= qtde_chamados_departamento()

"""


def ordem_alfabetica():
  select_query = '''
    SELECT nome_usuario, departamento
    FROM tbUsuario
    JOIN tbDepartamento 
    ON tbUsuario.departamentoID = tbDepartamento.ID
    ORDER BY nome_usuario
    '''
  result_df = pd.read_sql_query(select_query, conn)
  print("Resultado da consulta de relação dos usuarios por departamento em ordem alfabética:\n")
  print(result_df)


def prioridade():
  select_query = '''
    SELECT titulo, especialidade, prioridade, status, departamento, nome_tec as tecnico, nome_usuario as usuario
    FROM tbChamado
    JOIN tbEspecialidade ON tbChamado.especialidadeID = tbEspecialidade.ID       
    JOIN tbPrioridade ON tbChamado.prioridadeID = tbPrioridade.ID
    JOIN tbStatus ON tbChamado.statusID = tbStatus.ID
    JOIN tbComputador ON tbChamado.computadorID = tbComputador.ID
    JOIN tbDepartamento ON tbChamado.departamentoID = tbDepartamento.ID
    JOIN tbTecnico ON tbChamado.tecnicoID = tbTecnico.ID
    JOIN tbUsuario ON tbChamado.usuarioID = tbUsuario.ID
    WHERE status LIKE "%aberto%"
    ORDER BY prioridadeID DESC
    '''
  result_df = pd.read_sql_query(select_query, conn)
  print("Resultado da consulta de Chamados (em aberto) por prioridade:\n")
  print(result_df)


def qtde_chamados_usuario():
  select_query = '''
    SELECT nome_usuario as usuario_com_mais_chamados, departamento, count(titulo) as qtde_chamados
    FROM tbChamado
    JOIN tbUsuario ON tbChamado.usuarioID = tbUsuario.ID
    JOIN tbDepartamento ON tbChamado.departamentoID = tbDepartamento.ID
    GROUP BY usuario_com_mais_chamados
    ORDER BY qtde_chamados desc
    '''
  result_df = pd.read_sql_query(select_query, conn)
  print("Resultado da consulta de usuários com maior quantidade de chamados abertos:\n")
  print(result_df)


def qtde_chamados_departamento():
  select_query = '''
    SELECT departamento, count(titulo) as qtde_chamados
    FROM tbChamado
    JOIN tbDepartamento ON tbChamado.departamentoID = tbDepartamento.ID
    GROUP BY departamento
    ORDER BY qtde_chamados desc
    '''
  result_df = pd.read_sql_query(select_query, conn)
  print("Resultado da consulta de departamentos com mais quantidade de chamados:\n")
  print(result_df)


# Dados dos chamados
tbChamado = [
    {
        "ID": 1,
        "titulo": "Problema com a impressora",
        "descricao":
        "A impressora não está respondendo quando tento imprimir.",
        "especialidadeID": 1,
        "data_abertura": "2023-08-01",
        "data_encerramento": "2023-08-02",
        "prioridadeID": 1,
        "statusID": 1,
        "computadorID": 1,
        "departamentoID": 1,
        "tecnicoID": 1,
        "usuarioID": 1
    },
    {
        "ID": 2,
        "titulo": "Erro ao acessar o software",
        "descricao": "Recebo uma mensagem de erro ao tentar abrir o software.",
        "especialidadeID": 2,
        "data_abertura": "2023-08-02",
        "data_encerramento": "2023-08-03",
        "prioridadeID": 2,
        "statusID": 2,
        "computadorID": 2,
        "departamentoID": 2,
        "tecnicoID": 2,
        "usuarioID": 2
    },
    {
        "ID": 3,
        "titulo": "Computador lento",
        "descricao":
        "Meu computador está demorando muito para iniciar e executar programas.",
        "especialidadeID": 3,
        "data_abertura": "2023-08-03",
        "data_encerramento": "2023-08-04",
        "prioridadeID": 3,
        "statusID": 3,
        "computadorID": 3,
        "departamentoID": 3,
        "tecnicoID": 3,
        "usuarioID": 3
    },
    {
        "ID": 4,
        "titulo": "Problema de conexão à rede",
        "descricao": "Não consigo me conectar à rede Wi-Fi da empresa.",
        "especialidadeID": 4,
        "data_abertura": "2023-08-04",
        "data_encerramento": "2023-08-05",
        "prioridadeID": 4,
        "statusID": 4,
        "computadorID": 4,
        "departamentoID": 4,
        "tecnicoID": 4,
        "usuarioID": 4
    },
    {
        "ID": 5,
        "titulo": "Erro no email corporativo",
        "descricao":
        "Não estou conseguindo enviar ou receber emails pelo cliente de email.",
        "especialidadeID": 1,
        "data_abertura": "2023-08-05",
        "data_encerramento": "2023-08-06",
        "prioridadeID": 5,
        "statusID": 1,
        "computadorID": 5,
        "departamentoID": 5,
        "tecnicoID": 5,
        "usuarioID": 5
    },
    {
        "ID": 6,
        "titulo": "Atualização de software necessária",
        "descricao":
        "Recebi uma notificação sobre uma atualização de software importante.",
        "especialidadeID": 2,
        "data_abertura": "2023-08-06",
        "data_encerramento": "2023-08-07",
        "prioridadeID": 6,
        "statusID": 2,
        "computadorID": 6,
        "departamentoID": 1,
        "tecnicoID": 6,
        "usuarioID": 6
    },
    {
        "ID": 7,
        "titulo": "Tela do laptop quebrada",
        "descricao": "Deixei o laptop cair e agora a tela está quebrada.",
        "especialidadeID": 3,
        "data_abertura": "2023-08-07",
        "data_encerramento": "2023-08-08",
        "prioridadeID": 1,
        "statusID": 3,
        "computadorID": 7,
        "departamentoID": 2,
        "tecnicoID": 7,
        "usuarioID": 7
    },
    {
        "ID": 8,
        "titulo": "Problema com o mouse",
        "descricao":
        "O cursor do mouse não se move na tela, mesmo que o mouse esteja funcionando.",
        "especialidadeID": 4,
        "data_abertura": "2023-08-08",
        "data_encerramento": "2023-08-09",
        "prioridadeID": 2,
        "statusID": 4,
        "computadorID": 8,
        "departamentoID": 3,
        "tecnicoID": 8,
        "usuarioID": 8
    },
    {
        "ID": 9,
        "titulo": "Senha de acesso esquecida",
        "descricao": "Esqueci minha senha de acesso à rede interna.",
        "especialidadeID": 1,
        "data_abertura": "2023-08-09",
        "data_encerramento": "2023-08-10",
        "prioridadeID": 3,
        "statusID": 1,
        "computadorID": 9,
        "departamentoID": 4,
        "tecnicoID": 9,
        "usuarioID": 9
    },
    {
        "ID": 10,
        "titulo": "Erro na instalação do programa",
        "descricao":
        "Estou tendo problemas para instalar um novo programa no meu computador.",
        "especialidadeID": 2,
        "data_abertura": "2023-08-10",
        "data_encerramento": "2023-08-11",
        "prioridadeID": 4,
        "statusID": 2,
        "computadorID": 10,
        "departamentoID": 5,
        "tecnicoID": 10,
        "usuarioID": 10
    },
    {
        "ID": 11,
        "titulo": "Problema com a impressora a laser",
        "descricao":
        "A impressora a laser está apresentando problemas ao imprimir documentos.",
        "especialidadeID": 3,
        "data_abertura": "2023-08-11",
        "data_encerramento": "2023-08-12",
        "prioridadeID": 5,
        "statusID": 1,
        "computadorID": 6,
        "departamentoID": 1,
        "tecnicoID": 6,
        "usuarioID": 6
    },
    {
        "ID": 12,
        "titulo": "Aplicativo travando ao abrir arquivos grandes",
        "descricao":
        "O aplicativo fecha inesperadamente ao tentar abrir arquivos grandes.",
        "especialidadeID": 1,
        "data_abertura": "2023-08-12",
        "data_encerramento": "2023-08-13",
        "prioridadeID": 2,
        "statusID": 2,
        "computadorID": 7,
        "departamentoID": 2,
        "tecnicoID": 7,
        "usuarioID": 7
    },
    {
        "ID": 13,
        "titulo": "Solicitação de redefinição de senha de email",
        "descricao":
        "Esqueci minha senha de email e gostaria de solicitar uma redefinição.",
        "especialidadeID": 4,
        "data_abertura": "2023-08-13",
        "data_encerramento": "2023-08-14",
        "prioridadeID": 3,
        "statusID": 3,
        "computadorID": 8,
        "departamentoID": 3,
        "tecnicoID": 8,
        "usuarioID": 8
    },
    {
        "ID": 14,
        "titulo": "Erro ao acessar a VPN corporativa",
        "descricao":
        "Estou recebendo um erro ao tentar acessar a VPN da empresa.",
        "especialidadeID": 2,
        "data_abertura": "2023-08-14",
        "data_encerramento": "2023-08-15",
        "prioridadeID": 4,
        "statusID": 4,
        "computadorID": 9,
        "departamentoID": 4,
        "tecnicoID": 9,
        "usuarioID": 6
    },
    {
        "ID": 15,
        "titulo": "Dispositivo móvel não está sincronizando emails",
        "descricao":
        "Meu dispositivo móvel não está sincronizando meus emails corporativos corretamente.",
        "especialidadeID": 3,
        "data_abertura": "2023-08-15",
        "data_encerramento": "2023-08-16",
        "prioridadeID": 1,
        "statusID": 1,
        "computadorID": 10,
        "departamentoID": 5,
        "tecnicoID": 10,
        "usuarioID": 7
    },
]

df_tbChamado = pd.DataFrame(tbChamado)

df_tbChamado.to_csv('tbChamado.csv', index=False)

# Dados dos computadores
tbComputador = [
    {
        "ID": 1,
        "marca": "Dell",
        "modelo": "Latitude 5500",
        "numero_serie": "SN123456789",
        "SO_ID": 2,
        "data_aquisicao": "2022-01-15",
        "departamentoID": 3,
        "usuarioID": 7
    },
    {
        "ID": 2,
        "marca": "HP",
        "modelo": "EliteBook 840 G7",
        "numero_serie": "SN987654321",
        "SO_ID": 4,
        "data_aquisicao": "2021-06-20",
        "departamentoID": 2,
        "usuarioID": 3
    },
    {
        "ID": 3,
        "marca": "Lenovo",
        "modelo": "ThinkPad X1 Carbon",
        "numero_serie": "SN567891234",
        "SO_ID": 1,
        "data_aquisicao": "2023-03-10",
        "departamentoID": 5,
        "usuarioID": 10
    },
    {
        "ID": 4,
        "marca": "Apple",
        "modelo": "MacBook Pro",
        "numero_serie": "SN345678912",
        "SO_ID": 5,
        "data_aquisicao": "2020-09-05",
        "departamentoID": 1,
        "usuarioID": 1
    },
    {
        "ID": 5,
        "marca": "Dell",
        "modelo": "XPS 15",
        "numero_serie": "SN789123456",
        "SO_ID": 3,
        "data_aquisicao": "2022-11-30",
        "departamentoID": 4,
        "usuarioID": 5
    },
    {
        "ID": 6,
        "marca": "HP",
        "modelo": "Pavilion 14",
        "numero_serie": "SN456789123",
        "SO_ID": 2,
        "data_aquisicao": "2021-03-12",
        "departamentoID": 3,
        "usuarioID": 8
    },
    {
        "ID": 7,
        "marca": "Lenovo",
        "modelo": "IdeaPad 5",
        "numero_serie": "SN234567891",
        "SO_ID": 4,
        "data_aquisicao": "2023-07-18",
        "departamentoID": 2,
        "usuarioID": 2
    },
    {
        "ID": 8,
        "marca": "Acer",
        "modelo": "Aspire 5",
        "numero_serie": "SN891234567",
        "SO_ID": 1,
        "data_aquisicao": "2020-05-03",
        "departamentoID": 5,
        "usuarioID": 9
    },
    {
        "ID": 9,
        "marca": "Dell",
        "modelo": "Inspiron 13",
        "numero_serie": "SN678912345",
        "SO_ID": 5,
        "data_aquisicao": "2022-08-25",
        "departamentoID": 1,
        "usuarioID": 4
    },
    {
        "ID": 10,
        "marca": "Apple",
        "modelo": "MacBook Air",
        "numero_serie": "SN123457890",
        "SO_ID": 3,
        "data_aquisicao": "2021-12-08",
        "departamentoID": 4,
        "usuarioID": 6
    },
]

df_tbComputador = pd.DataFrame(tbComputador)

df_tbComputador.to_csv('tbComputador.csv', index=False)

# Dados dos status
tbStatus = [
    {
        "ID": 1,
        "status": "aberto"
    },
    {
        "ID": 2,
        "status": "solucionado"
    },
    {
        "ID": 3,
        "status": "atrasado"
    },
    {
        "ID": 4,
        "status": "fechado"
    },
]

df_tbStatus = pd.DataFrame(tbStatus)

df_tbStatus.to_csv('tbStatus.csv', index=False)

# Dados dos graus de prioridade
tbPrioridade = [
    {
        "ID": 1,
        "prioridade": "muito baixa"
    },
    {
        "ID": 2,
        "prioridade": "baixa"
    },
    {
        "ID": 3,
        "prioridade": "media"
    },
    {
        "ID": 4,
        "prioridade": "alta"
    },
    {
        "ID": 5,
        "prioridade": "muito alta"
    },
    {
        "ID": 6,
        "prioridade": "critico"
    },
]

df_tbPrioridade = pd.DataFrame(tbPrioridade)

df_tbPrioridade.to_csv('tbPrioridade.csv', index=False)

# Dados dos técnicos
tbTecnico = [
    {
        "ID": 1,
        "nome_tec": "Ricardo Silva",
        "idade": 27,
        "email": "ricardo@example.com",
        "especialidadeID": 2
    },
    {
        "ID": 2,
        "nome_tec": "Isabela Santos",
        "idade": 22,
        "email": "isabela@example.com",
        "especialidadeID": 3
    },
    {
        "ID": 3,
        "nome_tec": "Fernando Costa",
        "idade": 24,
        "email": "fernando@example.com",
        "especialidadeID": 1
    },
    {
        "ID": 4,
        "nome_tec": "Amanda Rodrigues",
        "idade": 20,
        "email": "amanda@example.com",
        "especialidadeID": 4
    },
    {
        "ID": 5,
        "nome_tec": "André Oliveira",
        "idade": 31,
        "email": "andre@example.com",
        "especialidadeID": 2
    },
    {
        "ID": 6,
        "nome_tec": "Carolina Pereira",
        "idade": 33,
        "email": "carolina@example.com",
        "especialidadeID": 3
    },
    {
        "ID": 7,
        "nome_tec": "Gabriel Fernandes",
        "idade": 30,
        "email": "gabriel@example.com",
        "especialidadeID": 1
    },
    {
        "ID": 8,
        "nome_tec": "Lúcia Almeida",
        "idade": 40,
        "email": "lucia@example.com",
        "especialidadeID": 4
    },
    {
        "ID": 9,
        "nome_tec": "Mário Santos",
        "idade": 24,
        "email": "mario@example.com",
        "especialidadeID": 1
    },
    {
        "ID": 10,
        "nome_tec": "Lara Lima",
        "idade": 26,
        "email": "lara@example.com",
        "especialidadeID": 2
    },
]

df_tbTecnico = pd.DataFrame(tbTecnico)

df_tbTecnico.to_csv('tbTecnico.csv', index=False)

# Dados dos tipos de departamentos
tbDepartamento = [
    {
        "ID": 1,
        "departamento": "RH"
    },
    {
        "ID": 2,
        "departamento": "Financeiro"
    },
    {
        "ID": 3,
        "departamento": "TI"
    },
    {
        "ID": 4,
        "departamento": "Marketing"
    },
    {
        "ID": 5,
        "departamento": "Comercial"
    },
]

df_tbDepartamento = pd.DataFrame(tbDepartamento)

df_tbDepartamento.to_csv('tbDepartamento.csv', index=False)

# Dados dos usuarios
tbUsuario = [
    {
        "ID": 1,
        "idade": 25,
        "nome_usuario": "João Silva",
        "email": "joao@example.com",
        "departamentoID": 1
    },
    {
        "ID": 2,
        "idade": 30,
        "nome_usuario": "Maria Santos",
        "email": "maria@example.com",
        "departamentoID": 2
    },
    {
        "ID": 3,
        "idade": 28,
        "nome_usuario": "Pedro Oliveira",
        "email": "pedro@example.com",
        "departamentoID": 3
    },
    {
        "ID": 4,
        "idade": 22,
        "nome_usuario": "Ana Souza",
        "email": "ana@example.com",
        "departamentoID": 4
    },
    {
        "ID": 5,
        "idade": 32,
        "nome_usuario": "Luiz Pereira",
        "email": "luiz@example.com",
        "departamentoID": 5
    },
    {
        "ID": 6,
        "idade": 27,
        "nome_usuario": "Juliana Costa",
        "email": "juliana@example.com",
        "departamentoID": 1
    },
    {
        "ID": 7,
        "idade": 29,
        "nome_usuario": "Rafael Almeida",
        "email": "rafael@example.com",
        "departamentoID": 2
    },
    {
        "ID": 8,
        "idade": 24,
        "nome_usuario": "Camila Rodrigues",
        "email": "camila@example.com",
        "departamentoID": 3
    },
    {
        "ID": 9,
        "idade": 26,
        "nome_usuario": "Gustavo Carvalho",
        "email": "gustavo@example.com",
        "departamentoID": 4
    },
    {
        "ID": 10,
        "idade": 31,
        "nome_usuario": "Fernanda Lima",
        "email": "fernanda@example.com",
        "departamentoID": 5
    },
]

df_tbUsuario = pd.DataFrame(tbUsuario)

df_tbUsuario.to_csv('tbUsuario.csv', index=False)

# Dados dos tipos de especialidades
tbEspecialidade = [
    {
        "ID": 1,
        "especialidade": "Help Desk"
    },
    {
        "ID": 2,
        "especialidade": "Service Desk"
    },
    {
        "ID": 3,
        "especialidade": "Redes e Segurança"
    },
    {
        "ID": 4,
        "especialidade": "Field Service"
    },
]

df_tbEspecialidade = pd.DataFrame(tbEspecialidade)

df_tbEspecialidade.to_csv('tbEspecialidade.csv', index=False)

# Dados dos tipos de sistemas operacionais.
tbSO = [
    {
        "ID": 1,
        "SO": "Windows 10"
    },
    {
        "ID": 2,
        "SO": "Windows 11"
    },
    {
        "ID": 3,
        "SO": "Ubuntu 20.04"
    },
    {
        "ID": 4,
        "SO": "macOS Big Sur"
    },
    {
        "ID": 5,
        "SO": "Chrome OS"
    },
]

df_tbSO = pd.DataFrame(tbSO)

df_tbSO.to_csv('tbSO.csv', index=False)

#----------------------------------------------------------------------
conn = sqlite3.connect('query.db')
#----------------------------------------------------------------------
create_tbChamado_sql = '''
CREATE TABLE IF NOT EXISTS tbChamado (
    ID INTEGER PRIMARY KEY,
    titulo TEXT,
    descricao INTEGER,
    especialidadeID INTEGER,
    data_abertura DATE,
    data_encerramento DATE,
    prioridadeID INTEGER,
    statusID INTEGER,
    computadorID INTEGER,
    departamentoID INTEGER,
    tecnicoID INTEGER,
    usuarioID INTEGER,
    FOREIGN KEY (especialidadeID) REFERENCES tbEspecialidade(ID),
    FOREIGN KEY (prioridadeID) REFERENCES tbPrioridade(ID),
    FOREIGN KEY (statusID) REFERENCES tbStatus(ID),
    FOREIGN KEY (computadorID) REFERENCES tbComputador(ID),
    FOREIGN KEY (departamentoID) REFERENCES tbDepartamento(ID),
    FOREIGN KEY (tecnicoID) REFERENCES tbTecnico(ID),
    FOREIGN KEY (usuarioID) REFERENCES tbUsuario(ID)
)
'''

conn.execute(create_tbChamado_sql)

df_tbChamado.to_sql('tbChamado', conn, if_exists='replace', index=False)
#----------------------------------------------------------------------

create_tbComputador_sql = '''
CREATE TABLE IF NOT EXISTS tbComputador (
    ID INTEGER PRIMARY KEY,
    marca TEXT,
    modelo TEXT,
    numero_serie TEXT,
    SO_ID,
    data_aquisicao DATE,
    departamentoID INTEGER,
    usuarioID INTEGER,
    FOREIGN KEY (SOID) REFERENCES tbSO(ID),
    FOREIGN KEY (departamentoID) REFERENCES tbDepartamento(ID),
    FOREIGN KEY (usuarioID) REFERENCES tbUsuario(ID)
)
'''

conn.execute(create_tbComputador_sql)

df_tbComputador.to_sql('tbComputador', conn, if_exists='replace', index=False)
#----------------------------------------------------------------------

create_tbStatus_sql = '''
CREATE TABLE IF NOT EXISTS tbStatus (
    ID INTEGER PRIMARY KEY,
    status TEXT
)
'''

conn.execute(create_tbStatus_sql)

df_tbStatus.to_sql('tbStatus', conn, if_exists='replace', index=False)
#----------------------------------------------------------------------

create_tbPrioridade_sql = '''
CREATE TABLE IF NOT EXISTS tbPrioridade (
    ID INTEGER PRIMARY KEY,
    prioridade TEXT
)
'''

conn.execute(create_tbPrioridade_sql)

df_tbPrioridade.to_sql('tbPrioridade', conn, if_exists='replace', index=False)
#----------------------------------------------------------------------

create_tbTecnico_sql = '''
CREATE TABLE IF NOT EXISTS tbTecnico (
    ID INTEGER PRIMARY KEY,
    nome_tec TEXT,
    idade INTEGER,
    email TEXT,
    especialidadeID INTEGER,
    FOREIGN KEY (especialidadeID) REFERENCES tbEspecialidade(ID)
)
'''

conn.execute(create_tbTecnico_sql)

df_tbTecnico.to_sql('tbTecnico', conn, if_exists='replace', index=False)
#----------------------------------------------------------------------

create_tbUsuario_sql = '''
CREATE TABLE IF NOT EXISTS tbUsuario (
    ID INTEGER PRIMARY KEY,
    nome_usuario TEXT,
    idade INTEGER,
    email TEXT,
    departamentoID INTEGER
)
'''

conn.execute(create_tbUsuario_sql)

df_tbUsuario.to_sql('tbUsuario', conn, if_exists='replace', index=False)
#----------------------------------------------------------------------

create_tbDepartamento_sql = '''
CREATE TABLE IF NOT EXISTS tbDepartamento (
    ID INTEGER PRIMARY KEY,
    departamento TEXT
)
'''

conn.execute(create_tbDepartamento_sql)

df_tbDepartamento.to_sql('tbDepartamento',
                         conn,
                         if_exists='replace',
                         index=False)
#----------------------------------------------------------------------

create_tbEspecialidade_sql = '''
CREATE TABLE IF NOT EXISTS tbEspecialidade (
    ID INTEGER PRIMARY KEY,
    especialidade TEXT
)
'''

conn.execute(create_tbEspecialidade_sql)

df_tbEspecialidade.to_sql('tbEspecialidade',
                          conn,
                          if_exists='replace',
                          index=False)
#----------------------------------------------------------------------

create_tbSO_sql = '''
CREATE TABLE IF NOT EXISTS tbSO (
    ID INTEGER PRIMARY KEY,
    SO TEXT
)
'''

conn.execute(create_tbSO_sql)

df_tbSO.to_sql('tbSO', conn, if_exists='replace', index=False)
#----------------------------------------------------------------------
#   ISERIR A QUERY AQUI

ordem_alfabetica()
print("\n----------------------------------------------------------------------\n")
prioridade()
print("\n----------------------------------------------------------------------\n")
qtde_chamados_usuario()
print("\n----------------------------------------------------------------------\n")
qtde_chamados_departamento()
print("")
#----------------------------------------------------------------------

# Fechando a conexão
conn.close()

#----------------------------------------------------------------------
