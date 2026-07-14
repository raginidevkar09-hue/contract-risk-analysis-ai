from src.rag.zero_shot import ZERO_SHOT_PROMPT
from src.rag.few_shot import FEW_SHOT_PROMPT
from src.rag.chain_of_thought import CHAIN_OF_THOUGHT_PROMPT
from src.rag.json_output import JSON_OUTPUT_PROMPT
from src.rag.risk_analysis_prompt import RISK_ANALYSIS_PROMPT

PROMPTS = {
    "zero_shot": ZERO_SHOT_PROMPT,
    "few_shot": FEW_SHOT_PROMPT,
    "chain_of_thought": CHAIN_OF_THOUGHT_PROMPT,
    "json_output": JSON_OUTPUT_PROMPT,
    "risk_analysis": RISK_ANALYSIS_PROMPT,
}


def get_prompt(prompt_type="zero_shot"):
    return PROMPTS[prompt_type]