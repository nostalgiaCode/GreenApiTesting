import requests

def errorHandler(response):
    if response.status_code == 400:
        return "Аккаунт находится в процессе запуска/перезапуска. Попробуйте повторить попытку спустя несколько секунд"
    if response.status_code == 403:
        return "Проблема с аутентификацией, проверьте корректность указания idInstance"
    if response.status_code == 401:
        return "Проблема с авторизацией, проверьте корректность указания apiTokenInstance"
    if response.status_code == 400:
        return "Аккаунт не авторизован. Для авторизации аккаунта перейдите в Личный кабинет и считайте QR-код из приложения WhatsApp Business на телефоне"
    if response.status_code == 429:
        return "Пользователь отправил слишком много запросов за заданный промежуток времени. Уменьшите частоту запросов. Рекомендации по частоте запросов"
    if response.status_code == 466:
        return "Исчерпан лимит"
    if response.status_code == 499:
        return "Пользователь закрыл соединение, пока сервер обрабатывал запрос. Требуется увеличить время ожидания ответа от сервера и повторить запрос с задержкой. Если ошибка повториться, то информировать оператора и дать возможность повторить отправку"
    if response.status_code == 500:
        return "Попытка отправки файла размером более 100 МБайт"
    if response.status_code == 502:
        return "Сервер не способен получить ответ от целевого сервера. Требуется 3 раза повторить запрос с задержкой. Если ошибка повторится, то информировать оператора и дать возможность повторить отправку"
    return response.text

def getSettings(apiUrl, idInstance, apiTokenInstance):
    url = f"{apiUrl}/waInstance{idInstance}/getSettings/{apiTokenInstance}"
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload)
    
    return errorHandler(response)

def getStateInstance(apiUrl, idInstance, apiTokenInstance):
    url = f"{apiUrl}/waInstance{idInstance}/getStateInstance/{apiTokenInstance}"
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload)

    return errorHandler(response)

def sendTextMessage(apiUrl, idInstance, apiTokenInstance, chatId, message):
    url = f"{apiUrl}/waInstance{idInstance}/sendMessage/{apiTokenInstance}"
    payload = f'{{\"chatId\": "{chatId}@c.us",\"message\": "{message}"}}'
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data = payload)

    return errorHandler(response)

def sendFileByURL(apiUrl, idInstance, apiTokenInstance, chatId, fileURL):
    url = f"{apiUrl}/waInstance{idInstance}/sendFileByUrl/{apiTokenInstance}"
    last_backslash_index = fileURL.rfind("/")
    fileName = fileURL[last_backslash_index + 1:]
    last_period_index = fileName.rfind(".")
    caption = fileName[:last_period_index]
    print(f"{fileURL}__{fileName}__{caption}")
    payload = f'{{\"chatId\": "{chatId}@c.us", "urlFile": "{fileURL}", "fileName": "{fileName}", "caption": "{caption}"}}'
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data = payload)

    return errorHandler(response)