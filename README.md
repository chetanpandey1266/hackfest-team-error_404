#  Intelligent Fashion System

Developed an interactive web platform to improve the user experience while shopping online. 

In the present situation, it is not possible for people to shop as they use to do earlier. This is a major problem in case of fashion industry. So we have come up a deep learning based approach where people can try and find the best outfit and accessories for them in the comfort of their home.


![Our Idea](./readme_imgs/fashionPPT_error_404.jpg)

## Fashion Advisor

### Main Idea

A recommendation system that suggests the user what minimal changes in his/her dress can make him/her look more fashionable. This helps the user to get better idea of what size and color he/she should pick for them.

### Implementation

This is an implementation of this paper: [Fashion++: Minimal Edits for Outfit Improvement](https://arxiv.org/pdf/1904.09261.pdf)

![Architecture](./readme_imgs/fashion%2B%2B_arch.jpg)

#### About the Architecture
The system uses a discriminative fashionability classifier that is trained on thousands of publicly available images of outfits that have been judged to be stylish. These serve as ground truth examples of fashionable outfits, and unfashionable examples are then bootstrapped by swapping garments on the fashionable examples with their least similar counterparts.

Once the classifier is trained, our system gradually updates the outfit in order to make it more fashionable. An image-generation neural network renders the newly adjusted look, using a variational auto-encoder to generate the silhouette and a conditional generative adversarial network (cGAN) to generate the color and pattern. 
 

## Make Up Transfer

### Main Idea

A generative adversial model to that transfers the makeup style of a person to other person's face. Using this network, user can try different make up styles and select which suits them the best.


This is an implementation of this paper: [Lipstick ain’t enough: Beyond Color Matching for In-the-Wild Makeup Transfer](https://arxiv.org/pdf/2104.01867.pdf)

![Architecture](./readme_imgs/makeup_arch.jpg)


## How to use

Download the necessary files from the following link:
 - [FashionPlus](https://drive.google.com/drive/folders/1KvCyxeoowHmVvTslO1VIhDtIExJwFzV3?usp=sharing): Create a `checkpoint` folder inside the `FashionPlus` folder and download all the files from the provided link to that folder
 - [CPM](https://drive.google.com/drive/folders/1fWc3s6ia4-gnyTnr2UfQ_gaQ-HERWgbq?usp=sharing): Download all the files from the provided link and place them inside the `CPM` folder.

Then open the main folder in your terminal and type the following commands to use the web app
```python
python3 app.py
```
Due to hardware restrictions, the make up transfer can't be integrated with web platform. So we have provided the google colab link of the following.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1wQt_uamj51rJNJ_6_dK3S3CMuwqefNtd?usp=sharing)



