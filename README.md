## python-flask-docker-sklearn-template
A simple example of python api for real time machine learning.
On init, a simple linear regression model is created and saved on machine. On request arrival for prediction, the simple model is loaded and returning prediction.    
For more information read [this post](https://blog.solutotlv.com/deployed-scikit-learn-model-flask-docker/?utm_source=Github&utm_medium=python-flask-sklearn-docker-template)


# requirements  
docker installed


# Run on docker  
docker build . -t {some tag name}   
detached : docker run -p 3000:5000 -d {some tag name}  
interactive (recommended for debug): docker run -p 3000:5000 -it {some tag name}  


# Run on local computer
python -m venv env  
env\Scripts\Activate  
python -m pip install -r ./requirements.txt  
python app.py  


# Use sample api  
127.0.0.1:3000/isAlive  
127.0.0.1:3000/prediction/api/v1.0/some_prediction?f1=4&f2=4&f3=4  
