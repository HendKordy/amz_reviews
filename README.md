![](https://www.business2community.com/wp-content/uploads/2014/04/how-to-get-amazon-reviews.png)

# amz_reviews



NLP Analysis on Amazon Reviews to Predict if the Customer Liked the Product or Not and Why


## Table of Content 
  
## Introduction 


The goal of this project is to use NLP to build a model that predict if the customer likes the product or not based on their written review, and find the reason why they gave this rating. I want to use NLP to reveal key cunsomer insights and track sentiment that could help businesses understand their products better.


## Data
  I used beautiful soup to scrape data from amazon.com. I focused mainly on t-shirt products, but I planning to adjust the model to incorporate a varity of products. The features scraped from amazon reviews are: 
   - **product name**
   - **attr** -- some reviews include details about the product such as what size was ordered and what color 
   - **score** (or rating out of 5)
   - **review title** 
   - **review body**


## Methods 


### Data cleaning:
* clean text from HTML format, remove punctuations 
* replace short words such as "I'll" -> "I will", "aren't" -> "are not"
* convert emojis to text :thumbsup: to "thumbsup"
* convert different words that describes the product into one word. Ex, "t-shirt, t shirt, tshirt" are all changes to "shirt" 



### Machine Learning:
I tested different models that predicts sentiment, the models I used are:
* Naive model
* Logistic regression on:
  * TD-IDF
  * N_grams

the best accuracy I reached was 0.9, and it is for using logistic regression on TD-IDF

### Explain Predictions 
Using LIME, I created functions that takes a model and a test review (any input review, including user input) and predicts if the review is positive or negative. Then, it will explain how it got to that prediction 


### Find Key Insights for each product 
I wanted initailly to create a model that takes a positive or a negative review text as an input, and it classifies the reason for that review. Reasons such as "wrong item", "arrived late", and so on. However, because there is no dataset that has "reason" column that I can use for training my model, I had to change my plan to something else. 
Instead of looking at one review, I am going to process multiple reviews for one product, then return most repeated reasons in the reviews. This helps descision makers to find out best and worst qualities of their products. 
To do that, I used N_grams on review text after doing lemmatization, removing stopwords, and splitting positive and negative reviews into separate dataframes. Then, I used collection.count to find the most common phrases. 

## Conclusion 
* There are many ways to do NLP, depending on the project, some methods will be more effective than others. You have to try different models and see which model has the best answer for your question.
* It is relatively easy to predict sentiment from reviews, but it is difficult to classify the reason behind the sentiment becuase there is no data to train the model as such. 
* LIME can be used to show which words contributed to the final prediction '
* Best accuracy reached was when I used Logistic regression on TD-IDF 



## Future work
* Train the models better to include different types of products 
* Create an app that:
  * takes input from user and gives prediction for sentiment 
  * takes a table of reviews and spits out top reasons for positive and negative reviews 
* Test the model on reviews from different websites
* Most of the products I scraped are for male, so I need to adjust the models to incorporate both male and female customer reviews. 




## Resources 
<https://towardsdatascience.com/from-dataframe-to-n-grams-e34e29df3460>
<https://towardsdatascience.com/customer-reviews-analysis-using-nlp-the-netflix-use-case-92b3645770e1>
<https://medium.com/artefact-engineering-and-data-science/customer-reviews-use-nlp-to-gain-insights-from-your-data-4629519b518e>
<https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568>



 
