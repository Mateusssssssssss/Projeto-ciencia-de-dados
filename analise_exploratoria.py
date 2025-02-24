import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from scipy import stats
#Ler o dataset
dados = pd.read_csv('sales_data.csv')
print(dados.head())
#Variaveis para teste shapiro
dados_discount = dados['Discount']
dados_salesamount = dados['Sales_Amount']
#confirmado assimetria nos dados, ja que se trata de vendas, onde pode se ter outlier muito altos ou baixos
#dependendo do numero de vendas
shapiro = stats.shapiro(dados_salesamount)
print(shapiro)
#descrição dos dados(minino e maximo, desvio padrao, quartil, media)
descricao = dados.describe()
print(descricao)
#Verificando duplicatas
dados_dup = dados.duplicated().sum()
print(dados_dup)
#Verificando se havia algum dados nulo no dataset
dados_null = dados.isnull().sum()
print(dados_null)
#Verificando se há algum Outlier
#Verificado que não há Outlier
sb.boxplot(dados[['Quantity_Sold', 'Unit_Price', 'Discount']])
plt.show()
#Comparação de valor de vendas por região
sales_by_region = dados.groupby('Region')['Sales_Amount'].sum().reset_index()
sb.barplot(sales_by_region, x='Region', y='Sales_Amount', hue='Region').set_title('Valor de Vendas Por Região')
plt.show()
#Verificando o Metodo de pagamento mais usado
method = dados.groupby('Payment_Method')['Sales_Amount'].sum().reset_index()
sb.barplot(method, x='Payment_Method', y='Sales_Amount', hue='Payment_Method').set_title('Metodos de Pagamento')
plt.show()
#Valor de vendas Por Vendendor
sales_rep = dados.groupby('Sales_Rep')['Sales_Amount'].sum().reset_index()
sb.barplot(sales_rep, x='Sales_Rep', y='Sales_Amount',hue='Sales_Rep').set_title('Valor de vendas Por Vendedores')
plt.show()

# Quantidade de Vendas por Vendedor
sales_qtd = dados.groupby('Sales_Rep')['Quantity_Sold'].sum().reset_index()
sb.barplot(sales_qtd, x='Sales_Rep', y='Quantity_Sold',hue='Sales_Rep').set_title('Quantidade de vendas Por Vendedores')
plt.show()

# Quais tipos de cliente geram mais receita(Novos CLientes ou Clientes Recorrentes)
sales_customer = dados.groupby('Customer_Type')['Sales_Amount']
sb.boxplot(x='Sales_Amount', y='Customer_Type', data=dados, hue='Customer_Type').set_title('Valor de Vendas: Clientes novos X Clientes Recorrentes')
plt.show()

#numero de Novos clientes e Clientes recorrentes
customers = dados['Customer_Type'].value_counts()
print(customers)

# cria uma tabela temporaria month e Extrai o mês
dados['month'] = pd.to_datetime(dados['Sale_Date']).dt.month
#Agrupo o valor de vendas por mes
sales_by_month = dados.groupby('month')['Sales_Amount'].sum().reset_index()
#Grafico
sb.barplot(sales_by_month, x='month', y='Sales_Amount', hue='Sales_Amount').set_title('Valor de Vendas por Mes')
plt.xticks(ticks=range(12), labels=['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
plt.show()
#Contagem de clientes novos por mes
new_customers = dados[dados['Customer_Type'] == 'New']
customer_type = new_customers.groupby('month').size().reset_index(name='Customer_Count')
sb.barplot(customer_type, x='month', y='Customer_Count',hue='Customer_Count').set_title('Novos clientes por Mes')
# Adiciona rotulos aos meses
plt.xticks(ticks=range(12), labels=['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
plt.show()

# Cria uma figura em branco
plt.figure()
#Localização de onde vai ficar a imagem
plt.subplot(2,2,1)
#Grafico
sb.barplot(sales_by_region, x='Region', y='Sales_Amount',hue='Region')
#Localização de onde vai ficar a imagem
plt.subplot(2,2,2)
#Grafico
sb.barplot(sales_rep, x='Sales_Rep', y='Sales_Amount',hue='Sales_Rep')
#Localização de onde vai ficar a imagem
plt.subplot(2,2,3)
#Grafico
sb.boxplot(x='Sales_Amount', y='Customer_Type', data=dados, hue='Customer_Type')
#Localização de onde vai ficar a imagem
plt.subplot(2,2,4)
#Grafico
sb.barplot(method, x='Payment_Method', y='Sales_Amount', hue='Payment_Method')
#Carrega as Fihuras
plt.show()

#Criação de uma Figura em Branco
plt.figure()
#localização da figura
plt.subplot(2,1,1)
#Grafico
sb.barplot(sales_rep, x='Sales_Rep', y='Sales_Amount',hue='Sales_Rep')
#localização da figura
plt.subplot(2,1,2)
#Grafico
sb.barplot(sales_qtd, x='Sales_Rep', y='Quantity_Sold',hue='Sales_Rep')

#Carrega a figura
plt.show()



