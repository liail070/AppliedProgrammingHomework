def sensor(signal: float) -> str:
    if signal == 0:
        return f"Датчик отключен"
    elif signal < 3.9 or signal > 20.1:
        return f"Датчик неисправен"

    pv_min = 0.0
    pv_max = 75.0
    pv = (signal - 4.0) * (pv_max - pv_min) / (20.0 - 4.0) + pv_min

    if 37.5 <= pv <= 39.0:
        cow_status = "с коровой все ок"
    elif 35.0 < pv <= 37.4:
        cow_status = "корова замерзла, требуется обогрев"
    elif 39.1 <= pv <= 39.5:
        cow_status = "корова перегрелась, требуется охлаждение"
    elif pv <= 34.9:
        cow_status = "требуется внимание"
    elif pv >= 39.6:
        cow_status = "срочно вызывайте ветеринара, коровка заболела"
    else:
        cow_status = "требуется внимание"

    return f"Получен сигнал датчика {signal:.2f} мА, датчик исправен, температура {pv:.1f} градусов, {cow_status}."

print(sensor(12))