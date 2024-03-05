import paramiko
import pandas as pd

#=== Adicionar credenciais
ssh_host = '15.235.110.107'
ssh_port = 2205
ssh_user = ''
ssh_password = ''

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh_client.connect(ssh_host, port=ssh_port, username=ssh_user, password=ssh_password)
    sftp_client = ssh_client.open_sftp()
    print('conectado')
except:
    print('Falha na conexão, credenciais possivelmente incorretas')
    exit()
    
remote_path = '/opt/dados/Mortalidade_Geral_2021.csv'

# É importante destacar que esse conjunto de dados possui 500mb de extensão
# e sua leitura remota com a biblioteca pandas pode ser longa. Sendo assim,
# é uma boa ideia utilizar o parâmetro 'nrows' para definir uma quantidade
# menor dos dados para exploração e somente depois tentar realizar a leitura
# completa, o que pode levar vários minutos

with sftp_client.open(remote_path) as file:
    df = pd.read_csv(file, delimiter=';')
    print('DataFrame pronto')