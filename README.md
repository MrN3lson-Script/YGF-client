# 🚀 YGF Client (Yandex GPT Free)

**YGF Client** — это Python-обертка для имитации моделей Yandex GPT / Алиса с использованием бесплатных конечных точек AI, агрегированных библиотекой `g4f`.

**Внимание:** Этот клиент использует **GPT-4** (через провайдеров `g4f`) в качестве основной "имитирующей" модели (fallback). Поведение имитируется с помощью специализированных системных промтов.

---

## ✨ Возможности

* **Имитация Яндекс Алисы (`alice`):** Использует дружелюбный, разговорный, неформальный тон.
* **Режим YandexThink (`think`):** Активирует внутренние рассуждения в тегах `</think> мысли </think>` перед ответом.
* **Использование g4f:** Получение доступа к мощным моделям (GPT-4) без необходимости в API-ключах.

---

## 💻 Установка

1.  Установите необходимые зависимости:
    ```bash
    pip install g4f setuptools wheel
    ```
2.  Перейдите в корневой каталог проекта (`YGF/`).
3.  Установите пакет локально:
    ```bash
    pip install .
    ```

---

## 📝 Использование

Импортируйте `YGFClient` и используйте метод `chat_completion`.

### Пример 1: Обычная Яндекс Алиса

```python
from ygf.client import YGFClient

client = YGFClient()

messages = [
    {"role": "user", "content": "Расскажи, пожалуйста, а что сейчас происходит с погодой?"}
]

response = client.chat_completion(
    model_choice="alice",
    messages=messages
)

if response and response.choices:
    print(response.choices[0].message.content)

