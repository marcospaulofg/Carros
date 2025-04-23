import requests

def get_car_ai_bio(modelo, marca, ano):
    HUGGINGFACE_API_KEY = "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"
    API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"Show a sales description for the car {marca} {modelo} {ano} in just 250 characters describing technical specifications of this car model."

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 100,
            "temperature": 0.7
        }
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        print(f"[DEBUG] Status code: {response.status_code}")
        print(f"[DEBUG] Response body: {response.text}")

        response.raise_for_status()
        output = response.json()

        if isinstance(output, list) and "generated_text" in output[0]:
            return output[0]["generated_text"].strip()
        else:
            return "Descrição não disponível no momento."

    except Exception as e:
        print(f"Erro ao chamar API da Hugging Face: {e}")
        return "Descrição não disponível no momento."