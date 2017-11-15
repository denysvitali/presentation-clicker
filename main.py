from klein import run, route
from subprocess import call

@route('/')
def home(request):
    return open("./index.html", 'r').read()

@route('/next')
def next(req):
    call(["zsh", '-c' , 'xdotool key --window "$(xdotool search "Slides" | head -n1)" Right'])
    return "ok"


@route('/prev')
def prev(req):
    print("Got prev")
    call(["zsh", '-c' , 'xdotool key --window "$(xdotool search "Slides" | head -n1)" Left'])
    return "ok"


run("0.0.0.0", 8080)