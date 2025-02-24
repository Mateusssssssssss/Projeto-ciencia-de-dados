import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from scipy import stats

dados = pd.read_csv('sales_data.csv')
print(dados)

dados['month'] = pd.to_datetime(dados['Sale_Date']).dt.month

customer_reg = dados[dados['Customer_Type'] == 'Returning']
#Variavel que agrupa Novos clientes por mes
customer_type = customer_reg.groupby('month').size().reset_index(name='Customer_Count')
#Variavel que agrupa Valor de venda por mes
sales_by_month = customer_reg.groupby('month')['Sales_Amount'].sum().reset_index(name='Total_Sales')
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
#Verificado que há uma correlação forte entre clientes recorrentes e Valor de vendas 
# Valor de correlação = 0.8830999044085946
