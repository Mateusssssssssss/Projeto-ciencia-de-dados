import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from scipy import stats
# Ler o dataset
dados = pd.read_csv('sales_data.csv')
print((dados.head()))
#Cria uma tabela Mes
dados['month'] = pd.to_datetime(dados['Sale_Date']).dt.month
#Variavel onde filta apenas novos clientes
new_customers = dados[dados['Customer_Type'] == 'New']
#Variavel que agrupa Novos clientes por mes
customer_type = new_customers.groupby('month').size().reset_index(name='Customer_Count')
#Variavel que agrupa Valor de venda por mes
sales_by_month = new_customers.groupby('month')['Sales_Amount'].sum().reset_index(name='Total_Sales')
#Agregação as dados Novos clientes e Valor de vendas
aggregated = pd.merge(customer_type, sales_by_month, on='month')
#Grafico de regressão para visualizar possivel correlação entre novos clientes e valor de vendas
sb.boxplot(aggregated)
plt.show()
sb.regplot(data=aggregated, x='Customer_Count', y='Total_Sales').set_title('Novos clientes por Mes')
plt.xlabel('Número de Novos Clientes')
plt.ylabel('Valor Total de Vendas')
plt.show()

# Calculo de correlação
correlation = aggregated['Customer_Count'].corr(aggregated['Total_Sales'])
print(correlation)
#Verificado que há uma correlação moderada a forte entre novos clientes e Valor de vendas 
# Valor de correlação = 0.6437009222786095