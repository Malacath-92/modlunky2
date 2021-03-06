from .character import (
    CharacterBlackSpriteMerger,
    CharacterLimeSpriteMerger,
    CharacterMagentaSpriteMerger,
    CharacterOliveSpriteMerger,
    CharacterOrangeSpriteMerger,
    CharacterPinkSpriteMerger,
    CharacterRedSpriteMerger,
    CharacterVioletSpriteMerger,
    CharacterWhiteSpriteMerger,
    CharacterYellowSpriteMerger,
    CharacterBlueSpriteMerger,
    CharacterCeruleanSpriteMerger,
    CharacterCinnabarSpriteMerger,
    CharacterCyanSpriteMerger,
    CharacterGoldSpriteMerger,
    CharacterGraySpriteMerger,
    CharacterGreenSpriteMerger,
    CharacterIrisSpriteMerger,
    CharacterKhakiSpriteMerger,
    CharacterLemonSpriteMerger,
    CharacterEggChildSpriteMerger,
    CharacterHiredHandSpriteMerger,
)
from .mounts import (
    TurkeySpriteMerger,
    RockdogSpriteMerger,
    AxolotlSpriteMerger,
    QilinSpriteMerger,
)
from .pets import MontySpriteMerger, PercySpriteMerger, PoochiSpriteMerger
from .ghost import *
from .monsters.basic import *
from .monsters.big import *

__all__ = [
    "CharacterBlackSpriteMerger",
    "CharacterLimeSpriteMerger",
    "CharacterMagentaSpriteMerger",
    "CharacterOliveSpriteMerger",
    "CharacterOrangeSpriteMerger",
    "CharacterPinkSpriteMerger",
    "CharacterRedSpriteMerger",
    "CharacterVioletSpriteMerger",
    "CharacterWhiteSpriteMerger",
    "CharacterYellowSpriteMerger",
    "CharacterBlueSpriteMerger",
    "CharacterCeruleanSpriteMerger",
    "CharacterCinnabarSpriteMerger",
    "CharacterCyanSpriteMerger",
    "CharacterGoldSpriteMerger",
    "CharacterGraySpriteMerger",
    "CharacterGreenSpriteMerger",
    "CharacterIrisSpriteMerger",
    "CharacterKhakiSpriteMerger",
    "CharacterLemonSpriteMerger",
    "CharacterEggChildSpriteMerger",
    "CharacterHiredHandSpriteMerger",
    "TurkeySpriteMerger",
    "RockdogSpriteMerger",
    "AxolotlSpriteMerger",
    "QilinSpriteMerger",
    "MontySpriteMerger",
    "PercySpriteMerger",
    "PoochiSpriteMerger",
    "SnakeSpriteMerger",
    "BatSpriteMerger",
    "FlySpriteMerger",
    "SkeletonSpriteMerger",
    "SpiderSpriteMerger",
    # "EarSpriteMerger",  # RIP Ear
    "ShopkeeperSpriteMerger",
    "UfoSpriteMerger",
    "AlienSpriteMerger",
    "CobraSpriteMerger",
    "ScorpionSpriteMerger",
    "GoldenMonkeySpriteMerger",
    "BeeSpriteMerger",
    "MagmarSpriteMerger",
    "VampireSpriteMerger",
    "VladSpriteMerger",
    "LeprechaunSpriteMerger",
    "CaveManSpriteMerger",
    "BodyguardSpriteMerger",
    "OldHunterSpriteMerger",
    "MerchantSpriteMerger",
    "HundunsServantSpriteMerger",
    "ThiefSpriteMerger",
    "ParmesanSpriteMerger",
    "ParsleySpriteMerger",
    "ParsnipSpriteMerger",
    "YangSpriteMerger",
    "BirdiesSpriteMerger",
    "RobotSpriteMerger",
    "ImpSpriteMerger",
    "TikiManSpriteMerger",
    "ManTrapSpriteMerger",
    "CritterSnailSpriteMerger",
    "CritterDungBeetleSpriteMerger",
    "FireBugSpriteMerger",
    "MoleSpriteMerger",
    "WitchDoctorSpriteMerger",
    "CritterButterflySpriteMerger",
    "HornedLizardSpriteMerger",
    "WitchDoctorSkullSpriteMerger",
    "MonkeySpriteMerger",
    "HangSpiderSpriteMerger",
    "MosquitoSpriteMerger",
    "JiangshiSpriteMerger",
    "HermitCrabSpriteMerger",
    "FlyingFishSpriteMerger",
    "OctopusSpriteMerger",
    "CritterCrabSpriteMerger",
    "CritterBlueCrabSpriteMerger",
    "FemaleJiangshiSpriteMerger",
    "CritterFishSpriteMerger",
    "CrocManSpriteMerger",
    "SorceressSpriteMerger",
    "CatMummySpriteMerger",
    "CritterAnchovySpriteMerger",
    "NecromancerSpriteMerger",
    "CrittersLocustSpriteMerger",
    "YetiSpriteMerger",
    "ProtoShopkeeperSpriteMerger",
    "CritterFireflySpriteMerger",
    "PenguinSpriteMerger",
    "DroneSpriteMerger",
    "SlimeSpriteMerger",
    "JumpdogSpriteMerger",
    "TadpoleSpriteMerger",
    "OlmiteNakedSpriteMerger",
    "OlmitedArmoredSpriteMerger",
    "OlmiteHelmetSpriteMerger",
    "GrubSpriteMerger",
    "FrogSpriteMerger",
    "FireFrogSpriteMerger",
    "QuillbackSpriteMerger",
    "GiantSpiderSpriteMerger",
    "QueenBeeSpriteMerger",
    "MummySpriteMerger",
    "AnubisSpriteMerger",
    "Anubis2SpriteMerger",
    "LamassuSpriteMerger",
    "YetiKingSpriteMerger",
    "YetiQueenSpriteMerger",
    "CrabManSpriteMerger",
    "LavamanderSpriteMerger",
    "GiantFlySpriteMerger",
    "GiantClamSpriteMerger",
    "AmmitSpriteMerger",
    "MadameTuskSpriteMerger",
    "EggplantMinisterSpriteMerger",
    "GiantFrogSpriteMerger",
    "GiantFishSpriteMerger",
    "KinguSpriteMerger",
    "StorageGuySpriteMerger",
    "OsirisSpriteMerger",
    "AlienQueenSpriteMerger",
    "OlmecSpriteMerger",
    "MechSpriteMerger",
    "GhistSpriteMerger",
    "GhostSpriteMerger",
    "GhostMediumSadSpriteMerger",
    "GhostMediumHappySpriteMerger",
    "GhostSmallSadSpriteMerger",
    "GhostSmallHappySpriteMerger",
    "GhostSmallSurprisedSpriteMerger",
    "GhostSmallAngrySpriteMerger",
    "MegaJellySpriteMerger",
]
