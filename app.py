from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello DevOps with Flask! Started by user Ranjana singh

Running as SYSTEM
Building in workspace /var/lib/jenkins/workspace/flaskapp
The recommended git tool is: NONE
No credentials specified
 > git rev-parse --resolve-git-dir /var/lib/jenkins/workspace/flaskapp/.git # timeout=10
Fetching changes from the remote Git repository
 > git config remote.origin.url https://github.com/Ranjana1984/flaskapp.git # timeout=10
Fetching upstream changes from https://github.com/Ranjana1984/flaskapp.git
 > git --version # timeout=10
 > git --version # 'git version 2.43.0'
 > git fetch --tags --force --progress -- https://github.com/Ranjana1984/flaskapp.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git rev-parse refs/remotes/origin/main^{commit} # timeout=10
Checking out Revision b24d1f90d68cce99f00c2638f77fde745fe768f6 (refs/remotes/origin/main)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f b24d1f90d68cce99f00c2638f77fde745fe768f6 # timeout=10
Commit message: "Add files via upload"
 > git rev-list --no-walk b24d1f90d68cce99f00c2638f77fde745fe768f6 # timeout=10
[flaskapp] $ /bin/sh -xe /tmp/jenkins6962172057216863824.sh
+ python3 -m venv venv
+ . venv/bin/activate
+ deactivate nondestructive
+ [ -n  ]
+ [ -n  ]
+ hash -r
+ [ -n  ]
+ unset VIRTUAL_ENV
+ unset VIRTUAL_ENV_PROMPT
+ [ ! nondestructive = nondestructive ]
+ [  = cygwin ]
+ [  = msys ]
+ export VIRTUAL_ENV=/var/lib/jenkins/workspace/flaskapp/venv
+ _OLD_VIRTUAL_PATH=/usr/lib/jvm/java-11-openjdk-amd64/bin:/usr/lib/jvm/java-11-openjdk-amd64/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/snap/bin
+ PATH=/var/lib/jenkins/workspace/flaskapp/venv/bin:/usr/lib/jvm/java-11-openjdk-amd64/bin:/usr/lib/jvm/java-11-openjdk-amd64/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/snap/bin
+ export PATH
+ [ -n  ]
+ [ -z  ]
+ _OLD_VIRTUAL_PS1=$ 
+ PS1=(venv) $ 
+ export PS1
+ VIRTUAL_ENV_PROMPT=(venv) 
+ export VIRTUAL_ENV_PROMPT
+ hash -r
+ pip install --upgrade pip
Requirement already satisfied: pip in ./venv/lib/python3.12/site-packages (24.0)
Collecting pip
  WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'ReadTimeoutError("HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Read timed out. (read timeout=15)")': /packages/de/f0/c81e05b613866b76d2d1066490adf1a3dbc4ee9d9c839961c3fc8a6997af/pip-26.0.1-py3-none-any.whl.metadata
  Downloading pip-26.0.1-py3-none-any.whl.metadata (4.7 kB)
Downloading pip-26.0.1-py3-none-any.whl (1.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 384.7 kB/s eta 0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 24.0
    Uninstalling pip-24.0:
      Successfully uninstalled pip-24.0
Successfully installed pip-26.0.1
+ pip install -r requirements.txt
Collecting flask==2.2.5 (from -r requirements.txt (line 1))
  Downloading Flask-2.2.5-py3-none-any.whl.metadata (3.9 kB)
Collecting Werkzeug>=2.2.2 (from flask==2.2.5->-r requirements.txt (line 1))
  Downloading werkzeug-3.1.5-py3-none-any.whl.metadata (4.0 kB)
Collecting Jinja2>=3.0 (from flask==2.2.5->-r requirements.txt (line 1))
  Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting itsdangerous>=2.0 (from flask==2.2.5->-r requirements.txt (line 1))
  Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting click>=8.0 (from flask==2.2.5->-r requirements.txt (line 1))
  Downloading click-8.3.1-py3-none-any.whl.metadata (2.6 kB)
Collecting MarkupSafe>=2.0 (from Jinja2>=3.0->flask==2.2.5->-r requirements.txt (line 1))
  Downloading markupsafe-3.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.7 kB)
Downloading Flask-2.2.5-py3-none-any.whl (101 kB)
Downloading click-8.3.1-py3-none-any.whl (108 kB)
Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
Downloading markupsafe-3.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)
Downloading werkzeug-3.1.5-py3-none-any.whl (225 kB)
Installing collected packages: MarkupSafe, itsdangerous, click, Werkzeug, Jinja2, flask

Successfully installed Jinja2-3.1.6 MarkupSafe-3.0.3 Werkzeug-3.1.5 click-8.3.1 flask-2.2.5 itsdangerous-2.2.0
+ python app.py
 * Serving Flask app 'app'
 * Debug mode: off
[31m[1mWARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.[0m
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.23.130.168:5000
[33mPress CTRL+C to quit[0m
127.0.0.1 - - [05/Feb/2026 16:15:27] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [05/Feb/2026 16:15:27] "[33mGET /favicon.ico HTTP/1.1[0m" 404 -
172.23.128.1 - - [05/Feb/2026 16:15:49] code 400, message Bad request version ('\x17m»¹Nh\x9e·É.ÈÅ')
172.23.128.1 - - [05/Feb/2026 16:15:49] "[31m[1m\x16\x03\x01\x06à\x01\x00\x06Ü\x03\x03Aµ\x0bZì\x1b\x88Z\\t~ð F\x0c¤\x07\x83/¨\x9a°Çk\x04\x80\x12"\x0d\x1fU§ x\x19­2P»Pë\x14\x96>DÂ^Å\x18\x8bb\x8e·\x9aw1\x19ù\x16îÑÀìçÒ\x00 JJ\x13\x01\x13\x02\x13\x03À+À/À,À0Ì©Ì¨À\x13À\x14\x00\x9c\x00\x9d\x00/\x005\x01\x00\x06sZZ\x00\x00ÿ\x01\x00\x01\x00þ\x0d\x00ú\x00\x00\x01\x00\x01£\x00 \x17m»¹Nh\x9e·É.ÈÅ[0m" 400 -
172.23.128.1 - - [05/Feb/2026 16:15:49] code 400, message Bad request version ('\xad\x02s§mô¢)\x861,§F>°aq\x15^ã\x89MáëÊz@»1\x97')
172.23.128.1 - - [05/Feb/2026 16:15:49] "[31m[1m\x16\x03\x01\x06à\x01\x00\x06Ü\x03\x03DÎc1\x11¿--\x8325v\x17P\x05Ýä*ôjÐÇ~ p½²7*22\x9a L\x02§¥\x8c?\x8a$d\x12\x95)ãÐÔ\x8aÑ\x1e_Ô ø\x12'$;l\x90íRÇ<\x00 jj\x13\x01\x13\x02\x13\x03À+À/À,À0Ì©Ì¨À\x13À\x14\x00\x9c\x00\x9d\x00/\x005\x01\x00\x06súú\x00\x00\x00\x1b\x00\x03\x02\x00\x02DÍ\x00\x05\x00\x03\x02h2\x00-\x00\x02\x01\x01\x003\x04ï\x04í\x8a\x8a\x00\x01\x00\x11ì\x04À~\x0c­\x02s§mô¢)\x861,§F>°aq\x15^ã\x89MáëÊz@»1\x97[0m" 400 -
172.23.128.1 - - [05/Feb/2026 16:16:01] "GET / HTTP/1.1" 200 -
172.23.128.1 - - [05/Feb/2026 16:16:01] "[33mGET /favicon.ico HTTP/1.1[0m" 404 -
"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
