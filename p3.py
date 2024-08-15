import pandas as pd
from mlxtend.frequent_patterns import fpgrowth, association_rules
from mlxtend.preprocessing import TransactionEncoder

# Load the dataset
file_name = r'C:\Users\harsh\OneDrive\Documents\VIT\FALLSEM 24-25\CBS3007\DA1 main\transactions.csv'
df = pd.read_csv(file_name)

# Convert the DataFrame to a list of transactions
transactions = df.groupby('TransactionID')['Item'].apply(list).tolist()

# Convert transactions to one-hot encoded DataFrame
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df_onehot = pd.DataFrame(te_ary, columns=te.columns_)

# Define the minimum support threshold
min_support = 0.4  # 40%

# Find frequent itemsets using FP-Growth
frequent_itemsets = fpgrowth(
    df_onehot, min_support=min_support, use_colnames=True)

# Print frequent itemsets
print("Frequent Itemsets:")
print(frequent_itemsets)

# Define the minimum confidence threshold
min_confidence = 0.7  # 70%

# Generate association rules
rules = association_rules(
    frequent_itemsets, metric="confidence", min_threshold=min_confidence)

# Print association rules
print("\nAssociation Rules:")
print(rules)
