from flask import Flask,redirect,url_for,render_template,request
import qrcode
import urllib.request, urllib.parse
import geocoder


app=Flask(__name__)

def sendtelegram(params):
    # 5467638311:AAGjx6lVUgSe2ihu9j7oHGjzNipW0hoEU_A
    url = "https://api.telegram.org/bot5738222395:AAEM5NwDAN1Zc052xI_i9-YlrVnvmSkN9p4/sendMessage?chat_id=-633441737&text=" + urllib.parse.quote(params)
    print("THere is nothing here.")
    content = urllib.request.urlopen(url).read()
    print(content)
    return content
    
@app.route('/home',methods=['GET','POST'])
def home():
    if request.method=='POST':
        indexNumber = request.form.get("indexNumber")
        Name = request.form.get("Name")
        Time = request.form.get("Time")
        
        img = qrcode.make( "Student Attendance" + '\n' + 
                    "Student ID = " + indexNumber  + '\n'
                    "Student Name = " + Name + '\n' + 
                    "Student Time = " + Time )
        img = qrcode.make(Name)
        img = qrcode.make(Time)
        type(img)  #qrcode.image.pil.PilImage
        img.save("static/img/qrcode.png")
        sendtelegram( 
                      "Student ID = " + indexNumber  + '\n' 
                      "Student Name = " + Name + '\n' + 
                      "Student Time = " + Time 
           )
       
        
        
        return redirect(url_for('scan'))
    return render_template('index.html')

@app.route('/',methods=['GET','POST'])
def test():
    if request.method=='POST':
        return render_template('test.html')
    return render_template('test.html')

@app.route('/sreen',methods=['GET','POST'])
def sreen():
    if request.method=='POST':
        return render_template('sreen.html')
    return render_template('sreen.html')


@app.route('/scan',methods=['GET','POST'])
def scan():
    if request.method=='POST':
        return render_template('scan.html')
    return render_template('scan.html')

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