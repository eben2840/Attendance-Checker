from flask import Flask,redirect,url_for,render_template,request
import qrcode
import urllib.request, urllib.parse
import geocoder


app=Flask(__name__)

def sendtelegram(params):
    # 5467638311:AAGjx6lVUgSe2ihu9j7oHGjzNipW0hoEU_A
    url = "https://api.telegram.org/bot5467638311:AAGjx6lVUgSe2ihu9j7oHGjzNipW0hoEU_A/sendMessage?chat_id=-635192651&text=" + urllib.parse.quote(params)
    print("THere is nothing here.")
    content = urllib.request.urlopen(url).read()
    print(content)
    return content
    
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        indexNumber = request.form.get("indexNumber")
        img = qrcode.make(indexNumber)
        type(img)  # qrcode.image.pil.PilImage
        img.save("static/img/qrcode.png")
        sendtelegram(indexNumber)
        return render_template('index.html')
    return render_template('index.html')


@app.route('/upload')
def upload():
    # upload location and id card image
    # 
    g = geocoder.ip('me')
    print(g.latlng)
    
    return redirect('http://maps.google.com/maps?z=12&t=m&q=loc:38.9419+'+lon)
    return "Testing location api"

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)