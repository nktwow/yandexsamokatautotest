# Панин Никита, 12-я когорта — Финальный проект. Инженер по тестированию плюс
import create_order


def get_track():
    res = create_order.post_new_order()
    if res.ok:
        return res.json()['track']
    else:
        return ''


def test1_check_response_status():
    track = get_track()
    res = create_order.get_view_order(track)
    assert res.status_code == 200
