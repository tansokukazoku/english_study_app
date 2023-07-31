import streamlit as st
from googletrans import Translator
from playsound import playsound
import glob

def translate(text):
    translator = Translator()
    changetext = translator.translate(text, dest='ja')
    return changetext.text

def main():
    st.title('さほのえいご学習')
    st.subheader(":blue[さあ、今日もがんばりましょう]")

    Lesson = st.sidebar.radio('レッスンをえらんでね',
        ('Lesson1','Lesson2', 'Lesson3'))
    
    if Lesson == 'Lesson1':
        Lesson1_texts = ['Good morning','Good night','Excuse me','Sure','Thank you',
                        'See you tomorrow','You are welcome','Nice to meet you',
                        'I am sorry','Here you are','Have a good time','That is good idea',
                        'big','music','guitar','water','small','window','piano','friend']
        
        selected = st.radio('えいご',Lesson1_texts,index=1,horizontal=True)
        
        col1,col2 = st.columns(2)
        with col1:
            jp_btn = st.button('日本語')
        with col2:
            onsei = st.button('発音')
        #cancel_btn = st.button('キャンセル')
        #next_btn = st.button('次へ')

        if jp_btn:
            for Lesson1_text in Lesson1_texts:
                if selected == Lesson1_text:
                    t1 = translate(Lesson1_text)
                    st.write(t1) 
        if onsei:
            for Lesson1_text in Lesson1_texts:
                if selected == Lesson1_text: 
                    playsound('./音声データ/Lesson1/'+Lesson1_text+'.mp3')  
    elif Lesson == 'Lesson2':
        Lesson2_texts = ['I live in Yokohama','Hou about you','I am in the soccer club',
                        'I am from America','What is your name','I am Yutaka','I am from Japan',
                        'I am eleven years old',
                        'many','page','speak','hot','like','fast','desk','time','classroom','textbook',
                        'over there','listen to','after','open','sit down','run','sunny','happy','read','sing']
        
        selected = st.radio('えいご',Lesson2_texts,index=1,horizontal=True)
        jp_btn = st.button('日本語')
        onsei = st.button('発音')
        
        if jp_btn:
            for Lesson2_text in Lesson2_texts:
                if selected == Lesson2_text:
                    t2 = translate(Lesson2_text)
                    st.write(t2) 
        if onsei:
            for Lesson2_text in Lesson2_texts:
                if selected == Lesson2_text: 
                    playsound('./音声データ/Lesson2/'+Lesson2_text+'.mp3')  
           
if __name__=='__main__':
    main()
    
            
            #files_onsei = glob.glob('./音声データ/Lesson1/*.mp3')
            #for file_onsei in files_onsei:
                #playsound(file_onsei)
    #Lesson1 = st.checkbox(label='Lesson1')
    #Lesson2 = st.checkbox(label='Lesson2')
    #Lesson3 = st.checkbox(label='Lesson3')