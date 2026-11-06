# Định nghĩa các tool (schema) cho Gemini
# Đây là format để Gemini biết có thể gọi những hàm nào

tools_definition = [
    {
        "name": "spawn_enemy",
        "description": "Spawn một quái vật mới trong trận chiến.",
        "parameters": {
            "type": "object",
            "properties": {
                "enemy_type": {"type": "string", "description": "Tên loại quái vật"},
                "difficulty": {"type": "integer", "description": "Độ khó (1-10)"}
            },
            "required": ["enemy_type", "difficulty"]
        }
    },
    {
        "name": "trigger_ambush",
        "description": "Tạo ra một tình huống phục kích bất ngờ.",
        "parameters": {"type": "object", "properties": {}}
    },
    {
        "name": "end_encounter",
        "description": "Kết thúc trận chiến hiện tại.",
        "parameters": {
            "type": "object",
            "properties": {
                "result": {"type": "string", "description": "Kết quả trận chiến (thắng/thua)"}
            },
            "required": ["result"]
        }
    }
]
