import eventlet
import socketio

from application.handler_messages.handler_messages import HandlerMessages
from application.models.users import Users

sio = socketio.Server()

app = socketio.WSGIApp(sio)

handler = HandlerMessages()

socket_data = {'online': 0}


@sio.event
def connect(sid, environ):
    socket_data['online'] += 1
    sio.emit('message', data=socket_data)
    sio.emit("message", to=sid, data="Добро пожаловать на сервер!")

@sio.event
def disconnect(sid, environ):
    socket_data['online'] -= 1
    sio.emit('message', to=sid, data=socket_data)


@sio.on('register')
def register(sid: str, data: dict):
    new_user = Users(data, sid)
    if new_user.check_user:
        sio.emit("message", to=sid, data=f'Твое имя: {new_user.user_name}, your_id: {new_user.id}')


@sio.on("make_turn")
def make_turn(sid: str, data: dict):
    if handler.check_sid(sid):
        if handler.word is None:
            handler.set_params(sid, data)
            sio.emit("message", data=f"Игра началась первое слово: --> {handler.word} <--")
            sio.emit("message",
                     data=f"Отвечает пользователь с именем: {handler.answer_name}, тебе на букву {handler.word[-1]}")

        else:
            if handler.check(sid, data):
                sio.emit("message", data=f"Верно!")
                sio.emit("message",
                         data=f"Отвечает пользователь с  именем: {handler.answer_name}, тебе на букву {handler.word[-1]}")

            else:
                sio.emit("message",
                         data=f" Неверно!! Отвечает пользователь с именем: {handler.answer_name}, тебе на букву {handler.word[-1]}")


def run_server() -> None:
    """Run the server using eventlet.wsgi"""
    eventlet.wsgi.server(
        eventlet.listen(('', 5000)), app
    )

if __name__ == '__main__':

    run_server()






