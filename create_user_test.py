import data
import sender_stand_request
# КСЕНИЯ ЯКОВЕНКО 13-Я КОГОРТА ДИПЛОМНЫЙ ПРОЕКТ. ИНЖИНЕР ПО ТЕСТИРОВАНИЮ ПЛЮС

def get_user_body(first_name, lastName, address,metroStation, rentTime, deliveryDate):
    current_body = data.user_body.copy()
    current_body["firstName"]    = first_name
    current_body["lastName"]     = lastName
    current_body["address"]      = address
    current_body["metroStation"] = metroStation
    current_body["rentTime"]     = rentTime
    current_body["deliveryDate"] = deliveryDate
    return current_body
def positive_assert(first_name, lastName, address,metroStation, rentTime, deliveryDate):
    user_body = get_user_body(first_name, lastName, address, metroStation, rentTime, deliveryDate)
    user_response = sender_stand_request.post_new_order(user_body)
    assert user_response.status_code == 201 # здесь проверяем что заказ создан
    assert user_response.json()["track"] != "" # и у него есть трек
    orders_trakc_response=sender_stand_request.post_new_order(user_body) # записываем трек в переменную
    response=sender_stand_request.post_orders_track(user_response.json()["track"]) # подставляем полученный трек в функцию полученя заказа по треку post_order_treck и записываем ответ
    assert response.status_code == 200 # проверяем что статус ответа 200





def test_poluchenie_zakaza_po_trecu(): # тест выполняет проверку создавая заказ с моими данными и подставляя его трек в функцию получения заказа
    positive_assert("Ксения", "Яковенко", "Ленина д.1", 12, 15, "2020-06-06")
