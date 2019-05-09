
from collections import OrderedDict

OPTIONS = OrderedDict([
  (
    "progression_dungeons",
    "This controls whether dungeons can contain progress items.<br><u>If this is not checked, dungeons will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "progression_great_fairies",
    "This controls whether the items given by Great Fairies can be progress items.<br><u>If this is not checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "progression_puzzle_secret_caves",
    "This controls whether puzzle-focused secret caves can contain progress items.<br><u>If this is not checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "progression_combat_secret_caves",
    "This controls whether combat-focused secret caves (besides Savage Labyrinth) can contain progress items.<br><u>If this is not checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "progression_short_sidequests",
    "This controls whether sidequests that can be completed quickly can reward progress items.<br><u>If this is not checked, they will still be randomized</u>, but will only reward optional items you don't need to beat the game."
  ),
  (
    "progression_long_sidequests",
    "This controls whether long sidequests (e.g. Lenzo's assistant, withered trees, goron trading) can reward progress items.<br><u>If this is not checked, they will still be randomized</u>, but will only reward optional items you don't need to beat the game."
  ),
  (
    "progression_spoils_trading",
    "This controls whether the items you get by trading in spoils to NPCs can be progress items.<br><u>If this is not checked, they will still be randomized</u>, but will only reward optional items you don't need to beat the game."
  ),
  (
    "progression_minigames",
    "This controls whether most minigames can reward progress items (auctions, mail sorting, barrel shooting, bird-man contest).<br><u>If this is not checked, minigames will still be randomized</u>, but will only reward optional items you don't need to beat the game."
  ),
  (
    "progression_free_gifts",
    "This controls whether gifts freely given by NPCs can be progress items (Tott, Salvage Corp, imprisoned Tingle).<br><u>If this is not checked, they will still be randomized</u>, but will only be optional items you don't need to beat the game."
  ),
  (
    "progression_mail",
    "This controls whether mail can contain progress items.<br><u>If this is not checked, mail will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "progression_platforms_rafts",
    "This controls whether lookout platforms and rafts can contain progress items.<br><u>If this is not checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "progression_submarines",
    "This controls whether submarines can contain progress items.<br><u>If this is not checked, submarines will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "progression_eye_reef_chests",
    "This controls whether the chests that appear after clearing out the eye reefs can contain progress items.<br><u>If this is not checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "progression_big_octos_gunboats",
    "This controls whether the items dropped by Big Octos and Gunboats can contain progress items.<br><u>If this is not checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "progression_triforce_charts",
    "This controls whether the sunken treasure chests marked on Triforce Charts can contain progress items.<br><u>If this is not checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "progression_treasure_charts",
    "This controls whether the sunken treasure chests marked on Treasure Charts can contain progress items.<br><u>If this is not checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "progression_expensive_purchases",
    "This controls whether items that cost a lot of rupees can be progress items (Rock Spire shop, auctions, Tingle's letter, trading quest).<br><u>If this is not checked, they will still be randomized</u>, but will only be optional items you don't need to beat the game."
  ),
  (
    "progression_misc",
    "Miscellaneous locations that don't fit into any of the above categories (outdoors chests, pig, wind shrine, Cyclos etc).<br><u>If this is not checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "progression_tingle_chests",
    "Tingle Chests that are hidden in dungeons and must be bombed to make them appear. (2 in DRC, 1 each in FW, TotG, ET, and WT).<br><u>If this is not checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "progression_battlesquid",
    "This controls whether the Windfall battleship minigame can reward progress items.<br><u>If this is not checked, it will still be randomized</u>, but will only reward optional items you don't need to beat the game."
  ),
  (
    "progression_savage_labyrinth",
    "This controls whether the Savage Labyrinth can contain progress items.<br><u>If this is not checked, it will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  
  
  (
    "keylunacy",
    "Allows dungeon keys (as well as maps and compasses) to appear anywhere in the game, not just in the dungeon they're for."
  ),
  (
    "randomize_entrances",
    "Shuffles around which dungeon entrances/secret cave entrances take you into which dungeons/secret caves.\n(No effect on Forsaken Fortress or Ganon's Tower.)"
  ),
  (
    "randomize_charts",
    "Randomizes which sector is drawn on each Triforce/Treasure Chart."
  ),
  (
    "randomize_starting_island",
    "Randomizes which island you start the game on."
  ),
  
  (
    "swift_sail",
    "Sailing speed is doubled and the direction of the wind is always at your back as long as the sail is out."
  ),
  (
    "instant_text_boxes",
    "Text appears instantly.<br>Also, the B button is changed to instantly skip through text as long as you hold it down."
  ),
  (
    "reveal_full_sea_chart",
    "Start the game with the sea chart fully drawn out."
  ),
  (
    "num_starting_triforce_shards",
    "Change the number of Triforce Shards you start the game with.<br>The higher you set this, the fewer you will need to find placed randomly."
  ),
  (
    "add_shortcut_warps_between_dungeons",
    "Adds new warp pots that act as shortcuts connecting dungeons to each other directly. (DRC, FW, TotG, and separately FF, ET, WT.)\nEach pot must be unlocked before it can be used, so you cannot use them to access dungeons you wouldn't already have access to."
  ),
  (
    "generate_spoiler_log",
    "Generate a text file that lists the location of every single item for this seed. (This also changes where items are placed in this seed.)<br><u>Generating a spoiler log is highly recommended even if you don't intend to use it</u>, just in case you get completely stuck."
  ),
  (
    "sword_mode",
    "Controls whether you start with the Hero's Sword, the Hero's Sword is randomized, or if there are no swords in the entire game.\nSwordless and Randomized Sword are challenge modes, not recommended for your first run."
  ),
  (
    "skip_rematch_bosses",
    "Removes the door in Ganon's Tower that only unlocks when you defeat the rematch versions of Gohma, Kalle Demos, Jalhalla, and Molgera."
  ),
  (
    "invert_camera_x_axis",
    "Inverts the horizontal axis of camera movement.",
  ),
  (
    "race_mode",
    "In Race Mode, 4 random dungeon bosses will drop required items (e.g. Triforce Shards). Nothing in the other 2 dungeons will ever be required.\nYou can see which islands have the required dungeons on them by opening the sea chart and checking which islands have blue quest markers.",
  ),
  (
    "randomize_bgm",
    "Shuffles around all the background music in the game to play at random locations.",
  ),
  
  (
    "custom_player_model",
    "Replaces Link's model with a custom player model.\nThese are loaded from the /models folder."
  ),
  (
    "player_in_casual_clothes",
    "Enable this if you want to wear your casual clothes instead of the Hero's Clothes."
  ),
  (
    "disable_custom_player_voice",
    "If the chosen custom model comes with custom voice files, you can check this option to turn them off and simply use Link's normal voice instead."
  ),
  (
    "randomized_gear",
    "Inventory items that will be randomized."
  ),
  (
    "starting_gear",
    "Items that will be in Link's inventory at the start of a new game."
  ),
  ( 
    "glitches_ledge_clips",
    "Using objects (bombs, statues, pots, etc) to clip yourself into the wall when grabbing a ledge."
  ),
  (
    "glitches_roll_clips",
    "Grabbing a ledge with Link's hand in the wall, and rolling on the first frame possible to clip into walls."
  ),
  (
    "glitches_door_storage",
    "Storing a door to either unload it or be in the previous room when it unloads to get out of bounds."
  ),
  (
    "glitches_leaf_pumps",
    "Putting away the leaf and pulling it back out immediately to maintain height better when flying."
  ),
  (
    "glitches_spring_jump_storage",
    "Pushing down a spring, using a first person item to get it out of view and unloading it (hookshot), force-unequiping the iron boots, and hookshotting yourself to a target to keep the spring unloaded. Then when you want to use the spring jump, turn the camera back towards the spring to load it back in."
  ),
  (
    "glitches_Lslide",
    "When you start firing the hookshot, hold target and a direction on the control stick. You will move around while the hookshot is firing. Sometimes this is paired with a bomb explosion to clip out of bounds."
  ),
  (
    "glitches_bomb_boost",
    "Using the knockback from an exploding bomb to give yourself extra distance/height from a jump."
  ),
  (
    "glitches_weapons_thru_rooms",
    "Throwing enemy's weapons so that they bounce through doors while you're opening them."
  ),
  (
    "glitches_wwdives",
    "Pulling out the Wind Waker at ledges in order to dive deep under the ocean."
  ),
  (
    "glitches_ww_wind_cancel",
    "Pulling the Wind Waker to repeatedly cancel the effect of blowing wind to slowly move through it."
  ),
  (
    "glitches_sidle_clips",
    "Sidling against certain objects allowing you to clip through them, like the song stone in the Wind Temple basement."
  ),
  (
    "glitches_door_cancel",
    "Cancelling a door opening animation with stored boat text on the overworld to get a very small hitbox (and blinding yourself, pause-unpause to briefly see where you are)."
  ),
  (
    "glitches_korl_cyclones",
    "Jumping out of the boat into a cyclone to quickly gain height with the leaf."
  ),
  (
    "glitch_selection_box",
    "Select items from this box to add them to the list below. All tricks in the list will be available for the logic to consider."
  ),
  (
    "glitch_list",
    "Tricks in this list are available for logic take into account when randomizing."
  ),
])

NON_PERMALINK_OPTIONS = [
  "invert_camera_x_axis",
  "custom_player_model",
  "player_in_casual_clothes",
  "disable_custom_player_voice",
  "glitch_selection_box",
]
