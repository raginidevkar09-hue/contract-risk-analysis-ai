from prompt_template import PROMPT_TEMPLATE

context = """
Termination Clause

Either party may terminate this agreement by giving
30 days written notice.
"""

question = "Can the agreement be terminated early?"

prompt = PROMPT_TEMPLATE.format(
    context=context,
    question=question
)

print(prompt)