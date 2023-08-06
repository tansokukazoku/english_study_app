import streamlit as st
from googletrans import Translator
from playsound import playsound
import glob

def main():
    st.title('さほのえいご学習')
    st.subheader(":blue[さあ、今日もがんばりましょう]")

    Lesson = st.sidebar.radio('レッスンをえらんでね',
        ('Lesson1','Lesson2', 'Lesson3'))
    
    if Lesson == 'Lesson1':
        Lesson1_texts = {'Good morning':'おはよう','Good night':'おやすみ','Excuse me':'すみません','Sure':'もちろん',
                         'Thank you':'ありがとう','See you tomorrow':'またあした','You are welcome':'どういたしまして',
                         'Nice to meet you':'はじめまして','I am sorry':'ごめんなさい','Here you are':'はいどうぞ',
                         'Have a good time':'たのしんできてね','That is good idea':'それはいいかんがえだ',
                         'big':'大きい','music':'おんがく','guitar':'ギター','water':'水','small':'小さい',
                         'window':'まど','piano':'ピアノ','friend':'友だち'}
        
        selected = st.radio('えいご',Lesson1_texts,index=1,horizontal=True)
        
        col1,col2 = st.columns(2)
        
        with col1:
            onsei = st.button('発音')
        with col2:
            jp_btn = st.button('日本語')

        if jp_btn:
            for Lesson1_text in Lesson1_texts:
                if selected == Lesson1_text:
                    t1 = Lesson1_texts.get(Lesson1_text)
                    st.write(t1) 
        if onsei:
            for Lesson1_text in Lesson1_texts:
                if selected == Lesson1_text: 
                    playsound('./english_study/音声データ/Lesson1/'+Lesson1_text+'.mp3')  
                    
    elif Lesson == 'Lesson2':
        Lesson2_texts = {'I live in Yokohama':'ぼくは横浜に住んでいます','Hou about you':'あなたはどうですか',
                         'I am in the soccer club':'僕はサッカークラブに入っています',
                        'I am from America':'私はアメリカ出身です','What is your name':'あなたの名前は何ですか',
                        'I am Yutaka':'僕はユタカです','I am from Japan':'僕は日本出身です',
                        'I am eleven years old':'僕は11歳です',
                        'many':'たくさん','page':'ページ','speak':'はなす','hot':'あつい','like':'すき',
                        'fast':'はやい','desk':'つくえ','time':'時間','classroom':'教室','textbook':'教科書',
                        'over there':'あそこで','listen to':'きく','after':'あとで','open':'ひらく',
                        'sit down':'すわる','run':'走る','sunny':'晴れ','happy':'うれしい',
                        'read':'読む','sing':'歌う'}
        
        selected = st.radio('えいご',Lesson2_texts,index=1,horizontal=True)
        
        col1,col2 = st.columns(2)
        
        with col1:
            onsei = st.button('発音')
        with col2:
            jp_btn = st.button('日本語')
        
        if jp_btn:
            for Lesson2_text in Lesson2_texts:
                if selected == Lesson2_text:
                    t2 = Lesson2_texts.get(Lesson2_text)
                    st.write(t2) 
        if onsei:
            for Lesson2_text in Lesson2_texts:
                if selected == Lesson2_text: 
                    playsound('./english_study/音声データ/Lesson2/'+Lesson2_text+'.mp3')  
                    
    elif Lesson == 'Lesson3':
        Lesson3_texts = {'Do you have any comic books':'あなたはマンガの本を持っていますか',
                         'Yes,I have a lot of them':'はい。私はたくさん持っています',
                         'Do you know the story of Cinderella':'あなたはシンデレラの物語を知っていますか',
                         'Do you have a pet?':'あなたはペットを飼っていますか','Yes,I do':'はい、飼っています',
                         'No,I do not':'いいえ、飼っていません','Do you want some tea?':'あなたは紅茶がほしいですか',
                         'I like chocolate ice cream':'私はチョコレートアイスクリームが好きです',
                         'library':'図書館','write':'書く','know':'知っている','chair':'いす','math':'さんすう',
                         'science':'科学','start':'はじめる','study':'勉強する','notebook':'ノート',
                         'homework':'宿題（しゅくだい）','dictionary':'辞書（じしょ）','favorite':'だいすき',
                         'magazine':'雑誌（ざっし）','a lot of':'たくさん','name':'なまえ','school':'学校（がっこう）',
                         'English':'英語（えいご）','Of course':'もちろん','Me,too':'わたしも','Yes,please':'はい、お願いします'}
        
        selected = st.radio('えいご',Lesson3_texts,index=1,horizontal=True)
        
        col1,col2 = st.columns(2)
        
        with col1:
            onsei = st.button('発音')
        with col2:
            jp_btn = st.button('日本語')
        
        if jp_btn:
            for Lesson3_text in Lesson3_texts:
                if selected == Lesson3_text:
                    t3 = Lesson3_texts.get(Lesson3_text)
                    st.write(t3) 
        if onsei:
            for Lesson3_text in Lesson3_texts:
                if selected == Lesson3_text: 
                    playsound('./english_study/音声データ/Lesson3/'+Lesson3_text+'.mp3')    
                       
if __name__=='__main__':
    main()
    