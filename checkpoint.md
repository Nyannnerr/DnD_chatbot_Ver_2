# KẾ HOẠCH CẢI THIỆN (CHECKPOINT)

## Nhiệm vụ
Giải quyết vấn đề Concurrency (mục A) và Hardcode logic (mục B) trong `GameEngine` và `DnDBot`.

## Kế hoạch hành động
1.  **Refactor `GameEngine` (Mục A & B):**
    *   Loại bỏ `self.active_player_id`, `self.current_scene`, `self.active_enemies` khỏi `__init__`.
    *   Cập nhật các phương thức để nhận tham số cần thiết (đặc biệt là `player_id`) thay vì dựa vào state của class.
    *   Di chuyển logic tính toán sát thương dựa trên class (fighter/mage) từ `DnDBot` vào `GameEngine` (dưới dạng một phương thức `calculate_class_damage`).

2.  **Cập nhật `DnDBot` (Mục A & B):**
    *   Sửa các phương thức `handle_...` để truyền `player_id` vào `GameEngine` một cách rõ ràng.
    *   Gọi `game_engine.calculate_class_damage` thay vì hardcode.

## Verification Gate (Mục 1 & 2)
*   **Gate A:** Chạy script test đơn giản (python code) mô phỏng 2 request `handle_attack` đồng thời, kiểm tra kết quả damage trả về đúng với chỉ số của mỗi người chơi, không bị trộn lẫn (giả định logic engine vẫn hoạt động đúng).
*   **Gate B:** Kiểm tra `bot.py` không còn chứa logic if-else theo class hardcode.

## Trạng thái
- Bắt đầu thực thi bước 1.
