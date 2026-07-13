import ollama


def generate_answer(prompt: str, model: str = "llama3.2:3b") -> str:

    response = ollama.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


if __name__ == "__main__":
    question = "Explain indemnity clause in simple words."

    answer = generate_answer(question)

    print("\nAnswer:\n")
    print(answer)
