from flask import Flask

from server import utilthiernoIbrahimaIIdiallo

app=Flask (__name__)


@app.route ('/image_classify', methods={'GET','POST'})
def image_classify():

   return "hello"
if __name__=="__main__":
    app.run (port=5000)
    utilthiernoIbrahimaIIdiallo.load_saved_modelsaving ()
    app.run (port=5000,debug=True)

