'''

A @staticmethod does not required self (the instance) as its first argument inside function.

It belongs to the class's namespace but behaves like a plain function - it has no access to instance variables.

------------------------------------------------------------------------------------------------------------------------

Example:


class PromptBuilder:
    'Builds and manages prompts for LLM interactions.'

    DEFAULT_SYSTEM_PROMPT = 'You are a helpful assistant.'

    def __init__(self, system_prompt: str = DEFAULT_SYSTEM_PROMPT):
        self.system_prompt = system_prompt
        self. history: list[dict] = []

    
    def _add_user_message(self, message: str) -> None:
        self.history.append({'role': 'user', 'content': message})


    @staticmethod
    def estimate_tokens(text:str) -> int:
        'Rought token estimate: ~4 chars per token'
        return len(text) // 4

'''