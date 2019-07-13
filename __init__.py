import os
import re
import json
from cudax_nodejs import run_node
from cuda_fmt import get_config_filename
import cudatext as app

tool_js = os.path.join(os.path.dirname(__file__), 'csscomb.js')

def get_config():
    fn = get_config_filename('CSS Comb')
    s = open(fn, 'r').read()
    #del // comments
    s = re.sub(r'(^|[^:])//.*', r'\1', s)   
    d = json.loads(s)
    return json.dumps(d)

def do_format_ex(text, syntax):
    config = get_config()
    try:
        return run_node(text, [tool_js, syntax, config, '.'])
    except Exception as e:
        app.msg_box('Error while running Node.js \n'+str(e), app.MB_OK+app.MB_ICONERROR)

def do_format_css(text):
    return do_format_ex(text, 'css')

def do_format_scss(text):
    return do_format_ex(text, 'scss')

def do_format_sass(text):
    return do_format_ex(text, 'sass')

def do_format_less(text):
    return do_format_ex(text, 'less')
