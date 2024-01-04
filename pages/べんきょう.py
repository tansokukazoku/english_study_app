import streamlit as st
from googletrans import Translator
from playsound import playsound
import glob
from gtts import gTTS
import os

def main():
    st.title('さほのえいご学習')
    st.subheader(":blue[さあ、今日もがんばりましょう]")

    Lesson = st.sidebar.radio('さあ英語学習！レッスンをえらんでね',
        ('Lesson1','Lesson2', 'Lesson3','Lesson4','Lesson5','Lesson6','Lesson7','Lesson8'))
    
    if Lesson == 'Lesson1':
        texts = {
                'Good morning':'おはよう','Good night':'おやすみ','Excuse me':'すみません','Sure':'もちろん',
                'Thank you':'ありがとう','See you tomorrow':'またあした','You are welcome':'どういたしまして',
                'Nice to meet you':'はじめまして','I am sorry':'ごめんなさい','Here you are':'はいどうぞ',
                'Have a good time':'たのしんできてね','That is good idea':'それはいいかんがえだ',
                'big':'大きい','music':'おんがく','guitar':'ギター','water':'水','small':'小さい',
                'window':'まど','piano':'ピアノ','friend':'友だち'
                }
    elif Lesson == 'Lesson2':
        texts = {
                'I live in Yokohama':'ぼくは横浜に住んでいます','Hou about you':'あなたはどうですか',
                'I am in the soccer club':'僕はサッカークラブに入っています',
                'I am from America':'私はアメリカ出身です','What is your name':'あなたの名前は何ですか',
                'I am Yutaka':'僕はユタカです','I am from Japan':'僕は日本出身です',
                'I am eleven years old':'僕は11歳です',
                'many':'たくさん','page':'ページ','speak':'はなす','hot':'あつい','like':'すき',
                'fast':'はやい','desk':'つくえ','time':'時間','classroom':'教室','textbook':'教科書',
                'over there':'あそこで','listen to':'きく','after':'あとで','open':'ひらく',
                'sit down':'すわる','run':'走る','sunny':'晴れ','happy':'うれしい',
                'read':'読む','sing':'歌う'
                }
    elif Lesson == 'Lesson3':
        texts = {
                'Do you have any comic books':'あなたはマンガの本を持っていますか',
                'Yes,I have a lot of them':'はい。私はたくさん持っています',
                'Do you know the story of Cinderella':'あなたはシンデレラの物語を知っていますか',
                'Do you have a pet?':'あなたはペットを飼っていますか','Yes,I do':'はい、飼っています',
                'No,I do not':'いいえ、飼っていません','Do you want some tea?':'あなたは紅茶がほしいですか',
                'I like chocolate ice cream':'私はチョコレートアイスクリームが好きです',
                'library':'図書館','write':'書く','know':'知っている','chair':'いす','math':'さんすう',
                'science':'科学','start':'はじめる','study':'勉強する','notebook':'ノート',
                'homework':'宿題（しゅくだい）','dictionary':'辞書（じしょ）','favorite':'だいすき',
                'magazine':'雑誌（ざっし）','a lot of':'たくさん','name':'なまえ','school':'学校（がっこう）',
                'English':'英語（えいご）','Of course':'もちろん','Me,too':'わたしも','Yes,please':'はい、お願いします'
                }
      
    elif Lesson == 'Lesson4':
        texts = {
                'He is eleven years old':'私は11歳です。',
                'He is twelve years old ':'私は12歳です。',
                'Is it your guitar ':'それはあなたのギターですか。',
                'She is in the music club':'彼女は音楽クラブに入っています。',
                'Is that girl your classmate':'あの女の子はあなたのクラスメートですか？',
                'Yes Her name is Mary':'はい、彼女の名前はメアリーです。',
                'Is this a violin?':'これはヴァイオリンですか？',
                'No,it is not':'いいえ、それはちがいます。','Is it yours?':'それはあなたのものですか？',
                'No,it is my brothers':'いいえ、私の兄のものです。',
                'tennis':'テニス','basketball':'バスケットボール','baseball':'野球（やきゅう）',
                'towel':'タオル','swim':'泳ぐ（およぐ）',
                'dance':'ダンス','soccer':'サッカー','badminton':'バトミントン','gym':'ジム',
                'pool':'プール','racket':'ラケット','sport':'スポーツ',
                'volleyball':'バレーボール','well':'よく','sleep':'眠る（ねむる）','bed':'ベッド',
                'hand':'手','see':'見る','doctor':'医者（いしゃ）','hospital':'病院（びょういん）'
                }     
         
    elif Lesson == 'Lesson5':
        texts = {
                'Does your father play any sports？':'あなたのお父さんは何かスポーツをしますか？',
                'He plays baseball very well.':'彼は野球がとても上手です。',
                'Does your brother play the violin?':'あなたのお兄さんはヴァイオリンを演奏しますか？',
                'No,he does not.':'いいえ、しません。',
                'My father gets up at six in the morning.':'私の父は朝6寺に起きます。',
                'Does she like music?':'彼女は音楽が好きですか？',
                'She does not like music.':'彼女は音楽が好きではありません。',
                'Does my father listen to Japanese music?':'あなたのお父さんは日本の音楽を聞きますか？',
                'next':'となりの','tall':'背が高い','mountain':'山',
                'bus':'バス','camera':'カメラ','shop':'店',
                'cold':'冷たい','jacket':'上着（うわぎ）','food':'食べ物','station':'駅（えき）',
                'get up':'起きる（おきる）','take a picture':'写真をとる','week':'1週間（1しゅうかん）',
                'Monday':'月曜日','Tuesday':'火曜日','Wednesday':'水曜日','Thursday':'木曜日',
                'Friday':'金曜日','Saturday':'土曜日','Sunday':'日曜日'
                } 
         
    elif Lesson == 'Lesson6':
        texts = {
                'they are not using the computer.':'彼らはコンピュータを使っていません。',
                'I am playing the piano.':'私はピアノを引いています。',
                'what are you doing?':'あなたは何をしているのですか？',
                'I am reading a book.':'私は本を読んでいます。',
                'what are they doing?':'彼らは何をしていますか？',
                'they are looking at the birds.':'彼らは鳥を見ています。',
                'is he watching TV?':'彼はテレビを見ていますか？',
                'he is watching a baseball game.':'彼は野球の試合を見ています。',
                'February':'2月','June':'6月','night':'夜',
                'May':'5月','March':'3月','August':'8月',
                'December':'12月','month':'月','September':'9月','calendar':'カレンダー',
                'July':'7月','every　day':'毎日','November':'11月',
                'October':'10月','birthday':'誕生日','year':'年','weekend':'週末',
                'today':'今日','January':'1月','April':'4月'
                } 
    
    elif Lesson == 'Lesson7':
        texts = {
                'I can play soccer.':'ぼくはサッカーが出来ます。',
                'can you play soccer?':'あなたはサッカーが出来ますか？',
                'I can not drink coffee.':'私はコーヒーが飲めません。',
                'can you drink coffee?':'あなたはコーヒーが飲めますか？',
                'can she run very fast?':'彼女はとても速く走ることは出来ますか？',
                'yes,she can.':'はい、出来ます。',
                'I can not have any pets.':'私はペットを飼うことが出来ません。',
                'Judy can make sandwiches very well.':'ジュディはサンドイッチを作ることがとても上手です。',
                'window':'窓（まど）','close':'閉める（しめる）','comic book':'漫画本（まんがぽん）',
                'tea':'紅茶（こうちゃ）','guitar':'ギター','before':'〜の前に',
                'bike':'自転車（じてんしゃ）','come':'来る（くる）','house':'家','make':'を作る',
                'room':'部屋','at home':'家で','bird':'鳥',
                'walk':'歩く','flower':'花','garden':'庭','wash':'を洗う',
                'morning':'朝','park':'公園','tree':'木'
                } 
    
    elif Lesson == 'Lesson8':
        texts = {
                'How much is this shirt?':'このシャツはいくらですか？',
                'Which do you like, baseball or soccer?':'あなたは野球とサッカーどちらが好きですか？',
                'Can I have a glass of water?':'水を一杯もらえますか？',
                'How old are you?':'あなたは何歳ですか？',
                'How many books do you have?':'あなたは本を何冊持っていますか？',
                'Can you pass me ketchup?':'ケチャップを取ってもらえますか？',
                'Whose bag is this?':'これはだれのカバンですか？',
                'How do you come to school?':'あなたはどのようにして学校へ来ますか？',
                'under':'〜の下に','years old':'〜さい','fish':'魚',
                'milk':'ミルク','buy':'〜を買う','fruit':'くだもの',
                'need':'ひつようとする','supermarket':'スーパーマーケット','father':'お父さん','mother':'お母さん',
                'brother':'兄','sister':'姉','grandfather':'おじいさん',
                'grandmother':'おばあさん','sofa':'ソファー','talk about':'〜について話す','family':'家族（かぞく）',
                'live':'住む','pet':'ペット','with':'といっしょに'
                } 
                  
    for text in texts:
        #音声ファイルを保存するファルダが無い時はフォルダを作成する 
        dir = './english_study/音声データ2/'+Lesson
        if not os.path.isdir(dir):
            os.mkdir(dir)
        else:
            pass
        
        #音声ファイルを作成する。音声ファイルがある時は音声ファイルを作成しない 
        fil = './english_study/音声データ2/'+Lesson+'/'+text+'.mp3'
        
        if os.path.isfile(fil):
            pass
        else:
            speech = gTTS(text=text, lang='en', slow=False)
            speech.save(fil)
        
         #音声ファイル(slow)を保存するファルダが無い時はフォルダを作成する 
        dir2 = './english_study/音声データ_slow/'+Lesson
        if not os.path.isdir(dir2):
            os.mkdir(dir2)
        else:
            pass
        
        #音声ファイル(slow)を作成する。音声ファイルがある時は音声ファイルを作成しない 
        fil2 = './english_study/音声データ_slow/'+Lesson+'/'+text+'.mp3'
        
        if os.path.isfile(fil2):
            pass
        else:
            speech = gTTS(text=text, lang='en', slow=True)
            speech.save(fil2)         
    
    selected = st.radio('えいご',texts,index=1,horizontal=True)
    
    col1,col2,col3 = st.columns(3)
    
    with col1:
        onsei = st.button('発音')
    with col2:
        onsei2 = st.button('発音(スロー)')
    with col3:
        jp_btn = st.button('日本語')

    if jp_btn:
        for text in texts:
            if selected == text:
                t1 = texts.get(text)
                st.write(t1) 
    if onsei:
        for text in texts:
            if selected == text: 
                fil = './english_study/音声データ2/'+Lesson+'/'+text+'.mp3'
                playsound(fil) 
    if onsei2:
        for text in texts:
            if selected == text: 
                fil2 = './english_study/音声データ_slow/'+Lesson+'/'+text+'.mp3'
                playsound(fil2)               
                       
if __name__=='__main__':
    main()
    