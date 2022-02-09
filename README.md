# engr-ALDA-fall2021-P42
# Amazon Review Data Sentiment Analysis 

## Abstract

We have implemented a project which performs mining on the data-set containing product reviews posted on Amazon.com. The data we used was preprocessed in order to make the textual part of the dataset more easy to handle by our models. We then performed a preliminary analysis to get an idea of the trends and relations present. This information was then used to perform sentiment analysis using a variety of techniques and then we introduce a new method that gave positive results. It can be found [here](https://www.kaggle.com/cynthiarempel/amazon-us-customer-reviews-dataset). The subset of data consisting of 360K reviews that was created using 10K rows from each file can be found [here](https://drive.google.com/file/d/1vxNYE9stXPzcsgPxHf8bb6NJS-umGn-_/view?usp=sharing)

## Background

Reviews are an integral part of the buying process. The enable the buyer to make an informed decision on whether or not to buy a particular product without having to directly interact with said product. An online shopping platform such an Amazon.com, relies heavily on reviews and ratings and these can be the difference between a customer choosing one product over another extremely similar product. At times a review may hold a sentiment more true to the reviews emotions on the product as opposed to just the star rating provided. We attempt to create a classifier that can accurately predict the sentiment present in a review.

Attributes such as the average the number of helpful votes received and whether it was a verified purchase can also help determine the degree of emotion.

In order to perform the above analysis and then create a model, chose to use a kaggle based Amazon Product Review Dataset. The dataset has approximately 113M reviews encompassing 36 product categories. The reviews are stored in separate tsv files based on the product category. For our analysis and modelling we will be using various samples of the data that are at most consisting of 3M reviews.


## Conclusion

The text preprocessing used has been shown to be good as it gives us just the lemmitized words that hold some meaning of the review without any other noise.

After comparing all the methods of sentiment analysis that we implemented, we find that using the word2vec representation to calculate the ratio of similarities of words of a sentences with the positive word 'good' and the negative word 'bad' and then taking all sentences below the threshhold of **1.25** to be nagative and anything above that to be positive gives us the best accuracy of **74.5%**

## File Descriptions

### ALDA Project Data Review

A preliminary analysis done on a subset of the data. This was to get a good overview of the data to better understand what preprocessing needs to be done.

### ALDA_Analysis_ReviewSize

Part of the preliminary data exploration and analysis done in order to find trends and relationships with regards to the size of a review. The data used in this notebook is the combined dataset of 360K rows.

### ALDA_TextRepresentation 

This notebook was used to experiment on multiple techniques of text processing and representation to find the best method. This was created before the midway report and is now outdated.

### SentimentAnalysisUsingVADER

This notebook was used to perform Sentiment Analysis using the existing lexicon NLTK lexicon called VADER.

### SentimentAnalysisUsingLR

This notebook was used to perform Sentiment Analysis using Binary Logistic Regression Model.

### ALDA_WordToVecSentimentAnalysis_Binary

This notebook has the latest text processing and representation used in this project. It also contains the implementation of all the sentiment analysis techniques using word2vec representation. The data used in this notebook is the combined dataset of 360K rows. Balacing reduced teh actually number of used rows to about 100K.

### ALDA_WordToVecSentimentAnalysis_Binary_BIG

This notebook has the latest text processing and representation used in this project. It also contains the implementation of all the sentiment analysis techniques using word2vec representation. The data used in this notebook is the electronics dataset consisting of 3M+ rows. Balacing reduced teh actually number of used rows to about 1M.

## Steps to run

All the jupyter notebooks were made using google colab using a tsv saved in a folder named ALDA_Project on google drive.

The steps to run any of the jupyter notebooks on google colab are as follows:

- Upload the dataset you want to work on onto google drive in a folder named ALDA_Project
- Upload the jupyter notebook to google drive
- Open the notebook saved on google drive using google colab
- Extablish the connection between the notebook and google drive by running the first block of code and filling in the authorization information
- Renam the file being imported using pandas based on what file you want to work on
- Run each block of code to get desired results


## Contributors

- [Anant Gadodia](agadodi@ncsu.edu)
- [Gabriel Francis](gfranci@ncsu.edu)
- [Shreya Someswar Karra](sskarra@ncsu.edu)


