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

### Explain Predictions 
Using LIME, I created functions that takes a model and a test review (any input review, including user input) and predicts if the review is positive or negative. Then, it will explain how it got to that prediction 


### Find Key Insights for each product 


## Conclusion 


## Resources 



 
