# Importando as bibliotecas
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import mysql.connector
from keras.optimizers import SGD
from keras.regularizers import l2
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
    cursor.execute("SELECT ph, dureza, turbidez, solido, condutividade, sulfato, potabilidade FROM sensores")
    dados = cursor.fetchall()
    return dados

# Função para inserir em uma tabela o resultado da previsão no banco de dados
def inserir_resultado(cursor, conexao, resultado):
    query = "INSERT INTO resultadosia (resultado) VALUES (%s)"
    valores = (resultado,)
    cursor.execute(query, valores)
    conexao.commit()

# Consultar os dados tabela
dados_completos = consultar_dados(cursor)

# Converter os dados consultados em um DataFrame do pandas
df_completo = pd.DataFrame(dados_completos, columns=['ph', 'dureza', 'turbidez', 'solido', 'condutividade', 'sulfato', 'potabilidade'])

df_completo = df_completo.dropna()

# Separar as colunas de treinamento e a coluna de teste
X = df_completo.drop('potabilidade', axis=1).values
y = df_completo['potabilidade'].values

# Normalizando as tabelas
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Dividindo os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state= 42)

# Definindo o modelo da IA
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
model.add(Dense(32, activation='relu', input_shape=(X_train.shape[1],)))
model.add(Dense(1, activation='sigmoid', input_shape=(X_train.shape[1],)))

# Compilando o modelo da IA
opt = SGD(learning_rate=0.01)
model.compile(optimizer='sgd', loss='mse', metrics=['accuracy'])

# Treinando o modelo nos dados de treino
history = model.fit(X_train, y_train, epochs=300, batch_size=32, validation_data=(X_test, y_test))


# Colocando os dados da acurácia dentro de um gráfico de visualização
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Acurácia de Treino')
plt.plot(history.history['val_accuracy'], label='Acurácia de Teste')
plt.title('Acurácia de Treino e Teste')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Perda de Treino')
plt.plot(history.history['val_loss'], label='Perda de Teste')
plt.title('Perda de Treino e Teste')
plt.legend()

plt.tight_layout()
plt.show()

# Fazendo previsões no conjunto de teste
y_pred = model.predict(X_test)
y_pred_classes = (y_pred > 0.5).astype(int)

# Gerando a matriz de confusão, pra saber quantos a IA acertou ou não
cm = confusion_matrix(y_test, y_pred_classes)

# Criando a matriz de confusão
plt.figure(figsize=(6, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Matriz de Confusão')
plt.xlabel('Previsão')
plt.ylabel('Verdadeiro')
plt.show()

# Fazendo previsões no conjunto de teste
previsoes = model.predict(X_test)
previsoes_classes = (previsoes > 0.5).astype(int)

# Inserir o resultado no banco de dados
for i, resultado in enumerate(previsoes_classes):
    inserir_resultado(cursor, conexao, int(resultado))

# Fechar a conexão com o banco de dados
conexao.close()
