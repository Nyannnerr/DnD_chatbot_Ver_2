#include "engine.h"
#include <stdio.h>

void init_player(Player* p, int hp, int str, int dex) {
    p->hp = hp;
    p->max_hp = hp;
    p->strength = str;
    p->dexterity = dex;
    printf("Player initialized with HP: %d\n", hp);
}

int calculate_damage(Player* p, int modifier) {
    return p->strength + modifier;
}
