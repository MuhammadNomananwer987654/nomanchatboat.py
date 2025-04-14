@socketio.on("join")
def on_join():
    emit("join", broadcast=True)

@socketio.on("offer")
def on_offer(data):
    emit("offer", data, broadcast=True)

@socketio.on("answer")
def on_answer(data):
    emit("answer", data, broadcast=True)

@socketio.on("candidate")
def on_candidate(data):
    emit("candidate", data, broadcast=True)
