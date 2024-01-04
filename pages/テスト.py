import streamlit as st
from googletrans import Translator
from playsound import playsound
import glob
from gtts import gTTS
import os
from PIL import Image


st.title('英語テスト')
st.subheader(":blue[テストです。間違えたら問題にもどりましょう！]")

Lesson = st.sidebar.radio('さあテストに挑戦！レッスンをえらんでね',
        ('Lesson1','Lesson2', 'Lesson3','Lesson4','Lesson5','Lesson6','Lesson7','Lesson8'))

if Lesson == 'Lesson1':
    texts = {
                'おはよう':'Good morning','おやすみ':'Good night','すみません':'Excuse me','もちろん':'Sure',
                'ありがとう':'Thank you','またあした':'See you tomorrow','どういたしまして':'You are welcome',
                'はじめまして':'Nice to meet you','ごめんなさい':'I am sorry','はいどうぞ':'Here you are',
                'たのしんできてね':'Have a good time','それはいいかんがえだ':'That is good idea'
                }
elif Lesson == 'Lesson2':
    texts = {
            'ぼくは横浜に住んでいます':'I live in Yokohama','あなたはどうですか':'Hou about you',
            '僕はサッカークラブに入っています':'I am in the soccer club',
            '私はアメリカ出身です':'I am from America','あなたの名前は何ですか':'What is your name',
            '僕はユタカです':'I am Yutaka','僕は日本出身です':'I am from Japan',
            '僕は11歳です':'I am eleven years old'
            }
elif Lesson == 'Lesson3':
    texts = {
            'あなたはマンガの本を持っていますか':'Do you have any comic books',
            'はい。私はたくさん持っています':'Yes,I have a lot of them',
            'あなたはシンデレラの物語を知っていますか':'Do you know the story of Cinderella',
            'あなたはペットを飼っていますか':'Do you have a pet?','はい、飼っています':'Yes,I do',
            'いいえ、飼っていません':'No,I do not','あなたは紅茶がほしいですか':'Do you want some tea?',
            '私はチョコレートアイスクリームが好きです':'I like chocolate ice cream'
            }
    
elif Lesson == 'Lesson4':
    texts = {
            '私は11歳です。':'He is eleven years old',
            '私は12歳です。':'He is twelve years old ',
            'それはあなたのギターですか。':'Is it your guitar ',
            '彼女は音楽クラブに入っています。':'She is in the music club',
            'あの女の子はあなたのクラスメートですか？':'Is that girl your classmate',
            'はい、彼女の名前はメアリーです。':'Yes Her name is Mary',
            'これはヴァイオリンですか？':'Is this a violin?',
            'いいえ、それはちがいます。':'No,it is not','それはあなたのものですか？':'Is it yours?',
            'いいえ、私の兄のものです。':'No,it is my brothers'
            }     
        
elif Lesson == 'Lesson5':
    texts = {
            'あなたのお父さんは何かスポーツをしますか？':'does your father play any sports？',
            '彼は野球がとても上手です。':'he plays baseball very well.',
            'あなたのお兄さんはヴァイオリンを演奏しますか？':'does your brother play the violin?',
            'いいえ、しません。':'no,he does not.',
            '私の父は朝6時に起きます。':'my father gets up at six in the morning.',
            '彼女は音楽が好きですか？':'does she like music?',
            '彼女は音楽が好きではありません。':'she does not like music.',
            'あなたのお父さんは日本の音楽を聞きますか？':'does my father listen to Japanese music?'
            } 
    test5_1 =('does father play your any sports','father does your play any sports','does your father play any sports？')
    test5_2 =('he baseball plays very well.','he plays baseball very well.','he plays very baseball well.')
    test5_3 =('does brother your play the violin?','does your brother play the violin?','your brother does play the violin?')
    test5_4 =('no,does he not.','no,he does not.','does he no not.')
    test5_5 =('my father gets up at six in the morning.','father gets up my six the morining does in.','my father gets up in six at the morning.')
    test5_6 =('does she like music?','she does like music?','does she music like?')
    test5_7 =('does she not like music.','she does not like music.','she like does not music.')
    test5_8 =('does my father listen to Japanese music?','my father does listen to Japanese music?','does my father Japanese listen to music?')
    tests = {'あなたのお父さんは何かスポーツをしますか？':test5_1,
                '彼は野球がとても上手です。':test5_2,
                'あなたのお兄さんはヴァイオリンを演奏しますか？':test5_3,
                'いいえ、しません。':test5_4,
                '私の父は朝6時に起きます。':test5_5,
                '彼女は音楽が好きですか？':test5_6,
                '彼女は音楽が好きではありません。':test5_6,
                '彼女は音楽が好きではありません。':test5_7,
                'あなたのお父さんは日本の音楽を聞きますか？':test5_8}
        
elif Lesson == 'Lesson6':
    texts = {
            '彼らはコンピュータを使っていません。':'they are not using the computer.',
            '私はピアノを引いています。':'I am playing the piano.',
            'あなたは何をしているのですか？':'what are you doing?',
            '私は本を読んでいます。':'I am reading a book.',
            '彼らは何をしていますか？':'what are they doing?',
            '彼らは鳥を見ています。':'they are looking at the birds.',
            '彼はテレビを見ていますか？':'is he watching TV?',
            '彼は野球の試合を見ています。':'he is watching a baseball game.'
            } 
    test6_1 =('are they not using the computer','they are not using the computer.','they are using not the computer')
    test6_2 =('am I playing the piano.','I am the playing  piano.','I am playing the piano.')
    test6_3 =('what are you doing?','what are doing you ?','what you are doing?')
    test6_4 =('I am a reading  book.','I am reading a book.','I reading am  a book.')
    test6_5 =('what are they doing?','what are doing they ?','what they are doing?')
    test6_6 =('they looking are at the birds.','they are looking the at birds.','they are looking at the birds.')
    test6_7 =('is he TV watching ?.','is he watching TV?','he is watching TV?')
    test6_8 =('he is a watching baseball game.','he is watching a baseball game.','he is watching a game baseball.')
    tests = {'彼らはコンピュータを使っていません。':test6_1,
                '私はピアノを引いています。':test6_2,
                'あなたは何をしているのですか？':test6_3,
                '私は本を読んでいます。':test6_4,
                '彼らは何をしていますか？':test6_5,
                '彼らは鳥を見ています。':test6_6,
                '彼はテレビを見ていますか？':test6_7,
                '彼は野球の試合を見ています。':test6_8}  

elif Lesson == 'Lesson7':
    texts = {
            'ぼくはサッカーが出来ます。':'I can play soccer.',
            'あなたはサッカーが出来ますか？':'can you play soccer?',
            '私はコーヒーが飲めません。':'I can not drink coffee.',
            'あなたはコーヒーが飲めますか？':'can you drink coffee?',
            '彼女はとても速く走ることは出来ますか？':'can she run very fast?',
            'はい、出来ます。':'yes,she can.',
            '私はペットを飼うことが出来ません。':'I can not have any pets.',
            'ジュディはサンドイッチを作ることがとても上手です。':'Judy can make sandwiches very well.'
            } 
    test7_1 =('can I play soccer.','I can play soccer.','I play can soccer.')
    test7_2 =('can you play soccer?','can you soccer play?','you can play soccer?')
    test7_3 =('I can  drink not coffee.','I can not drink coffee.','I can not coffee drink.')
    test7_4 =('can you drink coffee?','you can drink coffee?','can drink you coffee?')
    test7_5 =('can she fast run very?','can she very run fast?','can she run very fast?')
    test7_6 =('she can,yes.','yes,she can.','yes,can she.')
    test7_7 =('I can have not any pets.','I can not any have pets.','I can not have any pets.')
    test7_8 =('Judy make can sandwiches very well.','Judy can make very sandwiches well.','Judy can make sandwiches very well.')
    tests = {'ぼくはサッカーが出来ます。':test7_1,
                'あなたはサッカーが出来ますか？':test7_2,
                '私はコーヒーが飲めません。':test7_3,
                'あなたはコーヒーが飲めますか？':test7_4,
                '彼女はとても速く走ることは出来ますか？':test7_5,
                'はい、出来ます。':test7_6,
                '私はペットを飼うことが出来ません。':test7_7,
                'ジュディはサンドイッチを作ることがとても上手です。':test7_8} 
    
elif Lesson == 'Lesson8':
    texts = {
            'このシャツはいくらですか？':'How much is this shirt?',
            'あなたは野球とサッカーどちらが好きですか？':'Which do you like, baseball or soccer?',
            '水を一杯もらえますか？':'Can I have a glass of water?',
            'あなたは何歳ですか？':'How old are you?',
            'あなたは本を何冊持っていますか？':'How many books do you have?',
            'ケチャップを取ってもらえますか？':'Can you pass me ketchup?',
            'これはだれのカバンですか？':'Whose bag is this?',
            'あなたはどのようにして学校へ来ますか？':'How do you come to school?'
            } 
    test8_1 =('How much this shirt is ?','How much shirt is this?','How much is this shirt?')
    test8_2 =('do you Which like, baseball or soccer?','Which do you baseball, or soccer like?','Which do you like, baseball or soccer?')
    test8_3 =('Can I have a water glass of ?','Can I have a glass of water?','I Can have a glass of water?')
    test8_4 =('How old are you?','How are you old?','How old you are?')
    test8_5 =('How many you do have books?','How many do you have books?','How many books do you have?')
    test8_6 =('Can you pass ketchup me?','you Can pass me ketchup?','Can you pass me ketchup?')
    test8_7 =('Whose is bag this?','Whose is this bag?','Whose bag is this?')
    test8_8 =('How do you come to school?','How you do come to school?','How do you come school to?')
    tests = {   'このシャツはいくらですか？':test8_1,
                'あなたは野球とサッカーどちらが好きですか？':test8_2,
                '水を一杯もらえますか？':test8_3,
                'あなたは何歳ですか？':test8_4,
                'あなたは本を何冊持っていますか？':test8_5,
                'ケチャップを取ってもらえますか？':test8_6,
                'これはだれのカバンですか？':test8_7,
                'あなたはどのようにして学校へ来ますか？':test8_8}
                
selected = st.radio('テスト問題',texts,index=1,horizontal=True)

col1,col2 = st.columns(2)

with col1:
    for text in texts:
            if selected == text:
                for test in tests:
                    if text == test:
                        t2 = tests.get(test)
                        kaito_hyouji = st.radio('正しい並びのえいごをえらんでから決定ボタンを押してね!!',t2)
                        
    kettei_btn = st.button('決定')

with col2:
    if kettei_btn:
        st.write('回答は:',kaito_hyouji)

        for text in texts:
            if selected == text:
                t3 = texts.get(text)
                st.write('正解は:',t3) 
                if kaito_hyouji == t3:
                    img1 = Image.open('./english_study_ver2/data/正解.png')
                    st.image(img1,width=300)
                    playsound('./english_study_ver2/data/Buzzer_seikai.mp3')
                else:
                    img2 = Image.open('./english_study_ver2/data/不正解.png')
                    st.image(img2,width=300)
                    playsound('./english_study_ver2/data/Buzzer_fuseikai.mp3')
                        
                
                
                