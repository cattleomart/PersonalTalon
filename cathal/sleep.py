from talon import app, actions
# https://talon.wiki/Customization/Examples/turn_off_listening
def disable():
    actions.speech.disable()

app.register("ready", disable)