# import pyaudio
# p = pyaudio.PyAudio()
# for i in range(p.get_device_count()):
#     info = p.get_device_info_by_index(i)
#     print(info['index'], info['name'])

# import speech_recognition as sr

# def takeCommand():
#     r=sr.Recognizer()
#     with sr.Microphone(device_index=1) as source:
#         print("Listening...")
#       #  r.energy_threshold=300
#       #  r.pause_threshold = 0.8
#         # r.adjust_for_ambient_noise(source)
#         audio=r.listen(source)

#     try:
#         print("Recognizing...")    
#         query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
#         print(f"User said: {query}\n")  #User query will be printed.

#     except Exception as e:
#         # print(e)    
#         print("Say that again please...")   #Say that again will be printed in case of improper voice 
#         return "None" #None string will be returned
#     return query

# print(takeCommand())

"""
//Real-time speech recognition test
"""
import speech_recognition as sr
# import logging
# logging.basicConfig(level=logging.DEBUG)

# while True:
#     r = sr.Recognizer()
#     # Microphone
#     mic = sr.Microphone()

#     logging.info('In the recording...')
#     with mic as source:
#         r.adjust_for_ambient_noise(source)
#         audio = r.listen(source)
#     logging.info('End of recording, in recognition...')
#     test = r.recognize_google(audio, language='cmn-Hans-CN', show_all=True)
#     print(test)
#     logging.info('end')
r = sr.Recognizer()
with sr.Microphone(device_index = 1, sample_rate = 48000) as source:
    print('listening')
    audio = r.record(source, duration = 5)
with open("microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())