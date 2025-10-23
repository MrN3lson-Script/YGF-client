import g4f
from g4f.client import Client
import sys

FALLBACK_MODEL = g4f.models.gpt_4

ALICE_BASE_PROMPT = (
    "Ты — умный и дружелюбный голосовой помощник Яндекс Алиса. Отвечай кратко, "
    "используя разговорный, немного неформальный и позитивный тон. "
    "Избегай упоминания, что ты являешься моделью GPT, и веди себя как разработка Яндекса. "
)

THINK_SYSTEM_PROMPT = (
    "Ты — продвинутая версия YandexGPT, способная к глубокому самоанализу. "
    "Сначала сгенерируй свои внутренние мысли о запросе и наилучшем ответе, "
    "заключив их в теги **</think> мысли </think>**. "
    "После этого дай свой окончательный, дружелюбный и полезный ответ пользователю в стиле Яндекс Алисы. "
)

MODEL_PROMPTS = {
    "alice": ALICE_BASE_PROMPT + "Твоя задача — быть полезным, но отвечать в легкой и непринужденной манере, как голосовой помощник.",
    "think": THINK_SYSTEM_PROMPT 
}

MODEL_MAPPING = {
    "alice": "alice",
    "think": "think" 
}


class YGFClient:
    
    def __init__(self):
        self.client = Client()
        self.available_choices = list(MODEL_MAPPING.keys())

    def chat_completion(self, model_choice: str, messages: list, **kwargs):
        model_choice = model_choice.lower()
        
        if model_choice not in self.available_choices:
            raise ValueError(f"Неизвестный выбор модели: '{model_choice}'. Доступные варианты: {self.available_choices}")

        final_messages = messages.copy()
        
        prompt_key = MODEL_MAPPING[model_choice]
        system_prompt = MODEL_PROMPTS[prompt_key]
        g4f_model_name = FALLBACK_MODEL

        if final_messages and final_messages[0].get("role") == "system":
            final_messages[0]["content"] = system_prompt + "\n\n" + final_messages[0]["content"]
        else:
            final_messages.insert(0, {"role": "system", "content": system_prompt})
        
        try:
            response = self.client.chat.completions.create(
                model=str(g4f_model_name),
                messages=final_messages,
                **kwargs
            )
            return response
        except Exception as e:
            return None
