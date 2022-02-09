# used to take 10K rows from each TSV and create a new combined tsv

import pandas as pd
import os
os.chdir('data/')
lst=os.listdir()
print(lst)
df=pd.DataFrame()
i=0
for file in lst:
    print('reading ',file)
    df2=pd.read_csv(file,sep='\t',error_bad_lines=False, nrows=10_000)
    df2['product_category'].fillna(file.split('_')[3],inplace=True)
    print(df2.columns)
    df=df.append(df2, ignore_index=True)
    if i==0:
        df=df2
        i=1
    print(file," added")
    print(df.shape)
    print(df2.shape)
    
# print('out of loop')
# df2.columns

# len(pd.unique(df['review_id']))
# len(df.columns)
# df.groupby(['product_category']).size()
# print(pd.unique(df.product_category))
df.to_csv('amazon_reviews_us_combined.tsv',sep='\t',index=False)