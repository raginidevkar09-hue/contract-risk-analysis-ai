import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT))

from src.llm.rag_chain import run_rag


def main():

    question = input("Enter your question: ")

    print("\nAvailable Prompt Types")
    print("----------------------")
    print("1. zero_shot")
    print("2. few_shot")
    print("3. chain_of_thought")

    prompt_type = input("\nSelect Prompt Type: ").strip()

    result = run_rag(
        question=question,
        prompt_type=prompt_type
    )

    print("\n" + "=" * 80)
    print("Question")
    print("=" * 80)
    print(result["question"])

    print("\n" + "=" * 80)
    print("Retrieved Context")
    print("=" * 80)
    print(result["context"])

    print("\n" + "=" * 80)
    print("LLM Answer")
    print("=" * 80)
    print(result["answer"])


if __name__ == "__main__":
    main()