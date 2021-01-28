from pathlib import Path

from .base_classes import BaseSpriteLoader
from .util import chunks_from_animation


class ItemSheet(BaseSpriteLoader):
    _sprite_sheet_path = Path("Data/Textures/items.png")
    _chunk_size = 128
    _chunk_map = {
        "chest": (0, 0, 1, 1),
        "chest_open": (1, 0, 2, 1),
        "crate": (2, 0, 3, 1),
        "emerald": (3, 0, 4, 1),
        "sapphire": (4, 0, 5, 1),
        "ruby": (5, 0, 6, 1),
        "diamond": (6, 0, 7, 1),
        "emerald_small": (7, 0, 8, 1),
        "sapphire_small": (8, 0, 9, 1),
        "ruby_small": (9, 0, 10, 1),
        "small_gold_in_block": (10, 0, 11, 1),
        "gold_in_block": (11, 0, 12, 1),
        "gold_nugget": (12, 0, 13, 1),
        "gold_pebble": (13, 0, 14, 1),
        "gold_bar": (14, 0, 15, 1),
        "gold_bars": (15, 0, 16, 1),
        "rock": (0, 1, 1, 2),
        "arrow_wood": (1, 1, 2, 2),
        "arrow_stub": (2, 1, 3, 2),
        "urn_tall": (3, 1, 4, 2),
        "urn_short": (4, 1, 5, 2),
        "urn_pitcher": (5, 1, 6, 2),
        "udjat_eye": (6, 1, 7, 2),
        "kapala": (7, 1, 8, 2),
        "udjat_key": (8, 1, 9, 2),
        "udjat_chest": (9, 1, 10, 2),
        "udjat_chest_open": (10, 1, 11, 2),
        "ankh": (11, 1, 12, 2),
        "hedjet": (12, 1, 13, 2),
        "scepter": (13, 1, 14, 2),
        "crown": (14, 1, 15, 2),
        "idol": (15, 1, 16, 2),
        "bomb_bag": (0, 2, 1, 3),
        "bomb_box": (1, 2, 2, 3),
        "paste": (2, 2, 3, 3),
        "compass": (3, 2, 4, 3),
        "climbing_glove": (4, 2, 5, 3),
        "pitchers_mitt": (5, 2, 6, 3),
        "spike_shoes": (6, 2, 7, 3),
        "spring_shoes": (7, 2, 8, 3),
        "cape": (8, 2, 9, 3),
        "jetpack": (9, 2, 10, 3),
        "jetpack_back": (10, 2, 11, 3),
        "parachute": (11, 2, 12, 3),
        "parachute1": (12, 2, 13, 3),
        "parachute2": (13, 2, 14, 3),
        "parachute3": (14, 2, 15, 3),
        "tablet_of_destiny": (15, 2, 16, 3),
        "shotgun": (0, 3, 1, 4),
        "webgun": (1, 3, 2, 4),
        "freeze_ray": (2, 3, 3, 4),
        "alien_compass": (3, 3, 4, 4),
        "plasma_cannon_reloading": (4, 3, 5, 4),
        "plasma_cannon": (5, 3, 6, 4),
        "teleporter": (6, 3, 7, 4),
        "boomerang": (7, 3, 8, 4),
        "None1": (8, 3, 9, 4),
        "golden_parachute": (9, 3, 10, 4),
        "spectacles": (10, 3, 11, 4),
        "crumpled_parachute1": (11, 3, 12, 4),
        "crumpled_parachute2": (12, 3, 13, 4),
        "crumpled_parachute3": (13, 3, 14, 4),
        "skeleton_piece": (14, 3, 15, 4),
        "skull": (15, 3, 16, 4),
        "crossbow_empty_on_ground": (0, 4, 1, 5),
        "crossbow_loaded_on_ground": (1, 4, 2, 5),
        "crossbow_empty_held": (2, 4, 3, 5),
        "crosbow_loaded_held": (3, 4, 4, 5),
        "metal_arrow": (4, 4, 5, 5),
        "wood_arrow_poisoned": (5, 4, 6, 5),
        "metal_arrow_poisoned": (6, 4, 7, 5),
        "telepack": (7, 4, 8, 5),
        "telepack_on_rope": (8, 4, 9, 5),
        "crumpled_golden_parachute": (9, 4, 10, 5),
        "camera": (10, 4, 11, 5),
        "true_crown": (11, 4, 12, 5),
        "web1": (12, 4, 13, 5),
        "web2": (13, 4, 14, 5),
        "web3": (14, 4, 15, 5),
        "web4": (15, 4, 16, 5),
        "bomb": (0, 5, 1, 6),
        "bomb_exploding1": (1, 5, 2, 6),
        "bomb_exploding2": (2, 5, 3, 6),
        "paste_bomb": (3, 5, 4, 6),
        "paste_bomb_exploding1": (4, 5, 5, 6),
        "paste_bomb_exploding2": (5, 5, 6, 6),
        "None2": (6, 5, 7, 6),
        "None3": (7, 5, 8, 6),
        "None4": (8, 5, 9, 6),
        "None5": (9, 5, 10, 6),
        "None6": (10, 5, 11, 6),
        "None7": (11, 5, 12, 6),
        **chunks_from_animation("scarab", (12, 5, 13, 6), 4),
        "rope_pile": (0, 6, 1, 7),
        "bomb_box_damaged1": (1, 6, 2, 7),
        "bomb_box_damaged2": (2, 6, 3, 7),
        "vlads_cape": (3, 6, 4, 7),
        **chunks_from_animation("vlads_cape_worn", (4, 6, 5, 7), 7),
        "kali_ball": (11, 6, 12, 7),
        "kali_chain1": (12, 6, 13, 7),
        "kali_chain2": (13, 6, 14, 7),
        "None11": (14, 6, 15, 7),
        "None12": (15, 6, 16, 7),
        "machete": (0, 7, 1, 8),
        **chunks_from_animation("machete_worn", (1, 7, 2, 8), 3),
        **chunks_from_animation("cape_worn", (4, 7, 5, 8), 12),
        "mattock": (0, 8, 1, 9),
        **chunks_from_animation("mattock_worn", (1, 8, 2, 9), 3),
        "mattock_broken": (4, 8, 5, 9),
        "flag": (5, 8, 6, 9),
        **chunks_from_animation("flag_worn", (6, 8, 7, 9), 5),
        **chunks_from_animation("gold_bar_shiny", (11, 8, 12, 9), 5),
        "excalibur": (0, 9, 1, 10),
        **chunks_from_animation("excalibur_worn", (1, 9, 2, 10), 3),
        "hoverpack": (4, 9, 5, 10),
        "hoverpack_back": (5, 9, 6, 10),
        "hoverpack_flicker1": (6, 9, 7, 10),
        "hoverpack_flicker2": (7, 9, 8, 10),
        "clone_gun": (8, 9, 9, 10),
        "clone_gun_two_charges": (9, 9, 10, 10),
        "clone_gun_one_charge": (10, 9, 11, 10),
        **chunks_from_animation("gold_bars_shiny", (11, 9, 12, 10), 5),
        "totem_trap_arm": (0, 10, 1, 11),
        "lantern": (1, 10, 2, 11),
        "excalibur_in_stone": (2, 10, 3, 11),
        "excalibur_stone": (3, 10, 4, 11),
        "torch": (4, 10, 5, 11),
        "wall_torch": (5, 10, 6, 11),
        "paper_lantern": (6, 10, 7, 11),
        "hou_yi_bow": (7, 10, 8, 11),
        "hou_yi_bow_loaded": (8, 10, 9, 11),
        "lightarrow": (9, 10, 10, 11),
        "journal_key": (10, 10, 11, 11),
        "elixir": (11, 10, 12, 11),
        "tusk_idol": (12, 10, 13, 11),
        "eggplant": (13, 10, 14, 11),
        "note": (14, 10, 15, 11),
        "journal": (15, 10, 16, 11),
        "wood_spike": (0, 11, 1, 12),
        "metal_spike": (1, 11, 2, 12),
        "landmine_armed": (2, 11, 3, 12),
        "landmine_deactivated": (3, 11, 4, 12),
        "landmine_exploding1": (4, 11, 5, 12),
        "landmine_exploding2": (5, 11, 6, 12),
        "jumppad": (6, 11, 7, 12),
        "powerpack": (7, 11, 8, 12),
        "powerpack_back": (8, 11, 9, 12),
        **chunks_from_animation("sleep_bubble", (9, 11, 10, 12), 8),
        "yama_pot": (1, 12, 2, 13),
        "pot_of_gold": (2, 12, 3, 13),
        "broken_sword": (3, 12, 4, 13),
        **chunks_from_animation("broken_sword_worn", (4, 12, 5, 13), 3),
        "bear_trap_armed": (7, 12, 8, 13),
        "bear_trap_closed": (8, 12, 9, 13),
        "white_flag": (9, 12, 10, 13),
        "flag_stick": (10, 12, 11, 13),
        "wooden_idol": (11, 12, 12, 13),
        "None13": (12, 12, 13, 13),
        "None14": (13, 12, 14, 13),
        "None15": (14, 12, 15, 13),
        "eggplant_bit": (15, 12, 16, 13),
        "spike_ball": (0, 13, 1, 14),
        "key": (1, 13, 2, 14),
        "skeleton_key": (2, 13, 3, 14),
        "locked_door": (3, 13, 4, 14),
        "wooden_shield": (4, 13, 5, 14),
        "wooden_shield_damaged": (5, 13, 6, 14),
        "metal_shield": (6, 13, 7, 14),
        **chunks_from_animation("gold_coin", (7, 13, 8, 14), 6),
        "snowman": (13, 13, 14, 14),
        "snowball": (14, 13, 15, 14),
        "eggplant_crown": (15, 13, 16, 14),
        "bullet": (0, 14, 1, 15),
        "webgun_ball": (1, 14, 2, 15),
        "poison_bubble1": (2, 14, 3, 15),
        "poison_bubble2": (3, 14, 4, 15),
        "inkspot": (4, 14, 5, 15),
        **chunks_from_animation("dice_rolling", (5, 14, 6, 15), 6),
        "celestial_orb": (11, 14, 12, 15),
        "royal_jelly": (12, 14, 13, 15),
        "honey1": (13, 14, 14, 15),
        "honey2": (14, 14, 15, 15),
        "cooked_turkey": (15, 14, 16, 15),
        "ice_block1": (0, 15, 1, 16),
        "ice_block2": (1, 15, 2, 16),
        "clover": (2, 15, 3, 16),
        "scrap": (3, 15, 4, 16),
        "cursed_urn": (4, 15, 5, 16),
        **chunks_from_animation("dice", (5, 15, 6, 16), 6),
        **chunks_from_animation("present", (11, 15, 12, 16), 6),
    }