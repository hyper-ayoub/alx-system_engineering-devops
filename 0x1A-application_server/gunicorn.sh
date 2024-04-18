# Solving gunicorn service failed 

# checking 
python3 --version
pip3 list | grep flask
pip3 list | grep click

# install  &&  check 
pip3 install --upgrade flask click
gunicorn --version

# restart service
sudo systemctl restart gunicorn

# status check
sudo systemctl status gunicorn
