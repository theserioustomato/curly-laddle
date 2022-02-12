#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, render_template
import joblib


# In[2]:


app = Flask(__name__)


# In[3]:



#decorator: function to call
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rate = request.form.get("rate")
        print(rate)
        model = joblib.load("DBS")
        pred = model.predict([[float(rate)]])
        print(pred)
        s = "Predicted DBS share price:" + string(pred)
        print(s)
        return(render_template("index.html", result=":)"))
    else:
        return(render_template("index.html", result="Enter a number"))
    


# In[ ]:


if __name__ == "__main__":
    app.run()
    #app.run(host"0.0.0.0", port=int("80"))


# In[ ]:




