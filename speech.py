import speech_recognition as sr
import requests
from requests.auth import HTTPBasicAuth
import time

def audio(local_filename):

    ext = local_filename.rpartition('.')[-1]
    print('Hay que convertir: {}'.format(ext))
    if ext != 'wav':
        ##lo convertimos con zamzar
        api_key = '5f8ecc160e4fe261ffe611981539749d089dba73'
        endpoint = "https://sandbox.zamzar.com/v1/jobs"
        source_file = (local_filename)
        target_format = "wav"

        file_content = {'source_file': open(source_file, 'rb')}
        data_content = {'target_format': target_format}
        res = requests.post(endpoint, data=data_content, files=file_content, auth=HTTPBasicAuth(api_key, ''))
        results=res.json()
        job_id=results['id']
        print(job_id)
        time.sleep(20) #espero para que lo convierta
        endpoint = "https://sandbox.zamzar.com/v1/jobs/{}".format(job_id)
        response = requests.get(endpoint, auth=HTTPBasicAuth(api_key, ''))
        results2=response.json()
        print(results2)

        file_id=results2['target_files'][0].get('id')
        name_target=results2['target_files'][0].get('name')

        local_filename = 'audios/{}'.format(name_target) #donde guardar
        endpoint = "https://sandbox.zamzar.com/v1/files/{}/content".format(file_id)

        response = requests.get(endpoint, stream=True, auth=HTTPBasicAuth(api_key, ''))
        try:
            with open(local_filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                print ("File downloaded")

        except IOError:
            print ("Error")
        r = sr.Recognizer()
        with sr.AudioFile(local_filename) as source:
            r.adjust_for_ambient_noise(source)
            audio = r.record(source,  duration=30)  # read the entire audio file

            try:
                # for testing purposes, we're just using the default API key
                # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`

                # instead of `r.recognize_google(audio)`
                print("El audio dice: " + r.recognize_google(audio, language= 'es-AR', show_all=False))
                print("The audio says, in English: -  " + r.recognize_google(audio, language = "en-US"))
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

    else:
# use the audio file as the audio source
        r = sr.Recognizer()
        with sr.AudioFile(local_filename) as source:
            r.adjust_for_ambient_noise(source)
            audio = r.record(source,  duration=30)  # read the entire audio file

            try:
                # for testing purposes, we're just using the default API key
                # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`

                # instead of `r.recognize_google(audio)`
                print("El audio dice: " + r.recognize_google(audio, language= 'es-AR', show_all=False))
                print("The audio says, in English: -  " + r.recognize_google(audio, language = "en-US"))
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == '__main__':

    print('Enter the audio file path')

    local_filename = input()

    audio(local_filename) #'maximum_file_size': 1048576 para convertir con zamzar
