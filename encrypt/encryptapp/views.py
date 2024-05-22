from django.shortcuts import render,redirect
from encryptapp.models import FAQ
from encryptapp.models import police_station
from encryptapp.models import Laws
from encryptapp.models import Terms
from encryptapp.models import cybersecurity_laws
from encryptapp.models import userregister
from encryptapp.models import contact_us
from encryptapp.models import review
from encryptapp.models import help_support
from django.conf import settings
from django.core.mail import send_mail
from gtts import gTTS
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import speech_recognition as sr
import pyttsx3 
from textblob import TextBlob
from langdetect import detect
import langid
from googletrans import Translator
from django.db.models import Q
import spacy
import spacy.cli
from transformers import pipeline
import pandas as pd
import datetime
from datetime import date
from newsapi.newsapi_client import NewsApiClient


# Create your views here.
def footer (request):
	return render(request,'footer.html')

def homepage (request):
	return render(request,'homepage.html')	

def contactus(request):
	if request.method=="POST":
		x=contact_us()
		x.name=request.POST.get('nm')
		x.email=request.POST.get('em')
		x.company_name=request.POST.get('cnm')
		x.message=request.POST.get('msg')
		x.save()
		return render(request,'contactus.html',{'ms':1})
	else:
		return render(request,'contactus.html')

def header(request):
	return render(request,'header.html')

import random


def registerform(request):
	if request.method=="POST":
		name=request.POST.get('fn')
		email=request.POST.get('em')
		password=request.POST.get('ps')	
		confirm_password=request.POST.get('cps')
		if userregister.objects.filter(email=email).exists():
			return render(request,'registerform.html',)
		else:
			if password==confirm_password:
				f1=random.randrange(100000,999999)
				subject="OTP"
				message="welcome to cyber security Your OTP  is " +str(f1)
				email_from=settings.EMAIL_HOST_USER
				recipient_list=[email,]
				send_mail(subject,message,email_from,recipient_list)
				rest="Your OTP is sent to your respective email account. Please check"
				return render(request,'registerform1.html',{'otp':f1,'name':name,'email':email,'password':password,'rest':rest})


				'''x=userregister()
				x.name=request.POST.get('fn')
				x.email=request.POST.get('em')
				x.password=request.POST.get('ps')
				f1=random.randrange(100000,999999)'''



				#x.save()

				# return render(request,'registerform.html',{'ms':2})
			else:
				return render(request,'registerform.html',{'ms':3})
	else:
		return render(request,'registerform.html')

def registerform1(request):
	if request.method=="POST":
		otp_fill=request.POST.get('fill')
		otp_org=request.POST.get('org')
		if otp_fill==otp_org:

			x=userregister()
			x.name=request.POST.get('fn')
			x.email=request.POST.get('em')
			x.password=request.POST.get('ps')
			x.save()
			return render(request,'registerform.html',{'ms':1})
		else:
			return render(request,'registerform.html')




def login(request):
	if request.method=="POST":
		email=request.POST.get('em')
		password=request.POST.get('ps')
		x=userregister.objects.filter(email=email,password=password)
		k=len(x)
		if k>0:
			request.session['email']=email
			return redirect('/userprofile')
		else:
			return render(request,'login.html',{'msg':"Invalid Candidate"})	
	else:
		return render(request,'login.html')	


def logout(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	del request.session['email']
	return redirect('/logout')	

def base(request):
	return render(request,'base.html')	

def allfaq(request):
	if request.method=="POST":
		s_query=request.POST.get('se')
		res=FAQ.objects.filter(Q(question__icontains=s_query)|Q(answer__icontains=s_query))
		return render(request,'searchfaq.html',{'data':res})
	else:	
		res=FAQ.objects.all()
		return render(request,'allfaq.html',{'data':res})

def alllaws(request):
	res=Laws.objects.all()
	return render(request,'alllaws.html',{'data':res})	

def allterms(request):
	if request.method=="POST":
		s_query=request.POST.get('se')
		res=Terms.objects.filter(Q(title__icontains=s_query)|Q(description__icontains=s_query))
		return render(request,'searchterms.html',{'data':res})
	else:
		res=Terms.objects.all()
		return render(request,'allterms.html',{'data':res})	

def allpolicestation(request):
	res=police_station.objects.all()
	return render(request,'allpolicestation.html',{'data':res})		

def allcybersecuritylaws(request):
	if request.method=="POST":
		s_query=request.POST.get('se')
		res=cybersecurity_laws.objects.filter(Q(name__icontains=s_query)|Q(description__icontains=s_query))
		return render(request,'searchcyberlaws.html',{'data':res})
	else:	
		res=cybersecurity_laws.objects.all()
		return render(request,'allcybersecuritylaws.html',{'data':res})	


def sidear1 (request):
	if not request.session.has_key('email'):
		return redirect('/login')
	return render(request,'sidear1.html')	

def changepass (request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		o=request.POST.get("op")
		n=request.POST.get("np")
		c=request.POST.get("cp")
		if n==c:
			user=userregister.objects.get(email=request.session['email'])
			p=user.password
			if p==o :
				user.password=n
				user.save()
				msg="password succesfully changed"
				return render(request,'changepass.html',{'msg':msg})
			else:
				msg="invalid current password"
				return render(request,'changepass.html',{'msg':msg})
		else:
			msg="passwordand confirm password is not same"
			return render(request,'changepass.html',{'msg':msg})
	else:
		return render(request,'changepass.html')

def myreview (request):
	if not request.session.has_key('email'):
		return redirect('/login')
	# res=review.objects.all()
	if request.method=="POST":
		x=review()
		x.username=request.POST.get('un')
		x.title=request.POST.get('tl')
		x.message=request.POST.get('msg')
		x.save()
		return render(request,'review.html',{'ms':1})
	else:
		return render(request,'review.html')	


def help_support1(request):
	if not request.session.has_key('email'):
		return redirect('/login')

	if request.method=="POST":
		x=help_support()
		x.username=request.POST.get('un')
		x.title=request.POST.get('tl')
		x.message=request.POST.get('msg')
		x.save()
		return render(request,'help_support.html',{'ms':1})
	else:		
		return render(request,'help_support.html')		

	


def userprofile(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	user=userregister.objects.get(email=request.session['email'])
	if request.method=="POST":
		print("yes")
		user.image=request.FILES['file1']
		user.save()
		return render(request,'userprofile.html',{'user':user, 'msg':'success'})

	else:	
		return render(request,'userprofile.html',{'user':user})		


def editprofile (request):
	if not request.session.has_key('email'):
		return redirect('/login')

	user=userregister.objects.get(email=request.session['email'])
	if request.method=="POST":
		user.name=request.POST.get('name')
		user.first=request.POST.get('first')
		user.last=request.POST.get('last')
		user.contactno=request.POST.get('contactno')
		user.dob=request.POST.get('dob')
		user.email=request.POST.get('email')
		user.address=request.POST.get('address')
		user.address2=request.POST.get('address2')
		user.gender=request.POST.get('gender')
		user.city=request.POST.get('city')
		user.state=request.POST.get('state')
		user.pin=request.POST.get('pin')
		user.save()
		return redirect('/userprofile')
	else:
		return render(request,'editprofile.html',{'user':user})	


def forgotpass (request):
	if request.method=='POST':	
		em=request.POST.get('em')
		user=userregister.objects.filter(email=em)
		if(len(user)>0):
			pw=user[0].password
			subject="password"
			message="welcome to cyber security Your password is " +pw
			email_from=settings.EMAIL_HOST_USER
			recipient_list=[em,]
			send_mail(subject,message,email_from,recipient_list)
			rest="Your password is sent to your respective email account. Please check"
			return render(request,'forgotpass.html',{'rest':rest})
		else:
			rest="this email is not registered"
			return render(request,'forgotpass.html',{'rest':rest})
	else:
		return render(request,'forgotpass.html')	


def TTS (request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=='POST':
		data=request.POST.get('di')
		language='en'
		x=gTTS(text=data, lang=language, slow=False)
		x.save("static/output.mp3")
		return render(request,'ttsoutput.html',{'data':data})
	else:	
		return render(request,'TTS.html')		

def STT (request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=='POST':
		MyText=""
		r = sr.Recognizer() 

		def SpeakText(command):
			
			# Initialize the engine
			engine = pyttsx3.init()
			engine.say(command) 
			engine.runAndWait()

		while(1): 
			
			try:
				
				# use the microphone as source for input.
				with sr.Microphone() as source2:
					
					r.adjust_for_ambient_noise(source2, duration=0.2)
					
					#listens for the user's input 
					audio2 = r.listen(source2)
					
					# Using google to recognize audio
					MyText = r.recognize_google(audio2)
					MyText = MyText.lower()

					#print("Did you say ",MyText)
					#SpeakText(MyText)
					
			except sr.RequestError as e:
				print("Could not request results; {0}".format(e))
				
			except sr.UnknownValueError:
				print("unknown error occurred")	
			return render(request,'STToutput.html', {'MyText': MyText})
	else:
		return render(request,'STT.html')		

def WC(request):
	if request.method=='POST':
		data=request.POST.get('di')
		wordcloud = WordCloud().generate("ok this")


		plt.imshow(wordcloud, interpolation='bilinear')

		wordcloud = WordCloud(max_font_size=40).generate(data)
		wordcloud = WordCloud(background_color='white').generate(data)
		plt.figure()
		plt.imshow(wordcloud, interpolation="bilinear", )
		plt.axis("off")
		plt.savefig('static/wordcloud.png')
		return render (request,'wcresult.html',{'data':data})
	else:
		return render(request,'WC.html')	


def sentiment(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=='POST':
		data=request.POST.get('di')
		testimonial = TextBlob(data)
		testimonial.sentiment
		p=testimonial.sentiment.polarity
		msg=""
		if p==0:
		    print("comment is neutral")
		    msg="neutral"
		elif p<0:
		    print("comment is Negative")
		    msg="Negative"
		else:
		    print("comment is positive")
		    msg="positive"
		return render(request,'sentimentresult.html',{'msg':msg,'p':p})

	else:
		return render(request,'sentiment.html')


def langdetector (request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=='POST':
		data=request.POST.get('di')

		language_code,_=langid.classify(data)

		
		language_names={
			'en': 'english',
			'pa': 'punjabi',
			'hi': 'hindi',
			'es': 'Spanish',
			'fr': 'French',
			'de': 'German',
			'it': 'Italian',
			'pt': 'Portuguese',
			'nl':'Dutch',
			'ru': 'Russian',
			'zh':'Chinese',
			'ja': 'Japanese',
			'ar': 'Arabic',
			'bn': 'Bengali',
			'ur': 'Urdu',
			'ko': 'Korean',
			'tr': 'Turkish',
			'th': 'Thai',
			'vi': 'Vietnamese',
			'id' :'Indonesian',
			'el': 'Greek',
			}
		name=language_names.get(language_code,'Unknown')
		return render(request,'langdetectorresult.html',{'language_code':language_code,'name':name})
	else:
		return render(request,'langdetector.html')


def langconverter(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=='POST':
		data=request.POST.get('di')
		to=request.POST.get('conv')
		
		translator= Translator()
		translation=translator.translate(data,dest=to)
		res=translation.text
		return render(request,'langconverterresult.html',{'res':res})
	else:
		return render(request,'langconverter.html')


def linguistic(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=='POST':
		data=request.POST.get('di')
		nlp=spacy.load("en_core_web_sm")
		    
		doc=nlp(data)
		    
		print("Part-of-speech tagging.")
		for token in doc:
			print(f"{token.text}:{token.pos_}")
		        
		print("\n Named Entity Recognition.")
		for ent in doc.ents:
			print(f"{ent.text}:{ent.label_}")
		            
		print("\n Dependency parsing:")
		for token in doc:
			print(f"{token.text}:{token.dep_}-->{token.head.text}") 
		        
		#advanced_linguistic_analysis(text)
		return render(request, 'linguisticresult.html',{'doc':doc,'data':data})
	else:
		return render(request, 'linguistic.html')


def abusive (request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=='POST':
		data=request.POST.get('di')
		print("================",data)
		classifier=pipeline('text-classification',model='distilbert-base-uncased-finetuned-sst-2-english',device=0)
		print("yes")
		result=classifier(data)[0]
		if result['label']=='NEGATIVE':
			print("True")
			#return True
		else:
			print("False")
			#return False
		
		return render(request,'abusiveresult.html',{'data':data,'result':result})   
	else:
		return render(request,'abusive.html')




def news (request):
	newsapi= NewsApiClient (api_key='557b10c15bed498d8d9918904020b0d3')
	json_data = newsapi.get_everything(q='cybersecurity',
		language='en',from_param=str(date.today()-datetime.timedelta(days=29)),
		to=str(date.today()),page_size=18,page=1,sort_by='relevancy')
	k=json_data['articles']
	return render(request,'news.html',{'k':k})


def aboutus (request):
	return render(request,'aboutus.html')		