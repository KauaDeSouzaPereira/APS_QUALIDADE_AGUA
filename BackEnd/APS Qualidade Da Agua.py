# Importando as bibliotecas
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split, KFold
from sklearn.preprocessing import StandardScaler
import mysql.connector
from keras.optimizers import SGD
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns


# Conectando ao banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='aps',
    password='7654321',
    database='aps_qualidade_agua'
)

cursor = conexao.cursor()

# Função para consultar a tabela no banco de dados
def consultar_dados(cursor):
    cursor.execute("SELECT ph, dureza, solido, cloramina, sulfato, condutividade , carb_organico, trihametanes, turbidez, potabilidade FROM sensores")
    dados = cursor.fetchall()
    return dados

# Função para inserir em uma tabela o resultado da previsão no banco de dados
def inserir_resultado(cursor, conexao, resultado):
    query = "INSERT INTO resultadosia (resultado) VALUES (%s)"
    valores = (resultado,)
    cursor.execute(query, valores)
    conexao.commit()

# Função para realizar a conexão do servidor de socket
# def iniciar_servidor_socket():

    # Novo socket é criado usando a função socket 
    # O socket.AF_INET é o domínio do endereço do socket
    # O socket.SOCK_STREAM está indicando que é um socket TCP, orientado a conexão
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Associando a porta do servidor do Banco de Dados
    # server_address = ('localhost', 3306)
    # print('Iniciando servidor em {} porta {}'.format(*server_address))
    # sock.bind(server_address) O método bind associa o socket a esse endereço do servidor

    # Escute por conexões de entrada
    # sock.listen(1)

    # while True: Mantendo o servidor rodando, permitindo que ele aceite conexões
        # Aguarde por uma conexão
        # print('Aguardando por uma conexão')
        # connection, client_address = sock.accept() Está aguardando uma conexão de entrada

        # try: O servidor tentará receber dados do cliente e responder.
            # print('Conexão de', client_address)

            # Receba os dados em pequenos pedaços e retransmita-os
            # while True:
                # data = connection.recv(16) Recebendo dados do cliente
                # print('Recebido {!r}'.format(data))

                # if data: Se algum dado for recebido, o servidor imprimirá os dados e enviará uma resposta de volta ao cliente 
                    # print('Enviando dados de volta ao cliente')
                    # connection.sendall(data)
                # else:
                    # print('Nenhum dado de', client_address)
                    # break

        # finally:
            #connection.close() Fechando a conexão com o cliente


# iniciar_servidor_socket() Utilizando a função


# Consultar os dados tabela
dados_completos = consultar_dados(cursor)

# Converter os dados consultados em um DataFrame do pandas
df_completo = pd.DataFrame(dados_completos, columns=['ph', 'dureza', 'solido', 'cloramina', 'sulfato', 'condutividade' , 'carb_organico', 'trihametanes', 'turbidez', 'potabilidade'])

df_completo = df_completo.dropna()

# Separar as colunas de treinamento e a coluna de teste
X = df_completo.drop('potabilidade', axis=1).values
y = df_completo['potabilidade'].values

# Normalizando as tabelas
scaler = StandardScaler()
X = scaler.fit_transform(X)


    # Definindo o modelo da IA
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(X.shape[1],)))
model.add(Dense(32, activation='relu',))
model.add(Dense(1, activation='sigmoid',))

    # Compilando o modelo da IA
opt = SGD(learning_rate=0.04)
model.compile(optimizer=opt, loss='mean_squared_error', metrics=['accuracy'])

# Definindo a validação cruzada
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

# Listas para armazenar as métricas
train_acc_histories = []
test_acc_histories = []
train_loss_histories = []
test_loss_histories = []

# K-fold Cross Validation
for train, test in kfold.split(X, y):
    # Treinando o modelo nos dados de treino
    history = model.fit(X[train], y[train], epochs=60, batch_size=32, validation_data=(X[test], y[test]))

    # Armazenando as métricas de treinamento
    train_acc_histories.append(history.history['accuracy'])
    test_acc_histories.append(history.history['val_accuracy'])
    train_loss_histories.append(history.history['loss'])
    test_loss_histories.append(history.history['val_loss'])


# Calculando a acurácia e a perda média de treino e teste ao longo das épocas
train_acc_mean = np.mean(train_acc_histories, axis=0)
test_acc_mean = np.mean(test_acc_histories, axis=0)
train_loss_mean = np.mean(train_loss_histories, axis=0)
test_loss_mean = np.mean(test_loss_histories, axis=0)

# Plotando a acurácia média de treino e teste ao longo das épocas
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(train_acc_mean, label='Acurácia de Treino', color='blue')
plt.title('Acurácia de Treino')
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(test_acc_mean[::-1], label='Acurácia de Teste', color='orange')  # Invertendo o eixo x
plt.title('Acurácia de Teste')
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(train_loss_mean, label='Perda de Treino', color='blue')
plt.title('Perda de Treino')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(test_loss_mean[::-1], label='Perda de Teste', color='orange')  # Invertendo o eixo x
plt.title('Perda de Teste')
plt.legend()

plt.tight_layout()
plt.show()

# Fazendo previsões no conjunto de teste
y_pred = model.predict(X[test])
y_pred_classes = (y_pred > 0.5).astype(int)

# Gerando a matriz de confusão
cm = confusion_matrix(y[test], y_pred_classes)

# Plotando a matriz de confusão
plt.figure(figsize=(6, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Matriz de Confusão')
plt.xlabel('Previsão')
plt.ylabel('Acerto')
plt.show()

# Fazendo previsões no conjunto de teste
previsoes = model.predict(X[test])
previsoes_classes = (previsoes > 0.5).astype(int)

# Inserir o resultado no banco de dados
for i, resultado in enumerate(previsoes_classes):
    inserir_resultado(cursor, conexao, int(resultado))

# Fechar a conexão com o banco de dados
conexao.close()

def testar_modelo_manualmente():
    # Testando o modelo com valores manuais
    # Substitua os valores abaixo pelos seus próprios valores
    valores_manuais = np.array([[0, 204.0, 20791.0, 7.3, 333.0, 474.0, 12.4, 66.7, 4.5]])
    valores_manuais = scaler.transform(valores_manuais)  # Não se esqueça de normalizar os valores manuais!
    previsao_manual = model.predict(valores_manuais)
    previsao_manual_classe = (previsao_manual > 0.5).astype(int)

    if previsao_manual_classe[0] == 0:
        print("A água não é potável.")
    else:
        print("A água é potável.")
  
