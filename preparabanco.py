import mysql.connector
from mysql.connector import errorcode

print("Conectando...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='llforce2'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `Kantu`;")

cursor.execute("CREATE DATABASE `Kantu`;")

cursor.execute("USE `Kantu`;")

# criando tabelas
TABLES = {}

TABLES['PEDIDOS'] = ('''
      CREATE TABLE `PEDIDOS` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `id_agencia` int(11) NOT NULL,
      `origem` VARCHAR(255) NOT NULL,
      `destino` VARCHAR(255) NOT NULL,
      `data_ida` DATE NOT NULL,
      `horario_ida` TIME NOT NULL,
      `data_retorno` DATE,
      `horario_retorno` TIME,
      `tipo_veiculo` ENUM('Ônibus', 'Van', 'Micro-ônibus') NOT NULL,
      `guia` ENUM('sim', 'nao') NOT NULL,
      `DATA` DATE NOT NULL,
      `HORA` TIME NOT NULL,
      `STATUS` VARCHAR(1) NOT NULL,    
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['AGENCIA'] = ('''
      CREATE TABLE `AGENCIA` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `NOME` varchar(70) NOT NULL,
      `CNPJ` int(14) NOT NULL,
      `CADASTUR` int(20) NOT NULL,            
      `CEP` int(8) NOT NULL,
      `RUA` VARCHAR(255) NOT NULL,
      `NUMERO` VARCHAR(10) NOT NULL,
      `BAIRRO` VARCHAR(100) NOT NULL,
      `CIDADE` VARCHAR(100) NOT NULL,
      `ESTADO` VARCHAR(2) NOT NULL,
      `TELEFONE` varchar(15) NOT NULL,
      `EMAIL` varchar(100) NOT NULL,
      `SENHA` varchar(100) NOT NULL,
      `DATA` DATE NOT NULL,
      `HORA` TIME NOT NULL,
      `STATUS` VARCHAR(1) NOT NULL,    
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['TRANSPORTE'] = ('''
      CREATE TABLE `TRANSPORTE` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `NOME` varchar(70) NOT NULL,
      `CNPJ` int(14) NOT NULL,
      `CADASTUR` int(20) NOT NULL,            
      `CEP` int(8) NOT NULL,
      `RUA` VARCHAR(255) NOT NULL,
      `NUMERO` VARCHAR(10) NOT NULL,
      `BAIRRO` VARCHAR(100) NOT NULL,
      `CIDADE` VARCHAR(100) NOT NULL,
      `ESTADO` VARCHAR(2) NOT NULL,
      `TELEFONE` varchar(15) NOT NULL,
      `EMAIL` varchar(100) NOT NULL,
      `SENHA` varchar(100) NOT NULL,    
      `DATA` DATE NOT NULL,
      `HORA` TIME NOT NULL,
      `STATUS` VARCHAR(1) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['GUIA'] = ('''
      CREATE TABLE `GUIA` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `NOME` varchar(70) NOT NULL,
      `CPF` int(14) NOT NULL,
      `CADASTUR` int(20) NOT NULL,            
      `CEP` int(8) NOT NULL,
      `RUA` VARCHAR(255) NOT NULL,
      `NUMERO` VARCHAR(10) NOT NULL,
      `BAIRRO` VARCHAR(100) NOT NULL,
      `CIDADE` VARCHAR(100) NOT NULL,
      `ESTADO` VARCHAR(2) NOT NULL,
      `TELEFONE` varchar(15) NOT NULL,
      `EMAIL` varchar(100) NOT NULL,
      `SENHA` varchar(100) NOT NULL,    
      `DATA` DATE NOT NULL,
      `HORA` TIME NOT NULL,
      `STATUS` VARCHAR(1) NOT NULL,

      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['ACEITE'] = ('''
      CREATE TABLE `ACEITE` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `ID_PEDIDO` int(11) NOT NULL,
        `ID_GUIA` int(11) NOT NULL,
        `ID_TRANSPORTE` int(11) NOT NULL,
        `ID_AGENCIA` int(11) NOT NULL,
        `DATA` DATE NOT NULL,
        `HORA` TIME NOT NULL,
        `VALOR` DECIMAL(10,2) NOT NULL,
        `STATUS` VARCHAR(1) NOT NULL,

      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()