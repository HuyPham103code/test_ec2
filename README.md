# test_ec2

###  các bước

-  git --version
-  git clone "...."
-  sudo apt install python3-pip -y
-  sudo apt update
-  sudo apt install python3.12-venv
-  python3.12 -m venv venv
-  source venv/bin/activate
-  pip install django
-  pip install djangorestframework django-cors-headers joblib
-  pip install scikit-learn
-  python3 manage.py  runserver 0.0.0.0:8000


  ###  Nếu trong quá trình code mà có thay đổi thì trong git thì bên git cứ push bình thường, còn ec2 thì cd vào thư mục chứa code của git gõ lệnh
  - git pull origin main
