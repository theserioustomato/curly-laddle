#!/usr/bin/env python
# coding: utf-8

# In[13]:


from flask import Flask


# In[14]:


app = Flask(__name__)
#must be double underline


# In[15]:


from flask import request, render_template
import joblib

@app.route("/", methods=["GET", "POST"])
#must use methods with the s

def index():
    if request.method == "POST":
        rates = request.form.get("rate")
        print(rates)
        model = joblib.load("DBS")
        pred = model.predict([[float(rates)]])
        print(pred)
        s ="The predicted DBS share price is" + str(pred[0][0])
        return(render_template("index.html", result = s))
    else:
        return(render_template("index.html", result="2"))


# In[ ]:


if __name__=="__main__":
    app.run()
