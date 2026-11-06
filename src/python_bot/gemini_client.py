import os
from src.python_bot.tools import tools_definition

class GeminiClient:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        # genai.configure(api_key=self.api_key)
        # self.model = genai.GenerativeModel(
        #     'gemini-pro',
        #     tools=tools_definition
        # )

    def generate_narrative(self, prompt, context=None):
        if not self.api_key:
            return f"[Mock Gemini] Narrative: {prompt} | Context: {context}"
        
        # Ví dụ gọi API thật:
        # response = self.model.generate_content(prompt)
        # return response.text
        return "[Gemini Response]"

    def handle_tool_call(self, tool_name, args, engine):
        # Đây là nơi bot thực thi hàm mà Gemini yêu cầu
        if tool_name == "spawn_enemy":
            return engine.spawn_enemy(**args)
        elif tool_name == "trigger_ambush":
            return engine.trigger_ambush()
        elif tool_name == "end_encounter":
            return engine.end_encounter(**args)
        return "Unknown tool call"
