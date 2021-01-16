from wordcloud import WordCloud, ImageColorGenerator
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
import cv2
def get_noun(toss):
    
    okt = Okt()
    noun = okt.nouns(toss)
    for i,v in enumerate(noun):
            if len(v) <2 :
                noun.pop(i)
            
    
    count = Counter(noun)
    noun_list = count.most_common(1000)
    
    return noun_list


def Visualize(noun_list):
    img = cv2.imread("C:/python_ML/toss.jpeg", cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    img_mask = cv2.resize(img,(img.shape[1]*12,img.shape[0]*12))
    image_colors = ImageColorGenerator(img_mask)
    wc = WordCloud(font_path = 'C:\\Windows\\Fonts\\H2GTRE.TTF', 
                mask = img_mask,
                background_color = "white", 
                width = 4080, 
                height = 880, 
                max_words = 1000, 
                max_font_size = 300,
                min_font_size=1,
                scale = 2)
        
    wc.generate_from_frequencies(dict(noun_list))
    wc.recolor(color_func=image_colors)
    wc.to_file('keyword_6.png')
    
    
if __name__ =="__main__":
    filename = "C:/python_ML/tossopinion_2.txt"
    
    f = open(filename,'r',encoding = "UTF-16")
    toss = f.read()
    noun_list = get_noun(toss)
    Visualize(noun_list)