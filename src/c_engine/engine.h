#ifndef ENGINE_H
#define ENGINE_H

typedef struct {
    int hp;
    int max_hp;
    int strength;
    int dexterity;
} Player;

// Khởi tạo player
void init_player(Player* p, int hp, int str, int dex);

// Tính sát thương (ví dụ đơn giản)
int calculate_damage(Player* p, int modifier);

#endif
