import requests

BASE_URL = "http://127.0.0.1:8000"


def test_health():

    response = requests.get(
        f"{BASE_URL}/health/"
    )

    print("Health")
    print(response.status_code)
    print(response.json())


def test_chat():

    response = requests.post(
        f"{BASE_URL}/chat/",
        json={
            "question": "Is there a termination clause?",
            "prompt_type": "risk_analysis",
            "top_k": 5
        }
    )

    print("\nChat")
    print(response.status_code)
    print(response.json())


def test_analyze():

    response = requests.post(
        f"{BASE_URL}/analyze/",
        json={
            "question": "Analyze contract risks",
            "prompt_type": "risk_analysis",
            "top_k": 5
        }
    )

    print("\nAnalyze")
    print(response.status_code)
    print(response.json())


if __name__ == "__main__":
    test_health()
    test_chat()
    test_analyze()
    