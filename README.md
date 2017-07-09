## python-flask-docker-sklearn-template
# requirements  
docker installed

# docker:
docker build . -t <some tag name>    
detached : docker run -p 3000:5000 -d <some tag name>    
interactive (recommended for debug): docker run -p 3000:5000 -it <some tag name>    










python -m venv env   
env\Scripts\Activate   

windows:   
python -m pip install -r ./requirements_windows.txt   


linux:   
python -m pip install -r ./requirements.txt   

