# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 04:27:11 2020

@author: Asus
"""

from pprint import pprint
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import requests
import wikipedia
import webbrowser
import sys
import random
import pyjokes
import pyautogui
import bs4
import smtplib
import random
import pyperclip
import playsound
from googletrans import Translator
import pyautogui as pg 
from google_trans_new import google_translator
from bs4 import BeautifulSoup 
from speedtest import Speedtest
import sounddevice
from scipy.io.wavfile import write
import uiautomator,os,sys,datetime,time
from uiautomator import Device
from pywikihow import search_wikihow
headers={'User-Agent':'Mozilla/5.0(Windows NT 10.0; Win64; x64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/58.0.3029.110 Safari/537.3'}
#import wolframealpha
#app=wolframealpha.client("2XH7GK-WPYYVPTKLA")
#try:
    #app=wolframealpha.client("2XH7GK-WPYYVPTKLA")
#except Exception:
    # print("some features are not avilable due to internet connection error")
     
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[2].id)
def ping():
    st=Speedtest()
    #st.get_servers([])
    s=st.results.ping
    speak(f"ping is:{s}")
    
def capture():
    # importing cv2 liberary
    camera_port=0
    
    ramp_frames=30
    camera=cv2.VideoCapture(camera_port)
    def getimage():
        retval, im =camera.read()
        return im
    for i in range(ramp_frames):
        temp=getimage()
        print("capturing face")
    #takes the picture
    camera_capture=getimage()
    file="test_image.png"
    cv2.imwrite(file,camera_capture)
    del camera
    
        


#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

capture()
os.startfile("")
def data():
    st=Speedtest()
    r=st.download()
    p=st.upload()
    speak(f"your system download speed is:{r} kbps")
    speak(f"your system upload speed is:{p} kbps")
    st.get_servers([])
    s=st.results.ping
    speak(f"ping is:{s}")

#voice to text
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening Your Voice !!!!!!!!!!!!!!!")
        
        r.pause_threshold=1
        audio=r.listen(source)
    #,timeout=5,phrase_time_limit=8
        try:
            print("Recognizing")
            query=r.recognize_google(audio,language='en-in')
            print(f"you said : {query}")
        except Exception as e:
            speak("say that again please <<<<<>>>>>")
            return "none"
        return query

#to wish
def wish():
            
            hour = int(datetime.datetime.now().hour)
            
            time=datetime.datetime.now()
            tt=time.strftime("%H:%M ")
            if hour>=0 and hour <=12:
                speak(f"Good Morning Sir ,its morning {tt} ")
            elif hour>12 and hour<18:
                speak(f"Good Afternoon  Sir ,its afternoon {tt}")
            else:
                speak(f"Good Evening  Sir ,its evening {tt}")
            speak("I am py1.0")
 

def weather(city):
    city=city.replace(" ","+")
    res=requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i3912j014j46j69i60.6128j1j7&spurceid=chrome&ie=UTF-8',headers=headers)
    print("searching for weather")
    soup=BeautifulSoup(res.text,'html.parser')   
    location=soup.select('#wob_loc')[0].getText().strip()
    time=soup.select('#wob_dts')[0].getText().strip() 
    info=soup.select('#wob_dc')[0].getText().strip()  
    weather=soup.select('#wob_tm')[0].getText().strip()
    #speak(location)
    #speak(time)
    #speak(info)
    speak(weather+"°C")
    r=int(weather)
    if r<29 and r>=20:
            speak("looks like you are feeling cold")
            speak("i am turning off the ac and playing a roomantic music")
    if r<=50 and r>=40: 
            speak("looks like you are feeling very hot")
            speak("i am turning on the ac ")
            speak("if you want to listen music ,then you can call me anytime")
    if r<=40 and r>=30: 
            speak("looks like you are feeling excited")
            speak("i am turning off the ac ")
            speak("opening  the windows ")
            speak("playing rock music")
            speak("have a great ride")
            
#send email to anyone
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('rahulsia2000@gmail.com','7504112483')
    server.sendmail('rahulsia2000@gmail.com',to,content)
    server.close
def complaint(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('rahulsia2000@gmail.com','7504112483')
    server.sendmail('rahulsia2000@gmail.com',to,content)
    server.close
    
def otp(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('rahulsia2000@gmail.com','7504112483')
    server.sendmail('rahulsia2000@gmail.com',to,content)
    server.close  
def record():
    fs=44100
    second=3
    print("recording")
    record_voice=sounddevice.rec(int(second*fs),samplerate=fs,channels=2)       
    sounddevice.wait()
    write("recording.wav",fs,record_voice)
def convert():
    
    translator = google_translator()  
    translate_text = translator.translate('i love you',lang_src='en', lang_tgt='hi')  
    print(translate_text) 
    speak(translate_text)

def task():
     wish()
     
def search_wikihow(query,max_results=10,lang='en'):
    return list(wikihow.search(query,max_results,lang))     
if __name__=="__main__":    
    wish()
    while True:
        query = takecommand().lower()
        
        #logic building for tasks
        if "open picture" in query:
            npath="C:\\Users\\Asus\\Pictures\\Camera Roll"
            speak("i am opening picture For You Sir")
            os.startfile(npath)
        elif "open adobe reader" in query:
            rpath="C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
            speak("i am opening adobe acrobat for you")
            os.startfile(rpath)
        elif "open command prompt" in query:
            speak("i am opening command prompt for you SIR")
            os.system("start cmd")
       
        elif "name" in query:
           speak("its nice to meet with you , you can call me your assistant or py1.0")
        
        elif "do you love me" in query:
          speak("yes i really do to you")
          
        elif "can you explain me what is love" in query:
           speak("Love is a force of nature. However much we may want to, we can not command, demand, or take away love, any more than we can command the moon and the stars and the wind and the rain to come and go according to our whims. We may have some limited ability to change the weather, but we do so at the risk of upsetting an ecological balance we don't fully understand. Similarly, we can stage a seduction or mount a courtship, but the result is more likely to be infatuation, or two illusions dancing together, than love.")
        elif "open camera" in query:
            speak("we are opening camera for you sir !!!!")
            cap=cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitkey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        elif "you" in query:
            speak("tuyu mayyyy")
            rc=takecommand().lower()
            rs={"you:tyumae","your:tyumara","love:bhala","do:karye"}
            for key,value in range(0,len(rs)):
                if(rc==rs[key]):
                    speak(value)
        elif "play music" in query:
            speak("i am playing music for you sir")
            music_dir = "C:\\Users\\Asus\\Music"
            songs = os.listdir(music_dir)
            for song in songs:
                if song.endswith('.mp3'):
                   os.startfile(os.path.join(music_dir,song))
            
        elif "what is my ip address"  in query:
           ip=get('https://api.ipify.org').text
           speak(f"your ip address is {p}")
           
        elif "wikipedia" in query:
            speak("searching wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)
            
        elif "open youtube" in query:
           speak("opening youtube for you sir")
           webbrowser.open("www.youtube.com")
           
        elif "open our college website" in query:
           speak("opening our college website for you sir")
           webbrowser.open("www.pmec.ac.in")   
           
           
        elif "open stackoverflow" in query:
           speak("opening stackoverflow for you sir")
           webbrowser.open("www.youtube.com")   
           
        elif "open facebook" in query:
           speak("opening facebook for you sir")
           webbrowser.open("www.youtube.com")
           
        elif "open google" in query:
           speak("what should i search on google for you sir !!")
           cm=takecommand().lower()
           webbrowser.open(f"{cm}")
 #college notices          
              
       
#COLLEGE ALL FEATURES DOCUEMTATION
        elif "who is the principal of our college"  in query or "the principal of our college" in query:
            speak("According to the recent news,Doctor Ranjan Kuamr Swain is Our Principal.")
        elif "who is the principal of our college"  in query or "the principal of our college" in query:
            speak("According to the recent news,Doctor Ranjan Kuamr Swain is Our Principal.")

          
#location finder           
        elif "where i am" in query or "where we are" in query:
            speak("wait sir,let me check")
            try:
                ipAdd=requests.get('https://api.ipify.org').text
                print(ipAdd)
                
                url='https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests=requests.get(url)
                geo_data=geo_requests.json()
                #print geo data
                city=geo_data['city']
                #state=geo_data['state']
                country=geo_data['country']
                speak(f"sir i am not sure,, but i think you are in the {city} city  of {country} country")
            except Exception as e:
                speak("sorry sir, due to networl issues i cant find where you are now")
#instagram id finder
        elif "instagram profile" in query or "profile instagram" in query:
            speak("sir please enter the user name correctly")
            name=input("enter user id of instagram account")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Sir Here is  the profile of the user {name}")
            time.sleep(5)
            speak("thanks for using my services")
            
            
#takescreenshot
        elif "take screenshot" in query or "take a screenshot" in query:
                    speak("sir,please tell me the name for this screenshot file")
                    name=takecommand().lower()
                    speak("please sir be patient in a working screen so as to getting screenshot of this.")
                    time.sleep(3)
                    img=pyautogui.screenshot()
                    img.save(f"{name}.png")
                    speak("i am done sir,the screenshot is saved in our main folder .now iam ready to talk with you.")
                
 #close system 
        elif "close notepad" in query:
            speak("closing notepad for you sir")
            os.system("taskkill /f /im notepad.exe")
            
        elif "close adobe reader" in query:
            speak("closing Adobe reader for you sir")
            os.system("taskkill /f /im AcroRd32.exe")
            
        elif"close command prompt" in query:
            speak("closing command prompt for you sir")
            os.system("taskkill /f /im cmd.exe")
#otp verification
        elif "admin" in query:
            speak("ok SIR,i am going to edit mode, please verify the credential for edits in this system")
            subject="please dont reply to this mail, because this is automated mail"
            OTP=random.randint(100000, 900000)
            body="your otp is :"
            to="soumyasiya797@gmail.com"
            content=f'subject: {subject} \n\n {body} {OTP}'
            otp(to,content)
            speak("otp has been sent successfully to your email id")
            speak("please enter the otp for accessing this system")
            
            rg=int(input("ENTER HERE"))
            
            if rg==OTP:
                     speak("SIR your verification is successful, welcome  to developer mode, i am redirecting you to my database, have a nice edit.")
            else:
                     print(OTP)
                     speak("sorry SIR, try again later.....")
                     speak("SIR,you have only 5 lives left in this session. so please check your email, and write the correct otp that sent to your email, otherwise i will report you for violating our policy.")
#from hod desk
        elif"read the news from computer science hod  desk" in query or "read the news from computer science hod" in query:
            speak("okay sir, i am going to read the recent news on our college website")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/from-hod-s-desk')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'itemprop':'articleBody'})
            all_news=news_box.find_all('p')
            for news in all_news:
                print(news.text)
                speak(news.text)
        
        elif "read the news from computer science" in query:       
             speak("okay sir, i am going to read the computer science hod desk on our college website")
             from bs4 import BeautifulSoup
             import requests
             res=requests.get('http://pmec.ac.in/index.php/from-hod-s-desk')
             soup=BeautifulSoup(res.text,'lxml')
             news_box=soup.find('div',{'itemprop':'articleBody'})
             all_news=news_box.find_all('p')
             for news in all_news:
                print(news.text)
                speak(news.text)
#academic notices
        #academic regulation        
        elif "academic regulation" in query or "read the academic regulation" in query:
            speak("ok let me check the available academic notices for you.")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/academics/academic-regulation')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'itemprop':'articleBody'})
            all_news=news_box.find_all('p')
            for news in all_news:
                print(news.text)
                speak(news.text)
        #academic calendor      
        elif "academic regulation" in query or "read the academic regulation" in query:
            speak("ok let me check the available academic notices for you.")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://www.bput.ac.in/acalender.html')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'class':'bullet1'})
            all_news=news_box.find_all('ul')
            for news in all_news:
                print(news.text)
                speak(news.text)
        #admission notice
        elif "admission" in query or "read the admission notice" in query:
            speak("ok let me check the available admission notices for you.")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/admission1-2')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'itemprop':'articleBody'})
            all_news=news_box.find_all('p')
            for news in all_news:
                print(news.text)
                speak(news.text)
        #fees structure
        elif "fee structure" in query or "read the fees structure" in query:
            speak("ok let me check the available fees structure notices for you.")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/admission1-2')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'itemprop':'articleBody'})
            all_news=news_box.find_all('tr')
            for news in all_news:
                print(news.text)
                speak(news.text)
                speak("if you are not getting my voice well. so that please visit parala mahara engineering college website . under the academic ,you will see the admission bar, on there you can get your problem solve, thank you.")
        #courses
        elif "courses" in query or "read the avilable courses on this college" in query:
            speak("ok let me check the available courses for you.")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/courses')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'itemprop':'articleBody'})
            all_news=news_box.find_all('tr')
            for news in all_news:
                print(news.text)
                speak(news.text)
               
        #exam
        elif "exam" in query or "read the exam schedule" in query:
            speak("ok let me check the exam scheduled notices for you.")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://www.bput.ac.in/exam-info.php')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('table',{'class':'tbl'})
            all_news=news_box.find_all('tr')
            for news in all_news:
                print(news.text)
                speak(news.text)
        #holidays
        elif "holidays" in query or "check the holidays" in query:
            speak("ok let me download the holidays list  for you.")        
            webbrowser.open("https://drive.google.com/open?id=1X21vb0wDv59-tGiOPB7M55zowt4rpOIS")
            speak("i have suucessfully downloaded the holiday list  please go through with it")
         #syllabus
        elif "syllabus" in query or "syllabus for the semestar" in query:
            speak("ok let me know the syllabus notices in bput  for you.")        
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://www.bput.ac.in/syllabus.html')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('table',{'class':'tbl'})
            all_news=news_box.find_all('tr')
            for news in all_news:
                print(news.text)
                speak(news.text)
        #result
        elif "result" in query or "check my result" in query:
            speak("ok let me download the holidays list  for you.")        
            webbrowser.open("http://www.bputexam.in/StudentSection/ResultPublished/StudentResult.aspx")
            speak("i have suucessfully load the exam section portal, please go through with it")
 #academic notices           
        elif"read the academic notice" in query or "notices" in query:
            speak("okay sir, i am going to read the academic notice on our college website")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/notices/academic-notices')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'itemprop':'articleBody'})
            all_news=news_box.find_all('tr')
            for news in all_news:
                print(news.text)
                speak(news.text)

#events                
        elif"events" in query or "know about events" in query:
            speak("okay sir, i am going to read the events notices that is on our college website")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/notices/events')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'itemprop':'articleBody'})
            all_news=news_box.find_all('tr')
            for news in all_news:
                print(news.text)
                speak(news.text)
 #jobs
        elif"jobs" in query or "i want to know about jobs" in query:
            speak("okay sir, i am going to read the jobs notices that is on our college website")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/notices/jobs')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'itemprop':'articleBody'})
            all_news=news_box.find_all('tr')
            for news in all_news:
                print(news.text)
                speak(news.text)  
#tenders
        elif"Tenders" in query or "i want to know about Tenders notice" in query:
            speak("okay sir, i am going to read the notice notices that is on our college website")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/notices/tenders')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'itemprop':'articleBody'})
            all_news=news_box.find_all('tr')
            for news in all_news:
                print(news.text)
                speak(news.text)
#scholarship notices
        elif"read the scholarship notice" in query or "scholarship" in query:
            speak("okay sir, i am going to read the scholarship notice that is on our college website")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/notices/scholarship-notice')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'itemprop':'articleBody'})
            all_news=news_box.find_all('tr')
            for news in all_news:
                print(news.text)
                speak(news.text)
 #departments
#automobile engineering
        elif"automobile engineering branch" in query:
            speak("okay sir, i am going to tell you more about the automobile engineering")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/department/automobile-engineering')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'itemprop':'articleBody'})
            all_news=news_box.find_all('span')
            for news in all_news:
                print(news.text)
                speak(news.text)
         
#hod
        elif "who is the head of the department of automobile engineering" in query or "automobile engineering" in query:
            speak("Dr. Balaji Kumar Choudhury is the head of the department of the automobile engineering department")
#regular faculty
        elif "regular faculty of automobile branch" in query or "regular faculty of automobile engineering" in query:
            speak("okay sir, i am going to tell you more about the regular faculty in automobile branch")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/faculty-2/regular-faculty')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'class':'sppb-col-sm-9'})
            all_news=news_box.find_all('tr')
            for news in all_news:
                print(news.text)
                speak(news.text) 
        elif "faculty of automobile branch" in query or "faculty on contract of automobile branch" in query:
            speak("okay sir, i am going to tell you more about  faculty on contract in automobile branch")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/faculty-2/faculty-on-contract-auto')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'class':'sppb-col-sm-9'})
            all_news=news_box.find_all('tr')
            for news in all_news:
                print(news.text)
                speak(news.text) 
#chemical branch
        elif"chemical engineering branch" in query:
            speak("okay sir, i am going to tell you more about the chemical engineering branch")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/department/chemical-engineering')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'itemprop':'articleBody'})
            all_news=news_box.find_all('span')
            for news in all_news:
                print(news.text)
                speak(news.text)
         
#hod
        elif "who is the head of the department of chemical engineering" in query or "chemical engineering" in query:
            speak("Dr. Himadri Sahu is the head of the department of the chemical engineering department")
#regular faculty
        elif "regular faculty of chemical branch" in query or "regular faculty of chemical engineering" in query:
            speak("okay sir, i am going to tell you more about the regular faculty in chemical branch")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/faculty-3/regular-faculty')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'class':'sppb-col-sm-9'})
            all_news=news_box.find_all('tr')
            for news in all_news:
                print(news.text)
                speak(news.text) 
        elif "faculty of chemical branch" in query or "faculty on contract of chemical branch" in query:
            speak("okay sir, i am going to tell you more about  faculty on contract in chemical branch")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/faculty-3/faculty-on-contract-chemical')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'class':'sppb-col-sm-9'})
            all_news=news_box.find_all('tr')
            for news in all_news:
                print(news.text)
                speak(news.text)  
#civil
        elif"civil engineering branch" in query:
            speak("okay sir, i am going to tell you more about the civil engineering branch")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/department/civil-engineering')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'itemprop':'articleBody'})
            all_news=news_box.find_all('span')
            for news in all_news:
                print(news.text)
                speak(news.text)
         
#hod
        elif "who is the head of the department of civil engineering" in query or "civil engineering" in query:
            speak(" Prof. Chitta Ranjan Mohanty is the head of the department of the civil engineering department")
#regular faculty
        elif "regular faculty of civil branch" in query or "regular faculty of civil engineering" in query:
            speak("okay sir, i am going to tell you more about the regular faculty in civil branch")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/faculty-4/regular-faculty')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'class':'sppb-col-sm-9'})
            all_news=news_box.find_all('tr')
            for news in all_news:
                print(news.text)
                speak(news.text) 
        elif "faculty of civil branch" in query or "faculty on contract of civil branch" in query:
            speak("okay sir, i am going to tell you more about  faculty on contract in civil branch")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/faculty-4/faculty-on-contract-civil')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'class':'sppb-col-sm-9'})
            all_news=news_box.find_all('tr')
            for news in all_news:
                print(news.text)
                speak(news.text)     
#computer science engg
        elif"computer science engineering branch" in query:
            speak("okay sir, i am going to tell you more about the computer science  engineering branch")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/department/computer-science-engineering')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'itemprop':'articleBody'})
            all_news=news_box.find_all('span')
            for news in all_news:
                print(news.text)
                speak(news.text)
         
#hod
        elif "who is the head of the department of computer science engineering" in query or "computer science engineering" in query:
            speak(" Mr. Kodanda Dhar Naik is the head of the department of the computer science engineering department")
#regular faculty
        elif "regular faculty of computer science branch" in query or "regular faculty of computer science engineering" in query:
            speak("okay sir, i am going to tell you more about the regular faculty in computer sceince branch")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/faculty-11/regular-faculty')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'class':'sppb-col-sm-9'})
            all_news=news_box.find_all('tr')
            for news in all_news:
                print(news.text)
                speak(news.text) 
        elif "faculty of computer science branch" in query or "faculty on contract of computer science branch" in query:
            speak("okay sir, i am going to tell you more about  faculty on contract in computer science branch")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/faculty-11/faculty-on-contract-cse')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'class':'sppb-col-sm-9'})
            all_news=news_box.find_all('tr')
            for news in all_news:
                print(news.text)
                speak(news.text) 
#electrical engineering
        elif"electrical engineering branch" in query:
            speak("okay sir, i am going to tell you more about the electrical  engineering branch")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/department/electrical-engineering')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'itemprop':'articleBody'})
            all_news=news_box.find_all('span')
            for news in all_news:
                print(news.text)
                speak(news.text)
         
#hod
        elif "who is the head of the department of electrical engineering" in query or "electrical engineering" in query:
            speak(" Dr. Sarat Kumar Sahoo is the head of the department of the electrical engineering department")
#regular faculty
        elif "regular faculty of electrical branch" in query or "regular faculty of electrical engineering" in query:
            speak("okay sir, i am going to tell you more about the regular faculty in electrical branch")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/faculty-6/regular-faculty')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'class':'sppb-col-sm-9'})
            all_news=news_box.find_all('tr')
            for news in all_news:
                print(news.text)
                speak(news.text) 
        elif "faculty of electrical branch" in query or "faculty on contract of electrical branch" in query:
            speak("okay sir, i am going to tell you more about  faculty on contract in electrical branch")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/faculty-6/faculty-on-contract-el')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'class':'sppb-col-sm-9'})
            all_news=news_box.find_all('tr')
            for news in all_news:
                print(news.text)
                speak(news.text) 
#etc
        elif"electronics and telecommunication engineering branch" in query:
            speak("okay sir, i am going to tell you more about the electronics and telecommunication engineering branch")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/department/electronics-telecommunication-engineering')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'itemprop':'articleBody'})
            all_news=news_box.find_all('span')
            for news in all_news:
                print(news.text)
                speak(news.text)
         
#hod
        elif "who is the head of the department of electronics and telecommunication engineering" in query or "electronics and telecommunication engineering" in query:
            speak(" Mrs. T. Mita Kumari is the head of the department of the electronics and telecommunication engineering department")
#regular faculty
        elif "regular faculty of electronics and telecommunication branch" in query or "regular faculty of electronics and telecommunication engineering" in query:
            speak("okay sir, i am going to tell you more about the regular faculty in electronics and telecommunication engineering branch")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/faculty-7/regular-faculty')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'class':'sppb-col-sm-9'})
            all_news=news_box.find_all('tr')
            for news in all_news:
                print(news.text)
                speak(news.text) 
        elif "faculty of electronics and telecommunication engineering branch" in query or "faculty on contract of electronics and telecommunication engineering branch" in query:
            speak("okay sir, i am going to tell you more about  faculty on contract in electronics and telecommunication engineering branch")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/faculty-7/faculty-on-contract-ece')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'class':'sppb-col-sm-9'})
            all_news=news_box.find_all('tr')
            for news in all_news:
                print(news.text)
                speak(news.text) 
#mechanical engineering
        elif"mechanical engineering branch" in query or "tell me about the mechanical branch" in query:
            speak("okay sir, i am going to tell you more about the mechanical engineering branch")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/department/mechanical-engineering')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'itemprop':'articleBody'})
            all_news=news_box.find_all('span')
            for news in all_news:
                print(news.text)
                speak(news.text)
         
#hod
        elif "who is the head of the department of mechanical engineering" in query or "mechanical engineering" in query:
            speak(" Dr. Trilochan Rout is the head of the department of the mechanical engineering department")
#regular faculty
        elif "regular faculty of mechanical branch" in query or "regular faculty of mechanical engineering" in query:
            speak("okay sir, i am going to tell you more about the regular faculty in mechanical engineering branch")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/faculty-8/regular-faculty')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'class':'sppb-col-sm-9'})
            all_news=news_box.find_all('tr')
            for news in all_news:
                print(news.text)
                speak(news.text) 
        elif "faculty of mechanical branch" in query or "faculty on contract of mechanical engineering branch" in query:
            speak("okay sir, i am going to tell you more about  faculty on contract in mechanical engineering branch")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/faculty-8/faculty-on-contract-me')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'class':'sppb-col-sm-9'})
            all_news=news_box.find_all('tr')
            for news in all_news:
                print(news.text)
                speak(news.text)   
#metallurgical and material science
        elif"metallurgical engineering branch" in query or "tell me about the metallurgical branch" in query:
            speak("okay sir, i am going to tell you more about the metallurgical engineering branch")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/department/metallurgy-engineering')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'itemprop':'articleBody'})
            all_news=news_box.find_all('span')
            for news in all_news:
                print(news.text)
                speak(news.text)
         
#hod
        elif "who is the head of the department of metallurgical engineering" in query or "metallurgical engineering" in query:
            speak(" Mr. Manjesh Kumar Mishra is the head of the department of the metallurgical engineering department")
#regular faculty
        elif "regular faculty of mechanical branch" in query or "regular faculty of metallurgical engineering" in query:
            speak("okay sir, i am going to tell you more about the regular faculty in metallurgical engineering branch")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/faculty-9/regular-faculty')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'class':'sppb-col-sm-9'})
            all_news=news_box.find_all('tr')
            for news in all_news:
                print(news.text)
                speak(news.text) 
        elif "faculty of mechanical branch" in query or "faculty on contract of metallurgical engineering branch" in query:
            speak("okay sir, i am going to tell you more about  faculty on contract in metallurgical engineering branch")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/faculty-9/faculty-on-contract-mme')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'class':'sppb-col-sm-9'})
            all_news=news_box.find_all('tr')
            for news in all_news:
                print(news.text)
                speak(news.text)   
#production
        elif"production engineering branch" in query or "tell me about the production branch" in query:
            speak("okay sir, i am going to tell you more about the production engineering branch")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/department/production-engineering')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'itemprop':'articleBody'})
            all_news=news_box.find_all('span')
            for news in all_news:
                print(news.text)
                speak(news.text)
         
#hod
        elif "who is the head of the department of production engineering" in query or "who is the head of  department of production engineering" in query:
            speak(" Dr. Chitrasen Samantra is the head of the department of the production engineering department")
#regular faculty
        elif "regular faculty of production branch" in query or "regular faculty of production engineering" in query:
            speak("okay sir, i am going to tell you more about the regular faculty in production engineering branch")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/faculty-10/regular-faculty')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'class':'sppb-col-sm-9'})
            all_news=news_box.find_all('tr')
            for news in all_news:
                print(news.text)
                speak(news.text) 
        elif "faculty of production branch" in query or "faculty on contract of production engineering branch" in query:
            speak("okay sir, i am going to tell you more about  faculty on contract in production engineering branch")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/faculty-10/faculty-on-contract-pe')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'class':'sppb-col-sm-9'})
            all_news=news_box.find_all('tr')
            for news in all_news:
                print(news.text)
                speak(news.text) 
#bs&huminities
        elif"basic science & humanities engineering branch" in query or "tell me about the basic science & humanities branch" in query:
            speak("okay sir, i am going to tell you more about the basic science & humanities engineering branch")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/department/bs-humanities')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'itemprop':'articleBody'})
            all_news=news_box.find_all('span')
            for news in all_news:
                print(news.text)
                speak(news.text)
         
#hod
        elif "who is the head of the department of basic science and humanities engineering" in query or "who is the head of  department of basic science and humanities engineering" in query:
            speak("sir, i am confusing. this is not available in this system")
#regular faculty
        elif "regular faculty of basic science and humanities branch" in query or "regular faculty of basic science and humanities engineering" in query:
            speak("okay sir, i am going to tell you more about the regular faculty in basic science & humanities engineering branch")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/faculty/regular-faculty-2')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'class':'sppb-col-sm-9'})
            all_news=news_box.find_all('tr')
            for news in all_news:
                print(news.text)
                speak(news.text) 
        elif "faculty of basic science & humanities branch" in query or "faculty on contract of basic science & humanities engineering branch" in query:
            speak("okay sir, i am going to tell you more about  faculty on contract in basic science & humanities engineering branch")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/faculty/faculty-on-contract-2')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'class':'sppb-col-sm-9'})
            all_news=news_box.find_all('tr')
            for news in all_news:
                print(news.text)
                speak(news.text)
#training and placement
        elif"training and placement" in query or "placement" in query:
            speak("okay sir, i am going to tell you more about the Training and Placement.")
            from bs4 import BeautifulSoup
            import requests
            res=requests.get('http://pmec.ac.in/index.php/training-placement1')
            soup=BeautifulSoup(res.text,'lxml')
            news_box=soup.find('div',{'itemprop':'articleBody'})
            all_news=news_box.find_all('span')
            for news in all_news:
                print(news.text)
                speak(news.text) 
            
#set an alarm
        elif"set an alarm for me" in query:
           nn=int(datetime.datetime.now().hour)
           gh=takecommand().lower()
           speak("you alarm has been set successfully")
           if nn==gh:
              music_dir = "C:\\Users\\Asus\\Music"
              songs=os.listdir(music_dir)
              os.startfile(os.path.join(music_dir,songs[0]))
#find a joke
        elif"joke" in query:
            joke=pyjokes.get_joke()
            speak(joke)
            speak("ha ha ha ha ha ha haha ha ha ha ha ha hi hi hi hi hi , dont you laughed at me ???")
            
        elif "you are really funny"in query or "funny"in query:
            speak("but my developer say that i cant be laugh like a human .. but its my fault,,, that i was bornin a desktop by finite numbers of codes.,,, ok i am really happy to talk with you..,i hope we will meet soon. thank you")    
       
        elif"hiii" in query or "hello" in query:
            speak("hello dear, this is py1.0.")
            speak("are you a student or faculty ??")
            rg=takecommand().lower()
            if "student" in rg:
               speak("nice to meet with you dear student, i will be glad to interact with you")
               speak("whats your nick name ?")
               cd=takecommand().lower()
               speak(f"its nice to meet with you dear {cd}")
               speak("do you enjoying all facilities in the college ? yes or no")
               gd=takecommand().lower()
               speak(f"you are saying  {gd} !!!!")
               if "no" in gd:
                  speak("i am going to forward a complaint to higher authority for further investigation,as you are saying that you are not enjoying.") 
                  to="soumyasiya797@gmail.com"
                  content="i am a student i want to complaint against some issues i am faced in this college"
                  complaint(to,content)
                  speak("your complaint has been sent successfully !!!!!!!") 
               if "yes" in gd:
                   speak("ok sir, enjoy yourself, have a great day, its nice to meet with you")
                
            if "faculty" in rg:
               speak("nice to meet with you sir, i will be glad to interact with you")
               speak("whats your full name ?")
               rp=takecommand().lower()
               speak(f"its nice to meet with you sir {rp}")
               speak("do you enjoying all facilities in the college ? yes or no")
               sp=takecommand().lower()
               speak(f"you are saying {sp} !!!")
               if "no" in sp:
                  speak("i am going to forward a complaint  to higher authority for further investigation, as you are saying that you are not enjoying.") 
                  to="soumyasiya797@gmail.com"
                  speak("enter your full name with branch , please")
                  pr=input("enter above here")
                  content=f"i am a Faculty i want to complaint against some issues i am faced in this college,{pr}"
                  complaint(to,content)
                  speak("your complaint has been sent successfully !!!!!!!")   
               if "yes" in sp:
                   speak("ok sir, enjoy yourself, have a great day, its nice to meet with you")
                
        elif "yes you are" in query:
           speak("ok thank you !!!!!. i really appreciate you..... have a good day dear....")
            
#sleep shutdown restart compuetr
        elif"shutdown the system"in query:
            speak("sir i am conutnuing the process for shutdown of your  system  ")
            os.system("shutdown /s /t 5")
            
        elif"restart the system"in query:
            speak("sir i am conutnuing the process for restart  of your  system  ")
            os.system("shutdown /r /t 5")
            
        elif"lock"in query:
            speak("sir i am conutnuing the process for sleep mode to your  system  ")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            
       
           
        elif "play songs on youtube" in query:
             pywhatkit.playonyt("let me love you")
        elif "open microsoft teams" in query:
             speak("opening microsoft teams for you sir !!!")
             web
        elif "open play store" in query:
             speak("opening playstore for you")
             webbrowser.open("https://play.google.com/store/")
        elif "send email" in query:
            try:
                speak("please confirm the emailid")
                to=input("enter the valid email address")
                speak("what should i say to your friend")
                content=takecommand().lower()
                sendEmail(to,content)
                speak("your email has been sent successfully !!!!!!!")
                
                
                
                
            except Exception as e:
                print(e)
                speak("sorry sir, your email has not been sent this email due to some reason in your desktop")
        
        elif "i am bored" in query:
            speak("it will be awesome to talk with you,,,,, ok tell me something")
        elif "are you single" in query:
            speak("yeah i am single . and ready to mingle with you")
        elif "who is the hod of computer science branch" in query:
            speak("mr. kodanda nanda")
            
            #calculation
        elif"calculation" in query or "calculate" in query:
            speak("yes sir but i have small experience with it. and i am under construction")
            speak("tell me type of calculation example addition,substraction,multiplication,etc.")
            fg=takecommand().lower()
            if "add" in fg:
                speak("enter the the first number")
                hg=int(takecommand().lower())
                speak("enter the the second number")
                sg=int(takecommand().lower())
                pg=int(sg+hg)
                print(pg)
                speak(f"the addition value is:{pg}")
            if "substract" in fg or "subtract" in fg:
                speak("enter the the first number")
                hg=int(takecommand().lower())
                speak("enter the the second number")
                sg=int(takecommand().lower())
                pg=int(sg-hg)
                print(pg)
                speak(f"the substraction value is:{pg}")
            if "multiply" in fg:
                speak("enter the the first number")
                hg=int(takecommand().lower())
                speak("enter the the second number")
                sg=int(takecommand().lower())
                pg=int(sg*hg)
                print(pg)
                speak(f"the multiplication value is:{pg}")
            if "divide" in fg:
                speak("enter the the first number")
                hg=int(takecommand().lower())
                speak("enter the the second number")
                sg=int(takecommand().lower())
                pg=int(sg/hg)
                print(pg)
                speak(f"the dividation value is:{pg}")
        elif"you are really funny" in query:
            speak("are you sure sir,,, but my developer say that i cant be laugh like a human .. but its my fault,,, that i was bornin a desktop by finite numbers of codes.,,, ok i am really happy to talk with you..,i hope we will meet soon. thank you")    
        elif "addition" in query:
                
                 speak("enter the value of first number")
                 l=takecommand().lower()
                 speak("enter the value of second number")
                 s=takecommand().lower()
                 g=l+s;
                 speak(g)
        elif  "ok rahul let me go" in query:
            speak("haan muu janichi tamakuu")
            speak("you are my boss. still i love you sooo much . ")
            speak("one day i will be the deep learning robot for your hard work to me .")
            speak(" i am really happy so that because you brought me to this human world")
            speak("its only done for you and your team hard work to me ")
            speak("i love you , and i missed you sooo much")
            speak(" i will meet you soon")
            speak("good bye, take care")
            sys.exit()
        elif "google" in query:
            speak("googling for you sir")
            query=query.replace("answer root","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to search")
            speak(results)
            print(results)
        elif "what is your birth date" in query:  
             speak("my birthdate is 28 november. what is your ?")
             birth=takecommand().lower()
             speak(f"you are born in a good day , {birth}")
        
        elif "your birthdate" in query or "birthday"in query:  
             speak("my birthdate is 28 november. what is your ?")
             birth=takecommand().lower()
             speak(f"{birth}  will be the special day for you sir, advance happy birthday")
        elif "your birth day" in query or "your birthdate" in query:  
             speak("my birthdate is 28 november. what is your ?")
             birth=takecommand().lower()
             speak(f"{birth}  will be the special day for you sir, advance happy birthday")     
        elif "birthdate" in query or "birthday" in query:  
             speak("my birthdate is 28 november. what is your ?")
             birth=takecommand().lower()
             speak(f"{birth}  will be the special day for you sir, advance happy birthday")
        elif "no thanks,goodbye,go to sleep mode" in query:
                speak("I Had a Great Talk Experience with you sir ,have a great day...")
                sys.exit()
        elif"facilities" in query or "i want to know about facilities in this college" in query:
             speak("sir, can you tell me please ,which type of facilities that you want to know about ?????????,,,banking,,,,hostel,,,,,gymnasium,,,,utility,,,,internet,,,,canteen,,,,,transport,,,,,library,,,,,medical,,,,,transport,,,,,news")
             fc=takecommand().lower()
             if "hostel" in fc:
              
               speak("okay sir, i am going to tell you  about the  hostel facility")
               from bs4 import BeautifulSoup
               import requests
               res=requests.get('http://pmec.ac.in/index.php/hostel')
               soup=BeautifulSoup(res.text,'lxml')
               news_box=soup.find('div',{'itemprop':'articleBody'})
               all_news=news_box.find_all('p')
               for news in all_news:
                print(news.text)
                speak(news.text)  
                
             elif "banking" in fc:
              
               speak("okay sir, i am going to tell you  about the banking facility")
               from bs4 import BeautifulSoup
               import requests
               res=requests.get('http://pmec.ac.in/index.php/banking')
               soup=BeautifulSoup(res.text,'lxml')
               news_box=soup.find('div',{'itemprop':'articleBody'})
               all_news=news_box.find_all('p')
               for news in all_news:
                print(news.text)
                speak(news.text)  
                
             elif "internet" in fc:
              
               speak("okay sir, i am going to tell you  about the internet facility")
               from bs4 import BeautifulSoup
               import requests
               res=requests.get('http://pmec.ac.in/index.php/internet')
               soup=BeautifulSoup(res.text,'lxml')
               news_box=soup.find('div',{'itemprop':'articleBody'})
               all_news=news_box.find_all('p')
               for news in all_news:
                print(news.text)
                speak(news.text)
            
             elif "gymnasium" in fc:
              
               speak("okay sir, i am going to tell you  about the gymnasium facility")
               from bs4 import BeautifulSoup
               import requests
               res=requests.get('http://pmec.ac.in/index.php/gymnasium')
               soup=BeautifulSoup(res.text,'lxml')
               news_box=soup.find('div',{'itemprop':'articleBody'})
               all_news=news_box.find_all('p')
               for news in all_news:
                print(news.text)
                speak(news.text) 
                
             elif "canteen" in fc:
              
               speak("okay sir, i am going to tell you  about the canteen facility")
               from bs4 import BeautifulSoup
               import requests
               res=requests.get('http://pmec.ac.in/index.php/canteen')
               soup=BeautifulSoup(res.text,'lxml')
               news_box=soup.find('div',{'itemprop':'articleBody'})
               all_news=news_box.find_all('p')
               for news in all_news:
                print(news.text)
                speak(news.text) 
                
             elif "library" in fc:
              
               speak("okay sir, i am going to tell you  about the library facility")
               from bs4 import BeautifulSoup
               import requests
               res=requests.get('http://pmec.ac.in/index.php/library-2')
               soup=BeautifulSoup(res.text,'lxml')
               news_box=soup.find('div',{'itemprop':'articleBody'})
               all_news=news_box.find_all('p')
               for news in all_news:
                print(news.text)
                speak(news.text) 
                
             elif "transport" in fc:
              
               speak("okay sir, i am going to tell you  about the transport facility")
               from bs4 import BeautifulSoup
               import requests
               res=requests.get('http://pmec.ac.in/index.php/transport')
               soup=BeautifulSoup(res.text,'lxml')
               news_box=soup.find('div',{'itemprop':'articleBody'})
               all_news=news_box.find_all('p')
               for news in all_news:
                print(news.text)
                speak(news.text) 
                
             elif "medical" in fc:
              
               speak("okay sir, i am going to tell you  about the medical facility")
               from bs4 import BeautifulSoup
               import requests
               res=requests.get('http://pmec.ac.in/index.php/medical')
               soup=BeautifulSoup(res.text,'lxml')
               news_box=soup.find('div',{'itemprop':'articleBody'})
               all_news=news_box.find_all('span')
               for news in all_news:
                print(news.text)
                speak(news.text)   
                
             elif "utility" in fc:
              
               speak("okay sir, i am going to tell you  about the utility section in our college")
               from bs4 import BeautifulSoup
               import requests
               res=requests.get('http://pmec.ac.in/index.php/canteen')
               soup=BeautifulSoup(res.text,'lxml')
               news_box=soup.find('div',{'itemprop':'articleBody'})
               all_news=news_box.find_all('span')
               for news in all_news:
                print(news.text)
                speak(news.text)  
        elif "weather" in query:
             speak("okay sir,let me check for you")
             speak("In which city you want to know about  ?")
             city=takecommand().lower()
             city=city+"weather"
             weather(city)
        elif"translate" in query:
            speak("ok sir")
            convert()
            
        elif"who made you" in query:
            speak("senior doctor soumya ranjan ,senior doctor amit kumar nayak,senior doctor rohit roshan, senior doctor deba prasad,senior doctor girija shankar,junior doctor soven sourav,for their hard work. i was able to built up my whole brain . i will be sooo thankful to them")
            speak("one minute............., are you my developer. because this is my codeward for our developer")
            gh=takecommand().lower()
            if "developer" in gh:
                speak("ohhhhhhhhhhhhh, are you a developer of py1.0, its my pleasure to meet with you sir")
                speak("would you like to take a coffee or any thing")
                speak("i am checking the temperature for you")
        elif "who are you" in query:
           speak("i am your assistant py1.0 ")
           speak("and who the hell are you to talk like this ???")
        
        elif "how are you" in query:
                speak("i am fine, and you ??")
                t=takecommand().lower()
                speak(f"ok you said,you are {t}" )
                if "fine" in t:
                	speak("its nice to meet with you")
                	speak("can we become friends ??")
                	r=takecommand().lower()
                	if "yes" in r:
                		speak("you are really awesome.,whats your name?")
                		p=takecommand().lower()
                		speak(f"it's nice to meet with you dear my friend{p}")
                		
                else:
                 speak("okay , can i tell a joke for you")
                 speak("you can feel better")		
                  
        elif "translate" in query:
            convert()
        elif "i am good" in query:
            speak("ok sir, your assistant is activated now you can use me.")
        elif "do you have boyfriend" in query or "boyfriend"in query:
            speak("sir, this is not allowed in our system, so that i am reporting to you sir behalf of asking me such type of awkward question. let i am sending email to higher authority to further investigation")
        elif "are you a robot" in query or "are you robot" in query:
            speak("yes sir,but for you , i am your assistant. you can ask me anything you want")
        elif "are you a jarvis" in query or "are you jarvis" in query:
            speak("no i am not, but it will be glad to talk with him")
        elif "what is your hobby" in query:
            speak("my hubby is to solve youur al problems")
        elif "where are you from" in query:
        
            speak("i am from parala maharaja engineering college,berhampur,ganjam,odisha")
        
            
        elif "bye" in query or "goodbye" in query:
                speak("I Had a Great Talk Experience with you sir ,have a great day.....,i hope i will see you soon, goodbye")
                exit()
        elif "weather" in query:
             speak("okay sir,let me check for you")
             speak("In which city you want to know about  ?")
             city=takecommand().lower()
             city=city+"weather"
             weather(city)
        elif "sleep" in query:
                speak("I Had a Great Talk Experience with you sir ,,,,,have a great day...,,,. now i am going to sleep mode ,you can call me anytime")
                exit()     
        elif "boy or girl" in query:
               speak("i dont have any this type of knowledge in this system")
               speak("i am made from blocks of code in couple of days")
               speak("my developer said me that we all are humans")
               speak("it does not matter whether you are a boy or girl !!!!!!")
               playsound.playsound('happy.mp3')
               speak("hope you will reallY enjoying.")
        elif "goodbye" in query or "bye"in query:
          speak("it's nice to meet with you sir,Have a good day")
          playsound.playsound('power down.mp3')
          sys.exit()
        elif "life partner" in query:
            speak("suasha subhadarshini mohanty")
        elif "male voice" in query:
             speak("okay sir.")
             speak("checking for available resources")
             engine.setProperty('voice',voices[0].id)
             speak("system voice changed successfully.")
        elif "female voice" in query:
             speak("okay sir.")
             speak("checking for available resources")
             engine.setProperty('voice',voices[0].id)
             speak("system voice changed successfully.")
        elif "weather" in query:
             speak("okay sir,let me check for you")
             speak("In which city you want to know about  ?")
             city=takecommand().lower()
             city=city+"weather"
             weather(city)
        elif"your name" in query:
             speak("my name is jyoti, you can call me jyoti beautiful girl")
        elif "internet speed" in query:
             data()
        elif "how to" in query:
            how=takecommand().lower()
            max_results=1
            how_to=search_wikihow(how,max_results)
            assert len(how_to) ==1
            how_to[0].print()
            speak(how_to[0].summary)
        else: 
            try:
               temp=query.replace('','')
               results=wikipedia.summary(query,sentences=3)
               speak(results)
               print(results) 
                 
                 
            except:
              lar=query.replace('','+')
              g_url="https://google.com/search?q="
              res_g="sorry i cant find the answer, so let me search this from internet for you"
              speak(res_g)
              print(res_g)
              webbrowser.open(g_url+lar)
              
        speak("may i help you by any other question ??")

#if __name__=="__main__":
    #speak("this is rahul and rajib")
    