PALI_ROOTS={
    "√as": {
      "meaning": "to be, exist",
      "type": "primary",
      "frequency": "very_high",
      "stems": {
        "present": "atthi",
        "aorist": "āsi",
        "perfect": "āsa",
        "passive": "assīya",
        "causative": "āsāpe",
        "past_participle": "bhūta"
      },
      "prefixes": ["upa", "ati", "anu"],
      "generates_forms": 180,
      "generation_hints": {
        "irregular_present": "atthi not asati",
        "aorist_variants": ["āsi", "ahosi"],
        "avoid_generating": ["*asati", "*asanti"]
      }
    },

    "√bhū": {
      "meaning": "to become, arise",
      "type": "primary", 
      "frequency": "very_high",
      "stems": {
        "present": "bhava",
        "aorist": "abhūsi",
        "perfect": "babhūva",
        "passive": "bhūyīya",
        "causative": "bhāve",
        "past_participle": "bhūta"
      },
      "prefixes": ["ā", "sam", "pra", "vi", "upa", "anu"],
      "generates_forms": 240,
      "generation_hints": {
        "aorist_variants": ["ahū", "abhū"],
        "causative_meaning": "to cause to become"
      }
    },

    "√gam": {
      "meaning": "to go, move",
      "type": "primary",
      "frequency": "very_high", 
      "stems": {
        "present": "gaccha",
        "aorist": "agamā",
        "perfect": "jagāma",
        "passive": "gacchīya",
        "causative": "game",
        "past_participle": "gata"
      },
      "prefixes": ["ā", "upa", "ni", "pa", "vi", "saṃ", "anu"],
      "generates_forms": 250,
      "generation_hints": {
        "irregular_present": "gaccha not gama",
        "aorist_variants": ["agami", "agamā", "gañchi"],
        "avoid_generating": ["*gamati", "*gamanti"]
      }
    },

    "√gacch": {
      "meaning": "to go, proceed", 
      "type": "primary",
      "frequency": "very_high",
      "stems": {
        "present": "gaccha",
        "aorist": "agacchi",
        "perfect": "jagaccha",
        "passive": "gacchīya", 
        "causative": "gacchāpe",
        "past_participle": "gacchita"
      },
      "prefixes": ["ā", "upa", "ni", "pa", "vi", "saṃ"],
      "generates_forms": 240,
      "generation_hints": {
        "related_to": "√gam",
        "present_standard": "gacchati"
      }
    },

    "√yā": {
      "meaning": "to go, travel",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "yā",
        "aorist": "ayāsi",
        "perfect": "yayau",
        "passive": "yāyīya",
        "causative": "yāpe",
        "past_participle": "yāta"
      },
      "prefixes": ["ā", "upa", "pari", "vi"],
      "generates_forms": 200,
      "generation_hints": {
        "irregular_perfect": "yayau with reduplication",
        "causative_variants": ["yāpe", "yājāpe"]
      }
    },

    "√ṭhā": {
      "meaning": "to stand, remain",
      "type": "primary",
      "frequency": "very_high",
      "stems": {
        "present": "tiṭṭha",
        "aorist": "aṭṭhāsi",
        "perfect": "taṭṭhau",
        "passive": "ṭhīya",
        "causative": "ṭhāpe",
        "past_participle": "ṭhita"
      },
      "prefixes": ["ā", "upa", "sam", "ut"],
      "generates_forms": 220,
      "generation_hints": {
        "irregular_present": "tiṭṭhati not ṭhāti",
        "aorist_variants": ["aṭṭhā", "aṭṭhāsi"]
      }
    },

    "√sad": {
      "meaning": "to sit",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "sīda",
        "aorist": "asīdi",
        "perfect": "sasāda",
        "passive": "sīdīya",
        "causative": "sādāpe",
        "past_participle": "sanna"
      },
      "prefixes": ["ā", "upa", "ni", "pari"],
      "generates_forms": 180,
      "generation_hints": {
        "present_vowel_change": "sad > sīda",
        "participle_irregular": "sanna not *sadita"
      }
    },

    "√sī": {
      "meaning": "to lie down",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "saya",
        "aorist": "asayi",
        "perfect": "śaśāya",
        "passive": "sayīya",
        "causative": "sāye",
        "past_participle": "sayita"
      },
      "prefixes": ["upa", "vi", "pari"],
      "generates_forms": 160,
      "generation_hints": {
        "present_form": "sayati/seti",
        "variants": ["saya", "se"]
      }
    },

    "√vad": {
      "meaning": "to speak, say",
      "type": "primary",
      "frequency": "very_high",
      "stems": {
        "present": "vada",
        "aorist": "avadi",
        "perfect": "uvāda",
        "passive": "vuccati",
        "causative": "vādāpe",
        "past_participle": "vutta"
      },
      "prefixes": ["ā", "upa", "prati", "vi", "sam"],
      "generates_forms": 230,
      "generation_hints": {
        "irregular_passive": "vuccati not *vadīyati",
        "irregular_participle": "vutta not *vadita"
      }
    },

    "√vac": {
      "meaning": "to speak, tell",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "vaca",
        "aorist": "avoci",
        "perfect": "uvāca",
        "passive": "vuccati",
        "causative": "vācāpe",
        "past_participle": "vutta"
      },
      "prefixes": ["ā", "pra", "vi"],
      "generates_forms": 210,
      "generation_hints": {
        "aorist_variants": ["avoci", "avaca"],
        "shared_passive": "vuccati with √vad"
      }
    },

    "√bhās": {
      "meaning": "to speak, shine",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "bhāsa",
        "aorist": "abhāsi",
        "perfect": "babhāse",
        "passive": "bhāsīya",
        "causative": "bhāsāpe",
        "past_participle": "bhāsita"
      },
      "prefixes": ["ā", "pra", "vi"],
      "generates_forms": 180,
      "generation_hints": {
        "dual_meaning": "speak or shine contextually"
      }
    },

    "√kath": {
      "meaning": "to tell, relate",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "katha",
        "aorist": "akathi",
        "perfect": "cakātha",
        "passive": "kathīya",
        "causative": "kathāpe",
        "past_participle": "kathita"
      },
      "prefixes": ["ā", "pra", "vi", "sam"],
      "generates_forms": 190,
      "generation_hints": {
        "standard_forms": "regular conjugation"
      }
    },

    "√lap": {
      "meaning": "to talk, chatter",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "lapa",
        "aorist": "alapi",
        "perfect": "lalāpa",
        "passive": "lapīya",
        "causative": "lāpāpe",
        "past_participle": "lapita"
      },
      "prefixes": ["ā", "pra", "vi"],
      "generates_forms": 170,
      "generation_hints": {
        "meaning_nuance": "casual or excessive talking"
      }
    },

    "√kar": {
      "meaning": "to do, make",
      "type": "primary",
      "frequency": "very_high",
      "stems": {
        "present": "karo",
        "aorist": "akāsi",
        "perfect": "cakāra",
        "passive": "karīya",
        "causative": "kārāpe",
        "past_participle": "kata"
      },
      "prefixes": ["ā", "upa", "pra", "vi", "sam", "anu"],
      "generates_forms": 280,
      "generation_hints": {
        "aorist_variants": ["akāsi", "akari"],
        "irregular_participle": "kata not *karita"
      }
    },

    "√kā": {
      "meaning": "to do, make",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "kā",
        "aorist": "akāsi",
        "perfect": "cakau",
        "passive": "kāyīya",
        "causative": "kāpe",
        "past_participle": "kāta"
      },
      "prefixes": ["ā", "pra", "vi"],
      "generates_forms": 160,
      "generation_hints": {
        "variant_of": "√kar",
        "less_common": "archaic forms"
      }
    },

    "√dā": {
      "meaning": "to give",
      "type": "primary",
      "frequency": "very_high",
      "stems": {
        "present": "dada",
        "aorist": "adāsi",
        "perfect": "dadau",
        "passive": "dīya",
        "causative": "dāpe",
        "past_participle": "datta"
      },
      "prefixes": ["ā", "upa", "pra", "vi", "sam"],
      "generates_forms": 250,
      "generation_hints": {
        "irregular_present": "dadāti not *dāti",
        "irregular_passive": "dīyati",
        "irregular_participle": "datta"
      }
    },

    "√gah": {
      "meaning": "to take, grasp",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "gaṇhā",
        "aorist": "agahesi",
        "perfect": "jagāha",
        "passive": "gahīya",
        "causative": "gāhāpe",
        "past_participle": "gahita"
      },
      "prefixes": ["ā", "upa", "pari", "sam"],
      "generates_forms": 200,
      "generation_hints": {
        "irregular_present": "gaṇhāti not *gahati",
        "nasal_insertion": "gaṇh- forms"
      }
    },

    "√labh": {
      "meaning": "to get, obtain",
      "type": "primary",
      "frequency": "very_high",
      "stems": {
        "present": "labha",
        "aorist": "alabhī",
        "perfect": "lalābha",
        "passive": "labbha",
        "causative": "lābhāpe",
        "past_participle": "laddha"
      },
      "prefixes": ["ā", "upa", "pra", "vi", "sam"],
      "generates_forms": 220,
      "generation_hints": {
        "irregular_passive": "labbhati",
        "irregular_participle": "laddha not *labhita"
      }
    },

    "√ā + dā": {
      "meaning": "to take, receive",
      "type": "compound",
      "frequency": "high",
      "stems": {
        "present": "ādada",
        "aorist": "ādāsi",
        "perfect": "ādadau",
        "passive": "ādīya",
        "causative": "ādāpe",
        "past_participle": "ādinna"
      },
      "prefixes": ["pari", "sam"],
      "generates_forms": 180,
      "generation_hints": {
        "compound_root": "ā + √dā",
        "meaning_shift": "take vs give"
      }
    },

    "√har": {
      "meaning": "to carry, take",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "hara",
        "aorist": "ahāsi",
        "perfect": "jahāra",
        "passive": "harīya",
        "causative": "hārāpe",
        "past_participle": "haṭa"
      },
      "prefixes": ["ā", "upa", "pra", "vi", "sam"],
      "generates_forms": 210,
      "generation_hints": {
        "irregular_participle": "haṭa/hata variants"
      }
    },

    "√nī": {
      "meaning": "to lead, guide",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "naya",
        "aorist": "anesi",
        "perfect": "ninaya",
        "passive": "nīya",
        "causative": "nāyāpe",
        "past_participle": "nīta"
      },
      "prefixes": ["ā", "upa", "pra", "vi", "sam", "anu"],
      "generates_forms": 200,
      "generation_hints": {
        "present_change": "nī > naya",
        "regular_forms": "mostly regular"
      }
    },

    "√vah": {
      "meaning": "to carry, convey",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "vaha",
        "aorist": "avāhi",
        "perfect": "uvāha",
        "passive": "vūha",
        "causative": "vāhāpe",
        "past_participle": "vūḷha"
      },
      "prefixes": ["ā", "upa", "pra", "vi", "sam"],
      "generates_forms": 190,
      "generation_hints": {
        "irregular_passive": "vūhati",
        "irregular_participle": "vūḷha"
      }
    },

    "√dhā": {
      "meaning": "to put, place",
      "type": "primary",
      "frequency": "very_high",
      "stems": {
        "present": "dadha",
        "aorist": "adhāsi",
        "perfect": "dadau",
        "passive": "dhīya",
        "causative": "dhāpe",
        "past_participle": "hita"
      },
      "prefixes": ["ā", "upa", "ni", "pra", "vi", "sam"],
      "generates_forms": 240,
      "generation_hints": {
        "irregular_present": "dadhāti",
        "irregular_participle": "hita not *dhāta"
      }
    },

    "√ṭhap": {
      "meaning": "to establish, set up",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "ṭhape",
        "aorist": "aṭṭhapesi",
        "perfect": "taṭṭhāpa",
        "passive": "ṭhapīya",
        "causative": "ṭhāpāpe",
        "past_participle": "ṭhapita"
      },
      "prefixes": ["ā", "upa", "pra", "sam"],
      "generates_forms": 170,
      "generation_hints": {
        "causative_base": "inherently causative meaning"
      }
    },

    "√dhṛ": {
      "meaning": "to hold, bear",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "dhara",
        "aorist": "adhāresi",
        "perfect": "dadhāra",
        "passive": "dharīya",
        "causative": "dhārāpe",
        "past_participle": "dhata"
      },
      "prefixes": ["ā", "upa", "vi", "sam"],
      "generates_forms": 190,
      "generation_hints": {
        "regular_forms": "standard conjugation"
      }
    },

    "√bhṛ": {
      "meaning": "to bear, support",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "bhara",
        "aorist": "abhāresi",
        "perfect": "babhāra",
        "passive": "bharīya",
        "causative": "bhārāpe",
        "past_participle": "bhata"
      },
      "prefixes": ["ā", "upa", "vi", "sam"],
      "generates_forms": 180,
      "generation_hints": {
        "related_to": "√dhṛ",
        "similar_forms": "parallel conjugation"
      }
    },

    "√bandh": {
      "meaning": "to bind, tie",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "bandha",
        "aorist": "abandhi",
        "perfect": "babandha",
        "passive": "bajjha",
        "causative": "bandhāpe",
        "past_participle": "baddha"
      },
      "prefixes": ["ā", "upa", "pari", "sam"],
      "generates_forms": 200,
      "generation_hints": {
        "irregular_passive": "bajjhati",
        "irregular_participle": "baddha"
      }
    },

    "√muc": {
      "meaning": "to release, free",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "muñca",
        "aorist": "amuñci",
        "perfect": "mumuñca",
        "passive": "muccīya",
        "causative": "mocāpe",
        "past_participle": "mutta"
      },
      "prefixes": ["ā", "vi", "pari", "sam"],
      "generates_forms": 190,
      "generation_hints": {
        "present_nasal": "muñca not *muca",
        "causative_change": "moc- not muc-"
      }
    },

    "√yuj": {
      "meaning": "to join, yoke",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "yuñja",
        "aorist": "ayuñji",
        "perfect": "yuyoja",
        "passive": "yujjīya",
        "causative": "yojāpe",
        "past_participle": "yutta"
      },
      "prefixes": ["ā", "sam", "vi", "pra"],
      "generates_forms": 200,
      "generation_hints": {
        "present_nasal": "yuñja not *yuja",
        "causative_change": "yoj- not yuj-"
      }
    },

    "√chid": {
      "meaning": "to cut, sever",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "chinda",
        "aorist": "acchedi",
        "perfect": "ciccheda",
        "passive": "chijja",
        "causative": "chedāpe",
        "past_participle": "chinna"
      },
      "prefixes": ["ā", "vi", "pra", "sam"],
      "generates_forms": 180,
      "generation_hints": {
        "present_nasal": "chinda",
        "irregular_passive": "chijjati"
      }
    },

    "√bhid": {
      "meaning": "to break, split",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "bhinda",
        "aorist": "abhedi",
        "perfect": "bibheda",
        "passive": "bhijja",
        "causative": "bhedāpe",
        "past_participle": "bhinna"
      },
      "prefixes": ["ā", "vi", "pra", "sam"],
      "generates_forms": 180,
      "generation_hints": {
        "parallel_to": "√chid",
        "similar_patterns": "nasal present"
      }
    },

    "√bhañj": {
      "meaning": "to break, shatter",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "bhañja",
        "aorist": "abhañji",
        "perfect": "babhañja",
        "passive": "bhaññīya",
        "causative": "bhañjāpe",
        "past_participle": "bhañña"
      },
      "prefixes": ["ā", "vi", "sam"],
      "generates_forms": 170,
      "generation_hints": {
        "geminate_forms": "bhaññ- variants"
      }
    },

    "√han": {
      "meaning": "to strike, kill",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "hana",
        "aorist": "ahani",
        "perfect": "jaghāna",
        "passive": "haññīya",
        "causative": "ghātāpe",
        "past_participle": "hata"
      },
      "prefixes": ["ā", "vi", "pra", "sam"],
      "generates_forms": 200,
      "generation_hints": {
        "irregular_causative": "ghāt- not han-",
        "irregular_perfect": "jaghāna"
      }
    },

    "√vadh": {
      "meaning": "to kill, slay",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "vadha",
        "aorist": "avadhi",
        "perfect": "vavādha",
        "passive": "vajjha",
        "causative": "vadhāpe",
        "past_participle": "vaddha"
      },
      "prefixes": ["ā", "vi", "sam"],
      "generates_forms": 170,
      "generation_hints": {
        "passive_variants": "vajjh- forms"
      }
    },

    "√mar": {
      "meaning": "to die",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "mara",
        "aorist": "amari",
        "perfect": "mamāra",
        "passive": "marīya",
        "causative": "mārāpe",
        "past_participle": "mata"
      },
      "prefixes": ["ā", "vi", "pra"],
      "generates_forms": 180,
      "generation_hints": {
        "intransitive_primary": "usually intransitive"
      }
    },

    "√jīv": {
      "meaning": "to live",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "jīva",
        "aorist": "ajīvi",
        "perfect": "jijīva",
        "passive": "jīvīya",
        "causative": "jīvāpe",
        "past_participle": "jīvita"
      },
      "prefixes": ["ā", "pra", "sam"],
      "generates_forms": 180,
      "generation_hints": {
        "intransitive_primary": "usually intransitive"
      }
    },

    "√vas": {
      "meaning": "to dwell, live",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "vasa",
        "aorist": "avāsi",
        "perfect": "uvāsa",
        "passive": "vussīya",
        "causative": "vāsāpe",
        "past_participle": "vuttha"
      },
      "prefixes": ["ā", "ni", "pari", "sam"],
      "generates_forms": 190,
      "generation_hints": {
        "irregular_participle": "vuttha not *vasita"
      }
    },

    "√jan": {
      "meaning": "to be born, produce",
      "type": "primary",
      "frequency": "very_high",
      "stems": {
        "present": "jana",
        "aorist": "ajani",
        "perfect": "jajāna",
        "passive": "jāya",
        "causative": "janāpe",
        "past_participle": "jāta"
      },
      "prefixes": ["ā", "pra", "sam", "vi"],
      "generates_forms": 220,
      "generation_hints": {
        "irregular_passive": "jāyati",
        "dual_meaning": "be born/produce"
      }
    },

    "√jā": {
      "meaning": "to be born",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "jāya",
        "aorist": "ajāyi",
        "perfect": "jajau",
        "passive": "jāyīya",
        "causative": "jāpe",
        "past_participle": "jāta"
      },
      "prefixes": ["ā", "pra", "sam"],
      "generates_forms": 170,
      "generation_hints": {
        "related_to": "√jan",
        "primarily_passive": "jāyati common"
      }
    },

    "√vaḍḍh": {
      "meaning": "to grow, increase",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "vaḍḍha",
        "aorist": "avaḍḍhi",
        "perfect": "vavaḍḍha",
        "passive": "vaḍḍhīya",
        "causative": "vaḍḍhāpe",
        "past_participle": "vaḍḍhita"
      },
      "prefixes": ["ā", "vi", "sam"],
      "generates_forms": 180,
      "generation_hints": {
        "pali_specific": "distinctive Pali form"
      }
    },

    "√vṛdh": {
      "meaning": "to grow, prosper",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "vaddha",
        "aorist": "avardhi",
        "perfect": "vavardha",
        "passive": "vaddhīya",
        "causative": "vaddhāpe",
        "past_participle": "vaddha"
      },
      "prefixes": ["ā", "vi", "sam"],
      "generates_forms": 170,
      "generation_hints": {
        "related_to": "√vaḍḍh",
        "sanskrit_origin": "more archaic"
      }
    },

    "√hā": {
      "meaning": "to abandon, leave",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "jahā",
        "aorist": "ahāsi",
        "perfect": "jahau",
        "passive": "hīya",
        "causative": "hāpe",
        "past_participle": "hīna"
      },
      "prefixes": ["vi", "pari", "sam"],
      "generates_forms": 180,
      "generation_hints": {
        "irregular_present": "jahāti",
        "reduplication": "ja- prefix in present"
      }
    },

    "√tyaj": {
      "meaning": "to abandon, give up",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "cajja",
        "aorist": "atyaji",
        "perfect": "tatyāja",
        "passive": "cajjīya",
        "causative": "cajāpe",
        "past_participle": "cajita"
      },
      "prefixes": ["vi", "pari"],
      "generates_forms": 160,
      "generation_hints": {
        "pali_change": "ty > c in Pali"
      }
    },

    "√caj": {
      "meaning": "to give up, renounce",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "caja",
        "aorist": "acaji",
        "perfect": "cacāja",
        "passive": "cajjīya",
        "causative": "cajāpe",
        "past_participle": "cajita"
      },
      "prefixes": ["vi", "pari"],
      "generates_forms": 160,
      "generation_hints": {
        "related_to": "√tyaj",
        "pali_form": "simplified from tyaj"
      }
    },

    "√pac": {
      "meaning": "to cook, ripen",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "paca",
        "aorist": "apaci",
        "perfect": "papāca",
        "passive": "paccīya",
        "causative": "pācāpe",
        "past_participle": "pakka"
      },
      "prefixes": ["ā", "vi", "sam"],
      "generates_forms": 170,
      "generation_hints": {
        "irregular_participle": "pakka not *pacita"
      }
    },

    "√tap": {
      "meaning": "to heat, practice austerity",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "tapa",
        "aorist": "atapi",
        "perfect": "tatāpa",
        "passive": "tappīya",
        "causative": "tāpāpe",
        "past_participle": "tatta"
      },
      "prefixes": ["ā", "sam", "pari"],
      "generates_forms": 170,
      "generation_hints": {
        "dual_meaning": "physical heat or spiritual"
      }
    },

    "√dah": {
      "meaning": "to burn",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "daha",
        "aorist": "adahi",
        "perfect": "dadāha",
        "passive": "dayhīya",
        "causative": "dāhāpe",
        "past_participle": "daḍḍha"
      },
      "prefixes": ["ā", "vi", "sam"],
      "generates_forms": 170,
      "generation_hints": {
        "irregular_participle": "daḍḍha",
        "passive_variants": "dayh- forms"
      }
    },

    "√jal": {
      "meaning": "to burn, blaze",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "jala",
        "aorist": "ajali",
        "perfect": "jajāla",
        "passive": "jalīya",
        "causative": "jālāpe",
        "past_participle": "jalita"
      },
      "prefixes": ["ā", "vi", "pra"],
      "generates_forms": 160,
      "generation_hints": {
        "intransitive_focus": "usually intransitive"
      }
    },

    "√khād": {
      "meaning": "to eat, chew",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "khāda",
        "aorist": "akhādi",
        "perfect": "cakhāda",
        "passive": "khādīya",
        "causative": "khādāpe",
        "past_participle": "khādita"
      },
      "prefixes": ["ā", "vi", "sam"],
      "generates_forms": 160,
      "generation_hints": {
        "meaning_nuance": "chewing action emphasized"
      }
    },

    "√ad": {
      "meaning": "to eat",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "ada",
        "aorist": "ādāsi",
        "perfect": "ādāda",
        "passive": "adīya",
        "causative": "ādāpe",
        "past_participle": "anna"
      },
      "prefixes": ["ā", "pra", "sam"],
      "generates_forms": 150,
      "generation_hints": {
        "irregular_participle": "anna",
        "confusion_with": "avoid confusion with √dā"
      }
    },

    "√bhuñj": {
      "meaning": "to eat, enjoy",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "bhuñja",
        "aorist": "abhuñji",
        "perfect": "bubhoja",
        "passive": "bhuñjīya",
        "causative": "bhojāpe",
        "past_participle": "bhutta"
      },
      "prefixes": ["ā", "pari", "sam"],
      "generates_forms": 180,
      "generation_hints": {
        "dual_meaning": "eat or enjoy",
        "causative_change": "bhoj- not bhuñj-"
      }
    },

    "√pā": {
      "meaning": "to drink",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "piva",
        "aorist": "apāsi",
        "perfect": "papau",
        "passive": "pīya",
        "causative": "pāpe",
        "past_participle": "pīta"
      },
      "prefixes": ["ā", "pari", "sam"],
      "generates_forms": 170,
      "generation_hints": {
        "irregular_present": "pivati not *pāti",
        "irregular_passive": "pīyati"
      }
    },

    "√pib": {
      "meaning": "to drink",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "piba",
        "aorist": "apibi",
        "perfect": "pipiba",
        "passive": "pibīya",
        "causative": "pibāpe",
        "past_participle": "pīta"
      },
      "prefixes": ["ā", "pari"],
      "generates_forms": 150,
      "generation_hints": {
        "related_to": "√pā",
        "alternative_form": "less common variant"
      }
    },

    "√khip": {
      "meaning": "to throw, cast",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "khipa",
        "aorist": "akhipi",
        "perfect": "cikhipa",
        "passive": "khippīya",
        "causative": "khipāpe",
        "past_participle": "khitta"
      },
      "prefixes": ["ā", "ni", "pra", "vi", "sam"],
      "generates_forms": 180,
      "generation_hints": {
        "irregular_participle": "khitta"
      }
    },

    "√sic": {
      "meaning": "to sprinkle, pour",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "siñca",
        "aorist": "asiñci",
        "perfect": "sisiñca",
        "passive": "siñcīya",
        "causative": "secāpe",
        "past_participle": "sitta"
      },
      "prefixes": ["ā", "pari", "sam"],
      "generates_forms": 140,
      "generation_hints": {
        "present_nasal": "siñca not *sica",
        "causative_change": "sec- not sic-"
      }
    },

    "√vass": {
      "meaning": "to rain",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "vassa",
        "aorist": "avassi",
        "perfect": "vavassa",
        "passive": "vassīya",
        "causative": "vassāpe",
        "past_participle": "vuṭṭha"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 140,
      "generation_hints": {
        "weather_verb": "often impersonal",
        "irregular_participle": "vuṭṭha"
      }
    },

    "√vā": {
      "meaning": "to blow (wind)",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "vāya",
        "aorist": "avāyi",
        "perfect": "vavau",
        "passive": "vāyīya",
        "causative": "vāpe",
        "past_participle": "vāta"
      },
      "prefixes": ["ā", "pra", "vi"],
      "generates_forms": 140,
      "generation_hints": {
        "weather_verb": "wind blowing",
        "present_change": "vā > vāya"
      }
    },

    "√nad": {
      "meaning": "to roar, sound",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "nada",
        "aorist": "anadi",
        "perfect": "nanāda",
        "passive": "nadīya",
        "causative": "nādāpe",
        "past_participle": "nadita"
      },
      "prefixes": ["ā", "pra", "vi"],
      "generates_forms": 150,
      "generation_hints": {
        "sound_verb": "animal or natural sounds"
      }
    },

    "√gaj": {
      "meaning": "to roar, thunder",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "gaja",
        "aorist": "agaji",
        "perfect": "jagāja",
        "passive": "gajīya",
        "causative": "gajāpe",
        "past_participle": "gajita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 130,
      "generation_hints": {
        "elephant_roar": "specifically elephant sounds"
      }
    },

    "√gā": {
      "meaning": "to sing",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "gāya",
        "aorist": "agāyi",
        "perfect": "jagau",
        "passive": "gīya",
        "causative": "gāpe",
        "past_participle": "gīta"
      },
      "prefixes": ["ā", "pra", "sam"],
      "generates_forms": 160,
      "generation_hints": {
        "present_change": "gā > gāya",
        "irregular_passive": "gīyati"
      }
    },

    "√nac": {
      "meaning": "to dance",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "nacca",
        "aorist": "anacci",
        "perfect": "nanāca",
        "passive": "naccīya",
        "causative": "nācāpe",
        "past_participle": "nacca"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 130,
      "generation_hints": {
        "gemination": "nacc- forms"
      }
    },

    "√kīḷ": {
      "meaning": "to play, sport",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "kīḷa",
        "aorist": "akīḷi",
        "perfect": "cikīḷa",
        "passive": "kīḷīya",
        "causative": "kīḷāpe",
        "past_participle": "kīḷita"
      },
      "prefixes": ["ā", "vi", "sam"],
      "generates_forms": 150,
      "generation_hints": {
        "playful_activity": "games or sports"
      }
    },

 


    "√ram": {
      "meaning": "to delight, enjoy",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "rama",
        "aorist": "arami",
        "perfect": "rarāma",
        "passive": "ramīya",
        "causative": "ramāpe",
        "past_participle": "rata"
      },
      "prefixes": ["ā", "vi", "pari", "sam"],
      "generates_forms": 160,
      "generation_hints": {
        "intransitive_focus": "typically intransitive",
        "meaning_nuance": "pleasurable enjoyment"
      }
    },

    "√mod": {
      "meaning": "to rejoice",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "moda",
        "aorist": "amodi",
        "perfect": "mumoda",
        "passive": "modīya",
        "causative": "modāpe",
        "past_participle": "mudita"
      },
      "prefixes": ["ā", "pra", "sam"],
      "generates_forms": 150,
      "generation_hints": {
        "participle_change": "mudita not *modita",
        "emotional_state": "joy or gladness"
      }
    },

    "√hṛṣ": {
      "meaning": "to be glad, rejoice",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "haṃsa",
        "aorist": "ahṛṣi",
        "perfect": "harhṛṣa",
        "passive": "hṛṣīya",
        "causative": "harṣāpe",
        "past_participle": "hṛṣita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 130,
      "generation_hints": {
        "pali_adaptation": "ṛ > a in some forms",
        "archaic_usage": "mainly in compounds"
      }
    },

    "√tus": {
      "meaning": "to be satisfied, pleased",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "tussa",
        "aorist": "atuṣi",
        "perfect": "tutosa",
        "passive": "tussīya",
        "causative": "tosāpe",
        "past_participle": "tuṭṭha"
      },
      "prefixes": ["ā", "san", "pari"],
      "generates_forms": 150,
      "generation_hints": {
        "irregular_participle": "tuṭṭha",
        "causative_change": "tos- not tus-"
      }
    },

    "√rud": {
      "meaning": "to cry, weep",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "ruda",
        "aorist": "arudi",
        "perfect": "ruroda",
        "passive": "rudīya",
        "causative": "rodāpe",
        "past_participle": "rudita"
      },
      "prefixes": ["ā", "vi", "pari"],
      "generates_forms": 150,
      "generation_hints": {
        "causative_change": "rod- not rud-"
      }
    },

    "√kand": {
      "meaning": "to cry, lament",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "kanda",
        "aorist": "akandi",
        "perfect": "cakanda",
        "passive": "kandīya",
        "causative": "kandāpe",
        "past_participle": "kandita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 130,
      "generation_hints": {
        "sound_imitative": "crying sound basis"
      }
    },

    "√suc": {
      "meaning": "to grieve, mourn",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "soca",
        "aorist": "aśoci",
        "perfect": "śuśoca",
        "passive": "socīya",
        "causative": "socāpe",
        "past_participle": "sutta"
      },
      "prefixes": ["ā", "vi", "pari"],
      "generates_forms": 140,
      "generation_hints": {
        "present_change": "suc > soc",
        "irregular_participle": "sutta"
      }
    },

    "√bhī": {
      "meaning": "to fear",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "bhāya",
        "aorist": "abhāyi",
        "perfect": "bibhāya",
        "passive": "bhīya",
        "causative": "bhāyāpe",
        "past_participle": "bhīta"
      },
      "prefixes": ["ā", "vi", "sam"],
      "generates_forms": 150,
      "generation_hints": {
        "present_change": "bhī > bhāya",
        "intransitive_focus": "typically intransitive"
      }
    },

    "√tras": {
      "meaning": "to tremble, fear",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "tasa",
        "aorist": "atrāsi",
        "perfect": "tatrāsa",
        "passive": "tasīya",
        "causative": "trāsāpe",
        "past_participle": "trasta"
      },
      "prefixes": ["ā", "vi", "ut"],
      "generates_forms": 140,
      "generation_hints": {
        "pali_simplification": "tras > tas in present"
      }
    },

    "√kup": {
      "meaning": "to be angry",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "kuppa",
        "aorist": "akupi",
        "perfect": "cukopa",
        "passive": "kuppīya",
        "causative": "kopāpe",
        "past_participle": "kupita"
      },
      "prefixes": ["ā", "pra", "sam"],
      "generates_forms": 150,
      "generation_hints": {
        "gemination": "kupp- forms",
        "causative_change": "kop- not kup-"
      }
    },

    "√krudh": {
      "meaning": "to be angry",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "kujjha",
        "aorist": "akrudhi",
        "perfect": "cukrodha",
        "passive": "kujjhīya",
        "causative": "kodhāpe",
        "past_participle": "kuddha"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 130,
      "generation_hints": {
        "pali_change": "krudh > kujjh",
        "irregular_participle": "kuddha"
      }
    },

    "√dus": {
      "meaning": "to hate",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "dosa",
        "aorist": "adoṣi",
        "perfect": "dudosa",
        "passive": "dusīya",
        "causative": "dosāpe",
        "past_participle": "duṭṭha"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "present_change": "dus > dos",
        "irregular_participle": "duṭṭha"
      }
    },

    "√īrs": {
      "meaning": "to envy",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "issa",
        "aorist": "airṣi",
        "perfect": "īrṣa",
        "passive": "issīya",
        "causative": "issāpe",
        "past_participle": "issita"
      },
      "prefixes": ["ā"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_adaptation": "īrs > iss",
        "rare_usage": "mainly in compounds"
      }
    },

    "√lubh": {
      "meaning": "to covet, be greedy",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "lubha",
        "aorist": "alubhi",
        "perfect": "lulubha",
        "passive": "lubhīya",
        "causative": "lobhāpe",
        "past_participle": "luddha"
      },
      "prefixes": ["ā", "vi", "pari"],
      "generates_forms": 140,
      "generation_hints": {
        "irregular_participle": "luddha",
        "causative_change": "lobh- not lubh-"
      }
    },

    "√icch": {
      "meaning": "to wish, desire",
      "type": "primary",
      "frequency": "very_high",
      "stems": {
        "present": "iccha",
        "aorist": "aicci",
        "perfect": "īccha",
        "passive": "icchīya",
        "causative": "icchāpe",
        "past_participle": "iṭṭha"
      },
      "prefixes": ["ā", "abhi", "pati"],
      "generates_forms": 180,
      "generation_hints": {
        "irregular_participle": "iṭṭha not *icchita",
        "high_frequency": "very common verb"
      }
    },

    "√es": {
      "meaning": "to seek, search",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "iccha",
        "aorist": "aisi",
        "perfect": "īṣa",
        "passive": "esīya",
        "causative": "esāpe",
        "past_participle": "esita"
      },
      "prefixes": ["ā", "vi", "pari"],
      "generates_forms": 140,
      "generation_hints": {
        "confusion_with": "√icch forms overlap"
      }
    },

    "√gav": {
      "meaning": "to seek, search for",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "gava",
        "aorist": "agavi",
        "perfect": "jagāva",
        "passive": "gavīya",
        "causative": "gavāpe",
        "past_participle": "gavita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "archaic_usage": "rare in canonical texts"
      }
    },

    "√pucch": {
      "meaning": "to ask, question",
      "type": "primary",
      "frequency": "very_high",
      "stems": {
        "present": "puccha",
        "aorist": "apucchi",
        "perfect": "pupuccha",
        "passive": "pucchīya",
        "causative": "pucchāpe",
        "past_participle": "puṭṭha"
      },
      "prefixes": ["ā", "vi", "pari", "upa"],
      "generates_forms": 200,
      "generation_hints": {
        "irregular_participle": "puṭṭha not *pucchita",
        "high_frequency": "very common in dialogues"
      }
    },

    "√prach": {
      "meaning": "to ask, inquire",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "puccha",
        "aorist": "aprāṣi",
        "perfect": "paprācha",
        "passive": "pucchīya",
        "causative": "pucchāpe",
        "past_participle": "puṭṭha"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_merger": "merges with √pucch forms"
      }
    },

    "√ñā": {
      "meaning": "to know",
      "type": "primary",
      "frequency": "very_high",
      "stems": {
        "present": "jānā",
        "aorist": "aññāsi",
        "perfect": "jajñau",
        "passive": "ñāyīya",
        "causative": "ñāpe",
        "past_participle": "ñāta"
      },
      "prefixes": ["ā", "vi", "pari", "sam", "anu"],
      "generates_forms": 220,
      "generation_hints": {
        "irregular_present": "jānāti not *ñāti",
        "aorist_variants": ["aññāsi", "aññāṇi"]
      }
    },

    "√jān": {
      "meaning": "to know, understand",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "jāna",
        "aorist": "ajāni",
        "perfect": "jajāna",
        "passive": "jānīya",
        "causative": "jānāpe",
        "past_participle": "jāta"
      },
      "prefixes": ["ā", "vi", "pari"],
      "generates_forms": 170,
      "generation_hints": {
        "related_to": "√ñā",
        "participle_confusion": "jāta can mean born or known"
      }
    },

    "√budh": {
      "meaning": "to awaken, understand",
      "type": "primary",
      "frequency": "very_high",
      "stems": {
        "present": "bujjha",
        "aorist": "abujjhi",
        "perfect": "bubodha",
        "passive": "bujjhīya",
        "causative": "bodhāpe",
        "past_participle": "buddha"
      },
      "prefixes": ["ā", "vi", "prati", "sam", "anu"],
      "generates_forms": 240,
      "generation_hints": {
        "pali_change": "budh > bujjh",
        "religious_significance": "enlightenment term",
        "causative_change": "bodh- not budh-"
      }
    },

    "√vid": {
      "meaning": "to know, find",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "vinda",
        "aorist": "avidi",
        "perfect": "viveda",
        "passive": "vijjīya",
        "causative": "vedāpe",
        "past_participle": "vidita"
      },
      "prefixes": ["ā", "upa", "pari", "sam"],
      "generates_forms": 190,
      "generation_hints": {
        "present_nasal": "vinda not *vida",
        "passive_change": "vijj- forms"
      }
    },

    "√ved": {
      "meaning": "to feel, experience",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "veda",
        "aorist": "avedi",
        "perfect": "viveda",
        "passive": "vedīya",
        "causative": "vedāpe",
        "past_participle": "vedita"
      },
      "prefixes": ["ā", "anu", "prati", "sam"],
      "generates_forms": 180,
      "generation_hints": {
        "experiential_focus": "feeling or experiencing"
      }
    },

    "√cit": {
      "meaning": "to think, be conscious",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "ceta",
        "aorist": "aceti",
        "perfect": "ciceta",
        "passive": "cetīya",
        "causative": "cetāpe",
        "past_participle": "cinta"
      },
      "prefixes": ["ā", "vi", "sam", "anu"],
      "generates_forms": 170,
      "generation_hints": {
        "consciousness_root": "fundamental awareness",
        "irregular_participle": "cinta"
      }
    },

    "√cint": {
      "meaning": "to think, reflect",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "cinta",
        "aorist": "acinti",
        "perfect": "cicinta",
        "passive": "cintīya",
        "causative": "cintāpe",
        "past_participle": "cinta"
      },
      "prefixes": ["ā", "vi", "pari", "sam"],
      "generates_forms": 180,
      "generation_hints": {
        "deliberate_thinking": "conscious reflection"
      }
    },

    "√man": {
      "meaning": "to think, consider",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "mañña",
        "aorist": "amanni",
        "perfect": "mamana",
        "passive": "maññīya",
        "causative": "mānāpe",
        "past_participle": "mata"
      },
      "prefixes": ["ā", "anu", "pari", "sam"],
      "generates_forms": 180,
      "generation_hints": {
        "present_palatalization": "man > mañña",
        "opinion_forming": "believing or supposing"
      }
    },

    "√smṛ": {
      "meaning": "to remember",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "sara",
        "aorist": "asari",
        "perfect": "sasāra",
        "passive": "sarīya",
        "causative": "sārāpe",
        "past_participle": "sata"
      },
      "prefixes": ["ā", "anu", "prati", "sam"],
      "generates_forms": 170,
      "generation_hints": {
        "pali_change": "smṛ > sar",
        "memory_focus": "recollection"
      }
    },

    "√sar": {
      "meaning": "to remember, recollect",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "sara",
        "aorist": "asari",
        "perfect": "sasāra",
        "passive": "sarīya",
        "causative": "sārāpe",
        "past_participle": "sata"
      },
      "prefixes": ["ā", "anu", "prati"],
      "generates_forms": 160,
      "generation_hints": {
        "related_to": "√smṛ"
      }
    },

    "√mṛṣ": {
      "meaning": "to forget",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "mussa",
        "aorist": "amṛṣi",
        "perfect": "mamṛṣa",
        "passive": "mussīya",
        "causative": "mussāpe",
        "past_participle": "muṭṭha"
      },
      "prefixes": ["vi", "sam"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_change": "mṛṣ > muss",
        "irregular_participle": "muṭṭha"
      }
    },

    "√muh": {
      "meaning": "to be confused, deluded",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "muha",
        "aorist": "amuhi",
        "perfect": "mumuha",
        "passive": "muhīya",
        "causative": "mohāpe",
        "past_participle": "mūḷha"
      },
      "prefixes": ["ā", "vi", "sam"],
      "generates_forms": 150,
      "generation_hints": {
        "irregular_participle": "mūḷha",
        "causative_change": "moh- not muh-"
      }
    },

    "√bhram": {
      "meaning": "to wander, be confused",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "bhama",
        "aorist": "abhrami",
        "perfect": "babhrāma",
        "passive": "bhamīya",
        "causative": "bhamāpe",
        "past_participle": "bhanta"
      },
      "prefixes": ["ā", "vi", "pari"],
      "generates_forms": 150,
      "generation_hints": {
        "pali_simplification": "bhram > bham",
        "dual_meaning": "physical wandering or mental confusion"
      }
    },

    "√śak": {
      "meaning": "to be able, capable",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "sakka",
        "aorist": "aśaki",
        "perfect": "śaśāka",
        "passive": "sakkīya",
        "causative": "sakkāpe",
        "past_participle": "sakka"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 160,
      "generation_hints": {
        "ability_verb": "capability or power",
        "gemination": "sakk- forms"
      }
    },

    "√arh": {
      "meaning": "to deserve, be worthy",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "araha",
        "aorist": "ārahi",
        "perfect": "āraha",
        "passive": "arahīya",
        "causative": "arahāpe",
        "past_participle": "arahanta"
      },
      "prefixes": ["ā"],
      "generates_forms": 140,
      "generation_hints": {
        "religious_significance": "worthy, deserving respect",
        "participle_form": "arahanta special form"
      }
    },

    "√yat": {
      "meaning": "to strive, exert",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "yata",
        "aorist": "ayati",
        "perfect": "yayata",
        "passive": "yatīya",
        "causative": "yatāpe",
        "past_participle": "yata"
      },
      "prefixes": ["ā", "pra", "vi"],
      "generates_forms": 150,
      "generation_hints": {
        "effort_verb": "deliberate effort"
      }
    },

    "√yam": {
      "meaning": "to restrain, control",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "yaccha",
        "aorist": "ayami",
        "perfect": "yayāma",
        "passive": "yaccīya",
        "causative": "yamāpe",
        "past_participle": "yanta"
      },
      "prefixes": ["ā", "ni", "sam"],
      "generates_forms": 150,
      "generation_hints": {
        "present_change": "yam > yacch",
        "restraint_focus": "self-control"
      }
    },

    "√dam": {
      "meaning": "to tame, subdue",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "dama",
        "aorist": "adami",
        "perfect": "dadāma",
        "passive": "damīya",
        "causative": "damāpe",
        "past_participle": "danta"
      },
      "prefixes": ["ā", "vi", "sam"],
      "generates_forms": 150,
      "generation_hints": {
        "irregular_participle": "danta not *damita"
      }
    },

    "√śam": {
      "meaning": "to be calm, peaceful",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "sama",
        "aorist": "aśami",
        "perfect": "śaśāma",
        "passive": "samīya",
        "causative": "samāpe",
        "past_participle": "santa"
      },
      "prefixes": ["ā", "upa", "sam"],
      "generates_forms": 150,
      "generation_hints": {
        "irregular_participle": "santa",
        "peace_focus": "tranquility"
      }
    },

    "√kṣam": {
      "meaning": "to be patient, forgive",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "khama",
        "aorist": "akṣami",
        "perfect": "cakṣāma",
        "passive": "khamīya",
        "causative": "khamāpe",
        "past_participle": "khanta"
      },
      "prefixes": ["ā", "upa"],
      "generates_forms": 140,
      "generation_hints": {
        "pali_change": "kṣ > kh",
        "patience_virtue": "forbearance"
      }
    },

    "√sah": {
      "meaning": "to endure, bear",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "saha",
        "aorist": "asahi",
        "perfect": "sasāha",
        "passive": "sahīya",
        "causative": "sahāpe",
        "past_participle": "soḷha"
      },
      "prefixes": ["ā", "anu", "abhi"],
      "generates_forms": 150,
      "generation_hints": {
        "irregular_participle": "soḷha",
        "endurance_focus": "bearing hardship"
      }
    },

    "√rakṣ": {
      "meaning": "to protect, guard",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "rakka",
        "aorist": "arakṣi",
        "perfect": "rarakṣa",
        "passive": "rakkhīya",
        "causative": "rakkhāpe",
        "past_participle": "rakkhita"
      },
      "prefixes": ["ā", "pari", "sam"],
      "generates_forms": 170,
      "generation_hints": {
        "pali_change": "kṣ > kkh",
        "protection_verb": "guarding or defending"
      }
    },

    "√pā": {
      "meaning": "to protect, watch over",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "pāla",
        "aorist": "apāsi",
        "perfect": "papau",
        "passive": "pālīya",
        "causative": "pālāpe",
        "past_participle": "pālita"
      },
      "prefixes": ["ā", "anu", "pari"],
      "generates_forms": 150,
      "generation_hints": {
        "present_suffix": "pāl- extended form",
        "care_focus": "nurturing protection"
      }
    },

    "√tṛ": {
      "meaning": "to cross over",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "tara",
        "aorist": "atāri",
        "perfect": "tatāra",
        "passive": "tarīya",
        "causative": "tārāpe",
        "past_participle": "tinna"
      },
      "prefixes": ["ā", "ut", "pari"],
      "generates_forms": 150,
      "generation_hints": {
        "crossing_metaphor": "overcoming obstacles",
        "irregular_participle": "tinna"
      }
    },

    "√tar": {
      "meaning": "to cross, overcome",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "tara",
        "aorist": "atari",
        "perfect": "tatāra",
        "passive": "tarīya",
        "causative": "tārāpe",
        "past_participle": "tinna"
      },
      "prefixes": ["ā", "ut", "pari"],
      "generates_forms": 150,
      "generation_hints": {
        "related_to": "√tṛ"
      }
    },

    "√plu": {
      "meaning": "to float, swim",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "plava",
        "aorist": "aplavi",
        "perfect": "puplāva",
        "passive": "plavīya",
        "causative": "plavāpe",
        "past_participle": "pluta"
      },
      "prefixes": ["ā", "ut"],
      "generates_forms": 130,
      "generation_hints": {
        "water_movement": "floating or swimming"
      }
    },

    "√snā": {
      "meaning": "to bathe",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "naha",
        "aorist": "asnāsi",
        "perfect": "sasnau",
        "passive": "nahīya",
        "causative": "nahāpe",
        "past_participle": "nahāta"
      },
      "prefixes": ["ā", "ava"],
      "generates_forms": 140,
      "generation_hints": {
        "pali_change": "sn > nh",
        "ritual_significance": "purification"
      }
    },

    "√dhāv": {
      "meaning": "to wash, cleanse",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "dhova",
        "aorist": "adhāvi",
        "perfect": "dadhāva",
        "passive": "dhovīya",
        "causative": "dhavāpe",
        "past_participle": "dhota"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 140,
      "generation_hints": {
        "present_change": "dhāv > dhov"
      }
    },

    "√kṣāl": {
      "meaning": "to wash, rinse",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "khāla",
        "aorist": "akṣāli",
        "perfect": "cakṣāla",
        "passive": "khālīya",
        "causative": "khālāpe",
        "past_participle": "khālita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_change": "kṣ > kh"
      }
    },

    "√śudh": {
      "meaning": "to purify, be clean",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "sujjha",
        "aorist": "aśudhi",
        "perfect": "śuśodha",
        "passive": "sujjhīya",
        "causative": "sodhāpe",
        "past_participle": "suddha"
      },
      "prefixes": ["ā", "vi", "sam"],
      "generates_forms": 160,
      "generation_hints": {
        "pali_change": "śudh > sujjh",
        "purification_focus": "spiritual cleansing",
        "causative_change": "sodh- not śudh-"
      }
    },

    "√mṛj": {
      "meaning": "to wipe, clean",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "majja",
        "aorist": "amṛji",
        "perfect": "mamṛja",
        "passive": "majjīya",
        "causative": "majjāpe",
        "past_participle": "maṭṭa"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_change": "mṛj > majj",
        "irregular_participle": "maṭṭa"
      }
    },

    "√lip": {
      "meaning": "to smear, anoint",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "limpa",
        "aorist": "alipi",
        "perfect": "lilipa",
        "passive": "limpīya",
        "causative": "lepāpe",
        "past_participle": "litta"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "present_nasal": "limpa not *lipa",
        "causative_change": "lep- not lip-"
      }
    },

    "√añj": {
      "meaning": "to anoint, smear",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "añja",
        "aorist": "āñji",
        "perfect": "ānañja",
        "passive": "añjīya",
        "causative": "añjāpe",
        "past_participle": "atta"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "irregular_participle": "atta"
      }
    },

    "√rañj": {
      "meaning": "to dye, color",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "rañja",
        "aorist": "arañji",
        "perfect": "rarañja",
        "passive": "rañjīya",
        "causative": "rañjāpe",
        "past_participle": "ratta"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "irregular_participle": "ratta"
      }
    },

    "√siv": {
      "meaning": "to sew, stitch",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "siva",
        "aorist": "asivi",
        "perfect": "siseva",
        "passive": "sivīya",
        "causative": "sivāpe",
        "past_participle": "sivita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 110,
      "generation_hints": {
        "craft_verb": "textile work"
      }
    },

    "√vay": {
      "meaning": "to weave",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "vaya",
        "aorist": "avayi",
        "perfect": "vavāya",
        "passive": "vayīya",
        "causative": "vayāpe",
        "past_participle": "vuta"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 110,
      "generation_hints": {
        "irregular_participle": "vuta"
      }
    },

    "√tan": {
      "meaning": "to stretch, extend",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "tana",
        "aorist": "atani",
        "perfect": "tatāna",
        "passive": "tanīya",
        "causative": "tanāpe",
        "past_participle": "tata"
      },
      "prefixes": ["ā", "vi", "pra", "sam"],
      "generates_forms": 150,
      "generation_hints": {
        "extension_verb": "physical or temporal extension"
      }
    },

    "√likh": {
      "meaning": "to write, scratch",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "likha",
        "aorist": "alikhi",
        "perfect": "lilikha",
        "passive": "likhīya",
        "causative": "lekhāpe",
        "past_participle": "likhita"
      },
      "prefixes": ["ā", "upa"],
      "generates_forms": 140,
      "generation_hints": {
        "causative_change": "lekh- not likh-"
      }
    },

    "√gaṇ": {
      "meaning": "to count, calculate",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "gaṇa",
        "aorist": "agaṇi",
        "perfect": "jagaṇa",
        "passive": "gaṇīya",
        "causative": "gaṇāpe",
        "past_participle": "gaṇita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 140,
      "generation_hints": {
        "mathematical_focus": "enumeration"
      }
    },

    "√saṅkh": {
      "meaning": "to count, reckon",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "saṅkha",
        "aorist": "asaṅkhi",
        "perfect": "sasaṅkha",
        "passive": "saṅkhīya",
        "causative": "saṅkhāpe",
        "past_participle": "saṅkhāta"
      },
      "prefixes": ["ā", "pari"],
      "generates_forms": 120,
      "generation_hints": {
        "calculation_focus": "numerical reasoning"
      }
    },

    "√mā": {
      "meaning": "to measure",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "mina",
        "aorist": "amāsi",
        "perfect": "mamau",
        "passive": "mīya",
        "causative": "māpe",
        "past_participle": "mita"
      },
      "prefixes": ["ā", "pari", "sam"],
      "generates_forms": 140,
      "generation_hints": {
        "present_nasal": "mina not *māya",
        "irregular_passive": "mīyati"
      }
    },

    "√tul": {
      "meaning": "to weigh, compare",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "tola",
        "aorist": "atuli",
        "perfect": "tutola",
        "passive": "tolīya",
        "causative": "tolāpe",
        "past_participle": "tulita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 120,
      "generation_hints": {
        "present_change": "tul > tol"
      }
    },

    "√cal": {
      "meaning": "to move, shake",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "cala",
        "aorist": "acali",
        "perfect": "cacāla",
        "passive": "calīya",
        "causative": "calāpe",
        "past_participle": "calita"
      },
      "prefixes": ["ā", "pra", "vi"],
      "generates_forms": 140,
      "generation_hints": {
        "movement_verb": "oscillation or motion"
      }
    },

    "√kamp": {
      "meaning": "to tremble, shake",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "kampa",
        "aorist": "akampi",
        "perfect": "cakampa",
        "passive": "kampīya",
        "causative": "kampāpe",
        "past_participle": "kampita"
      },
      "prefixes": ["ā", "pra", "vi"],
      "generates_forms": 140,
      "generation_hints": {
        "trembling_focus": "fear or cold trembling"
      }
    },

    "√vep": {
      "meaning": "to tremble, quiver",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "vepa",
        "aorist": "avepi",
        "perfect": "vivepa",
        "passive": "vepīya",
        "causative": "vepāpe",
        "past_participle": "vepita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "subtle_trembling": "slight quivering"
      }
    },

    "√spand": {
      "meaning": "to throb, quiver",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "panda",
        "aorist": "aspandi",
        "perfect": "paspanda",
        "passive": "pandīya",
        "causative": "pandāpe",
        "past_participle": "pandita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_change": "sp > p initially"
      }
    },

    "√sphur": {
      "meaning": "to throb, vibrate",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "phura",
        "aorist": "asphuri",
        "perfect": "pusphura",
        "passive": "phurīya",
        "causative": "phurāpe",
        "past_participle": "phurita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_change": "sph > ph"
      }
    },

    "√syand": {
      "meaning": "to flow, ooze",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "sanda",
        "aorist": "asyandi",
        "perfect": "sasyanda",
        "passive": "sandīya",
        "causative": "sandāpe",
        "past_participle": "sanna"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_change": "sy > s",
        "irregular_participle": "sanna"
      }
    },

    "√sru": {
      "meaning": "to flow, stream",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "sava",
        "aorist": "asravi",
        "perfect": "susrāva",
        "passive": "savīya",
        "causative": "savāpe",
        "past_participle": "suta"
      },
      "prefixes": ["ā", "pra", "ni"],
      "generates_forms": 140,
      "generation_hints": {
        "present_change": "sru > sav",
        "irregular_participle": "suta"
      }
    },

    "√kṣar": {
      "meaning": "to flow, drip",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "khara",
        "aorist": "akṣari",
        "perfect": "cakṣāra",
        "passive": "kharīya",
        "causative": "kharāpe",
        "past_participle": "kharita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_change": "kṣ > kh"
      }
    },

    "√dru": {
      "meaning": "to run, flow",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "dhāva",
        "aorist": "adravi",
        "perfect": "dudrāva",
        "passive": "dhāvīya",
        "causative": "dhāvāpe",
        "past_participle": "dhāvita"
      },
      "prefixes": ["ā", "pra", "sam"],
      "generates_forms": 140,
      "generation_hints": {
        "present_change": "dru > dhāv in some forms",
        "running_focus": "rapid movement"
      }
    },

    "√pat": {
      "meaning": "to fall, fly",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "pata",
        "aorist": "apati",
        "perfect": "papāta",
        "passive": "patīya",
        "causative": "pātāpe",
        "past_participle": "patita"
      },
      "prefixes": ["ā", "upa", "ni", "vi", "sam"],
      "generates_forms": 180,
      "generation_hints": {
        "dual_meaning": "falling or flying"
      }
    },

    "√pad": {
      "meaning": "to fall, go",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "pajja",
        "aorist": "apadi",
        "perfect": "papāda",
        "passive": "pajjīya",
        "causative": "pādāpe",
        "past_participle": "panna"
      },
      "prefixes": ["ā", "upa", "ni"],
      "generates_forms": 150,
      "generation_hints": {
        "present_change": "pad > pajj",
        "irregular_participle": "panna"
      }
    },

    "√as": {
      "meaning": "to throw, cast",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "asa",
        "aorist": "āsi",
        "perfect": "āsa",
        "passive": "asīya",
        "causative": "āsāpe",
        "past_participle": "asta"
      },
      "prefixes": ["ni", "vi"],
      "generates_forms": 110,
      "generation_hints": {
        "confusion_with": "√as 'to be' - different root"
      }
    },

    "√iṣ": {
      "meaning": "to send, impel",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "iccha",
        "aorist": "aiṣi",
        "perfect": "īṣa",
        "passive": "icchīya",
        "causative": "icchāpe",
        "past_participle": "iṭṭha"
      },
      "prefixes": ["pra", "ava"],
      "generates_forms": 110,
      "generation_hints": {
        "confusion_with": "√icch 'to wish' - similar forms"
      }
    },

    "√preṣ": {
      "meaning": "to send forth",
      "type": "compound",
      "frequency": "low",
      "stems": {
        "present": "pesa",
        "aorist": "apresi",
        "perfect": "papresa",
        "passive": "pesīya",
        "causative": "pesāpe",
        "past_participle": "pesita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 110,
      "generation_hints": {
        "compound_origin": "pra + √iṣ",
        "pali_simplification": "pres > pes"
      }
    },

    "√diś": {
      "meaning": "to show, point",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "disa",
        "aorist": "adisi",
        "perfect": "didesa",
        "passive": "disīya",
        "causative": "desāpe",
        "past_participle": "diṭṭha"
      },
      "prefixes": ["ā", "upa", "ni"],
      "generates_forms": 140,
      "generation_hints": {
        "irregular_participle": "diṭṭha",
        "causative_change": "des- not dis-"
      }
    },

    "√darś": {
      "meaning": "to see, show",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "dassa",
        "aorist": "adarśi",
        "perfect": "dadarśa",
        "passive": "dassīya",
        "causative": "dassāpe",
        "past_participle": "diṭṭha"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 140,
      "generation_hints": {
        "pali_change": "darś > dass",
        "shared_participle": "diṭṭha with √diś"
      }
    },

    "√dṛś": {
      "meaning": "to see",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "passa",
        "aorist": "addasa",
        "perfect": "dadassa",
        "passive": "dassīya",
        "causative": "dassāpe",
        "past_participle": "diṭṭha"
      },
      "prefixes": ["ā", "pra", "anu", "vi"],
      "generates_forms": 180,
      "generation_hints": {
        "pali_change": "dṛś > pass",
        "aorist_special": "addasa special form"
      }
    },

    "√paś": {
      "meaning": "to see, look",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "passa",
        "aorist": "apassi",
        "perfect": "papaśa",
        "passive": "passīya",
        "causative": "passāpe",
        "past_participle": "passa"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 140,
      "generation_hints": {
        "merged_with": "√dṛś in Pali"
      }
    },

    "√lok": {
      "meaning": "to look, see",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "loka",
        "aorist": "aloki",
        "perfect": "luloka",
        "passive": "lokīya",
        "causative": "lokāpe",
        "past_participle": "lokita"
      },
      "prefixes": ["ā", "ava", "vi"],
      "generates_forms": 140,
      "generation_hints": {
        "looking_focus": "deliberate observation"
      }
    },

    "√īkṣ": {
      "meaning": "to see, look",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "ikka",
        "aorist": "aikṣi",
        "perfect": "īkṣa",
        "passive": "ikkīya",
        "causative": "ikkāpe",
        "past_participle": "iṭṭha"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_change": "īkṣ > ikk"
      }
    },

    "√prekṣ": {
      "meaning": "to look at, behold",
      "type": "compound",
      "frequency": "low",
      "stems": {
        "present": "pekka",
        "aorist": "aprekṣi",
        "perfect": "paprekṣa",
        "passive": "pekkīya",
        "causative": "pekkāpe",
        "past_participle": "pekkha"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 110,
      "generation_hints": {
        "compound_origin": "pra + √īkṣ",
        "pali_simplification": "prekṣ > pekk"
      }
    },

    "√śru": {
      "meaning": "to hear",
      "type": "primary",
      "frequency": "very_high",
      "stems": {
        "present": "suṇa",
        "aorist": "assosi",
        "perfect": "suśrāva",
        "passive": "suyīya",
        "causative": "sāve",
        "past_participle": "suta"
      },
      "prefixes": ["ā", "anu", "pari", "sam"],
      "generates_forms": 200,
      "generation_hints": {
        "pali_change": "śru > suṇ in present",
        "irregular_passive": "suyīyati",
        "aorist_special": "assosi"
      }
    },

    "√su": {
      "meaning": "to hear, listen",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "sava",
        "aorist": "asavi",
        "perfect": "susāva",
        "passive": "savīya",
        "causative": "savāpe",
        "past_participle": "suta"
      },
      "prefixes": ["ā", "anu"],
      "generates_forms": 140,
      "generation_hints": {
        "related_to": "√śru"
      }
    },

    "√ghrā": {
      "meaning": "to smell",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "jigha",
        "aorist": "aghrāsi",
        "perfect": "jaghrau",
        "passive": "jighīya",
        "causative": "ghāpe",
        "past_participle": "ghāta"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_change": "ghr > jigh",
        "present_reduplicated": "jighati"
      }
    },

    "√ras": {
      "meaning": "to taste, enjoy",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "rasa",
        "aorist": "arasi",
        "perfect": "rarāsa",
        "passive": "rasīya",
        "causative": "rasāpe",
        "past_participle": "rasita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 140,
      "generation_hints": {
        "dual_meaning": "physical taste or aesthetic enjoyment"
      }
    },

    "√svād": {
      "meaning": "to taste, relish",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "sāda",
        "aorist": "asvādi",
        "perfect": "sasvāda",
        "passive": "sādīya",
        "causative": "sādāpe",
        "past_participle": "svādita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 120,
      "generation_hints": {
        "present_change": "svād > sād"
      }
    },

    "√spṛś": {
      "meaning": "to touch",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "phusa",
        "aorist": "aspṛśi",
        "perfect": "pasparśa",
        "passive": "phusīya",
        "causative": "phusāpe",
        "past_participle": "phuṭṭha"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 140,
      "generation_hints": {
        "pali_change": "spṛś > phus",
        "irregular_participle": "phuṭṭha"
      }
    },

    "√phuṣ": {
      "meaning": "to touch, contact",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "phuṣa",
        "aorist": "aphuṣi",
        "perfect": "puphuṣa",
        "passive": "phuṣīya",
        "causative": "phuṣāpe",
        "past_participle": "phuṭṭha"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 120,
      "generation_hints": {
        "related_to": "√spṛś"
      }
    },

    "√gṛh": {
      "meaning": "to grasp, seize",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "gaṇhā",
        "aorist": "agahesi",
        "perfect": "jagṛha",
        "passive": "gahīya",
        "causative": "gāhāpe",
        "past_participle": "gahita"
      },
      "prefixes": ["ā", "upa", "pari", "sam"],
      "generates_forms": 180,
      "generation_hints": {
        "pali_change": "gṛh > gaṇh",
        "nasal_insertion": "gaṇhāti"
      }
    },

    "√grabh": {
      "meaning": "to grasp, take",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "gabbha",
        "aorist": "agrabhi",
        "perfect": "jagrabha",
        "passive": "gabbhīya",
        "causative": "gabbhāpe",
        "past_participle": "gahita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 140,
      "generation_hints": {
        "pali_change": "grabh > gabbh",
        "shared_participle": "gahita with √gṛh"
      }
    },

    "√muṣ": {
      "meaning": "to steal, rob",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "musa",
        "aorist": "amuṣi",
        "perfect": "mumuṣa",
        "passive": "musīya",
        "causative": "mosāpe",
        "past_participle": "mūsita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "causative_change": "mos- not muṣ-"
      }
    },

    "√cur": {
      "meaning": "to steal",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "cora",
        "aorist": "acuri",
        "perfect": "cucora",
        "passive": "corīya",
        "causative": "corāpe",
        "past_participle": "corita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "present_change": "cur > cor"
      }
    },

    "√hṛ": {
      "meaning": "to take away, steal",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "hara",
        "aorist": "ahāri",
        "perfect": "jahāra",
        "passive": "harīya",
        "causative": "hārāpe",
        "past_participle": "haṭa"
      },
      "prefixes": ["ā", "upa", "pra", "vi"],
      "generates_forms": 160,
      "generation_hints": {
        "related_to": "√har but different meaning",
        "theft_context": "taking unlawfully"
      }
    },

    "√nud": {
      "meaning": "to push, drive",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "nuda",
        "aorist": "anudi",
        "perfect": "nunoda",
        "passive": "nudīya",
        "causative": "nodāpe",
        "past_participle": "nutta"
      },
      "prefixes": ["ā", "vi", "pra"],
      "generates_forms": 130,
      "generation_hints": {
        "causative_change": "nod- not nud-",
        "irregular_participle": "nutta"
      }
    },

    "√tud": {
      "meaning": "to push, strike",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "tuda",
        "aorist": "atudi",
        "perfect": "tutoda",
        "passive": "tudīya",
        "causative": "todāpe",
        "past_participle": "tunna"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 120,
      "generation_hints": {
        "causative_change": "tod- not tud-",
        "irregular_participle": "tunna"
      }
    },

    "√ṛ": {
      "meaning": "to go, move",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "iyya",
        "aorist": "āri",
        "perfect": "ārāya",
        "passive": "īrīya",
        "causative": "īrāpe",
        "past_participle": "īrita"
      },
      "prefixes": ["ā", "upa"],
      "generates_forms": 110,
      "generation_hints": {
        "archaic_root": "very rare usage",
        "pali_adaptation": "ṛ > iy/īr"
      }
    },

    "√ṛcch": {
      "meaning": "to go, reach",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "iccha",
        "aorist": "ārcchi",
        "perfect": "ārcha",
        "passive": "icchīya",
        "causative": "icchāpe",
        "past_participle": "icchita"
      },
      "prefixes": ["ā"],
      "generates_forms": 100,
      "generation_hints": {
        "confusion_with": "√icch 'to wish' - homophonous",
        "rare_usage": "mainly archaic"
      }
    },

    "√āp": {
      "meaning": "to reach, obtain",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "appa",
        "aorist": "āpi",
        "perfect": "āpa",
        "passive": "appīya",
        "causative": "āpāpe",
        "past_participle": "atta"
      },
      "prefixes": ["pra", "sam", "vi"],
      "generates_forms": 160,
      "generation_hints": {
        "gemination": "app- forms",
        "irregular_participle": "atta"
      }
    },

    "√prāp": {
      "meaning": "to reach, attain",
      "type": "compound",
      "frequency": "medium",
      "stems": {
        "present": "pappa",
        "aorist": "aprāpi",
        "perfect": "paprāpa",
        "passive": "pappīya",
        "causative": "pappāpe",
        "past_participle": "patta"
      },
      "prefixes": ["sam", "vi"],
      "generates_forms": 140,
      "generation_hints": {
        "compound_origin": "pra + √āp",
        "pali_simplification": "prāp > papp"
      }
    },

    "√i": {
      "meaning": "to go",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "eti",
        "aorist": "agā",
        "perfect": "iyāya",
        "passive": "īyīya",
        "causative": "āyāpe",
        "past_participle": "ita"
      },
      "prefixes": ["ā", "upa", "adhi", "abhi"],
      "generates_forms": 170,
      "generation_hints": {
        "irregular_present": "eti not *iyati",
        "suppletive_aorist": "agā from √gam"
      }
    },

    "√e": {
      "meaning": "to come, approach",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "eti",
        "aorist": "ayi",
        "perfect": "ayayau",
        "passive": "īyīya",
        "causative": "āyāpe",
        "past_participle": "āyāta"
      },
      "prefixes": ["ā", "upa"],
      "generates_forms": 140,
      "generation_hints": {
        "merged_with": "√i in many forms"
      }
    },

    "√āgam": {
      "meaning": "to come, arrive",
      "type": "compound",
      "frequency": "very_high",
      "stems": {
        "present": "āgaccha",
        "aorist": "āgami",
        "perfect": "āgata",
        "passive": "āgacchīya",
        "causative": "āgame",
        "past_participle": "āgata"
      },
      "prefixes": ["pra", "sam", "vi"],
      "generates_forms": 180,
      "generation_hints": {
        "compound_origin": "ā + √gam",
        "high_frequency": "very common arrival verb"
      }
    },

    "√upagam": {
      "meaning": "to approach, come near",
      "type": "compound",
      "frequency": "medium",
      "stems": {
        "present": "upagaccha",
        "aorist": "upagami",
        "perfect": "upagata",
        "passive": "upagacchīya",
        "causative": "upagame",
        "past_participle": "upagata"
      },
      "prefixes": ["pari", "sam"],
      "generates_forms": 140,
      "generation_hints": {
        "compound_origin": "upa + √gam"
      }
    },

    "√abhigam": {
      "meaning": "to approach, go towards",
      "type": "compound",
      "frequency": "medium",
      "stems": {
        "present": "abhigaccha",
        "aorist": "abhigami",
        "perfect": "abhigata",
        "passive": "abhigacchīya",
        "causative": "abhigame",
        "past_participle": "abhigata"
      },
      "prefixes": ["sam"],
      "generates_forms": 130,
      "generation_hints": {
        "compound_origin": "abhi + √gam"
      }
    },

    "√saṃgam": {
      "meaning": "to come together, meet",
      "type": "compound",
      "frequency": "medium",
      "stems": {
        "present": "saṅgaccha",
        "aorist": "saṅgami",
        "perfect": "saṅgata",
        "passive": "saṅgacchīya",
        "causative": "saṅgame",
        "past_participle": "saṅgata"
      },
      "prefixes": ["vi"],
      "generates_forms": 130,
      "generation_hints": {
        "compound_origin": "sam + √gam",
        "meeting_focus": "convergence"
      }
    },

    "√vigam": {
      "meaning": "to go away, depart",
      "type": "compound",
      "frequency": "low",
      "stems": {
        "present": "vigaccha",
        "aorist": "vigami",
        "perfect": "vigata",
        "passive": "vigacchīya",
        "causative": "vigame",
        "past_participle": "vigata"
      },
      "prefixes": [],
      "generates_forms": 120,
      "generation_hints": {
        "compound_origin": "vi + √gam"
      }
    },

    "√atigam": {
      "meaning": "to pass by, surpass",
      "type": "compound",
      "frequency": "low",
      "stems": {
        "present": "atigaccha",
        "aorist": "atigami",
        "perfect": "atigata",
        "passive": "atigacchīya",
        "causative": "atigame",
        "past_participle": "atigata"
      },
      "prefixes": [],
      "generates_forms": 120,
      "generation_hints": {
        "compound_origin": "ati + √gam"
      }
    },

    "√sam": {
      "meaning": "to be quiet, calm down",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "samma",
        "aorist": "asami",
        "perfect": "sasāma",
        "passive": "sammīya",
        "causative": "samāpe",
        "past_participle": "santa"
      },
      "prefixes": ["upa", "vi"],
      "generates_forms": 140,
      "generation_hints": {
        "irregular_participle": "santa",
        "peace_focus": "tranquility"
      }
    },

    "√kṣi": {
      "meaning": "to destroy, diminish",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "khaya",
        "aorist": "akṣayi",
        "perfect": "cakṣaya",
        "passive": "khayīya",
        "causative": "khayāpe",
        "past_participle": "khīṇa"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_change": "kṣi > khay",
        "irregular_participle": "khīṇa"
      }
    },

    "√kṣay": {
      "meaning": "to waste away, perish",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "khaya",
        "aorist": "akṣayi",
        "perfect": "cakṣaya",
        "passive": "khayīya",
        "causative": "khayāpe",
        "past_participle": "khīṇa"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 140,
      "generation_hints": {
        "related_to": "√kṣi",
        "decay_focus": "gradual destruction"
      }
    },

    "√naś": {
      "meaning": "to perish, be lost",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "nassa",
        "aorist": "anaśi",
        "perfect": "nanaśa",
        "passive": "nassīya",
        "causative": "nāsāpe",
        "past_participle": "naṭṭha"
      },
      "prefixes": ["vi", "pra"],
      "generates_forms": 140,
      "generation_hints": {
        "pali_change": "naś > nass",
        "irregular_participle": "naṭṭha"
      }
    },

    "√vinaś": {
      "meaning": "to perish, be destroyed",
      "type": "compound",
      "frequency": "low",
      "stems": {
        "present": "vinassa",
        "aorist": "avinaśi",
        "perfect": "vinaśa",
        "passive": "vinassīya",
        "causative": "vinasāpe",
        "past_participle": "vinaṭṭha"
      },
      "prefixes": [],
      "generates_forms": 120,
      "generation_hints": {
        "compound_origin": "vi + √naś"
      }
    },

    "√upaśam": {
      "meaning": "to become quiet, cease",
      "type": "compound",
      "frequency": "medium",
      "stems": {
        "present": "upasama",
        "aorist": "upaśami",
        "perfect": "upaśama",
        "passive": "upasamīya",
        "causative": "upasamāpe",
        "past_participle": "upasanta"
      },
      "prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "compound_origin": "upa + √śam",
        "cessation_focus": "calming down"
      }
    },

    "√nirvā": {
      "meaning": "to be extinguished, cease",
      "type": "compound",
      "frequency": "high",
      "stems": {
        "present": "nibbāya",
        "aorist": "anirvāyi",
        "perfect": "nirvāya",
        "passive": "nibbāyīya",
        "causative": "nibbāpe",
        "past_participle": "nibbuta"
      },
      "prefixes": [],
      "generates_forms": 150,
      "generation_hints": {
        "compound_origin": "nir + √vā",
        "pali_change": "nirvā > nibbā",
        "religious_significance": "enlightenment term"
      }
    },

    "√ni": {
      "meaning": "to lead, guide",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "naya",
        "aorist": "anesi",
        "perfect": "ninaya",
        "passive": "nīya",
        "causative": "nāyāpe",
        "past_participle": "nīta"
      },
      "prefixes": ["ā", "pra", "vi"],
      "generates_forms": 150,
      "generation_hints": {
        "related_to": "√nī",
        "leadership_focus": "guidance"
      }
    },

    "√prani": {
      "meaning": "to lead forth",
      "type": "compound",
      "frequency": "low",
      "stems": {
        "present": "panaya",
        "aorist": "apranesi",
        "perfect": "pranaya",
        "passive": "panīya",
        "causative": "panāyāpe",
        "past_participle": "panīta"
      },
      "prefixes": [],
      "generates_forms": 110,
      "generation_hints": {
        "compound_origin": "pra + √ni",
        "pali_simplification": "prani > pan"
      }
    },

    "√anuni": {
      "meaning": "to lead along",
      "type": "compound",
      "frequency": "very_low",
      "stems": {
        "present": "ananaya",
        "aorist": "ananesi",
        "perfect": "ananaya",
        "passive": "ananīya",
        "causative": "ananāyāpe",
        "past_participle": "ananīta"
      },
      "prefixes": [],
      "generates_forms": 90,
      "generation_hints": {
        "compound_origin": "anu + √ni",
        "rare_usage": "very archaic"
      }
    },

    "√vin": {
      "meaning": "to lead away, remove",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "vinaya",
        "aorist": "avinesi",
        "perfect": "vivinaya",
        "passive": "vinīya",
        "causative": "vinayāpe",
        "past_participle": "vinīta"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 140,
      "generation_hints": {
        "religious_significance": "vinaya discipline",
        "removal_focus": "leading away from wrong"
      }
    },

    "√udvin": {
      "meaning": "to lead up, raise",
      "type": "compound",
      "frequency": "low",
      "stems": {
        "present": "udvinaya",
        "aorist": "audvinesi",
        "perfect": "udvinaya",
        "passive": "udvinīya",
        "causative": "udvinayāpe",
        "past_participle": "udvinīta"
      },
      "prefixes": [],
      "generates_forms": 100,
      "generation_hints": {
        "compound_origin": "ud + √vin"
      }
    },

    "√upani": {
      "meaning": "to lead near, bring close",
      "type": "compound",
      "frequency": "low",
      "stems": {
        "present": "upanaya",
        "aorist": "aupanesi",
        "perfect": "upanaya",
        "passive": "upanīya",
        "causative": "upanayāpe",
        "past_participle": "upanīta"
      },
      "prefixes": [],
      "generates_forms": 110,
      "generation_hints": {
        "compound_origin": "upa + √ni"
      }
    },

    "√prakṣip": {
      "meaning": "to throw forth",
      "type": "compound",
      "frequency": "low",
      "stems": {
        "present": "pakkhipa",
        "aorist": "aprakṣipi",
        "perfect": "prakṣipa",
        "passive": "pakkhipīya",
        "causative": "pakkhipāpe",
        "past_participle": "pakkhitta"
      },
      "prefixes": [],
      "generates_forms": 110,
      "generation_hints": {
        "compound_origin": "pra + √kṣip",
        "pali_simplification": "prakṣip > pakkhip"
      }
    },

    "√nikṣip": {
      "meaning": "to throw down, deposit",
      "type": "compound",
      "frequency": "medium",
      "stems": {
        "present": "nikkhipa",
        "aorist": "anikṣipi",
        "perfect": "nikṣipa",
        "passive": "nikkhipīya",
        "causative": "nikkhipāpe",
        "past_participle": "nikkhitta"
      },
      "prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "compound_origin": "ni + √kṣip",
        "pali_simplification": "nikṣip > nikkhip"
      }
    },

    "√vikṣip": {
      "meaning": "to scatter, disperse",
      "type": "compound",
      "frequency": "low",
      "stems": {
        "present": "vikkhipa",
        "aorist": "avikṣipi",
        "perfect": "vikṣipa",
        "passive": "vikkhipīya",
        "causative": "vikkhipāpe",
        "past_participle": "vikkhitta"
      },
      "prefixes": [],
      "generates_forms": 120,
      "generation_hints": {
        "compound_origin": "vi + √kṣip"
      }
    },

    "√utkṣip": {
      "meaning": "to throw up, raise",
      "type": "compound",
      "frequency": "low",
      "stems": {
        "present": "ukkhipa",
        "aorist": "autkṣipi",
        "perfect": "utkṣipa",
        "passive": "ukkhipīya",
        "causative": "ukkhipāpe",
        "past_participle": "ukkhitta"
      },
      "prefixes": [],
      "generates_forms": 110,
      "generation_hints": {
        "compound_origin": "ut + √kṣip",
        "pali_simplification": "utkṣip > ukkhip"
      }
    },

    "√apakṣip": {
      "meaning": "to throw away, reject",
      "type": "compound",
      "frequency": "low",
      "stems": {
        "present": "apakkhipa",
        "aorist": "aapakṣipi",
        "perfect": "apakṣipa",
        "passive": "apakkhipīya",
        "causative": "apakkhipāpe",
        "past_participle": "apakkhitta"
      },
      "prefixes": [],
      "generates_forms": 110,
      "generation_hints": {
        "compound_origin": "apa + √kṣip"
      }
    },

    "√kram": {
      "meaning": "to step, walk",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "kama",
        "aorist": "akrami",
        "perfect": "cakrāma",
        "passive": "kamīya",
        "causative": "kramāpe",
        "past_participle": "kanta"
      },
      "prefixes": ["ā", "upa", "pra", "vi"],
      "generates_forms": 150,
      "generation_hints": {
        "pali_simplification": "kr lost in present",
        "irregular_participle": "kanta"
      }
    },

    "√ākram": {
      "meaning": "to step upon, attack",
      "type": "compound",
      "frequency": "medium",
      "stems": {
        "present": "ākama",
        "aorist": "ākrami",
        "perfect": "ākrama",
        "passive": "ākamīya",
        "causative": "ākramāpe",
        "past_participle": "ākanta"
      },
      "prefixes": ["pra", "sam"],
      "generates_forms": 130,
      "generation_hints": {
        "compound_origin": "ā + √kram",
        "attack_focus": "aggressive stepping"
      }
    },

    "√vikram": {
      "meaning": "to step apart, stride",
      "type": "compound",
      "frequency": "low",
      "stems": {
        "present": "vikama",
        "aorist": "avikrami",
        "perfect": "vikrama",
        "passive": "vikamīya",
        "causative": "vikramāpe",
        "past_participle": "vikanta"
      },
      "prefixes": [],
      "generates_forms": 120,
      "generation_hints": {
        "compound_origin": "vi + √kram"
      }
    },

    "√prakram": {
      "meaning": "to step forward, advance",
      "type": "compound",
      "frequency": "low",
      "stems": {
        "present": "pakama",
        "aorist": "aprakrami",
        "perfect": "prakrama",
        "passive": "pakamīya",
        "causative": "pakramāpe",
        "past_participle": "pakanta"
      },
      "prefixes": [],
      "generates_forms": 110,
      "generation_hints": {
        "compound_origin": "pra + √kram",
        "pali_simplification": "prakram > pakam"
      }
    },

    "√utkram": {
      "meaning": "to step up, rise above",
      "type": "compound",
      "frequency": "very_low",
      "stems": {
        "present": "ukkama",
        "aorist": "autkrami",
        "perfect": "utkrama",
        "passive": "ukkamīya",
        "causative": "ukkramāpe",
        "past_participle": "ukkanta"
      },
      "prefixes": [],
      "generates_forms": 100,
      "generation_hints": {
        "compound_origin": "ut + √kram",
        "pali_simplification": "utkram > ukkam"
      }
    },

    "√laṅgh": {
      "meaning": "to leap over, transgress",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "laṅgha",
        "aorist": "alaṅghi",
        "perfect": "lalaṅgha",
        "passive": "laṅghīya",
        "causative": "laṅghāpe",
        "past_participle": "laṅghita"
      },
      "prefixes": ["ā", "ava", "ut"],
      "generates_forms": 120,
      "generation_hints": {
        "transgression_focus": "overstepping boundaries"
      }
    },

    "√ullaṅgh": {
      "meaning": "to leap up, transgress",
      "type": "compound",
      "frequency": "very_low",
      "stems": {
        "present": "ullaṅgha",
        "aorist": "aullaṅghi",
        "perfect": "ullaṅgha",
        "passive": "ullaṅghīya",
        "causative": "ullaṅghāpe",
        "past_participle": "ullaṅghita"
      },
      "prefixes": [],
      "generates_forms": 90,
      "generation_hints": {
        "compound_origin": "ud + √laṅgh"
      }
    },

    "√car": {
      "meaning": "to move, wander",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "cara",
        "aorist": "acari",
        "perfect": "cacāra",
        "passive": "carīya",
        "causative": "cārāpe",
        "past_participle": "carita"
      },
      "prefixes": ["ā", "anu", "pari", "vi", "sam"],
      "generates_forms": 180,
      "generation_hints": {
        "conduct_focus": "behavior or movement"
      }
    },

    "√vicar": {
      "meaning": "to move about, wander",
      "type": "compound",
      "frequency": "medium",
      "stems": {
        "present": "vicara",
        "aorist": "avicari",
        "perfect": "vicara",
        "passive": "vicarīya",
        "causative": "vicārāpe",
        "past_participle": "vicarita"
      },
      "prefixes": ["pari"],
      "generates_forms": 140,
      "generation_hints": {
        "compound_origin": "vi + √car",
        "mental_wandering": "thinking or pondering"
      }
    },

    "√saṃcar": {
      "meaning": "to move together, wander",
      "type": "compound",
      "frequency": "low",
      "stems": {
        "present": "saṅcara",
        "aorist": "asaṅcari",
        "perfect": "saṅcara",
        "passive": "saṅcarīya",
        "causative": "saṅcārāpe",
        "past_participle": "saṅcarita"
      },
      "prefixes": [],
      "generates_forms": 120,
      "generation_hints": {
        "compound_origin": "sam + √car"
      }
    },

    "√pracar": {
      "meaning": "to move forward, proceed",
      "type": "compound",
      "frequency": "low",
      "stems": {
        "present": "pacara",
        "aorist": "apracari",
        "perfect": "pracara",
        "passive": "pacarīya",
        "causative": "pacārāpe",
        "past_participle": "pacarita"
      },
      "prefixes": [],
      "generates_forms": 110,
      "generation_hints": {
        "compound_origin": "pra + √car",
        "pali_simplification": "pracar > pacar"
      }
    },

    "√anucar": {
      "meaning": "to follow, accompany",
      "type": "compound",
      "frequency": "low",
      "stems": {
        "present": "anucara",
        "aorist": "aanucari",
        "perfect": "anucara",
        "passive": "anucarīya",
        "causative": "anucārāpe",
        "past_participle": "anucarita"
      },
      "prefixes": [],
      "generates_forms": 110,
      "generation_hints": {
        "compound_origin": "anu + √car",
        "following_focus": "accompanying someone"
      }
    },

    "√ācar": {
      "meaning": "to practice, conduct",
      "type": "compound",
      "frequency": "high",
      "stems": {
        "present": "ācara",
        "aorist": "ācari",
        "perfect": "ācara",
        "passive": "ācarīya",
        "causative": "ācārāpe",
        "past_participle": "ācarita"
      },
      "prefixes": ["sam"],
      "generates_forms": 150,
      "generation_hints": {
        "compound_origin": "ā + √car",
        "ethical_focus": "moral conduct"
      }
    },

    "√samācar": {
      "meaning": "to practice properly",
      "type": "compound",
      "frequency": "medium",
      "stems": {
        "present": "samācara",
        "aorist": "asamācari",
        "perfect": "samācara",
        "passive": "samācarīya",
        "causative": "samācārāpe",
        "past_participle": "samācarita"
      },
      "prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "compound_origin": "sam + ā + √car"
      }
    },

    "√aṅg": {
      "meaning": "to mark, brand",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "aṅga",
        "aorist": "āṅgi",
        "perfect": "ānaṅga",
        "passive": "aṅgīya",
        "causative": "aṅgāpe",
        "past_participle": "aṅgita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 110,
      "generation_hints": {
        "marking_focus": "physical marking"
      }
    },

    "√aṅk": {
      "meaning": "to mark, count",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "aṅka",
        "aorist": "āṅki",
        "perfect": "ānaṅka",
        "passive": "aṅkīya",
        "causative": "aṅkāpe",
        "past_participle": "aṅkita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 110,
      "generation_hints": {
        "numerical_focus": "counting or numbering"
      }
    },

    "√liṅg": {
      "meaning": "to paint, mark",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "liṅga",
        "aorist": "aliṅgi",
        "perfect": "liliṅga",
        "passive": "liṅgīya",
        "causative": "liṅgāpe",
        "past_participle": "liṅgita"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "artistic_focus": "decorative marking"
      }
    },

    "√śaṅk": {
      "meaning": "to doubt, suspect",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "saṅka",
        "aorist": "aśaṅki",
        "perfect": "śaśaṅka",
        "passive": "saṅkīya",
        "causative": "saṅkāpe",
        "past_participle": "saṅkita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 140,
      "generation_hints": {
        "pali_change": "ś > s",
        "doubt_focus": "uncertainty or suspicion"
      }
    },

    "√śaṅs": {
      "meaning": "to proclaim, praise",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "saṅsa",
        "aorist": "aśaṅsi",
        "perfect": "śaśaṅsa",
        "passive": "saṅsīya",
        "causative": "saṅsāpe",
        "past_participle": "saṅsita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_change": "ś > s"
      }
    },

    "√kīrt": {
      "meaning": "to mention, praise",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "kīrta",
        "aorist": "akīrti",
        "perfect": "cakīrta",
        "passive": "kīrtīya",
        "causative": "kīrtāpe",
        "past_participle": "kīrtita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 120,
      "generation_hints": {
        "fame_focus": "reputation or praise"
      }
    },

    "√stu": {
      "meaning": "to praise",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "stava",
        "aorist": "astavi",
        "perfect": "tustāva",
        "passive": "stavīya",
        "causative": "stavāpe",
        "past_participle": "stuta"
      },
      "prefixes": ["ā", "abhi"],
      "generates_forms": 140,
      "generation_hints": {
        "present_change": "stu > stav"
      }
    },

    "√stav": {
      "meaning": "to praise, extol",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "stava",
        "aorist": "astavi",
        "perfect": "tastāva",
        "passive": "stavīya",
        "causative": "stavāpe",
        "past_participle": "stuta"
      },
      "prefixes": ["ā", "abhi"],
      "generates_forms": 120,
      "generation_hints": {
        "related_to": "√stu"
      }
    },

    "√nind": {
      "meaning": "to blame, censure",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "ninda",
        "aorist": "anindi",
        "perfect": "nininda",
        "passive": "nindīya",
        "causative": "nindāpe",
        "past_participle": "nindita"
      },
      "prefixes": ["ā", "apa"],
      "generates_forms": 140,
      "generation_hints": {
        "criticism_focus": "fault-finding"
      }
    },

    "√garh": {
      "meaning": "to blame, criticize",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "garha",
        "aorist": "agarhi",
        "perfect": "jagarha",
        "passive": "garhīya",
        "causative": "garhāpe",
        "past_participle": "garhita"
      },
      "prefixes": ["ā", "upa"],
      "generates_forms": 120,
      "generation_hints": {
        "condemnation_focus": "strong disapproval"
      }
    },

    "√bharts": {
      "meaning": "to threaten, scold",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "bharsa",
        "aorist": "abharsi",
        "perfect": "babharsa",
        "passive": "bharsīya",
        "causative": "bharsāpe",
        "past_participle": "bharsita"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "pali_change": "t lost",
        "anger_expression": "verbal aggression"
      }
    },

    "√śap": {
      "meaning": "to curse",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "sapa",
        "aorist": "aśapi",
        "perfect": "śaśāpa",
        "passive": "sapīya",
        "causative": "sapāpe",
        "past_participle": "sapta"
      },
      "prefixes": ["ā", "abhi"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_change": "ś > s",
        "curse_focus": "invoking evil"
      }
    },
  
    "√ās": {
      "meaning": "to sit",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "āsa",
        "aorist": "āsi",
        "perfect": "āsa",
        "passive": "āsīya",
        "causative": "āsāpe",
        "past_participle": "āsīna"
      },
      "prefixes": ["upa", "adhi", "pari"],
      "generates_forms": 160,
      "generation_hints": {
        "sitting_focus": "seated position",
        "meditation_context": "often used for sitting meditation"
      }
    },

    "√upaviś": {
      "meaning": "to sit down, enter",
      "type": "compound",
      "frequency": "medium",
      "stems": {
        "present": "upavisati",
        "aorist": "upavisi",
        "perfect": "upaviveśa",
        "passive": "upavisīya",
        "causative": "upavisāpe",
        "past_participle": "upaviṭṭha"
      },
      "prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "compound_origin": "upa + √viś",
        "entering_sitting": "sitting down upon entering"
      }
    },

    "√niṣad": {
      "meaning": "to sit down",
      "type": "compound",
      "frequency": "low",
      "stems": {
        "present": "nisīda",
        "aorist": "aniṣadi",
        "perfect": "niṣada",
        "passive": "nisīdīya",
        "causative": "nisīdāpe",
        "past_participle": "niṣanna"
      },
      "prefixes": [],
      "generates_forms": 120,
      "generation_hints": {
        "compound_origin": "ni + √sad",
        "pali_change": "niṣad > nisīd"
      }
    },

    "√śī": {
      "meaning": "to lie down, rest",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "saya",
        "aorist": "aśayi",
        "perfect": "śiśāya",
        "passive": "sayīya",
        "causative": "sāyāpe",
        "past_participle": "sayita"
      },
      "prefixes": ["upa", "ava", "pra"],
      "generates_forms": 150,
      "generation_hints": {
        "pali_change": "ś > s",
        "present_change": "śī > say"
      }
    },

    "√svap": {
      "meaning": "to sleep",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "supa",
        "aorist": "asvapi",
        "perfect": "suṣvāpa",
        "passive": "supīya",
        "causative": "svāpāpe",
        "past_participle": "supta"
      },
      "prefixes": ["ava", "pra"],
      "generates_forms": 140,
      "generation_hints": {
        "present_change": "svap > sup"
      }
    },

    "√sup": {
      "meaning": "to sleep",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "supa",
        "aorist": "asupi",
        "perfect": "suṣupa",
        "passive": "supīya",
        "causative": "sopāpe",
        "past_participle": "sutta"
      },
      "prefixes": ["ava", "pra"],
      "generates_forms": 150,
      "generation_hints": {
        "irregular_participle": "sutta",
        "related_to": "√svap"
      }
    },

    "√jāgṛ": {
      "meaning": "to be awake, watchful",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "jāga",
        "aorist": "ajāgari",
        "perfect": "jajāgāra",
        "passive": "jāgarīya",
        "causative": "jāgarāpe",
        "past_participle": "jāgarita"
      },
      "prefixes": ["pra", "sam"],
      "generates_forms": 140,
      "generation_hints": {
        "pali_simplification": "jāgṛ > jāg",
        "vigilance_focus": "mindful awareness"
      }
    },

    "√prabodh": {
      "meaning": "to awake, become conscious",
      "type": "compound",
      "frequency": "medium",
      "stems": {
        "present": "pabujjha",
        "aorist": "aprabodhi",
        "perfect": "prabodha",
        "passive": "pabujjhīya",
        "causative": "pabodhāpe",
        "past_participle": "pabuddha"
      },
      "prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "compound_origin": "pra + √budh",
        "pali_change": "prabodh > pabujjh",
        "awakening_focus": "spiritual awakening"
      }
    },

    "√utthā": {
      "meaning": "to rise up, get up",
      "type": "compound",
      "frequency": "high",
      "stems": {
        "present": "uṭṭhāha",
        "aorist": "auṭṭhāsi",
        "perfect": "utthāha",
        "passive": "uṭṭhāhīya",
        "causative": "uṭṭhāpe",
        "past_participle": "uṭṭhita"
      },
      "prefixes": [],
      "generates_forms": 160,
      "generation_hints": {
        "compound_origin": "ud + √sthā",
        "pali_change": "utthā > uṭṭhā"
      }
    },

    "√samutthā": {
      "meaning": "to rise up together",
      "type": "compound",
      "frequency": "low",
      "stems": {
        "present": "samuṭṭhāha",
        "aorist": "asamuṭṭhāsi",
        "perfect": "samutthāha",
        "passive": "samuṭṭhāhīya",
        "causative": "samuṭṭhāpe",
        "past_participle": "samuṭṭhita"
      },
      "prefixes": [],
      "generates_forms": 120,
      "generation_hints": {
        "compound_origin": "sam + ud + √sthā"
      }
    },

    "√viś": {
      "meaning": "to enter",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "visa",
        "aorist": "avisi",
        "perfect": "viveśa",
        "passive": "visīya",
        "causative": "vesāpe",
        "past_participle": "viṭṭha"
      },
      "prefixes": ["ā", "pra", "anu"],
      "generates_forms": 170,
      "generation_hints": {
        "pali_change": "ś > s",
        "irregular_participle": "viṭṭha"
      }
    },

    "√praviś": {
      "meaning": "to enter into",
      "type": "compound",
      "frequency": "high",
      "stems": {
        "present": "pavisa",
        "aorist": "apravisi",
        "perfect": "praviveśa",
        "passive": "pavisīya",
        "causative": "pavesāpe",
        "past_participle": "paviṭṭha"
      },
      "prefixes": [],
      "generates_forms": 150,
      "generation_hints": {
        "compound_origin": "pra + √viś",
        "pali_simplification": "praviś > pavis"
      }
    },

    "√nirgam": {
      "meaning": "to go out, exit",
      "type": "compound",
      "frequency": "medium",
      "stems": {
        "present": "nikkham",
        "aorist": "anirgami",
        "perfect": "nirgama",
        "passive": "nikkhama",
        "causative": "nikkhamāpe",
        "past_participle": "nikkhanta"
      },
      "prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "compound_origin": "nir + √gam",
        "pali_change": "nirgam > nikkham"
      }
    },

    "√niṣkram": {
      "meaning": "to go out, depart",
      "type": "compound",
      "frequency": "low",
      "stems": {
        "present": "nikkama",
        "aorist": "aniṣkrami",
        "perfect": "niṣkrama",
        "passive": "nikkamīya",
        "causative": "nikkramāpe",
        "past_participle": "nikkanta"
      },
      "prefixes": [],
      "generates_forms": 120,
      "generation_hints": {
        "compound_origin": "niṣ + √kram",
        "pali_change": "niṣkram > nikkam"
      }
    },

    "√pratipad": {
      "meaning": "to enter upon, practice",
      "type": "compound",
      "frequency": "medium",
      "stems": {
        "present": "paṭipajja",
        "aorist": "apatipadi",
        "perfect": "pratipad",
        "passive": "paṭipajjīya",
        "causative": "paṭipādāpe",
        "past_participle": "paṭipanna"
      },
      "prefixes": [],
      "generates_forms": 140,
      "generation_hints": {
        "compound_origin": "prati + √pad",
        "pali_change": "pratipad > paṭipajj",
        "practice_focus": "spiritual practice"
      }
    },

    "√anupratipad": {
      "meaning": "to follow in practice",
      "type": "compound",
      "frequency": "low",
      "stems": {
        "present": "anupaṭipajja",
        "aorist": "aanupatipadi",
        "perfect": "anupratipad",
        "passive": "anupaṭipajjīya",
        "causative": "anupaṭipādāpe",
        "past_participle": "anupaṭipanna"
      },
      "prefixes": [],
      "generates_forms": 110,
      "generation_hints": {
        "compound_origin": "anu + prati + √pad"
      }
    },

    "√bhaj": {
      "meaning": "to divide, share, worship",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "bhaja",
        "aorist": "abhaji",
        "perfect": "babhāja",
        "passive": "bhajīya",
        "causative": "bhājāpe",
        "past_participle": "bhatta"
      },
      "prefixes": ["ā", "vi", "sam"],
      "generates_forms": 150,
      "generation_hints": {
        "dual_meaning": "divide or worship contextually",
        "irregular_participle": "bhatta"
      }
    },

    "√ruc": {
      "meaning": "to shine, please",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "roca",
        "aorist": "aruci",
        "perfect": "ruroca",
        "passive": "rocīya",
        "causative": "rocāpe",
        "past_participle": "rucita"
      },
      "prefixes": ["ā", "vi", "pra"],
      "generates_forms": 140,
      "generation_hints": {
        "present_change": "ruc > roc",
        "dual_meaning": "physical shine or mental pleasure"
      }
    },

    "√dīp": {
      "meaning": "to shine, blaze",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "dīpa",
        "aorist": "adīpi",
        "perfect": "didīpa",
        "passive": "dīpīya",
        "causative": "dīpāpe",
        "past_participle": "dīpita"
      },
      "prefixes": ["ā", "pra", "sam"],
      "generates_forms": 140,
      "generation_hints": {
        "light_focus": "illumination"
      }
    },

    "√mih": {
      "meaning": "to urinate",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "meha",
        "aorist": "amehi",
        "perfect": "mimeha",
        "passive": "mehīya",
        "causative": "mehāpe",
        "past_participle": "mūtta"
      },
      "prefixes": ["ava", "pra"],
      "generates_forms": 110,
      "generation_hints": {
        "present_change": "mih > meh",
        "irregular_participle": "mūtta",
        "bodily_function": "natural process"
      }
    },

    "√vam": {
      "meaning": "to vomit",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "vama",
        "aorist": "avami",
        "perfect": "vavāma",
        "passive": "vamīya",
        "causative": "vamāpe",
        "past_participle": "vanta"
      },
      "prefixes": ["ā", "ud"],
      "generates_forms": 110,
      "generation_hints": {
        "irregular_participle": "vanta"
      }
    },

    "√kās": {
      "meaning": "to cough",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "kāsa",
        "aorist": "akāsi",
        "perfect": "cakāsa",
        "passive": "kāsīya",
        "causative": "kāsāpe",
        "past_participle": "kāsita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 110,
      "generation_hints": {
        "sound_imitative": "coughing sound"
      }
    },

    "√nam": {
      "meaning": "to bend, bow",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "nama",
        "aorist": "anami",
        "perfect": "nanāma",
        "passive": "namīya",
        "causative": "namāpe",
        "past_participle": "nata"
      },
      "prefixes": ["ā", "vi", "pra"],
      "generates_forms": 140,
      "generation_hints": {
        "respect_gesture": "bowing in reverence"
      }
    },

    "√phal": {
      "meaning": "to bear fruit, result",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "phala",
        "aorist": "aphali",
        "perfect": "paphāla",
        "passive": "phalīya",
        "causative": "phalāpe",
        "past_participle": "phalita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 140,
      "generation_hints": {
        "result_focus": "producing outcomes"
      }
    },

    "√mil": {
      "meaning": "to meet, assemble",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "mila",
        "aorist": "amili",
        "perfect": "mimila",
        "passive": "milīya",
        "causative": "milāpe",
        "past_participle": "milita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 140,
      "generation_hints": {
        "gathering_focus": "coming together"
      }
    },

    "√ghaṭ": {
      "meaning": "to strive, endeavor",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "ghaṭa",
        "aorist": "aghaṭi",
        "perfect": "jaghaṭa",
        "passive": "ghaṭīya",
        "causative": "ghaṭāpe",
        "past_participle": "ghaṭita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 140,
      "generation_hints": {
        "effort_focus": "determined striving"
      }
    },

    "√paṭ": {
      "meaning": "to split, tear",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "paṭa",
        "aorist": "apaṭi",
        "perfect": "papaṭa",
        "passive": "paṭīya",
        "causative": "paṭāpe",
        "past_participle": "paṭita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "tearing_focus": "ripping apart"
      }
    },

    "√khud": {
      "meaning": "to be hungry",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "khuda",
        "aorist": "akhudi",
        "perfect": "cukhuda",
        "passive": "khudīya",
        "causative": "khodāpe",
        "past_participle": "khudhita"
      },
      "prefixes": ["ā"],
      "generates_forms": 120,
      "generation_hints": {
        "hunger_state": "physical need for food",
        "causative_change": "khod- not khud-"
      }
    },

    "√pip": {
      "meaning": "to be thirsty",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "pipa",
        "aorist": "apipi",
        "perfect": "pipipa",
        "passive": "pipīya",
        "causative": "pipāpe",
        "past_participle": "pipāsita"
      },
      "prefixes": ["ā"],
      "generates_forms": 110,
      "generation_hints": {
        "thirst_state": "physical need for water"
      }
    },

    "√klis": {
      "meaning": "to be afflicted, suffer",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "kilissa",
        "aorist": "aklisi",
        "perfect": "cikliśa",
        "passive": "kilissīya",
        "causative": "kilesāpe",
        "past_participle": "kiliṭṭha"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 140,
      "generation_hints": {
        "pali_change": "klis > kiliss",
        "suffering_focus": "mental affliction"
      }
    },

    "√klam": {
      "meaning": "to be tired, weary",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "kamma",
        "aorist": "aklami",
        "perfect": "caklāma",
        "passive": "kammīya",
        "causative": "klamāpe",
        "past_participle": "klanta"
      },
      "prefixes": ["ā", "pari"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_change": "klam > kamm in present"
      }
    },

    "√śram": {
      "meaning": "to toil, be weary",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "sama",
        "aorist": "aśrami",
        "perfect": "śaśrāma",
        "passive": "samīya",
        "causative": "samāpe",
        "past_participle": "santa"
      },
      "prefixes": ["ā", "pari"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_change": "śram > sam",
        "toil_focus": "laborious effort"
      }
    },

    "√glā": {
      "meaning": "to be weary, exhausted",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "gilāya",
        "aorist": "aglāyi",
        "perfect": "jaglau",
        "passive": "gilāyīya",
        "causative": "gilāyāpe",
        "past_participle": "glāta"
      },
      "prefixes": ["ā"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_change": "glā > gilāy",
        "exhaustion_state": "complete weariness"
      }
    },

    "√mlā": {
      "meaning": "to fade, wither",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "milāya",
        "aorist": "amlāyi",
        "perfect": "mamlau",
        "passive": "milāyīya",
        "causative": "milāyāpe",
        "past_participle": "mlāta"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 110,
      "generation_hints": {
        "pali_change": "mlā > milāy",
        "withering_focus": "gradual decay"
      }
    },

    "√piṣ": {
      "meaning": "to grind, crush",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "pisa",
        "aorist": "apiṣi",
        "perfect": "pipiśa",
        "passive": "pisīya",
        "causative": "pesāpe",
        "past_participle": "piṭṭha"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_change": "ṣ > s",
        "irregular_participle": "piṭṭha"
      }
    },

    "√math": {
      "meaning": "to churn, stir",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "mantha",
        "aorist": "amathi",
        "perfect": "mamantha",
        "passive": "manthīya",
        "causative": "mathāpe",
        "past_participle": "mathita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "churning_focus": "stirring motion"
      }
    },

    "√dal": {
      "meaning": "to split, crack",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "dala",
        "aorist": "adali",
        "perfect": "dadāla",
        "passive": "dalīya",
        "causative": "dalāpe",
        "past_participle": "dalita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "splitting_focus": "creating cracks"
      }
    },

    "√sphaṭ": {
      "meaning": "to burst, split",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "phaṭa",
        "aorist": "asphaṭi",
        "perfect": "pasphaṭa",
        "passive": "phaṭīya",
        "causative": "phaṭāpe",
        "past_participle": "sphaṭita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_change": "sph > ph initially",
        "bursting_focus": "sudden splitting"
      }
    },

    "√sphāy": {
      "meaning": "to swell, increase",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "phāya",
        "aorist": "asphāyi",
        "perfect": "pasphāya",
        "passive": "phāyīya",
        "causative": "phāyāpe",
        "past_participle": "sphāyita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_change": "sph > ph",
        "swelling_focus": "expansion"
      }
    },

    "√has": {
      "meaning": "to laugh",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "hasa",
        "aorist": "ahasi",
        "perfect": "jahāsa",
        "passive": "hasīya",
        "causative": "hāsāpe",
        "past_participle": "hasita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 140,
      "generation_hints": {
        "laughter_focus": "expression of joy"
      }
    },

    "√smay": {
      "meaning": "to smile",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "sita",
        "aorist": "asmayi",
        "perfect": "sismaya",
        "passive": "sitīya",
        "causative": "sitāpe",
        "past_participle": "smayita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_change": "smay > sit in present",
        "subtle_joy": "gentle expression"
      }
    },

    "√day": {
      "meaning": "to have compassion",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "daya",
        "aorist": "adayi",
        "perfect": "dadaya",
        "passive": "dayīya",
        "causative": "dayāpe",
        "past_participle": "dayita"
      },
      "prefixes": ["ā", "anu"],
      "generates_forms": 120,
      "generation_hints": {
        "compassion_focus": "feeling pity"
      }
    },

    "√kṛp": {
      "meaning": "to have pity",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "kipa",
        "aorist": "akṛpi",
        "perfect": "cakṛpa",
        "passive": "kipīya",
        "causative": "kopāpe",
        "past_participle": "kṛpita"
      },
      "prefixes": ["ā", "anu"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_change": "ṛ > i",
        "pity_focus": "feeling sympathy"
      }
    },

    "√khid": {
      "meaning": "to be depressed",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "khida",
        "aorist": "akhidi",
        "perfect": "cikhida",
        "passive": "khidīya",
        "causative": "khedāpe",
        "past_participle": "khinna"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "depression_state": "mental dejection",
        "causative_change": "khed- not khid-"
      }
    },

    "√viṣad": {
      "meaning": "to despair, be dejected",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "visīda",
        "aorist": "aviṣadi",
        "perfect": "viṣada",
        "passive": "visīdīya",
        "causative": "visādāpe",
        "past_participle": "visanna"
      },
      "prefixes": ["ā"],
      "generates_forms": 110,
      "generation_hints": {
        "pali_change": "ṣ > s",
        "despair_focus": "loss of hope"
      }
    },

    "√śrath": {
      "meaning": "to loosen, relax",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "satha",
        "aorist": "aśrathi",
        "perfect": "śaśrātha",
        "passive": "sathīya",
        "causative": "sathāpe",
        "past_participle": "śrathita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_change": "śr > s",
        "loosening_focus": "becoming slack"
      }
    },

    "√dṛh": {
      "meaning": "to be firm, steady",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "daḷha",
        "aorist": "adṛhi",
        "perfect": "dadṛha",
        "passive": "daḷhīya",
        "causative": "daḷhāpe",
        "past_participle": "dṛḍha"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_change": "ṛ > aḷ",
        "firmness_focus": "stability"
      }
    },

    "√kṣubh": {
      "meaning": "to be agitated",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "khubha",
        "aorist": "akṣubhi",
        "perfect": "cukṣubha",
        "passive": "khubbhīya",
        "causative": "khobbhāpe",
        "past_participle": "kṣubdhita"
      },
      "prefixes": ["ā", "pra", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_change": "kṣ > kh, bh doubling",
        "agitation_focus": "mental disturbance"
      }
    },

    "√lul": {
      "meaning": "to move to and fro",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "lola",
        "aorist": "aluli",
        "perfect": "lulula",
        "passive": "lolīya",
        "causative": "lolāpe",
        "past_participle": "lulita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "present_change": "lul > lol",
        "oscillation_focus": "swaying motion"
      }
    },

    "√div": {
      "meaning": "to play, gamble",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "dīva",
        "aorist": "adīvi",
        "perfect": "dideva",
        "passive": "dīvīya",
        "causative": "dīvāpe",
        "past_participle": "dīvita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "present_lengthening": "div > dīv",
        "gaming_focus": "playful competition"
      }
    },

    "√bhaṇ": {
      "meaning": "to speak, say",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "bhaṇa",
        "aorist": "abhaṇi",
        "perfect": "babhāṇa",
        "passive": "bhaṇīya",
        "causative": "bhāṇāpe",
        "past_participle": "bhaṇita"
      },
      "prefixes": ["ā", "abhi", "pra"],
      "generates_forms": 160,
      "generation_hints": {
        "speech_emphasis": "formal speaking"
      }
    },

    "√sidh": {
      "meaning": "to succeed, accomplish",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "sijjha",
        "aorist": "asidhi",
        "perfect": "sisedha",
        "passive": "sijjhīya",
        "causative": "sādhāpe",
        "past_participle": "siddha"
      },
      "prefixes": ["ā", "abhi", "sam"],
      "generates_forms": 150,
      "generation_hints": {
        "pali_change": "sidh > sijjh",
        "causative_change": "sādh- not sidh-",
        "success_focus": "achievement"
      }
    },

    "√sādh": {
      "meaning": "to accomplish, achieve",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "sādha",
        "aorist": "asādhi",
        "perfect": "sasādha",
        "passive": "sādhīya",
        "causative": "sādhāpe",
        "past_participle": "sādhita"
      },
      "prefixes": ["ā", "sam", "pari"],
      "generates_forms": 140,
      "generation_hints": {
        "related_to": "√sidh causative"
      }
    },

    "√rādh": {
      "meaning": "to succeed, accomplish",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "rādha",
        "aorist": "arādhi",
        "perfect": "rarādha",
        "passive": "rādhīya",
        "causative": "rādhāpe",
        "past_participle": "rāddha"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 120,
      "generation_hints": {
        "accomplishment_focus": "fulfillment"
      }
    },

    "√lamb": {
      "meaning": "to hang down",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "lamba",
        "aorist": "alambi",
        "perfect": "lalamba",
        "passive": "lambīya",
        "causative": "lambāpe",
        "past_participle": "lambita"
      },
      "prefixes": ["ā", "ava"],
      "generates_forms": 120,
      "generation_hints": {
        "hanging_focus": "suspended position"
      }
    },

    "√śri": {
      "meaning": "to resort to, take refuge",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "saya",
        "aorist": "aśrayi",
        "perfect": "śiśrāya",
        "passive": "sayīya",
        "causative": "sāyāpe",
        "past_participle": "śrita"
      },
      "prefixes": ["ā", "upa", "sam"],
      "generates_forms": 140,
      "generation_hints": {
        "pali_change": "śri > say in present",
        "refuge_focus": "seeking protection"
      }
    },

    "√sev": {
      "meaning": "to serve, practice",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "seva",
        "aorist": "asevi",
        "perfect": "siseva",
        "passive": "sevīya",
        "causative": "sevāpe",
        "past_participle": "sevita"
      },
      "prefixes": ["ā", "upa", "pari"],
      "generates_forms": 160,
      "generation_hints": {
        "service_focus": "devotional practice"
      }
    },

    "√arc": {
      "meaning": "to worship, honor",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "acca",
        "aorist": "ārci",
        "perfect": "ānarca",
        "passive": "accīya",
        "causative": "accāpe",
        "past_participle": "accita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_change": "arc > acc",
        "worship_focus": "reverent honor"
      }
    },

    "√pūj": {
      "meaning": "to worship, honor",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "pūja",
        "aorist": "apūji",
        "perfect": "pupūja",
        "passive": "pūjīya",
        "causative": "pūjāpe",
        "past_participle": "pūjita"
      },
      "prefixes": ["ā", "sam", "pari"],
      "generates_forms": 160,
      "generation_hints": {
        "ritual_worship": "ceremonial honor"
      }
    },

    "√vand": {
      "meaning": "to praise, salute",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "vanda",
        "aorist": "avandi",
        "perfect": "vavanda",
        "passive": "vandīya",
        "causative": "vandāpe",
        "past_participle": "vandita"
      },
      "prefixes": ["ā", "abhi"],
      "generates_forms": 150,
      "generation_hints": {
        "salutation_focus": "respectful greeting"
      }
    },

    "√yāc": {
      "meaning": "to ask, beg",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "yāca",
        "aorist": "ayāci",
        "perfect": "yayāca",
        "passive": "yācīya",
        "causative": "yācāpe",
        "past_participle": "yācita"
      },
      "prefixes": ["ā", "pra", "vi"],
      "generates_forms": 140,
      "generation_hints": {
        "requesting_focus": "humble asking"
      }
    },

    "√arth": {
      "meaning": "to ask for, request",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "attha",
        "aorist": "ārthi",
        "perfect": "ānārtha",
        "passive": "atthīya",
        "causative": "atthāpe",
        "past_participle": "atthita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_change": "r lost in present"
      }
    },

    "√lī": {
      "meaning": "to cling, adhere",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "līya",
        "aorist": "alāyi",
        "perfect": "lilāya",
        "passive": "līyīya",
        "causative": "lāyāpe",
        "past_participle": "līna"
      },
      "prefixes": ["ā", "upa"],
      "generates_forms": 120,
      "generation_hints": {
        "clinging_focus": "attachment"
      }
    },

    "√lag": {
      "meaning": "to attach, adhere",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "laga",
        "aorist": "alagi",
        "perfect": "lalāga",
        "passive": "lagīya",
        "causative": "lagāpe",
        "past_participle": "lagita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 120,
      "generation_hints": {
        "attachment_focus": "sticking to"
      }
    },

    "√saj": {
      "meaning": "to attach, cling",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "sajja",
        "aorist": "asaji",
        "perfect": "sasāja",
        "passive": "sajjīya",
        "causative": "sajjāpe",
        "past_participle": "satta"
      },
      "prefixes": ["ā", "upa"],
      "generates_forms": 120,
      "generation_hints": {
        "gemination": "sajj- forms",
        "irregular_participle": "satta"
      }
    },

    "√śliṣ": {
      "meaning": "to embrace, cling",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "silisa",
        "aorist": "aśliṣi",
        "perfect": "śiśliṣa",
        "passive": "silisīya",
        "causative": "silesāpe",
        "past_participle": "śliṣṭa"
      },
      "prefixes": ["ā", "pari"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_change": "śliṣ > silis",
        "embrace_focus": "close contact"
      }
    },

    "√guh": {
      "meaning": "to hide, conceal",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "gūha",
        "aorist": "agūhi",
        "perfect": "jugūha",
        "passive": "gūhīya",
        "causative": "gūhāpe",
        "past_participle": "gūḷha"
      },
      "prefixes": ["ā", "pari", "sam"],
      "generates_forms": 140,
      "generation_hints": {
        "present_lengthening": "guh > gūh",
        "concealment_focus": "hiding from view"
      }
    },

    "√vṛ": {
      "meaning": "to cover, conceal",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "vara",
        "aorist": "avari",
        "perfect": "vavāra",
        "passive": "varīya",
        "causative": "vārāpe",
        "past_participle": "vata"
      },
      "prefixes": ["ā", "anu", "pari"],
      "generates_forms": 140,
      "generation_hints": {
        "covering_focus": "concealment"
      }
    },

    "√chad": {
      "meaning": "to cover",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "chāda",
        "aorist": "achādi",
        "perfect": "cachāda",
        "passive": "chādīya",
        "causative": "chādāpe",
        "past_participle": "channa"
      },
      "prefixes": ["ā", "pari"],
      "generates_forms": 120,
      "generation_hints": {
        "present_lengthening": "chad > chād",
        "irregular_participle": "channa"
      }
    },

    "√pidhā": {
      "meaning": "to cover, close",
      "type": "compound",
      "frequency": "low",
      "stems": {
        "present": "pidaha",
        "aorist": "apidhāsi",
        "perfect": "pidaha",
        "passive": "pidahīya",
        "causative": "pidahāpe",
        "past_participle": "pidahita"
      },
      "prefixes": [],
      "generates_forms": 120,
      "generation_hints": {
        "compound_origin": "pi + √dhā",
        "closing_focus": "shutting off"
      }
    },

    "√rudh": {
      "meaning": "to obstruct, confine",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "rujjha",
        "aorist": "arodhi",
        "perfect": "rurodha",
        "passive": "rujjhīya",
        "causative": "rodhāpe",
        "past_participle": "ruddha"
      },
      "prefixes": ["ā", "ni", "pari"],
      "generates_forms": 130,
      "generation_hints": {
        "pali_change": "rudh > rujjh",
        "obstruction_focus": "blocking passage"
      }
    },

    "√stambh": {
      "meaning": "to stop, arrest",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "tabbha",
        "aorist": "astambhi",
        "perfect": "tastambha",
        "passive": "tabbhīya",
        "causative": "tabbhāpe",
        "past_participle": "stabdha"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_change": "st > t, mbh > bbh",
        "stopping_focus": "sudden halt"
      }
    },

    "√ruh": {
      "meaning": "to grow, ascend",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "ruha",
        "aorist": "aruhi",
        "perfect": "ruroha",
        "passive": "ruhīya",
        "causative": "ropāpe",
        "past_participle": "rūḷha"
      },
      "prefixes": ["ā", "ā", "sam"],
      "generates_forms": 140,
      "generation_hints": {
        "causative_change": "rop- not ruh-",
        "irregular_participle": "rūḷha"
      }
    },

    "√hiṃs": {
      "meaning": "to hurt, injure",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "hiṃsa",
        "aorist": "ahiṃsi",
        "perfect": "jahiṃsa",
        "passive": "hiṃsīya",
        "causative": "hiṃsāpe",
        "past_participle": "hiṃsita"
      },
      "prefixes": ["ā", "pari"],
      "generates_forms": 140,
      "generation_hints": {
        "harm_focus": "causing injury"
      }
    },

    "√pīḍ": {
      "meaning": "to oppress, hurt",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "pīḷa",
        "aorist": "apīḍi",
        "perfect": "pipīḍa",
        "passive": "pīḷīya",
        "causative": "pīḷāpe",
        "past_participle": "pīḷita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 140,
      "generation_hints": {
        "pali_change": "ḍ > ḷ",
        "oppression_focus": "crushing pressure"
      }
    },

    "√bādh": {
      "meaning": "to oppress, torment",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "bādha",
        "aorist": "abādhi",
        "perfect": "babādha",
        "passive": "bādhīya",
        "causative": "bādhāpe",
        "past_participle": "bādhita"
      },
      "prefixes": ["ā", "pari"],
      "generates_forms": 120,
      "generation_hints": {
        "torment_focus": "persistent harassment"
      }
    },

    "√tāḍ": {
      "meaning": "to beat, strike",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "tāḷa",
        "aorist": "atāḍi",
        "perfect": "tatāḍa",
        "passive": "tāḷīya",
        "causative": "tāḷāpe",
        "past_participle": "tāḷita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_change": "ḍ > ḷ",
        "beating_focus": "rhythmic striking"
      }
    },

    "√ud": {
      "meaning": "to wet, moisten",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "unda",
        "aorist": "aundi",
        "perfect": "unoda",
        "passive": "undīya",
        "causative": "undāpe",
        "past_participle": "unna"
      },
      "prefixes": ["ā"],
      "generates_forms": 100,
      "generation_hints": {
        "present_nasal": "und- forms",
        "irregular_participle": "unna"
      }
    },

    "√ukṣ": {
      "meaning": "to sprinkle, wet",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "ukka",
        "aorist": "aukṣi",
        "perfect": "ukṣa",
        "passive": "ukkīya",
        "causative": "ukkāpe",
        "past_participle": "ukṣita"
      },
      "prefixes": ["ā", "pari"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_change": "kṣ > kk",
        "sprinkling_focus": "water droplets"
      }
    },

    "√gal": {
      "meaning": "to drip, flow",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "gala",
        "aorist": "agali",
        "perfect": "jagāla",
        "passive": "galīya",
        "causative": "galāpe",
        "past_participle": "galita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 120,
      "generation_hints": {
        "dripping_focus": "liquid flowing"
      }
    },

    "√ric": {
      "meaning": "to evacuate, empty",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "rica",
        "aorist": "arici",
        "perfect": "ririca",
        "passive": "ricīya",
        "causative": "recāpe",
        "past_participle": "ricita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "causative_change": "rec- not ric-",
        "emptying_focus": "making vacant"
      }
    },

    "√chṛd": {
      "meaning": "to vomit",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "chada",
        "aorist": "achṛdi",
        "perfect": "cacharda",
        "passive": "chadīya",
        "causative": "chadāpe",
        "past_participle": "chṛdita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_change": "chṛd > chad",
        "vomiting_focus": "expelling stomach contents"
      }
    },

    "√jṛmbh": {
      "meaning": "to yawn",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "jambha",
        "aorist": "ajṛmbhi",
        "perfect": "jajṛmbha",
        "passive": "jambhīya",
        "causative": "jambhāpe",
        "past_participle": "jṛmbhita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 110,
      "generation_hints": {
        "pali_change": "jṛmbh > jambh",
        "yawning_focus": "opening mouth wide"
      }
    },

    "√kṣu": {
      "meaning": "to sneeze",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "khuva",
        "aorist": "akṣavi",
        "perfect": "cukṣāva",
        "passive": "khuvīya",
        "causative": "khuvāpe",
        "past_participle": "kṣuta"
      },
      "prefixes": ["ā"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_change": "kṣu > khuv",
        "sneezing_focus": "nasal expulsion"
      }
    },

    "√śvas": {
      "meaning": "to breathe",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "sasa",
        "aorist": "aśvasi",
        "perfect": "śaśvāsa",
        "passive": "sasīya",
        "causative": "sasāpe",
        "past_participle": "śvasita"
      },
      "prefixes": ["ā", "pra", "vi"],
      "generates_forms": 140,
      "generation_hints": {
        "pali_change": "śvas > sas",
        "breathing_focus": "respiratory action"
      }
    },

    "√an": {
      "meaning": "to breathe",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "ana",
        "aorist": "āni",
        "perfect": "ānana",
        "passive": "anīya",
        "causative": "anāpe",
        "past_participle": "anita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 130,
      "generation_hints": {
        "breathing_focus": "life breath"
      }
    },

    "√śīt": {
      "meaning": "to be cold",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "sīta",
        "aorist": "aśīti",
        "perfect": "śiśīta",
        "passive": "sītīya",
        "causative": "sītāpe",
        "past_participle": "śīta"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_change": "ś > s",
        "cold_state": "temperature sensation"
      }
    },

    "√jvar": {
      "meaning": "to have fever",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "jara",
        "aorist": "ajvari",
        "perfect": "jajvāra",
        "passive": "jarīya",
        "causative": "jarāpe",
        "past_participle": "jvarita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_change": "jvar > jar",
        "fever_state": "elevated temperature"
      }
    },

    "√svid": {
      "meaning": "to sweat",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "sida",
        "aorist": "asvidi",
        "perfect": "sisveda",
        "passive": "sidīya",
        "causative": "sedāpe",
        "past_participle": "svinna"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_change": "svid > sid",
        "sweating_focus": "perspiration"
      }
    },

    "√kled": {
      "meaning": "to be wet, moist",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "kela",
        "aorist": "akledi",
        "perfect": "cikleda",
        "passive": "kelīya",
        "causative": "kelāpe",
        "past_participle": "klinna"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_change": "kled > kel",
        "moisture_state": "dampness"
      }
    },

    "√śuṣ": {
      "meaning": "to dry up",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "sussa",
        "aorist": "aśuṣi",
        "perfect": "śuśoṣa",
        "passive": "sussīya",
        "causative": "sosāpe",
        "past_participle": "sukkha"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_change": "śuṣ > suss",
        "drying_focus": "removing moisture"
      }
    },

    "√vikas": {
      "meaning": "to open, bloom",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "vikasa",
        "aorist": "avikasi",
        "perfect": "vivikasa",
        "passive": "vikasīya",
        "causative": "vikasāpe",
        "past_participle": "vikasita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 120,
      "generation_hints": {
        "blooming_focus": "flowering or opening"
      }
    },

    "√tṛp": {
      "meaning": "to be satisfied",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "tappa",
        "aorist": "atṛpi",
        "perfect": "tatṛpa",
        "passive": "tappīya",
        "causative": "tappāpe",
        "past_participle": "titta"
      },
      "prefixes": ["ā", "pari"],
      "generates_forms": 130,
      "generation_hints": {
        "pali_change": "ṛ > app",
        "satisfaction_state": "contentment"
      }
    },

    "√pūr": {
      "meaning": "to fill",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "pūra",
        "aorist": "apūri",
        "perfect": "pupūra",
        "passive": "pūrīya",
        "causative": "pūrāpe",
        "past_participle": "pūrita"
      },
      "prefixes": ["ā", "sam", "pari"],
      "generates_forms": 140,
      "generation_hints": {
        "filling_focus": "making full"
      }
    },

    "√vṛt": {
      "meaning": "to turn, happen",
      "type": "primary",
      "frequency": "high",
      "stems": {
        "present": "vatta",
        "aorist": "avartti",
        "perfect": "vavarta",
        "passive": "vattīya",
        "causative": "vattāpe",
        "past_participle": "vaṭṭa"
      },
      "prefixes": ["ā", "ni", "pra", "vi"],
      "generates_forms": 170,
      "generation_hints": {
        "pali_change": "ṛ > att",
        "turning_focus": "circular motion or occurrence"
      }
    },

    "√ceṣṭ": {
      "meaning": "to move, act",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "ceṭṭa",
        "aorist": "aceṣṭi",
        "perfect": "ciceṣṭa",
        "passive": "ceṭṭīya",
        "causative": "ceṭṭāpe",
        "past_participle": "ceṣṭita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_change": "ṣṭ > ṭṭ",
        "activity_focus": "purposeful action"
      }
    },

    "√īh": {
      "meaning": "to endeavor, attempt",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "īha",
        "aorist": "āhi",
        "perfect": "īha",
        "passive": "īhīya",
        "causative": "īhāpe",
        "past_participle": "īhita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 120,
      "generation_hints": {
        "endeavor_focus": "striving effort"
      }
    },

    "√kḷp": {
      "meaning": "to be fit, arrange",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "kappa",
        "aorist": "akḷpi",
        "perfect": "cakḷpa",
        "passive": "kappīya",
        "causative": "kappāpe",
        "past_participle": "kata"
      },
      "prefixes": ["ā", "sam", "vi"],
      "generates_forms": 140,
      "generation_hints": {
        "pali_change": "ḷ > app",
        "arrangement_focus": "organizing or fitting"
      }
    },

    "√lup": {
      "meaning": "to disappear, be lost",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "luppa",
        "aorist": "alupi",
        "perfect": "lulopa",
        "passive": "luppīya",
        "causative": "lopāpe",
        "past_participle": "lutta"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "gemination": "lupp- forms",
        "disappearance_focus": "vanishing"
      }
    },

    "√dhvaṃs": {
      "meaning": "to perish, fall",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "dhvaṃsa",
        "aorist": "adhvaṃsi",
        "perfect": "dadhvaṃsa",
        "passive": "dhvaṃsīya",
        "causative": "dhvaṃsāpe",
        "past_participle": "dhvasta"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "destruction_focus": "collapsing"
      }
    },

    "√kuth": {
      "meaning": "to rot, decay",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "kutha",
        "aorist": "akuthi",
        "perfect": "cukutha",
        "passive": "kuthīya",
        "causative": "kothāpe",
        "past_participle": "kuthita"
      },
      "prefixes": ["ā", "vi", "pari"],
      "generates_forms": 110,
      "generation_hints": {
        "causative_change": "koth- not kuth-",
        "decay_focus": "organic decomposition"
      }
    },

    "√pūy": {
      "meaning": "to stink, putrefy",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "puya",
        "aorist": "apuyi",
        "perfect": "pupuya",
        "passive": "puyīya",
        "causative": "puyāpe",
        "past_participle": "pūta"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "irregular_participle": "pūta",
        "putrefaction_focus": "foul decay"
      }
    },

    "√gand": {
      "meaning": "to smell (bad)",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "gandha",
        "aorist": "agandi",
        "perfect": "jaganda",
        "passive": "gandhīya",
        "causative": "gandhāpe",
        "past_participle": "gandhita"
      },
      "prefixes": ["ā", "dur"],
      "generates_forms": 100,
      "generation_hints": {
        "odor_focus": "unpleasant smell"
      }
    },

    "√kṛṣ": {
      "meaning": "to drag, pull",
      "type": "primary",
      "frequency": "medium",
      "stems": {
        "present": "kaḍḍha",
        "aorist": "akṛṣi",
        "perfect": "cakāra",
        "passive": "kaḍḍhīya",
        "causative": "kaḍḍhāpe",
        "past_participle": "kaḍḍhita"
      },
      "prefixes": ["ā", "upa", "pra", "vi"],
      "generates_forms": 140,
      "generation_hints": {
        "pali_change": "kṛṣ > kaḍḍh",
        "dragging_focus": "pulling motion"
      }
    },

    "√akṣ": {
      "meaning": "to reach, penetrate",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "accha",
        "aorist": "ākṣi",
        "perfect": "ānākṣa",
        "passive": "acchīya",
        "causative": "acchāpe",
        "past_participle": "atta"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_change": "kṣ > cch",
        "penetration_focus": "reaching through"
      }
    },

    "√vyath": {
      "meaning": "to be disturbed, tremble",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "byatha",
        "aorist": "avyathi",
        "perfect": "vivyatha",
        "passive": "byathīya",
        "causative": "byathāpe",
        "past_participle": "byathita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 110,
      "generation_hints": {
        "pali_change": "vy > by",
        "disturbance_focus": "mental agitation"
      }
    },

    "√kṣip": {
      "meaning": "to blame, reproach",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "khitta",
        "aorist": "akṣipi",
        "perfect": "cikṣipa",
        "passive": "khittīya",
        "causative": "khittāpe",
        "past_participle": "kṣipta"
      },
      "prefixes": ["ā", "upa"],
      "generates_forms": 110,
      "generation_hints": {
        "different_from": "√khip 'to throw'",
        "blame_focus": "verbal criticism"
      }
    },

    "√tṛṣ": {
      "meaning": "to thirst, desire intensely",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "tassa",
        "aorist": "atṛṣi",
        "perfect": "tatṛṣa",
        "passive": "tassīya",
        "causative": "tassāpe",
        "past_participle": "tṛṣita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 110,
      "generation_hints": {
        "pali_change": "ṛ > ass",
        "craving_focus": "intense desire"
      }
    },

    "√kṣudh": {
      "meaning": "to hunger, be hungry",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "khujjha",
        "aorist": "akṣudhi",
        "perfect": "cukṣudha",
        "passive": "khujjhīya",
        "causative": "khudhāpe",
        "past_participle": "kṣudhita"
      },
      "prefixes": ["ā"],
      "generates_forms": 110,
      "generation_hints": {
        "pali_change": "kṣudh > khujjh",
        "different_from": "√khud",
        "hunger_state": "physical need"
      }
    },

    "√klaś": {
      "meaning": "to torment, afflict",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "kilasa",
        "aorist": "aklaśi",
        "perfect": "caklaśa",
        "passive": "kilasīya",
        "causative": "kilasāpe",
        "past_participle": "klaśita"
      },
      "prefixes": ["ā", "pari"],
      "generates_forms": 110,
      "generation_hints": {
        "pali_change": "klaś > kilas",
        "torment_focus": "causing suffering"
      }
    },

    "√tul": {
      "meaning": "to lift, raise",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "tula",
        "aorist": "atuli",
        "perfect": "tutola",
        "passive": "tulīya",
        "causative": "tolāpe",
        "past_participle": "tulita"
      },
      "prefixes": ["ā", "ut", "sam"],
      "generates_forms": 120,
      "generation_hints": {
        "different_from": "√tul 'to weigh'",
        "lifting_focus": "upward motion"
      }
    },

    "√kṛt": {
      "meaning": "to cut, split",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "kata",
        "aorist": "akṛti",
        "perfect": "cakarta",
        "passive": "katīya",
        "causative": "katāpe",
        "past_participle": "kṛtta"
      },
      "prefixes": ["ā", "vi", "pra"],
      "generates_forms": 110,
      "generation_hints": {
        "pali_change": "ṛ lost in present",
        "cutting_focus": "sharp division"
      }
    },

    "√bhṛś": {
      "meaning": "to fall, drop",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "bhassa",
        "aorist": "abhṛśi",
        "perfect": "babhṛśa",
        "passive": "bhassīya",
        "causative": "bhassāpe",
        "past_participle": "bhṛśita"
      },
      "prefixes": ["ā", "ava"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_change": "bhṛś > bhass",
        "falling_focus": "dropping down"
      }
    },

    "√dhṛṣ": {
      "meaning": "to dare, be bold",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "dhassa",
        "aorist": "adhṛṣi",
        "perfect": "dadhṛṣa",
        "passive": "dhassīya",
        "causative": "dhassāpe",
        "past_participle": "dhṛṣita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 110,
      "generation_hints": {
        "pali_change": "dhṛṣ > dhass",
        "boldness_focus": "courageous action"
      }
    },

    "√vars": {
      "meaning": "to rain",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "vassa",
        "aorist": "avarṣi",
        "perfect": "vavarṣa",
        "passive": "vassīya",
        "causative": "vassāpe",
        "past_participle": "varṣita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 100,
      "generation_hints": {
        "different_from": "√vass",
        "raining_focus": "precipitation"
      }
    },

    "√ghuṣ": {
      "meaning": "to sound, make noise",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "ghosa",
        "aorist": "aghuṣi",
        "perfect": "jughuṣa",
        "passive": "ghosīya",
        "causative": "ghosāpe",
        "past_participle": "ghuṣita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_change": "ghuṣ > ghos",
        "sound_focus": "making audible noise"
      }
    },

    "√kṛś": {
      "meaning": "to become thin, emaciate",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "kisa",
        "aorist": "akṛśi",
        "perfect": "cakṛśa",
        "passive": "kisīya",
        "causative": "kisāpe",
        "past_participle": "kṛśa"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 110,
      "generation_hints": {
        "pali_change": "ṛ > i",
        "thinning_focus": "becoming lean"
      }
    },

    "√pṛṣ": {
      "meaning": "to sprinkle, spray",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "pissa",
        "aorist": "apṛṣi",
        "perfect": "papṛṣa",
        "passive": "pissīya",
        "causative": "pissāpe",
        "past_participle": "pṛṣita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_change": "pṛṣ > piss",
        "sprinkling_focus": "liquid dispersion"
      }
    },

    "√murc": {
      "meaning": "to faint, become unconscious",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "muccha",
        "aorist": "amurci",
        "perfect": "mumurc",
        "passive": "mucchīya",
        "causative": "mocchāpe",
        "past_participle": "mūrcchita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 110,
      "generation_hints": {
        "pali_change": "murc > mucch",
        "fainting_focus": "loss of consciousness"
      }
    },

    "√ghuṇ": {
      "meaning": "to turn, revolve",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "ghuṇa",
        "aorist": "aghuṇi",
        "perfect": "jughuṇa",
        "passive": "ghuṇīya",
        "causative": "ghuṇāpe",
        "past_participle": "ghuṇita"
      },
      "prefixes": ["ā", "pari"],
      "generates_forms": 100,
      "generation_hints": {
        "rotation_focus": "circular motion"
      }
    },

    "√kuṭ": {
      "meaning": "to pound, crush",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "kuṭa",
        "aorist": "akuṭi",
        "perfect": "cukuṭa",
        "passive": "kuṭīya",
        "causative": "koṭāpe",
        "past_participle": "kuṭita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 110,
      "generation_hints": {
        "causative_change": "koṭ- not kuṭ-",
        "pounding_focus": "repetitive crushing"
      }
    },

    "√ghūrṇ": {
      "meaning": "to whirl, spin",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "ghuṇṇa",
        "aorist": "aghūrṇi",
        "perfect": "jaghūrṇa",
        "passive": "ghuṇṇīya",
        "causative": "ghuṇṇāpe",
        "past_participle": "ghūrṇita"
      },
      "prefixes": ["ā", "pari"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_change": "ūrṇ > uṇṇ",
        "whirling_focus": "spinning motion"
      }
    },

    "√ḍī": {
      "meaning": "to fly",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "ḍaya",
        "aorist": "aḍāyi",
        "perfect": "daḍāya",
        "passive": "ḍayīya",
        "causative": "ḍāyāpe",
        "past_participle": "ḍīta"
      },
      "prefixes": ["ā", "ud", "pari"],
      "generates_forms": 110,
      "generation_hints": {
        "present_change": "ḍī > ḍay",
        "flight_focus": "aerial movement"
      }
    },

    "√plavate": {
      "meaning": "to swim, float",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "plava",
        "aorist": "aplavi",
        "perfect": "paplāva",
        "passive": "plavīya",
        "causative": "plavāpe",
        "past_participle": "pluta"
      },
      "prefixes": ["ā", "ut", "sam"],
      "generates_forms": 110,
      "generation_hints": {
        "different_from": "√plu",
        "swimming_focus": "water movement"
      }
    },

    "√jhāp": {
      "meaning": "to burn, blaze",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "jhāpa",
        "aorist": "ajhāpi",
        "perfect": "jajhāpa",
        "passive": "jhāpīya",
        "causative": "jhāpāpe",
        "past_participle": "jhāpita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 110,
      "generation_hints": {
        "burning_focus": "intense flame"
      }
    },

    "√dhūp": {
      "meaning": "to smoke, fumigate",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "dhūpa",
        "aorist": "adhūpi",
        "perfect": "dadhūpa",
        "passive": "dhūpīya",
        "causative": "dhūpāpe",
        "past_participle": "dhūpita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 110,
      "generation_hints": {
        "smoking_focus": "producing smoke"
      }
    },

    "√kṣvel": {
      "meaning": "to sound, make noise",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "khela",
        "aorist": "akṣveli",
        "perfect": "cakṣvela",
        "passive": "khelīya",
        "causative": "khelāpe",
        "past_participle": "kṣvelita"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "pali_change": "kṣv > kh",
        "noise_focus": "making sounds"
      }
    },

    "√kūj": {
      "meaning": "to coo, warble",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "kūja",
        "aorist": "akūji",
        "perfect": "cukūja",
        "passive": "kūjīya",
        "causative": "kūjāpe",
        "past_participle": "kūjita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 100,
      "generation_hints": {
        "bird_sound": "melodic bird calls"
      }
    },

    "√kil": {
      "meaning": "to bind, fasten",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "kila",
        "aorist": "akili",
        "perfect": "cikila",
        "passive": "kilīya",
        "causative": "kilāpe",
        "past_participle": "kilita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 110,
      "generation_hints": {
        "binding_focus": "securing tightly"
      }
    },

    "√kṛnt": {
      "meaning": "to spin, cut",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "kanta",
        "aorist": "akṛnti",
        "perfect": "cakṛnta",
        "passive": "kantīya",
        "causative": "kantāpe",
        "past_participle": "kṛnta"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_change": "ṛnt > ant",
        "cutting_spinning": "rotary cutting"
      }
    },

    "√phlut": {
      "meaning": "to overflow, surge",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "phuta",
        "aorist": "aphluti",
        "perfect": "paphluta",
        "passive": "phutīya",
        "causative": "phutāpe",
        "past_participle": "phluta"
      },
      "prefixes": ["ā", "ut"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_change": "phl > ph",
        "overflow_focus": "liquid surging"
      }
    },

    "√skand": {
      "meaning": "to leap, attack",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "kanda",
        "aorist": "askandi",
        "perfect": "caskanda",
        "passive": "kandīya",
        "causative": "kandāpe",
        "past_participle": "skanna"
      },
      "prefixes": ["ā", "ut"],
      "generates_forms": 110,
      "generation_hints": {
        "pali_change": "sk > k initially",
        "leaping_attack": "aggressive jumping"
      }
    },

    "√dhvan": {
      "meaning": "to sound, resound",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "dhvana",
        "aorist": "adhvani",
        "perfect": "dadhvana",
        "passive": "dhvanīya",
        "causative": "dhvanāpe",
        "past_participle": "dhvanita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 110,
      "generation_hints": {
        "sound_focus": "resonant noise"
      }
    },

    "√kṣar": {
      "meaning": "to melt, dissolve",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "khara",
        "aorist": "akṣari",
        "perfect": "cakṣāra",
        "passive": "kharīya",
        "causative": "kharāpe",
        "past_participle": "kṣara"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 110,
      "generation_hints": {
        "different_from": "√kṣar 'to flow'",
        "melting_focus": "dissolution"
      }
    },

    "√śrī": {
      "meaning": "to cook, boil",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "siya",
        "aorist": "aśrāyi",
        "perfect": "śiśrāya",
        "passive": "siyīya",
        "causative": "siyāpe",
        "past_participle": "śrīta"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_change": "śrī > siy",
        "cooking_focus": "thermal preparation"
      }
    },

    "√plakṣ": {
      "meaning": "to sprinkle, splash",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "pakka",
        "aorist": "aplakṣi",
        "perfect": "paplakṣa",
        "passive": "pakkīya",
        "causative": "pakkāpe",
        "past_participle": "plakṣita"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "pali_change": "plakṣ > pakk",
        "splashing_focus": "water scattering"
      }
    },

    "√ghṛṣ": {
      "meaning": "to rub, grind",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "ghassa",
        "aorist": "aghṛṣi",
        "perfect": "jaghṛṣa",
        "passive": "ghassīya",
        "causative": "ghassāpe",
        "past_participle": "ghṛṣṭa"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 110,
      "generation_hints": {
        "pali_change": "ghṛṣ > ghass",
        "rubbing_focus": "abrasive action"
      }
    },

    "√krand": {
      "meaning": "to cry out, roar",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "kanda",
        "aorist": "akrandi",
        "perfect": "cakranda",
        "passive": "kandīya",
        "causative": "kandāpe",
        "past_participle": "kranna"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 110,
      "generation_hints": {
        "different_from": "√kand 'to cry'",
        "loud_cry": "intense vocalization"
      }
    },

    "√bhaṅg": {
      "meaning": "to break, bend",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "bhaṅga",
        "aorist": "abhaṅgi",
        "perfect": "babhaṅga",
        "passive": "bhaṅgīya",
        "causative": "bhaṅgāpe",
        "past_participle": "bhagga"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 110,
      "generation_hints": {
        "irregular_participle": "bhagga",
        "breaking_bending": "flexible breaking"
      }
    },

    "√dhauk": {
      "meaning": "to burn, heat",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "dhoka",
        "aorist": "adhauki",
        "perfect": "dadhauka",
        "passive": "dhokīya",
        "causative": "dhokāpe",
        "past_participle": "dhaukita"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "present_change": "dhauk > dhok",
        "heating_focus": "thermal activity"
      }
    },

    "√śubh": {
      "meaning": "to shine, be beautiful",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "sobha",
        "aorist": "aśubhi",
        "perfect": "śuśubha",
        "passive": "sobhīya",
        "causative": "sobhāpe",
        "past_participle": "śubhita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 110,
      "generation_hints": {
        "pali_change": "ś > s",
        "beauty_shine": "aesthetic radiance"
      }
    },

    "√gup": {
      "meaning": "to protect, guard secretly",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "gopa",
        "aorist": "agupi",
        "perfect": "jugopa",
        "passive": "gopīya",
        "causative": "gopāpe",
        "past_participle": "gupta"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 110,
      "generation_hints": {
        "present_change": "gup > gop",
        "secret_protection": "hidden guarding"
      }
    },

    "√trap": {
      "meaning": "to be ashamed",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "tappa",
        "aorist": "atrapi",
        "perfect": "tatrāpa",
        "passive": "tappīya",
        "causative": "tappāpe",
        "past_participle": "trapita"
      },
      "prefixes": ["ā"],
      "generates_forms": 110,
      "generation_hints": {
        "gemination": "tapp- forms",
        "shame_focus": "feeling embarrassed"
      }
    },

    "√hrī": {
      "meaning": "to be ashamed, blush",
      "type": "primary",
      "frequency": "low",
      "stems": {
        "present": "harāya",
        "aorist": "ahrāyi",
        "perfect": "jahrāya",
        "passive": "harāyīya",
        "causative": "harāyāpe",
        "past_participle": "hrīta"
      },
      "prefixes": ["ā"],
      "generates_forms": 110,
      "generation_hints": {
        "present_change": "hrī > harāy",
        "shame_modesty": "bashful feeling"
      }
    },

    "√vraṇ": {
      "meaning": "to wound, injure",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "vaṇa",
        "aorist": "avraṇi",
        "perfect": "vavraṇa",
        "passive": "vaṇīya",
        "causative": "vaṇāpe",
        "past_participle": "vraṇita"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "pali_change": "vr > v",
        "wounding_focus": "creating injuries"
      }
    },

    "√kṣaṇ": {
      "meaning": "to hurt, injure",
      "type": "primary",
      "frequency": "very_low",
      "stems": {
        "present": "khaṇa",
        "aorist": "akṣaṇi",
        "perfect": "cakṣāṇa",
        "passive": "khaṇīya",
        "causative": "khaṇāpe",
        "past_participle": "kṣaṇita"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "pali_change": "kṣ > kh",
        "hurting_focus": "causing pain"
      }
    },

    "√kuṣṭh": {
      "meaning": "to suffer skin disease, be leprous",
      "type": "primary",
      "frequency": "very_low",
      "attestation": "medical_texts",
      "stems": {
        "present": "kuṭṭha",
        "aorist": "akuṣṭhi",
        "perfect": "cukuṣṭha",
        "passive": "kuṭṭhīya",
        "causative": "kuṭṭhāpe",
        "past_participle": "kuṣṭhita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "pali_change": "kuṣṭh > kuṭṭh",
        "medical_technical": "dermatological condition",
        "usage": "medical commentaries only"
      }
    },

    "√glai": {
      "meaning": "to be sick, languish",
      "type": "primary",
      "frequency": "very_low",
      "attestation": "late_canonical",
      "stems": {
        "present": "gilāna",
        "aorist": "aglāyi",
        "perfect": "jaglāya",
        "passive": "gilānīya",
        "causative": "gilānāpe",
        "past_participle": "glāna"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "pali_change": "glai > gilān",
        "illness_focus": "chronic sickness",
        "usage": "medical contexts"
      }
    },

    "√āmay": {
      "meaning": "to digest improperly, be diseased",
      "type": "primary",
      "frequency": "very_low",
      "attestation": "medical_commentaries",
      "stems": {
        "present": "āmaya",
        "aorist": "āmayi",
        "perfect": "āmaya",
        "passive": "āmayīya",
        "causative": "āmayāpe",
        "past_participle": "āmayita"
      },
      "prefixes": [],
      "generates_forms": 80,
      "generation_hints": {
        "medical_technical": "digestive disorder",
        "usage": "Ayurvedic Pali texts"
      }
    },

    "√sphuṭ": {
      "meaning": "to calculate, be accurate",
      "type": "primary",
      "frequency": "very_low",
      "attestation": "astronomical_texts",
      "stems": {
        "present": "phuṭa",
        "aorist": "asphuṭi",
        "perfect": "pasphuṭa",
        "passive": "phuṭīya",
        "causative": "phuṭāpe",
        "past_participle": "sphuṭa"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "pali_change": "sph > ph initially",
        "mathematical_technical": "precise calculation",
        "usage": "astronomical commentaries"
      }
    },

    "√gaṇit": {
      "meaning": "to compute, enumerate systematically",
      "type": "denominative",
      "frequency": "very_low",
      "attestation": "technical_commentaries",
      "stems": {
        "present": "gaṇita",
        "aorist": "agaṇiti",
        "perfect": "jagaṇita",
        "passive": "gaṇitīya",
        "causative": "gaṇitāpe",
        "past_participle": "gaṇita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 80,
      "generation_hints": {
        "mathematical_technical": "systematic enumeration",
        "usage": "mathematical treatises"
      }
    },

    "√mlev": {
      "meaning": "to speak indistinctly, mumble",
      "type": "primary",
      "frequency": "very_low",
      "attestation": "late_commentaries",
      "stems": {
        "present": "mileva",
        "aorist": "amlevi",
        "perfect": "mamleva",
        "passive": "milevīya",
        "causative": "milevāpe",
        "past_participle": "mlevita"
      },
      "prefixes": ["ā"],
      "generates_forms": 70,
      "generation_hints": {
        "pali_change": "mlev > milev",
        "speech_defect": "unclear articulation",
        "usage": "very rare, commentarial"
      }
    },

    "√kṣar": {
      "meaning": "to ooze, exude gradually",
      "type": "primary",
      "frequency": "very_low",
      "attestation": "medical_texts",
      "stems": {
        "present": "khāra",
        "aorist": "akṣāri",
        "perfect": "cakṣāra",
        "passive": "khārīya",
        "causative": "khārāpe",
        "past_participle": "kṣārita"
      },
      "prefixes": ["ā", "ni"],
      "generates_forms": 80,
      "generation_hints": {
        "different_from": "previous √kṣar entries",
        "pali_change": "kṣ > kh",
        "medical_usage": "bodily secretions",
        "usage": "medical descriptions"
      }
    },

    "√kroṣṭu": {
      "meaning": "to cry hoarsely, croak",
      "type": "primary",
      "frequency": "very_low",
      "attestation": "literary",
      "stems": {
        "present": "koṭṭhu",
        "aorist": "akroṣṭu",
        "perfect": "cakroṣṭu",
        "passive": "koṭṭhīya",
        "causative": "koṭṭhāpe",
        "past_participle": "kroṣṭu"
      },
      "prefixes": ["ā"],
      "generates_forms": 70,
      "generation_hints": {
        "pali_change": "kroṣṭ > koṭṭh",
        "animal_sound": "harsh bird calls",
        "usage": "nature descriptions"
      }
    },

    "√kakhati": {
      "meaning": "to scratch, scrape",
      "type": "primary",
      "frequency": "very_low",
      "attestation": "commentarial",
      "stems": {
        "present": "kakha",
        "aorist": "akakhi",
        "perfect": "cakakha",
        "passive": "kakhīya",
        "causative": "kakhāpe",
        "past_participle": "kakhita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 80,
      "generation_hints": {
        "scratching_action": "surface abrasion",
        "usage": "physical descriptions"
      }
    },

    "√ulūk": {
      "meaning": "to hoot, make owl sounds",
      "type": "primary",
      "frequency": "very_low",
      "attestation": "literary",
      "stems": {
        "present": "ulūka",
        "aorist": "aulūki",
        "perfect": "ululūka",
        "passive": "ulūkīya",
        "causative": "ulūkāpe",
        "past_participle": "ulūkita"
      },
      "prefixes": ["ā"],
      "generates_forms": 70,
      "generation_hints": {
        "onomatopoetic": "owl call imitation",
        "usage": "poetic descriptions"
      }
    },

    "√jhajjhati": {
      "meaning": "to burn fiercely, blaze",
      "type": "primary",
      "frequency": "very_low",
      "attestation": "late_texts",
      "stems": {
        "present": "jhajjha",
        "aorist": "ajhajjhi",
        "perfect": "jajhajjha",
        "passive": "jhajjhīya",
        "causative": "jhajjhāpe",
        "past_participle": "jhajjhita"
      },
      "prefixes": ["ā"],
      "generates_forms": 70,
      "generation_hints": {
        "intensive_burning": "fierce combustion",
        "usage": "descriptive contexts"
      }
    },

    "√dhaṭṭhati": {
      "meaning": "to be bold, impudent",
      "type": "primary",
      "frequency": "very_low",
      "attestation": "late_canonical",
      "stems": {
        "present": "dhaṭṭha",
        "aorist": "adhaṭṭhi",
        "perfect": "dadhaṭṭha",
        "passive": "dhaṭṭhīya",
        "causative": "dhaṭṭhāpe",
        "past_participle": "dhaṭṭhita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "boldness_impudence": "shameless behavior",
        "usage": "character descriptions"
      }
    },

    "√kūṭ": {
      "meaning": "to deceive, cheat",
      "type": "primary",
      "frequency": "very_low",
      "attestation": "ethical_texts",
      "stems": {
        "present": "kūṭa",
        "aorist": "akūṭi",
        "perfect": "cukūṭa",
        "passive": "kūṭīya",
        "causative": "kūṭāpe",
        "past_participle": "kūṭita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "deception_focus": "fraudulent behavior",
        "usage": "ethical discussions"
      }
    },

    "√ḍaṃs": {
      "meaning": "to bite, sting",
      "type": "primary",
      "frequency": "very_low",
      "attestation": "natural_descriptions",
      "stems": {
        "present": "ḍasa",
        "aorist": "aḍaṃsi",
        "perfect": "daḍaṃsa",
        "passive": "ḍasīya",
        "causative": "ḍasāpe",
        "past_participle": "daṭṭha"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "pali_change": "ḍaṃs > ḍas",
        "biting_action": "animal attacks",
        "irregular_participle": "daṭṭha"
      }
    },

    "√mṛj": {
      "meaning": "to polish, burnish",
      "type": "primary",
      "frequency": "very_low",
      "attestation": "technical_descriptions",
      "stems": {
        "present": "majja",
        "aorist": "amṛji",
        "perfect": "mamṛja",
        "passive": "majjīya",
        "causative": "majjāpe",
        "past_participle": "mṛjita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 80,
      "generation_hints": {
        "different_from": "previous √mṛj",
        "polishing_focus": "surface refinement",
        "usage": "craft descriptions"
      }
    },

    "√kṣvel": {
      "meaning": "to sound loudly, resound",
      "type": "primary",
      "frequency": "very_low",
      "attestation": "poetic",
      "stems": {
        "present": "khela",
        "aorist": "akṣveli",
        "perfect": "cakṣvela",
        "passive": "khelīya",
        "causative": "khelāpe",
        "past_participle": "kṣvelita"
      },
      "prefixes": ["ā"],
      "generates_forms": 70,
      "generation_hints": {
        "different_usage": "loud resounding",
        "pali_change": "kṣv > kh",
        "usage": "sound descriptions"
      }
    },

    "√jhaṃp": {
      "meaning": "to jump suddenly, leap",
      "type": "primary",
      "frequency": "very_low",
      "attestation": "narrative_texts",
      "stems": {
        "present": "jhaṃpa",
        "aorist": "ajhaṃpi",
        "perfect": "jajhaṃpa",
        "passive": "jhaṃpīya",
        "causative": "jhaṃpāpe",
        "past_participle": "jhaṃpita"
      },
      "prefixes": ["ā", "ud"],
      "generates_forms": 80,
      "generation_hints": {
        "sudden_movement": "abrupt leaping",
        "usage": "action descriptions"
      }
    },

    "√thak": {
      "meaning": "to cover, conceal",
      "type": "primary",
      "frequency": "very_low",
      "attestation": "commentarial",
      "stems": {
        "present": "thaka",
        "aorist": "athaki",
        "perfect": "tatthaka",
        "passive": "thakīya",
        "causative": "thakāpe",
        "past_participle": "thakita"
      },
      "prefixes": ["ā", "pari"],
      "generates_forms": 70,
      "generation_hints": {
        "concealment_focus": "hiding from view",
        "usage": "descriptive contexts"
      }
    },

    "√duṭṭh": {
      "meaning": "to be corrupted, spoiled",
      "type": "primary",
      "frequency": "very_low",
      "attestation": "ethical_texts",
      "stems": {
        "present": "duṭṭha",
        "aorist": "aduṭṭhi",
        "perfect": "daduṭṭha",
        "passive": "duṭṭhīya",
        "causative": "doṭṭhāpe",
        "past_participle": "duṭṭha"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "corruption_focus": "moral degradation",
        "usage": "ethical discussions"
      }
    },

    "√khalīti": {
      "meaning": "to be bald, become bare",
      "type": "primary",
      "frequency": "very_low",
      "attestation": "descriptive_texts",
      "stems": {
        "present": "khalī",
        "aorist": "akhalīti",
        "perfect": "cakhalī",
        "passive": "khalīya",
        "causative": "khalīpe",
        "past_participle": "khalīta"
      },
      "prefixes": ["ā"],
      "generates_forms": 70,
      "generation_hints": {
        "baldness_focus": "loss of hair",
        "usage": "physical descriptions"
      }
    },

    "√ghaṭṭ": {
      "meaning": "to rub against, friction",
      "type": "primary",
      "frequency": "very_low",
      "attestation": "technical_texts",
      "stems": {
        "present": "ghaṭṭa",
        "aorist": "aghaṭṭi",
        "perfect": "jaghaṭṭa",
        "passive": "ghaṭṭīya",
        "causative": "ghaṭṭāpe",
        "past_participle": "ghaṭṭita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 80,
      "generation_hints": {
        "friction_focus": "rubbing contact",
        "usage": "technical descriptions"
      }
    },

    "√ṭhaṅk": {
      "meaning": "to limp, walk lamely",
      "type": "primary",
      "frequency": "very_low",
      "attestation": "narrative_texts",
      "stems": {
        "present": "ṭhaṅka",
        "aorist": "aṭhaṅki",
        "perfect": "taṭhaṅka",
        "passive": "ṭhaṅkīya",
        "causative": "ṭhaṅkāpe",
        "past_participle": "ṭhaṅkita"
      },
      "prefixes": ["ā"],
      "generates_forms": 70,
      "generation_hints": {
        "limping_focus": "impaired walking",
        "usage": "character descriptions"
      }
    },

    "√kuṇṭh": {
      "meaning": "to be blunt, dull",
      "type": "primary",
      "frequency": "very_low",
      "attestation": "technical_texts",
      "stems": {
        "present": "kuṇṭha",
        "aorist": "akuṇṭhi",
        "perfect": "cukuṇṭha",
        "passive": "kuṇṭhīya",
        "causative": "kuṇṭhāpe",
        "past_participle": "kuṇṭhita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "bluntness_focus": "loss of sharpness",
        "usage": "tool descriptions"
      }
    },

    "√ḍubh": {
      "meaning": "to sink, submerge",
      "type": "primary",
      "frequency": "very_low",
      "attestation": "narrative_texts",
      "stems": {
        "present": "ḍubha",
        "aorist": "aḍubhi",
        "perfect": "daḍubha",
        "passive": "ḍubhīya",
        "causative": "ḍobhāpe",
        "past_participle": "ḍubba"
      },
      "prefixes": ["ā", "ni"],
      "generates_forms": 80,
      "generation_hints": {
        "sinking_focus": "going underwater",
        "causative_change": "ḍobh- not ḍubh-"
      }
    },

    "√tiṇ": {
      "meaning": "to be sharp, pointed",
      "type": "primary",
      "frequency": "very_low",
      "attestation": "technical_descriptions",
      "stems": {
        "present": "tiṇa",
        "aorist": "atiṇi",
        "perfect": "tatiṇa",
        "passive": "tiṇīya",
        "causative": "tiṇāpe",
        "past_participle": "tiṇṇa"
      },
      "prefixes": ["ā"],
      "generates_forms": 70,
      "generation_hints": {
        "sharpness_focus": "pointed quality",
        "usage": "tool descriptions"
      }
    },

    "√ghargh": {
      "meaning": "to gargle, gurgle",
      "type": "primary",
      "frequency": "very_low",
      "attestation": "medical_texts",
      "stems": {
        "present": "gaggha",
        "aorist": "agarghi",
        "perfect": "jagargha",
        "passive": "gagghīya",
        "causative": "gagghāpe",
        "past_participle": "garghita"
      },
      "prefixes": ["ā"],
      "generates_forms": 70,
      "generation_hints": {
        "pali_change": "ghargh > gaggha",
        "throat_sound": "liquid in throat",
        "usage": "medical procedures"
      }
    },

    "√khāṇu": {
      "meaning": "to dig, excavate",
      "type": "primary",
      "frequency": "very_low",
      "attestation": "technical_texts",
      "stems": {
        "present": "khāṇa",
        "aorist": "akhāṇi",
        "perfect": "cakhāṇa",
        "passive": "khāṇīya",
        "causative": "khāṇāpe",
        "past_participle": "khāta"
      },
      "prefixes": ["ā", "ud"],
      "generates_forms": 80,
      "generation_hints": {
        "digging_focus": "earth excavation",
        "irregular_participle": "khāta"
      }
    },

    "√pipīlika": {
      "meaning": "to move like ants, swarm",
      "type": "denominative",
      "frequency": "very_low",
      "attestation": "nature_descriptions",
      "stems": {
        "present": "pipīlika",
        "aorist": "apipīliki",
        "perfect": "papipīlika",
        "passive": "pipīlikīya",
        "causative": "pipīlikāpe",
        "past_participle": "pipīlikita"
      },
      "prefixes": ["ā"],
      "generates_forms": 70,
      "generation_hints": {
        "ant_movement": "swarming motion",
        "denominative_origin": "from pipīlikā 'ant'",
        "usage": "metaphorical descriptions"
      }
    },

    "√kṛkala": {
      "meaning": "to make partridge sounds",
      "type": "denominative",
      "frequency": "very_low",
      "attestation": "literary",
      "stems": {
        "present": "kakala",
        "aorist": "akakali",
        "perfect": "cakakala",
        "passive": "kakalīya",
        "causative": "kakalāpe",
        "past_participle": "kakalita"
      },
      "prefixes": ["ā"],
      "generates_forms": 70,
      "generation_hints": {
        "pali_change": "kṛk > kak",
        "bird_sound": "partridge call",
        "usage": "nature poetry"
      }
    },

    "√bhṛṅga": {
      "meaning": "to buzz like bees",
      "type": "denominative",
      "frequency": "very_low",
      "attestation": "poetic",
      "stems": {
        "present": "bhaṅga",
        "aorist": "abhaṅgi",
        "perfect": "babhaṅga",
        "passive": "bhaṅgīya",
        "causative": "bhaṅgāpe",
        "past_participle": "bhaṅgita"
      },
      "prefixes": ["ā"],
      "generates_forms": 70,
      "generation_hints": {
        "pali_change": "bhṛṅg > bhaṅg",
        "bee_sound": "buzzing noise",
        "usage": "poetic descriptions"
      }
    },

    "√jhiṅk": {
      "meaning": "to chirp, make cricket sounds",
      "type": "primary",
      "frequency": "very_low",
      "attestation": "nature_descriptions",
      "stems": {
        "present": "jhiṅka",
        "aorist": "ajhiṅki",
        "perfect": "jajhiṅka",
        "passive": "jhiṅkīya",
        "causative": "jhiṅkāpe",
        "past_participle": "jhiṅkita"
      },
      "prefixes": ["ā"],
      "generates_forms": 70,
      "generation_hints": {
        "cricket_sound": "insect chirping",
        "onomatopoetic": "sound imitation",
        "usage": "natural sound descriptions"
      }
    },

    "√thuthuti": {
      "meaning": "to praise, eulogize",
      "type": "denominative",
      "frequency": "very_low",
      "attestation": "late_commentaries",
      "stems": {
        "present": "thuthu",
        "aorist": "athuthuti",
        "perfect": "tathuthu",
        "passive": "thuthīya",
        "causative": "thuthāpe",
        "past_participle": "thuthita"
      },
      "prefixes": ["ā"],
      "generates_forms": 70,
      "generation_hints": {
        "praise_focus": "elaborate eulogy",
        "reduplicated_origin": "intensive praise",
        "usage": "ceremonial contexts"
      }
    },

    "√ḍaḍḍha": {
      "meaning": "to burn completely, be consumed",
      "type": "intensive",
      "frequency": "very_low",
      "attestation": "descriptive_texts",
      "stems": {
        "present": "ḍaḍḍha",
        "aorist": "aḍaḍḍhi",
        "perfect": "daḍaḍḍha",
        "passive": "ḍaḍḍhīya",
        "causative": "ḍaḍḍhāpe",
        "past_participle": "ḍaḍḍha"
      },
      "prefixes": ["ā"],
      "generates_forms": 70,
      "generation_hints": {
        "intensive_burning": "complete combustion",
        "reduplicated_form": "intensive aspect",
        "usage": "destruction descriptions"
      }
    },

    "√kacch": {
      "meaning": "to move sideways, go crabwise",
      "type": "primary",
      "frequency": "very_low",
      "attestation": "movement_descriptions",
      "stems": {
        "present": "kaccha",
        "aorist": "akacchi",
        "perfect": "cakaccha",
        "passive": "kacchīya",
        "causative": "kacchāpe",
        "past_participle": "kacchita"
      },
      "prefixes": ["ā"],
      "generates_forms": 70,
      "generation_hints": {
        "sideways_movement": "lateral motion",
        "crab_like": "sideways scuttling",
        "usage": "animal movement descriptions"
      }
    },

    "√ḍimbh": {
      "meaning": "to move like a young animal",
      "type": "primary",
      "frequency": "very_low",
      "attestation": "animal_descriptions",
      "stems": {
        "present": "ḍimbha",
        "aorist": "aḍimbhi",
        "perfect": "daḍimbha",
        "passive": "ḍimbhīya",
        "causative": "ḍimbhāpe",
        "past_participle": "ḍimbhita"
      },
      "prefixes": ["ā"],
      "generates_forms": 70,
      "generation_hints": {
        "young_animal_movement": "awkward juvenile motion",
        "usage": "animal behavior descriptions"
      }
    },
  
    "√budh_variant_1": {
      "meaning": "to awaken, understand",
      "type": "class_transfer_variant",
      "base_root": "√budh",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "bodha",
        "aorist": "abodhi",
        "perfect": "bubodha",
        "passive": "bodhīya",
        "causative": "bodhāpe",
        "past_participle": "buddha"
      },
      "prefixes": ["ā", "sam", "pra"],
      "generates_forms": 140,
      "generation_hints": {
        "class_difference": "Class I vs VII (bujjh-)",
        "variant_type": "older Vedic formation",
        "usage": "mainly in compounds and causatives"
      }
    },

    "√gam_variant_1": {
      "meaning": "to go, move",
      "type": "stem_alternation",
      "base_root": "√gam",
      "frequency": "low",
      "attestation": "archaic_canonical",
      "stems": {
        "present": "gama",
        "aorist": "agami",
        "perfect": "jagāma",
        "passive": "gamīya",
        "causative": "game",
        "past_participle": "gata"
      },
      "prefixes": ["ā", "upa", "sam"],
      "generates_forms": 120,
      "generation_hints": {
        "vs_standard": "gama- vs gaccha-",
        "variant_type": "unthematized present",
        "usage": "archaic and poetic contexts"
      }
    },

    "√dā_variant_1": {
      "meaning": "to give",
      "type": "stem_alternation",
      "base_root": "√dā",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "de",
        "aorist": "adāsi",
        "perfect": "dadau",
        "passive": "dīya",
        "causative": "dāpe",
        "past_participle": "datta"
      },
      "prefixes": ["ā", "upa", "pari"],
      "generates_forms": 130,
      "generation_hints": {
        "vs_standard": "deti vs dadāti",
        "variant_type": "simplified present stem",
        "usage": "common in later canonical texts"
      }
    },

    "√car_variant_1": {
      "meaning": "to move, practice",
      "type": "voice_variant",
      "base_root": "√car",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "care",
        "aorist": "acari",
        "perfect": "cacāra",
        "passive": "carīya",
        "causative": "cārāpe",
        "past_participle": "carita"
      },
      "prefixes": ["ā", "vi", "sam"],
      "generates_forms": 140,
      "generation_hints": {
        "voice_difference": "middle voice formation",
        "variant_type": "carate vs carati",
        "usage": "reflexive or intensive meaning"
      }
    },

    "√labh_variant_1": {
      "meaning": "to get, obtain",
      "type": "voice_variant", 
      "base_root": "√labh",
      "frequency": "high",
      "attestation": "canonical",
      "stems": {
        "present": "labbha",
        "aorist": "alabbhi",
        "perfect": "lalābha",
        "passive": "labbha",
        "causative": "lābhāpe",
        "past_participle": "laddha"
      },
      "prefixes": ["ā", "upa", "sam"],
      "generates_forms": 160,
      "generation_hints": {
        "voice_difference": "labbhate vs labhati",
        "variant_type": "passive-like middle formation",
        "usage": "very common passive substitute"
      }
    },

    "√yuj_variant_1": {
      "meaning": "to join, yoke",
      "type": "class_transfer_variant",
      "base_root": "√yuj",
      "frequency": "low",
      "attestation": "commentarial",
      "stems": {
        "present": "yoge",
        "aorist": "ayoji",
        "perfect": "yuyoja",
        "passive": "yogīya",
        "causative": "yogāpe",
        "past_participle": "yutta"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 120,
      "generation_hints": {
        "class_difference": "thematic vs athematic",
        "variant_type": "yogeti formation",
        "usage": "causative-like meanings"
      }
    },

    "√han_variant_1": {
      "meaning": "to strike, kill",
      "type": "morphophonological_variant",
      "base_root": "√han",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "ghāta",
        "aorist": "aghāti",
        "perfect": "jaghāta",
        "passive": "ghātīya",
        "causative": "ghātāpe",
        "past_participle": "ghāta"
      },
      "prefixes": ["ā", "vi", "sam"],
      "generates_forms": 140,
      "generation_hints": {
        "sound_change": "han- → ghāt-",
        "variant_type": "causative stem generalized",
        "usage": "killing/destroying contexts"
      }
    },

    "√vad_variant_1": {
      "meaning": "to speak, say",
      "type": "morphophonological_variant",
      "base_root": "√vad",
      "frequency": "low",
      "attestation": "late_canonical",
      "stems": {
        "present": "vaja",
        "aorist": "avaji",
        "perfect": "vavāja",
        "passive": "vajīya",
        "causative": "vajāpe",
        "past_participle": "vajita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 110,
      "generation_hints": {
        "sound_change": "vad- → vaj-",
        "variant_type": "palatalization variant",
        "usage": "regional dialectical"
      }
    },

    "√pac_variant_1": {
      "meaning": "to cook, ripen",
      "type": "causativization_variant",
      "base_root": "√pac",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "pāce",
        "aorist": "apācesi",
        "perfect": "papāca",
        "passive": "pācīya",
        "causative": "pācāpe",
        "past_participle": "pakka"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 130,
      "generation_hints": {
        "length_difference": "pāc- vs pac-",
        "variant_type": "causative-like formation",
        "usage": "intensive cooking meaning"
      }
    },

    "√rudh_variant_1": {
      "meaning": "to obstruct, confine",
      "type": "class_transfer_variant",
      "base_root": "√rudh",
      "frequency": "low",
      "attestation": "commentarial",
      "stems": {
        "present": "rodha",
        "aorist": "arodhi",
        "perfect": "rurodha",
        "passive": "rodhīya",
        "causative": "rodhāpe",
        "past_participle": "ruddha"
      },
      "prefixes": ["ā", "ni"],
      "generates_forms": 120,
      "generation_hints": {
        "class_difference": "Class I vs VII (rujjh-)",
        "variant_type": "thematic present",
        "usage": "causative and transitive contexts"
      }
    },

    "√chid_variant_1": {
      "meaning": "to cut, sever", 
      "type": "class_transfer_variant",
      "base_root": "√chid",
      "frequency": "low",
      "attestation": "late_texts",
      "stems": {
        "present": "cheda",
        "aorist": "achedi",
        "perfect": "cicheda",
        "passive": "chedīya",
        "causative": "chedāpe",
        "past_participle": "chinna"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 110,
      "generation_hints": {
        "class_difference": "Class I vs VII (chind-)",
        "variant_type": "simple thematic",
        "usage": "causative meanings"
      }
    },

    "√bhid_variant_1": {
      "meaning": "to break, split",
      "type": "class_transfer_variant", 
      "base_root": "√bhid",
      "frequency": "low",
      "attestation": "commentarial",
      "stems": {
        "present": "bheda",
        "aorist": "abhedi",
        "perfect": "bibheda",
        "passive": "bhedīya",
        "causative": "bhedāpe",
        "past_participle": "bhinna"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 110,
      "generation_hints": {
        "class_difference": "Class I vs VII (bhind-)",
        "variant_type": "thematic formation",
        "usage": "transitive breaking"
      }
    },

    "√muc_variant_1": {
      "meaning": "to release, free",
      "type": "class_transfer_variant",
      "base_root": "√muc",
      "frequency": "low",
      "attestation": "late_canonical",
      "stems": {
        "present": "moca",
        "aorist": "amuci",
        "perfect": "mumoca",
        "passive": "mocīya",
        "causative": "mocāpe",
        "past_participle": "mutta"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 110,
      "generation_hints": {
        "class_difference": "Class I vs VII (muñc-)",
        "variant_type": "simple thematic",
        "usage": "causative liberation"
      }
    },

    "√as_variant_1": {
      "meaning": "to be, exist",
      "type": "archaic_variant",
      "base_root": "√as",
      "frequency": "very_low",
      "attestation": "archaic_canonical",
      "stems": {
        "present": "asa",
        "aorist": "āsi",
        "perfect": "āsa",
        "passive": "asīya",
        "causative": "āsāpe",
        "past_participle": "anta"
      },
      "prefixes": ["pra"],
      "generates_forms": 90,
      "generation_hints": {
        "vs_standard": "asa- vs atthi",
        "variant_type": "archaic Vedic formation",
        "usage": "very rare, mainly compounds"
      }
    },

    "√i_variant_1": {
      "meaning": "to go",
      "type": "suppletive_variant",
      "base_root": "√i",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "yā",
        "aorist": "ayi",
        "perfect": "iyāya",
        "passive": "īyīya",
        "causative": "āyāpe",
        "past_participle": "ita"
      },
      "prefixes": ["ā", "upa"],
      "generates_forms": 130,
      "generation_hints": {
        "vs_standard": "yāti vs eti",
        "variant_type": "suppletive present",
        "usage": "especially with prefixes"
      }
    },

    "√kṛ_variant_1": {
      "meaning": "to do, make",
      "type": "stem_alternation",
      "base_root": "√kar",
      "frequency": "high",
      "attestation": "canonical",
      "stems": {
        "present": "kuru",
        "aorist": "akāsi",
        "perfect": "cakāra",
        "passive": "kurīya",
        "causative": "kārāpe",
        "past_participle": "kata"
      },
      "prefixes": ["ā", "sam", "pra"],
      "generates_forms": 170,
      "generation_hints": {
        "vs_standard": "kurute vs karoti",
        "variant_type": "middle voice formation",
        "usage": "reflexive and passive meanings"
      }
    },

    "√bhū_variant_1": {
      "meaning": "to become, be",
      "type": "stem_alternation",
      "base_root": "√bhū",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "hu",
        "aorist": "abhūsi",
        "perfect": "babhūva",
        "passive": "hūyīya",
        "causative": "bhāve",
        "past_participle": "bhūta"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 120,
      "generation_hints": {
        "vs_standard": "hoti vs bhavati",
        "variant_type": "contracted form",
        "usage": "especially in compounds"
      }
    },

    "√vid_variant_1": {
      "meaning": "to know, find",
      "type": "class_transfer_variant",
      "base_root": "√vid",
      "frequency": "low",
      "attestation": "archaic",
      "stems": {
        "present": "veda",
        "aorist": "avedi",
        "perfect": "viveda",
        "passive": "vedīya",
        "causative": "vedāpe",
        "past_participle": "vidita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 120,
      "generation_hints": {
        "vs_standard": "vetti vs vindati",
        "variant_type": "perfect-present",
        "usage": "knowing vs finding"
      }
    },

    "√śru_variant_1": {
      "meaning": "to hear",
      "type": "class_transfer_variant",
      "base_root": "√śru",
      "frequency": "low",
      "attestation": "commentarial",
      "stems": {
        "present": "sava",
        "aorist": "aśravi",
        "perfect": "śuśrāva",
        "passive": "savīya",
        "causative": "sāvāpe",
        "past_participle": "suta"
      },
      "prefixes": ["ā", "anu"],
      "generates_forms": 120,
      "generation_hints": {
        "vs_standard": "savati vs suṇāti",
        "variant_type": "different class formation",
        "usage": "hearing vs listening"
      }
    },

    "√sad_variant_1": {
      "meaning": "to sit",
      "type": "length_variant",
      "base_root": "√sad",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "sāda",
        "aorist": "asādi",
        "perfect": "sasāda",
        "passive": "sādīya",
        "causative": "sādāpe",
        "past_participle": "sanna"
      },
      "prefixes": ["ā", "upa"],
      "generates_forms": 130,
      "generation_hints": {
        "vs_standard": "sādeti vs sīdati",
        "variant_type": "causative-like lengthening",
        "usage": "seat-making vs sitting"
      }
    },

    "√sthā_variant_1": {
      "meaning": "to stand",
      "type": "stem_alternation",
      "base_root": "√ṭhā",
      "frequency": "low",
      "attestation": "archaic",
      "stems": {
        "present": "sthita",
        "aorist": "asthāsi",
        "perfect": "tasthau",
        "passive": "sthīya",
        "causative": "sthāpe",
        "past_participle": "sthita"
      },
      "prefixes": ["ā", "ut"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "sthita- vs tiṭṭh-",
        "variant_type": "Sanskritic formation",
        "usage": "archaic and learned contexts"
      }
    },

    "√gā_variant_1": {
      "meaning": "to sing",
      "type": "stem_alternation",
      "base_root": "√gā",
      "frequency": "low",
      "attestation": "poetic",
      "stems": {
        "present": "gī",
        "aorist": "agāyi",
        "perfect": "jagau",
        "passive": "gīyīya",
        "causative": "gāpe",
        "past_participle": "gīta"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 110,
      "generation_hints": {
        "vs_standard": "gīyati vs gāyati",
        "variant_type": "vowel alternation",
        "usage": "passive and intransitive"
      }
    },

    "√dhā_variant_1": {
      "meaning": "to put, place",
      "type": "class_transfer_variant",
      "base_root": "√dhā",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "dhe",
        "aorist": "adhāsi",
        "perfect": "dadau",
        "passive": "dhīya",
        "causative": "dhāpe",
        "past_participle": "hita"
      },
      "prefixes": ["ā", "upa", "ni"],
      "generates_forms": 140,
      "generation_hints": {
        "vs_standard": "dheti vs dadhāti",
        "variant_type": "simplified present",
        "usage": "later canonical period"
      }
    },

    "√hā_variant_1": {
      "meaning": "to abandon, leave", 
      "type": "stem_alternation",
      "base_root": "√hā",
      "frequency": "low",
      "attestation": "late_canonical",
      "stems": {
        "present": "hī",
        "aorist": "ahāsi",
        "perfect": "jahau",
        "passive": "hīya",
        "causative": "hāpe",
        "past_participle": "hīna"
      },
      "prefixes": ["vi", "pari"],
      "generates_forms": 110,
      "generation_hints": {
        "vs_standard": "hīyati vs jahāti",
        "variant_type": "passive-like formation",
        "usage": "being abandoned vs abandoning"
      }
    },

    "√khād_variant_1": {
      "meaning": "to eat, chew",
      "type": "length_variant",
      "base_root": "√khād",
      "frequency": "low",
      "attestation": "regional",
      "stems": {
        "present": "khā",
        "aorist": "akhādi",
        "perfect": "cakhāda",
        "passive": "khāyīya",
        "causative": "khāpe",
        "past_participle": "khāyita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 110,
      "generation_hints": {
        "vs_standard": "khāyati vs khādati",
        "variant_type": "shortened form",
        "usage": "simple eating vs chewing"
      }
    },

    "√bandh_variant_1": {
      "meaning": "to bind, tie",
      "type": "voice_variant",
      "base_root": "√bandh",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "bajjha",
        "aorist": "abajjhi",
        "perfect": "babandha",
        "passive": "bajjha",
        "causative": "bandhāpe",
        "past_participle": "baddha"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 140,
      "generation_hints": {
        "vs_standard": "bajjhati vs bandhati",
        "variant_type": "passive formation as middle",
        "usage": "being bound vs binding"
      }
    },

    "√grah_variant_1": {
      "meaning": "to grasp, take",
      "type": "morphophonological_variant",
      "base_root": "√gah",
      "frequency": "low",
      "attestation": "archaic",
      "stems": {
        "present": "graha",
        "aorist": "agrahi",
        "perfect": "jagrāha",
        "passive": "grahīya",
        "causative": "grāhāpe",
        "past_participle": "gṛhīta"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 110,
      "generation_hints": {
        "vs_standard": "gṛhṇāti vs gaṇhāti",
        "variant_type": "Sanskritic retention",
        "usage": "learned and archaic texts"
      }
    },

    "√sic_variant_1": {
      "meaning": "to sprinkle, pour",
      "type": "class_transfer_variant",
      "base_root": "√sic",
      "frequency": "low",
      "attestation": "technical",
      "stems": {
        "present": "seca",
        "aorist": "aseci",
        "perfect": "siseca",
        "passive": "secīya",
        "causative": "secāpe",
        "past_participle": "sikta"
      },
      "prefixes": ["ā", "pari"],
      "generates_forms": 110,
      "generation_hints": {
        "vs_standard": "secati vs siñcati",
        "variant_type": "different class",
        "usage": "watering vs sprinkling"
      }
    },

    "√śak_variant_1": {
      "meaning": "to be able, capable",
      "type": "stem_alternation",
      "base_root": "√śak",
      "frequency": "low",
      "attestation": "late_texts",
      "stems": {
        "present": "sake",
        "aorist": "aśaki",
        "perfect": "śaśāka",
        "passive": "sakīya",
        "causative": "sakāpe",
        "past_participle": "śakta"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 110,
      "generation_hints": {
        "vs_standard": "sakoti vs sakkoti",
        "variant_type": "ungeminated formation",
        "usage": "ability vs capability"
      }
    },

    "√pad_variant_1": {
      "meaning": "to fall, go",
      "type": "morphophonological_variant",
      "base_root": "√pad",
      "frequency": "low",
      "attestation": "commentarial",
      "stems": {
        "present": "pāda",
        "aorist": "apādi",
        "perfect": "papāda",
        "passive": "pādīya",
        "causative": "pādāpe",
        "past_participle": "panna"
      },
      "prefixes": ["ā", "upa"],
      "generates_forms": 110,
      "generation_hints": {
        "vs_standard": "pādeti vs pajjati",
        "variant_type": "causative formation",
        "usage": "causing to fall vs falling"
      }
    },

    "√yam_variant_1": {
      "meaning": "to restrain, control",
      "type": "stem_alternation",
      "base_root": "√yam",
      "frequency": "low",
      "attestation": "technical",
      "stems": {
        "present": "yama",
        "aorist": "ayami",
        "perfect": "yayāma",
        "passive": "yamīya",
        "causative": "yamāpe",
        "past_participle": "yata"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 110,
      "generation_hints": {
        "vs_standard": "yamati vs yacchati",
        "variant_type": "unpalatalized form",
        "usage": "control vs restraint"
      }
    },

    "√jīv_variant_1": {
      "meaning": "to live",
      "type": "length_variant",
      "base_root": "√jīv",
      "frequency": "low",
      "attestation": "late_canonical",
      "stems": {
        "present": "jī",
        "aorist": "ajīvi",
        "perfect": "jijīva",
        "passive": "jīyīya",
        "causative": "jīpe",
        "past_participle": "jīta"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 110,
      "generation_hints": {
        "vs_standard": "jīyati vs jīvati",
        "variant_type": "shortened form",
        "usage": "simple being alive"
      }
    },

    "√div_variant_1": {
      "meaning": "to shine, be bright",
      "type": "semantic_variant",
      "base_root": "√div",
      "frequency": "very_low",
      "attestation": "poetic",
      "stems": {
        "present": "deva",
        "aorist": "adevi",
        "perfect": "dideva",
        "passive": "devīya",
        "causative": "devāpe",
        "past_participle": "dyuta"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "different from div 'to play'",
        "variant_type": "different semantic development",
        "usage": "shining vs playing"
      }
    },

    "√sru_variant_1": {
      "meaning": "to flow, stream",
      "type": "stem_alternation",
      "base_root": "√sru",
      "frequency": "low",
      "attestation": "canonical",
      "stems": {
        "present": "sara",
        "aorist": "asari",
        "perfect": "sasāra",
        "passive": "sarīya",
        "causative": "sārāpe",
        "past_participle": "sata"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 120,
      "generation_hints": {
        "vs_standard": "sarati vs savati",
        "variant_type": "different vowel grade",
        "usage": "flowing vs streaming"
      }
    },

    "√kram_variant_1": {
      "meaning": "to step, walk",
      "type": "cluster_simplification",
      "base_root": "√kram",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "kama",
        "aorist": "akāmi",
        "perfect": "cakāma",
        "passive": "kamīya",
        "causative": "kamāpe",
        "past_participle": "kata"
      },
      "prefixes": ["ā", "upa"],
      "generates_forms": 130,
      "generation_hints": {
        "vs_standard": "kamati vs kramati",
        "variant_type": "cluster reduction",
        "usage": "Pali simplification"
      }
    },

    "√śubh_variant_1": {
      "meaning": "to shine, be beautiful",
      "type": "voice_variant",
      "base_root": "√śubh",
      "frequency": "low",
      "attestation": "poetic",
      "stems": {
        "present": "sobhe",
        "aorist": "aśubhi",
        "perfect": "śuśubha",
        "passive": "sobhīya",
        "causative": "sobhāpe",
        "past_participle": "śubhita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 110,
      "generation_hints": {
        "vs_standard": "sobhate vs sobhati",
        "variant_type": "middle voice formation",
        "usage": "self-beautification"
      }
    },

    "√pat_variant_1": {
      "meaning": "to fall, fly",
      "type": "semantic_variant",
      "base_root": "√pat",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "pāta",
        "aorist": "apāti",
        "perfect": "papāta",
        "passive": "pātīya",
        "causative": "pātāpe",
        "past_participle": "pātita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 130,
      "generation_hints": {
        "vs_standard": "pāteti vs patati",
        "variant_type": "causative formation",
        "usage": "causing to fall vs falling"
      }
    },

    "√nam_variant_1": {
      "meaning": "to bend, bow",
      "type": "voice_variant",
      "base_root": "√nam",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "namma",
        "aorist": "anami",
        "perfect": "nanāma",
        "passive": "nammīya",
        "causative": "namāpe",
        "past_participle": "nata"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 130,
      "generation_hints": {
        "vs_standard": "nammati vs namati",
        "variant_type": "intensive gemination",
        "usage": "intensive bending"
      }
    },

    "√vas_variant_1": {
      "meaning": "to dwell, live",
      "type": "length_variant",
      "base_root": "√vas",
      "frequency": "low",
      "attestation": "late_canonical",
      "stems": {
        "present": "vāsa",
        "aorist": "avāsi",
        "perfect": "vavāsa",
        "passive": "vāsīya",
        "causative": "vāsāpe",
        "past_participle": "vāsita"
      },
      "prefixes": ["ā", "ni"],
      "generates_forms": 120,
      "generation_hints": {
        "vs_standard": "vāseti vs vasati",
        "variant_type": "lengthened form",
        "usage": "causing to dwell"
      }
    },

    "√gup_variant_1": {
      "meaning": "to protect, guard",
      "type": "stem_alternation",
      "base_root": "√gup",
      "frequency": "low",
      "attestation": "commentarial",
      "stems": {
        "present": "gūpa",
        "aorist": "agūpi",
        "perfect": "jugūpa",
        "passive": "gūpīya",
        "causative": "gūpāpe",
        "past_participle": "gupta"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 110,
      "generation_hints": {
        "vs_standard": "gūpeti vs gopāyati", 
        "variant_type": "vowel lengthening",
        "usage": "secret protection"
      }
    },

    "√tud_variant_1": {
      "meaning": "to push, strike",
      "type": "class_transfer_variant",
      "base_root": "√tud",
      "frequency": "low",
      "attestation": "technical",
      "stems": {
        "present": "toda",
        "aorist": "atodi",
        "perfect": "tutoda",
        "passive": "todīya",
        "causative": "todāpe",
        "past_participle": "tunna"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 110,
      "generation_hints": {
        "vs_standard": "todeti vs tudati",
        "variant_type": "causative formation",
        "usage": "causing to push vs pushing"
      }
    },

    "√bhās_variant_1": {
      "meaning": "to speak, shine",
      "type": "semantic_differentiation",
      "base_root": "√bhās",
      "frequency": "low",
      "attestation": "literary",
      "stems": {
        "present": "bhāse",
        "aorist": "abhāsi",
        "perfect": "babhāse",
        "passive": "bhāsīya",
        "causative": "bhāsāpe",
        "past_participle": "bhāsita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 110,
      "generation_hints": {
        "vs_standard": "bhāsate vs bhāsati",
        "variant_type": "middle voice for speech",
        "usage": "speaking vs shining"
      }
    },

    "√cint_variant_1": {
      "meaning": "to think, reflect",
      "type": "voice_variant",
      "base_root": "√cint",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "cinte",
        "aorist": "acinti",
        "perfect": "cicinta",
        "passive": "cintīya",
        "causative": "cintāpe",
        "past_participle": "cinta"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 130,
      "generation_hints": {
        "vs_standard": "cintayate vs cinteti",
        "variant_type": "middle voice formation",
        "usage": "self-reflection"
      }
    },

    "√kṣā_variant_1": {
      "meaning": "to burn, destroy",
      "type": "length_variant",
      "base_root": "√kṣa",
      "frequency": "very_low",
      "attestation": "archaic",
      "stems": {
        "present": "khāya",
        "aorist": "akṣāyi",
        "perfect": "cakṣāya",
        "passive": "khāyīya",
        "causative": "khāyāpe",
        "past_participle": "kṣāya"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 90,
      "generation_hints": {
        "pali_change": "kṣā > khāy",
        "variant_type": "rare archaic form",
        "usage": "destruction contexts"
      }
    },

    "√dhyā_variant_1": {
      "meaning": "to meditate, contemplate",
      "type": "pali_adaptation",
      "base_root": "√dhyā",
      "frequency": "low",
      "attestation": "late_canonical",
      "stems": {
        "present": "jhāya",
        "aorist": "ajhāyi",
        "perfect": "jajhāya",
        "passive": "jhāyīya",
        "causative": "jhāyāpe",
        "past_participle": "jhāta"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 120,
      "generation_hints": {
        "pali_change": "dhyā > jhāy",
        "variant_type": "meditation terminology",
        "usage": "contemplative practices"
      }
    },

    "√kṣam_variant_1": {
      "meaning": "to be patient, endure",
      "type": "voice_variant",
      "base_root": "√kṣam",
      "frequency": "low",
      "attestation": "ethical_texts",
      "stems": {
        "present": "khame",
        "aorist": "akṣami",
        "perfect": "cakṣāma",
        "passive": "khamīya",
        "causative": "khamāpe",
        "past_participle": "khanta"
      },
      "prefixes": ["ā", "upa"],
      "generates_forms": 110,
      "generation_hints": {
        "vs_standard": "khamate vs khamati",
        "variant_type": "middle voice patience",
        "usage": "self-forbearance"
      }
    },

    "√trap_variant_1": {
      "meaning": "to be ashamed",
      "type": "voice_variant",
      "base_root": "√trap",
      "frequency": "low",
      "attestation": "late_texts",
      "stems": {
        "present": "trappe",
        "aorist": "atrapi",
        "perfect": "tatrāpa",
        "passive": "trappīya",
        "causative": "trappāpe",
        "past_participle": "trapita"
      },
      "prefixes": ["ā"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "trappate vs trapati",
        "variant_type": "middle voice shame",
        "usage": "self-consciousness"
      }
    },

    "√ghuṣ_variant_1": {
      "meaning": "to sound, make noise",
      "type": "morphophonological_variant",
      "base_root": "√ghuṣ",
      "frequency": "very_low",
      "attestation": "technical",
      "stems": {
        "present": "ghossa",
        "aorist": "aghossi",
        "perfect": "jaghossa",
        "passive": "ghossīya",
        "causative": "ghossāpe",
        "past_participle": "ghoṣita"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "vs_standard": "ghossati vs ghosati",
        "variant_type": "geminated form",
        "usage": "loud sounds"
      }
    },

    "√mlai_variant_1": {
      "meaning": "to wither, fade",
      "type": "stem_alternation",
      "base_root": "√mlā",
      "frequency": "very_low",
      "attestation": "poetic",
      "stems": {
        "present": "milāye",
        "aorist": "amlāyi",
        "perfect": "mamlāya",
        "passive": "milāyīya",
        "causative": "milāyāpe",
        "past_participle": "mlāna"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 90,
      "generation_hints": {
        "vs_standard": "milāyate vs milāyati",
        "variant_type": "middle voice withering",
        "usage": "self-fading"
      }
    },

    "√śliṣ_variant_1": {
      "meaning": "to embrace, stick",
      "type": "class_transfer_variant",
      "base_root": "√śliṣ",
      "frequency": "very_low",
      "attestation": "late_texts",
      "stems": {
        "present": "silesa",
        "aorist": "aślesi",
        "perfect": "śiśleṣa",
        "passive": "silesīya",
        "causative": "silesāpe",
        "past_participle": "śliṣṭa"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "vs_standard": "silesati vs silisati",
        "variant_type": "different class formation",
        "usage": "technical adhesion"
      }
    },

    "√kṣvel_variant_1": {
      "meaning": "to sound, resound",
      "type": "morphophonological_variant",
      "base_root": "√kṣvel",
      "frequency": "very_low", 
      "attestation": "archaic",
      "stems": {
        "present": "khella",
        "aorist": "akṣvelli",
        "perfect": "cakṣvella",
        "passive": "khellīya",
        "causative": "khellāpe",
        "past_participle": "kṣvellita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "vs_standard": "khellati vs khelati",
        "variant_type": "geminated variant",
        "usage": "intensive sound"
      }
    },
   
    "√drā_variant_1": {
      "meaning": "to run, flee",
      "type": "stem_alternation",
      "base_root": "√dru",
      "frequency": "low",
      "attestation": "canonical",
      "stems": {
        "present": "dhāva",
        "aorist": "adrāvi",
        "perfect": "dadrāva",
        "passive": "dhāvīya",
        "causative": "dhāvāpe",
        "past_participle": "dhāvita"
      },
      "prefixes": ["ā", "upa", "pra"],
      "generates_forms": 120,
      "generation_hints": {
        "vs_standard": "dhāvati vs dravati",
        "variant_type": "lengthened grade",
        "usage": "running vs flowing"
      }
    },

    "√vṛdh_variant_1": {
      "meaning": "to grow, increase",
      "type": "morphophonological_variant",
      "base_root": "√vaḍḍh",
      "frequency": "low",
      "attestation": "archaic",
      "stems": {
        "present": "vuddha",
        "aorist": "avṛddhi",
        "perfect": "vavṛddha",
        "passive": "vuddhīya",
        "causative": "vuddhāpe",
        "past_participle": "vṛddha"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 110,
      "generation_hints": {
        "vs_standard": "vuddhati vs vaḍḍhati",
        "variant_type": "Sanskritic retention",
        "usage": "learned contexts"
      }
    },

    "√bhañj_variant_1": {
      "meaning": "to break, destroy",
      "type": "voice_variant",
      "base_root": "√bhañj",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "bhijja",
        "aorist": "abhijji",
        "perfect": "babhañja",
        "passive": "bhijjīya",
        "causative": "bhañjāpe",
        "past_participle": "bhagga"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 130,
      "generation_hints": {
        "vs_standard": "bhijjati vs bhañjati",
        "variant_type": "passive-like middle",
        "usage": "breaking apart vs being broken"
      }
    },

    "√lub_variant_1": {
      "meaning": "to desire, covet",
      "type": "length_variant",
      "base_root": "√lubh",
      "frequency": "low",
      "attestation": "late_canonical",
      "stems": {
        "present": "luba",
        "aorist": "alubi",
        "perfect": "luluba",
        "passive": "lubīya",
        "causative": "lubāpe",
        "past_participle": "lubita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 110,
      "generation_hints": {
        "vs_standard": "lubati vs lubhati",
        "variant_type": "consonant reduction",
        "usage": "simplified form"
      }
    },

    "√spṛś_variant_1": {
      "meaning": "to touch, contact",
      "type": "class_transfer_variant",
      "base_root": "√spṛś",
      "frequency": "low",
      "attestation": "commentarial",
      "stems": {
        "present": "passa",
        "aorist": "aspṛśi",
        "perfect": "pasparśa",
        "passive": "passīya",
        "causative": "passāpe",
        "past_participle": "pasṣṭa"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 110,
      "generation_hints": {
        "vs_standard": "passati vs phusati",
        "variant_type": "different phonetic development",
        "usage": "archaic touching"
      }
    },

    "√klam_variant_1": {
      "meaning": "to be tired, weary",
      "type": "voice_variant",
      "base_root": "√klam",
      "frequency": "low",
      "attestation": "late_texts",
      "stems": {
        "present": "kilame",
        "aorist": "aklami",
        "perfect": "caklāma",
        "passive": "kilamīya",
        "causative": "kilamāpe",
        "past_participle": "kilanta"
      },
      "prefixes": ["ā", "pari"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "kilamate vs kilamati",
        "variant_type": "middle voice weariness",
        "usage": "becoming weary oneself"
      }
    },

    "√vṛj_variant_1": {
      "meaning": "to turn, avoid",
      "type": "morphophonological_variant",
      "base_root": "√vṛj",
      "frequency": "very_low",
      "attestation": "archaic",
      "stems": {
        "present": "vajja",
        "aorist": "avṛji",
        "perfect": "vavarja",
        "passive": "vajjīya",
        "causative": "vajjāpe",
        "past_participle": "vṛjita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 90,
      "generation_hints": {
        "pali_change": "vṛj > vajj",
        "variant_type": "palatalization",
        "usage": "avoidance contexts"
      }
    },

    "√dhuk_variant_1": {
      "meaning": "to milk, extract",
      "type": "stem_alternation",
      "base_root": "√duh",
      "frequency": "low",
      "attestation": "technical",
      "stems": {
        "present": "dhoka",
        "aorist": "adhoki",
        "perfect": "dadhoka",
        "passive": "dhokīya",
        "causative": "dhokāpe",
        "past_participle": "dugdha"
      },
      "prefixes": ["ā", "ni"],
      "generates_forms": 110,
      "generation_hints": {
        "vs_standard": "dhoketi vs dohati",
        "variant_type": "causative-like formation",
        "usage": "extraction processes"
      }
    },

    "√vac_variant_1": {
      "meaning": "to speak, tell",
      "type": "voice_variant",
      "base_root": "√vac",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "ucca",
        "aorist": "avaci",
        "perfect": "uvāca",
        "passive": "uccīya",
        "causative": "uccāpe",
        "past_participle": "ukta"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 130,
      "generation_hints": {
        "vs_standard": "uccati vs vacati",
        "variant_type": "prefix-influenced",
        "usage": "utterance vs speech"
      }
    },

    "√ṛdh_variant_1": {
      "meaning": "to prosper, succeed",
      "type": "morphophonological_variant",
      "base_root": "√ṛdh",
      "frequency": "very_low",
      "attestation": "archaic",
      "stems": {
        "present": "ijjha",
        "aorist": "ārdhi",
        "perfect": "ānṛdha",
        "passive": "ijjhīya",
        "causative": "ijjhāpe",
        "past_participle": "ṛddha"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_change": "ṛdh > ijjh",
        "variant_type": "sound change adaptation",
        "usage": "prosperity contexts"
      }
    },

    "√svap_variant_1": {
      "meaning": "to sleep",
      "type": "voice_variant",
      "base_root": "√svap",
      "frequency": "low",
      "attestation": "late_canonical",
      "stems": {
        "present": "supe",
        "aorist": "asvapi",
        "perfect": "suṣvāpa",
        "passive": "supīya",
        "causative": "supāpe",
        "past_participle": "supta"
      },
      "prefixes": ["ava", "pra"],
      "generates_forms": 110,
      "generation_hints": {
        "vs_standard": "supate vs supati",
        "variant_type": "middle voice sleep",
        "usage": "falling asleep oneself"
      }
    },

    "√lup_variant_1": {
      "meaning": "to cut, break",
      "type": "stem_alternation", 
      "base_root": "√lup",
      "frequency": "very_low",
      "attestation": "technical",
      "stems": {
        "present": "lopa",
        "aorist": "alopi",
        "perfect": "lulopa",
        "passive": "lopīya",
        "causative": "lopāpe",
        "past_participle": "lupta"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "lopeti vs lumpati",
        "variant_type": "causative formation",
        "usage": "elision vs cutting"
      }
    },

    "√vyadh_variant_1": {
      "meaning": "to pierce, wound",
      "type": "morphophonological_variant",
      "base_root": "√vyadh",
      "frequency": "low",
      "attestation": "narrative",
      "stems": {
        "present": "vijjha",
        "aorist": "avyādhi",
        "perfect": "vivyādha",
        "passive": "vijjhīya",
        "causative": "vijjhāpe",
        "past_participle": "viddha"
      },
      "prefixes": ["ā", "ni"],
      "generates_forms": 110,
      "generation_hints": {
        "pali_change": "vyadh > vijjh",
        "variant_type": "cluster simplification",
        "usage": "piercing weapons"
      }
    },

    "√dṛś_variant_1": {
      "meaning": "to see, look",
      "type": "suppletive_variant",
      "base_root": "√dṛś",
      "frequency": "low",
      "attestation": "archaic",
      "stems": {
        "present": "dakka",
        "aorist": "adṛkṣi",
        "perfect": "dadarśa",
        "passive": "dakkīya",
        "causative": "dakkāpe",
        "past_participle": "dṛṣṭa"
      },
      "prefixes": ["ā", "ava"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "dakkati vs passati",
        "variant_type": "archaic formation",
        "usage": "learned contexts"
      }
    },

    "√vṛṇ_variant_1": {
      "meaning": "to choose, select",
      "type": "class_transfer_variant",
      "base_root": "√var",
      "frequency": "low",
      "attestation": "late_canonical",
      "stems": {
        "present": "vaṇa",
        "aorist": "avṛṇi",
        "perfect": "vavṛṇa",
        "passive": "vaṇīya",
        "causative": "vaṇāpe",
        "past_participle": "vṛta"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 110,
      "generation_hints": {
        "vs_standard": "vaṇati vs vareti",
        "variant_type": "different class formation",
        "usage": "selection processes"
      }
    },

    "√jṛmbh_variant_1": {
      "meaning": "to open wide, gape",
      "type": "morphophonological_variant",
      "base_root": "√jṛmbh",
      "frequency": "low",
      "attestation": "descriptive",
      "stems": {
        "present": "jamba",
        "aorist": "ajṛmbhi",
        "perfect": "jajṛmbha",
        "passive": "jambīya",
        "causative": "jambāpe",
        "past_participle": "jṛmbhita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "jambati vs jambhati",
        "variant_type": "cluster reduction",
        "usage": "opening movements"
      }
    },

    "√pṛc_variant_1": {
      "meaning": "to ask, question",
      "type": "morphophonological_variant",
      "base_root": "√pucch",
      "frequency": "very_low",
      "attestation": "archaic",
      "stems": {
        "present": "piccha",
        "aorist": "apṛcci",
        "perfect": "papṛccha",
        "passive": "picchīya",
        "causative": "picchāpe",
        "past_participle": "pṛcchita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 90,
      "generation_hints": {
        "vs_standard": "picchati vs pucchati",
        "variant_type": "vowel alternation",
        "usage": "archaic questioning"
      }
    },

    "√mṛd_variant_1": {
      "meaning": "to rub, grind soft",
      "type": "morphophonological_variant",
      "base_root": "√mṛd",
      "frequency": "very_low",
      "attestation": "technical",
      "stems": {
        "present": "mudda",
        "aorist": "amṛdi",
        "perfect": "mamṛda",
        "passive": "muddīya",
        "causative": "muddāpe",
        "past_participle": "mṛdita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 90,
      "generation_hints": {
        "pali_change": "mṛd > mudd",
        "variant_type": "gemination",
        "usage": "soft grinding"
      }
    },

    "√tṛd_variant_1": {
      "meaning": "to bore, pierce",
      "type": "morphophonological_variant",
      "base_root": "√tṛd",
      "frequency": "very_low",
      "attestation": "technical",
      "stems": {
        "present": "tudda",
        "aorist": "atṛdi",
        "perfect": "tatarda",
        "passive": "tuddīya",
        "causative": "tuddāpe",
        "past_participle": "tṛdita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 90,
      "generation_hints": {
        "pali_change": "tṛd > tudd",
        "variant_type": "gemination variant",
        "usage": "boring holes"
      }
    },

    "√vṛṣ_variant_1": {
      "meaning": "to rain, sprinkle",
      "type": "morphophonological_variant",
      "base_root": "√vass",
      "frequency": "very_low",
      "attestation": "poetic",
      "stems": {
        "present": "vussa",
        "aorist": "avṛṣi",
        "perfect": "vavarṣa",
        "passive": "vussīya",
        "causative": "vussāpe",
        "past_participle": "vṛṣita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 90,
      "generation_hints": {
        "vs_standard": "vussati vs vassati",
        "variant_type": "Sanskritic retention",
        "usage": "poetic precipitation"
      }
    },

    "√krīḍ_variant_1": {
      "meaning": "to play, sport",
      "type": "morphophonological_variant",
      "base_root": "√kīḷ",
      "frequency": "low",
      "attestation": "literary",
      "stems": {
        "present": "kiḷa",
        "aorist": "akriḍi",
        "perfect": "cikrīḍa",
        "passive": "kiḷīya",
        "causative": "kiḷāpe",
        "past_participle": "krīḍita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "kiḷati vs kīḷati",
        "variant_type": "vowel shortening",
        "usage": "playful activity"
      }
    },

    "√kṣud_variant_1": {
      "meaning": "to pound, crush small",
      "type": "morphophonological_variant",
      "base_root": "√kṣud",
      "frequency": "very_low",
      "attestation": "technical",
      "stems": {
        "present": "khuda",
        "aorist": "akṣudi",
        "perfect": "cukṣuda",
        "passive": "khudīya",
        "causative": "khudāpe",
        "past_participle": "kṣudita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 90,
      "generation_hints": {
        "different_from": "√kṣudh 'hunger'",
        "pali_change": "kṣ > kh",
        "usage": "fine crushing"
      }
    },

    "√gṛdh_variant_1": {
      "meaning": "to be greedy, eager",
      "type": "morphophonological_variant",
      "base_root": "√gṛdh",
      "frequency": "low",
      "attestation": "ethical_texts",
      "stems": {
        "present": "giddha",
        "aorist": "agṛdhi",
        "perfect": "jagṛdha",
        "passive": "giddhīya",
        "causative": "giddhāpe",
        "past_participle": "gṛddhita"
      },
      "prefixes": ["ā", "anu"],
      "generates_forms": 110,
      "generation_hints": {
        "pali_change": "gṛdh > giddh",
        "variant_type": "gemination",
        "usage": "greed contexts"
      }
    },

    "√śṛṇ_variant_1": {
      "meaning": "to break, shatter",
      "type": "morphophonological_variant",
      "base_root": "√śṛṇ",
      "frequency": "very_low",
      "attestation": "archaic",
      "stems": {
        "present": "siṇa",
        "aorist": "aśṛṇi",
        "perfect": "śiśṛṇa",
        "passive": "siṇīya",
        "causative": "siṇāpe",
        "past_participle": "śṛṇa"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 90,
      "generation_hints": {
        "pali_change": "śṛṇ > siṇ",
        "variant_type": "rare archaic",
        "usage": "breaking contexts"
      }
    },

    "√gṛh_variant_1": {
      "meaning": "to take, accept",
      "type": "voice_variant",
      "base_root": "√gṛh",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "giṇhe",
        "aorist": "agṛhīt",
        "perfect": "jagrāha",
        "passive": "giṇhīya",
        "causative": "giṇhāpe",
        "past_participle": "gahita"
      },
      "prefixes": ["ā", "pari"],
      "generates_forms": 130,
      "generation_hints": {
        "vs_standard": "giṇhate vs gaṇhāti",
        "variant_type": "middle voice taking",
        "usage": "receiving for oneself"
      }
    },

    "√piś_variant_1": {
      "meaning": "to shape, form",
      "type": "morphophonological_variant",
      "base_root": "√piś",
      "frequency": "very_low",
      "attestation": "craft_texts",
      "stems": {
        "present": "pissa",
        "aorist": "apiśi",
        "perfect": "pipiśa",
        "passive": "pissīya",
        "causative": "pissāpe",
        "past_participle": "piśita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 90,
      "generation_hints": {
        "pali_change": "ś > ss",
        "variant_type": "craft terminology",
        "usage": "artistic shaping"
      }
    },

    "√mṛś_variant_1": {
      "meaning": "to touch, handle",
      "type": "morphophonological_variant",
      "base_root": "√mṛś",
      "frequency": "very_low",
      "attestation": "late_texts",
      "stems": {
        "present": "massa",
        "aorist": "amṛśi",
        "perfect": "mamṛśa",
        "passive": "massīya",
        "causative": "massāpe",
        "past_participle": "mṛśita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 90,
      "generation_hints": {
        "pali_change": "mṛś > mass",
        "variant_type": "gemination",
        "usage": "gentle touching"
      }
    },

    "√dṛh_variant_1": {
      "meaning": "to make firm, strengthen",
      "type": "causativization_variant",
      "base_root": "√dṛh",
      "frequency": "low",
      "attestation": "technical",
      "stems": {
        "present": "daḷhe",
        "aorist": "adṛhi",
        "perfect": "dadṛha",
        "passive": "daḷhīya",
        "causative": "daḷhāpe",
        "past_participle": "dṛḍha"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "daḷheti vs daḷhati",
        "variant_type": "causative formation",
        "usage": "strengthening action"
      }
    },

    "√spand_variant_1": {
      "meaning": "to throb, pulsate",
      "type": "cluster_simplification",
      "base_root": "√spand",
      "frequency": "low",
      "attestation": "medical",
      "stems": {
        "present": "panda",
        "aorist": "aspandi",
        "perfect": "paspanda",
        "passive": "pandīya",
        "causative": "pandāpe",
        "past_participle": "spandita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "pandati vs spandati",
        "variant_type": "initial cluster loss",
        "usage": "pulse descriptions"
      }
    },

    "√sphur_variant_1": {
      "meaning": "to quiver, vibrate",
      "type": "cluster_simplification", 
      "base_root": "√sphur",
      "frequency": "low",
      "attestation": "descriptive",
      "stems": {
        "present": "phura",
        "aorist": "asphuri",
        "perfect": "pusphura",
        "passive": "phurīya",
        "causative": "phurāpe",
        "past_participle": "sphurita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "phureti vs sphureti",
        "variant_type": "cluster reduction",
        "usage": "vibration contexts"
      }
    },

    "√vyā_variant_1": {
      "meaning": "to cover, wrap",
      "type": "morphophonological_variant",
      "base_root": "√vyā",
      "frequency": "very_low",
      "attestation": "technical",
      "stems": {
        "present": "viya",
        "aorist": "avyāyi",
        "perfect": "vivyāya",
        "passive": "viyīya",
        "causative": "viyāpe",
        "past_participle": "vyāta"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 90,
      "generation_hints": {
        "pali_change": "vy > v",
        "variant_type": "cluster simplification",
        "usage": "wrapping actions"
      }
    },

    "√plakṣ_variant_1": {
      "meaning": "to wash, rinse",
      "type": "cluster_simplification",
      "base_root": "√plakṣ",
      "frequency": "very_low",
      "attestation": "ritual_texts",
      "stems": {
        "present": "pakka",
        "aorist": "aplakṣi",
        "perfect": "paplakṣa",
        "passive": "pakkīya",
        "causative": "pakkāpe",
        "past_participle": "plakṣita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 80,
      "generation_hints": {
        "vs_standard": "pakkati vs plakṣati",
        "variant_type": "cluster loss",
        "usage": "ritual washing"
      }
    },

    "√vṛś_variant_1": {
      "meaning": "to tear, rend",
      "type": "morphophonological_variant",
      "base_root": "√vṛś",
      "frequency": "very_low",
      "attestation": "archaic",
      "stems": {
        "present": "vassa",
        "aorist": "avṛśi",
        "perfect": "vavarśa",
        "passive": "vassīya",
        "causative": "vassāpe",
        "past_participle": "vṛśita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 80,
      "generation_hints": {
        "pali_change": "vṛś > vass",
        "different_from": "√vṛṣ rain",
        "usage": "tearing actions"
      }
    },

    "√skhalati_variant_1": {
      "meaning": "to stumble, slip",
      "type": "cluster_simplification",
      "base_root": "√skhal",
      "frequency": "low",
      "attestation": "narrative",
      "stems": {
        "present": "khala",
        "aorist": "askhalī",
        "perfect": "caskāla",
        "passive": "khalīya",
        "causative": "khalāpe",
        "past_participle": "skhalita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "khalati vs skhalati",
        "variant_type": "initial cluster loss",
        "usage": "stumbling motion"
      }
    },

    "√śvas_variant_1": {
      "meaning": "to breathe, pant",
      "type": "voice_variant",
      "base_root": "√śvas",
      "frequency": "low",
      "attestation": "medical",
      "stems": {
        "present": "sase",
        "aorist": "aśvasi",
        "perfect": "śaśvāsa",
        "passive": "sasīya",
        "causative": "sasāpe",
        "past_participle": "śvasita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "sasate vs sasati",
        "variant_type": "middle voice breathing",
        "usage": "heavy breathing"
      }
    },

    "√mlecch_variant_1": {
      "meaning": "to speak barbarously",
      "type": "denominative_variant",
      "base_root": "√mlecch",
      "frequency": "very_low",
      "attestation": "late_commentaries",
      "stems": {
        "present": "miccha",
        "aorist": "amlecchi",
        "perfect": "mamleccha",
        "passive": "micchīya",
        "causative": "micchāpe",
        "past_participle": "mlecchita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "vs_standard": "micchati vs mlecchati",
        "variant_type": "phonetic adaptation",
        "usage": "language criticism"
      }
    },

    "√gṛṇ_variant_1": {
      "meaning": "to sing praise",
      "type": "morphophonological_variant",
      "base_root": "√gṛṇ",
      "frequency": "very_low",
      "attestation": "hymnic",
      "stems": {
        "present": "gaṇa",
        "aorist": "agṛṇī",
        "perfect": "jagṛṇa",
        "passive": "gaṇīya",
        "causative": "gaṇāpe",
        "past_participle": "gṛṇita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 80,
      "generation_hints": {
        "pali_change": "gṛṇ > gaṇ",
        "variant_type": "rare hymnic usage",
        "usage": "praise songs"
      }
    },

    "√vraś_variant_1": {
      "meaning": "to fall, drop",
      "type": "morphophonological_variant", 
      "base_root": "√vraś",
      "frequency": "very_low",
      "attestation": "archaic",
      "stems": {
        "present": "vassa",
        "aorist": "avraśi",
        "perfect": "vavraśa",
        "passive": "vassīya",
        "causative": "vassāpe",
        "past_participle": "vraśita"
      },
      "prefixes": ["ā", "ni"],
      "generates_forms": 80,
      "generation_hints": {
        "pali_change": "vraś > vass",
        "different_from": "√vṛṣ rain",
        "usage": "falling objects"
      }
    },

    "√kṛp_variant_1": {
      "meaning": "to lament, mourn",
      "type": "semantic_variant",
      "base_root": "√kṛp",
      "frequency": "low",
      "attestation": "emotional_texts",
      "stems": {
        "present": "kappa",
        "aorist": "akṛpi",
        "perfect": "cakṛpa",
        "passive": "kappīya",
        "causative": "kappāpe",
        "past_participle": "kṛpta"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "different from kṛp 'pity'",
        "variant_type": "semantic differentiation",
        "usage": "grief expression"
      }
    },

    "√tṛṣ_variant_1": {
      "meaning": "to be thirsty, crave",
      "type": "voice_variant",
      "base_root": "√tṛṣ",
      "frequency": "low",
      "attestation": "psychological_texts",
      "stems": {
        "present": "tusse",
        "aorist": "atṛṣi",
        "perfect": "tatṛṣa",
        "passive": "tussīya",
        "causative": "tussāpe",
        "past_participle": "tṛṣita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "tussate vs tassati",
        "variant_type": "middle voice craving",
        "usage": "psychological thirst"
      }
    },

    "√śṛ_variant_1": {
      "meaning": "to injure, harm",
      "type": "morphophonological_variant",
      "base_root": "√śṛ",
      "frequency": "very_low",
      "attestation": "archaic",
      "stems": {
        "present": "sara",
        "aorist": "aśāri",
        "perfect": "śaśāra",
        "passive": "sarīya",
        "causative": "sārāpe",
        "past_participle": "śṛta"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 80,
      "generation_hints": {
        "pali_change": "śṛ > sar",
        "variant_type": "archaic harm verb",
        "usage": "injury contexts"
      }
    },

    "√pṝ_variant_1": {
      "meaning": "to fill, satisfy",
      "type": "morphophonological_variant",
      "base_root": "√pṝ",
      "frequency": "very_low",
      "attestation": "vedic_retention",
      "stems": {
        "present": "pāra",
        "aorist": "apāri",
        "perfect": "papāra",
        "passive": "pārīya",
        "causative": "pārāpe",
        "past_participle": "pūrṇa"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 80,
      "generation_hints": {
        "pali_change": "pṝ > pār",
        "variant_type": "Vedic retention",
        "usage": "satisfaction contexts"
      }
    },

    "√stṛ_variant_1": {
      "meaning": "to spread, strew",
      "type": "morphophonological_variant",
      "base_root": "√stṛ",
      "frequency": "very_low",
      "attestation": "ritual_texts",
      "stems": {
        "present": "sara",
        "aorist": "astāri",
        "perfect": "tastāra",
        "passive": "sarīya",
        "causative": "sārāpe",
        "past_participle": "stṛta"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 80,
      "generation_hints": {
        "pali_change": "stṛ > sar",
        "variant_type": "cluster loss",
        "usage": "ritual spreading"
      }
    },

    "√rañj_variant_1": {
      "meaning": "to be colored, affected",
      "type": "voice_variant",
      "base_root": "√rañj",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "rajje",
        "aorist": "arañji",
        "perfect": "rarañja",
        "passive": "rajjīya",
        "causative": "rajjāpe",
        "past_participle": "ratta"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "vs_standard": "rajjate vs rañjeti",
        "variant_type": "middle voice coloring",
        "usage": "being emotionally affected"
      }
    },

    "√lip_variant_1": {
      "meaning": "to smear, anoint",
      "type": "voice_variant",
      "base_root": "√lip",
      "frequency": "low",
      "attestation": "ritual_texts",
      "stems": {
        "present": "lippe",
        "aorist": "alipi",
        "perfect": "lilipa",
        "passive": "lippīya",
        "causative": "limpāpe",
        "past_participle": "litta"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "lippate vs limpati",
        "variant_type": "middle voice anointing",
        "usage": "self-anointing"
      }
    },

    "√kṣip_variant_2": {
      "meaning": "to throw, cast",
      "type": "length_variant",
      "base_root": "√kṣip",
      "frequency": "low",
      "attestation": "late_canonical",
      "stems": {
        "present": "khīpa",
        "aorist": "akṣīpi",
        "perfect": "cikṣīpa",
        "passive": "khīpīya",
        "causative": "khīpāpe",
        "past_participle": "kṣīpta"
      },
      "prefixes": ["ā", "ni"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "khīpeti vs khipati",
        "variant_type": "vowel lengthening",
        "usage": "forceful throwing"
      }
    },

    "√añj_variant_1": {
      "meaning": "to anoint, honor",
      "type": "voice_variant",
      "base_root": "√añj",
      "frequency": "low",
      "attestation": "ceremonial",
      "stems": {
        "present": "ajje",
        "aorist": "āñji",
        "perfect": "ānañja",
        "passive": "ajjīya",
        "causative": "ajjāpe",
        "past_participle": "atta"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "ajjate vs añjeti",
        "variant_type": "middle voice anointing",
        "usage": "ceremonial consecration"
      }
    },

    "√sev_variant_1": {
      "meaning": "to serve, honor",
      "type": "voice_variant",
      "base_root": "√sev",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "seve",
        "aorist": "asevi",
        "perfect": "siseva",
        "passive": "sevīya",
        "causative": "sevāpe",
        "past_participle": "sevita"
      },
      "prefixes": ["ā", "upa"],
      "generates_forms": 130,
      "generation_hints": {
        "vs_standard": "sevate vs sevati",
        "variant_type": "middle voice service",
        "usage": "devotional service"
      }
    },

    "√vand_variant_1": {
      "meaning": "to praise, worship",
      "type": "voice_variant",
      "base_root": "√vand",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "vande",
        "aorist": "avandi",
        "perfect": "vavanda",
        "passive": "vandīya",
        "causative": "vandāpe",
        "past_participle": "vandita"
      },
      "prefixes": ["ā", "abhi"],
      "generates_forms": 130,
      "generation_hints": {
        "vs_standard": "vandate vs vandati",
        "variant_type": "middle voice reverence",
        "usage": "self-prostration"
      }
    },

    "√tup_variant_1": {
      "meaning": "to hurt, injure",
      "type": "morphophonological_variant",
      "base_root": "√tup",
      "frequency": "very_low",
      "attestation": "archaic",
      "stems": {
        "present": "tuppa",
        "aorist": "atupi",
        "perfect": "tutopa",
        "passive": "tuppīya",
        "causative": "tuppāpe",
        "past_participle": "tupta"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 80,
      "generation_hints": {
        "variant_type": "gemination variant",
        "usage": "harm contexts"
      }
    },

    "√ghuṣ_variant_1": {
      "meaning": "to rub, chafe",
      "type": "semantic_variant",
      "base_root": "√ghuṣ",
      "frequency": "very_low",
      "attestation": "technical",
      "stems": {
        "present": "ghosa",
        "aorist": "aghuṣi",
        "perfect": "jughuṣa",
        "passive": "ghosīya",
        "causative": "ghosāpe",
        "past_participle": "ghuṣita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 80,
      "generation_hints": {
        "vs_standard": "different from sound meaning",
        "variant_type": "semantic split",
        "usage": "friction contexts"
      }
    },

    "√vyadh_variant_2": {
      "meaning": "to pierce, penetrate",
      "type": "class_transfer_variant",
      "base_root": "√vyadh",
      "frequency": "low",
      "attestation": "technical",
      "stems": {
        "present": "vedha",
        "aorist": "avedhi",
        "perfect": "vivedha",
        "passive": "vedhīya",
        "causative": "vedhāpe",
        "past_participle": "viddha"
      },
      "prefixes": ["ā", "ni"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "vedheti vs vijjhati",
        "variant_type": "causative formation",
        "usage": "technical piercing"
      }
    },

    "√smṛ_variant_1": {
      "meaning": "to remember, recollect",
      "type": "voice_variant",
      "base_root": "√smṛ",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "sare",
        "aorist": "asmṛta",
        "perfect": "sasmāra",
        "passive": "sarīya",
        "causative": "sārāpe",
        "past_participle": "sata"
      },
      "prefixes": ["ā", "anu"],
      "generates_forms": 120,
      "generation_hints": {
        "vs_standard": "sarate vs sarati",
        "variant_type": "middle voice memory",
        "usage": "spontaneous recollection"
      }
    },

    "√spṛh_variant_1": {
      "meaning": "to desire, long for",
      "type": "morphophonological_variant",
      "base_root": "√spṛh",
      "frequency": "very_low",
      "attestation": "emotional_texts",
      "stems": {
        "present": "paha",
        "aorist": "aspṛhi",
        "perfect": "paspṛha",
        "passive": "pahīya",
        "causative": "pahāpe",
        "past_participle": "spṛhita"
      },
      "prefixes": ["ā", "anu"],
      "generates_forms": 80,
      "generation_hints": {
        "pali_change": "spṛh > pah",
        "variant_type": "cluster loss",
        "usage": "emotional longing"
      }
    },

    "√grah_variant_2": {
      "meaning": "to seize, capture",
      "type": "archaic_retention",
      "base_root": "√gah",
      "frequency": "very_low",
      "attestation": "learned_texts",
      "stems": {
        "present": "gṛhṇā",
        "aorist": "agrāhīt",
        "perfect": "jagrāha",
        "passive": "gṛhyīya",
        "causative": "grāhāpe",
        "past_participle": "gṛhīta"
      },
      "prefixes": ["ā", "sam", "pari"],
      "generates_forms": 90,
      "generation_hints": {
        "vs_standard": "gṛhṇāti vs gaṇhāti",
        "variant_type": "complete Sanskritic retention",
        "usage": "very learned, archaic contexts"
      }
    },

    "√tvar_variant_1": {
      "meaning": "to hurry, hasten",
      "type": "morphophonological_variant",
      "base_root": "√tvar",
      "frequency": "low",
      "attestation": "narrative",
      "stems": {
        "present": "tara",
        "aorist": "atvari",
        "perfect": "tatvāra",
        "passive": "tarīya",
        "causative": "tarāpe",
        "past_participle": "tvarita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_change": "tvar > tar",
        "variant_type": "consonant cluster simplification",
        "usage": "hurried motion"
      }
    },

    "√sthag_variant_1": {
      "meaning": "to cover, conceal",
      "type": "morphophonological_variant",
      "base_root": "√sthag",
      "frequency": "very_low",
      "attestation": "archaic",
      "stems": {
        "present": "chāda",
        "aorist": "asthagi",
        "perfect": "tasthāga",
        "passive": "chādīya",
        "causative": "chādāpe",
        "past_participle": "sthagita"
      },
      "prefixes": ["ā", "pari"],
      "generates_forms": 80,
      "generation_hints": {
        "pali_change": "sthag > chād",
        "variant_type": "major sound change",
        "usage": "covering actions"
      }
    },

    "√jṛ_variant_1": {
      "meaning": "to grow old, decay",
      "type": "morphophonological_variant",
      "base_root": "√jṛ",
      "frequency": "low",
      "attestation": "aging_contexts",
      "stems": {
        "present": "jīra",
        "aorist": "ajāri",
        "perfect": "jajāra",
        "passive": "jīrīya",
        "causative": "jīrāpe",
        "past_participle": "jīrṇa"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_change": "jṛ > jīr",
        "variant_type": "vowel lengthening",
        "usage": "aging processes"
      }
    },

    "√kṣar_variant_2": {
      "meaning": "to waste away, diminish",
      "type": "semantic_variant",
      "base_root": "√kṣar",
      "frequency": "low",
      "attestation": "medical",
      "stems": {
        "present": "khaya",
        "aorist": "akṣāri",
        "perfect": "cakṣāra",
        "passive": "khayīya",
        "causative": "khayāpe",
        "past_participle": "kṣāra"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "different from flow meaning",
        "variant_type": "semantic specialization",
        "usage": "wasting diseases"
      }
    },

    "√mlā_variant_1": {
      "meaning": "to wilt, fade",
      "type": "voice_variant",
      "base_root": "√mlā",
      "frequency": "low",
      "attestation": "poetic",
      "stems": {
        "present": "mīle",
        "aorist": "amlāyi",
        "perfect": "mamlāya",
        "passive": "mīlīya",
        "causative": "mīlāpe",
        "past_participle": "mlāna"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "mīlate vs milāyati",
        "variant_type": "middle voice withering",
        "usage": "self-wilting"
      }
    },

    "√glai_variant_1": {
      "meaning": "to be weak, languid",
      "type": "morphophonological_variant",
      "base_root": "√glai",
      "frequency": "low",
      "attestation": "medical",
      "stems": {
        "present": "gila",
        "aorist": "aglāyi",
        "perfect": "jaglāya",
        "passive": "gilīya",
        "causative": "gilāpe",
        "past_participle": "glāna"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "gilati vs gilānāti",
        "variant_type": "shortened form",
        "usage": "weakness states"
      }
    },

    "√kṣīṇ_variant_1": {
      "meaning": "to waste away, diminish",
      "type": "morphophonological_variant",
      "base_root": "√kṣīṇ",
      "frequency": "low",
      "attestation": "canonical",
      "stems": {
        "present": "khīṇa",
        "aorist": "akṣīṇī",
        "perfect": "cakṣīṇa",
        "passive": "khīṇīya",
        "causative": "khīṇāpe",
        "past_participle": "kṣīṇa"
      },
      "prefixes": ["ā", "pari"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_change": "kṣ > kh",
        "variant_type": "stative formation",
        "usage": "diminishment states"
      }
    },

    "√bhraṃś_variant_1": {
      "meaning": "to fall, drop",
      "type": "morphophonological_variant",
      "base_root": "√bhraṃś",
      "frequency": "low",
      "attestation": "narrative",
      "stems": {
        "present": "bhaṃsa",
        "aorist": "abhraṃśi",
        "perfect": "babhraṃśa",
        "passive": "bhaṃsīya",
        "causative": "bhaṃsāpe",
        "past_participle": "bhraṣṭa"
      },
      "prefixes": ["ā", "ava"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_change": "bhraṃś > bhaṃs",
        "variant_type": "cluster simplification",
        "usage": "falling from height"
      }
    },

    "√dhvaṃs_variant_1": {
      "meaning": "to destroy, ruin",
      "type": "morphophonological_variant",
      "base_root": "√dhvaṃs",
      "frequency": "low",
      "attestation": "destruction_contexts",
      "stems": {
        "present": "dhaṃsa",
        "aorist": "adhvaṃsi",
        "perfect": "dadhvaṃsa",
        "passive": "dhaṃsīya",
        "causative": "dhaṃsāpe",
        "past_participle": "dhvasta"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_change": "dhvaṃs > dhaṃs",
        "variant_type": "cluster reduction",
        "usage": "destruction contexts"
      }
    },

    "√stambh_variant_1": {
      "meaning": "to support, prop",
      "type": "morphophonological_variant",
      "base_root": "√stambh",
      "frequency": "low",
      "attestation": "technical",
      "stems": {
        "present": "thambha",
        "aorist": "astambhi",
        "perfect": "tastambha",
        "passive": "thamhīya",
        "causative": "thambhāpe",
        "past_participle": "stambhita"
      },
      "prefixes": ["ā", "ut"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_change": "st > th",
        "variant_type": "cluster change",
        "usage": "supporting structures"
      }
    },

    "√kḷp_variant_1": {
      "meaning": "to be suitable, fit",
      "type": "voice_variant",
      "base_root": "√kḷp",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "kappe",
        "aorist": "akḷpi",
        "perfect": "cakḷpa",
        "passive": "kappīya",
        "causative": "kappāpe",
        "past_participle": "kḷpta"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 120,
      "generation_hints": {
        "vs_standard": "kappate vs kappeti",
        "variant_type": "middle voice fitness",
        "usage": "being suitable"
      }
    },

    "√tṛp_variant_1": {
      "meaning": "to be satisfied, content",
      "type": "voice_variant",
      "base_root": "√tṛp",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "tippe",
        "aorist": "atṛpi",
        "perfect": "tatṛpa",
        "passive": "tippīya",
        "causative": "tippāpe",
        "past_participle": "titta"
      },
      "prefixes": ["ā", "pari"],
      "generates_forms": 120,
      "generation_hints": {
        "vs_standard": "tippate vs tappati",
        "variant_type": "middle voice satisfaction",
        "usage": "self-contentment"
      }
    },

    "√dhū_variant_1": {
      "meaning": "to shake off, remove",
      "type": "length_variant",
      "base_root": "√dhū",
      "frequency": "low",
      "attestation": "action_contexts",
      "stems": {
        "present": "dhova",
        "aorist": "adhāvi",
        "perfect": "dadhāva",
        "passive": "dhovīya",
        "causative": "dhovāpe",
        "past_participle": "dhūta"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "dhovati vs dhūnāti",
        "variant_type": "different formation",
        "usage": "washing vs shaking"
      }
    },

    "√pūṣ_variant_1": {
      "meaning": "to nourish, foster",
      "type": "morphophonological_variant",
      "base_root": "√pūṣ",
      "frequency": "low",
      "attestation": "care_contexts",
      "stems": {
        "present": "posa",
        "aorist": "apūṣi",
        "perfect": "pupūṣa",
        "passive": "posīya",
        "causative": "posāpe",
        "past_participle": "puṣṭa"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_change": "pūṣ > pos",
        "variant_type": "sibilant change",
        "usage": "nurturing care"
      }
    },

    "√tuṣ_variant_1": {
      "meaning": "to be pleased, satisfied",
      "type": "voice_variant",
      "base_root": "√tuṣ",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "tusse",
        "aorist": "atuṣi",
        "perfect": "tutosa",
        "passive": "tussīya",
        "causative": "tussāpe",
        "past_participle": "tuṭṭha"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 120,
      "generation_hints": {
        "vs_standard": "tussate vs tussati",
        "variant_type": "middle voice pleasure",
        "usage": "being pleased"
      }
    },

    "√riṣ_variant_1": {
      "meaning": "to be angry, injure",
      "type": "morphophonological_variant",
      "base_root": "√riṣ",
      "frequency": "low",
      "attestation": "emotional_texts",
      "stems": {
        "present": "rissa",
        "aorist": "ariṣi",
        "perfect": "rariṣa",
        "passive": "rissīya",
        "causative": "rissāpe",
        "past_participle": "riṣṭa"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_change": "ṣ > ss",
        "variant_type": "sibilant gemination",
        "usage": "anger expressions"
      }
    },

    "√dviṣ_variant_1": {
      "meaning": "to hate, dislike",
      "type": "morphophonological_variant",
      "base_root": "√dviṣ",
      "frequency": "low",
      "attestation": "emotional_texts",
      "stems": {
        "present": "dissa",
        "aorist": "adviṣi",
        "perfect": "didveṣa",
        "passive": "dissīya",
        "causative": "dissāpe",
        "past_participle": "dviṣṭa"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_change": "dviṣ > diss",
        "variant_type": "cluster simplification",
        "usage": "hatred expressions"
      }
    },

    "√viś_variant_1": {
      "meaning": "to enter, penetrate",
      "type": "voice_variant",
      "base_root": "√viś",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "vise",
        "aorist": "avisi",
        "perfect": "viveśa",
        "passive": "visīya",
        "causative": "visāpe",
        "past_participle": "viṭṭha"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 120,
      "generation_hints": {
        "vs_standard": "visate vs visati",
        "variant_type": "middle voice entry",
        "usage": "entering for oneself"
      }
    },

    "√iṣ_variant_1": {
      "meaning": "to wish, desire",
      "type": "morphophonological_variant",
      "base_root": "√iṣ",
      "frequency": "low",
      "attestation": "desire_contexts",
      "stems": {
        "present": "iccha",
        "aorist": "aiṣi",
        "perfect": "īṣa",
        "passive": "icchīya",
        "causative": "icchāpe",
        "past_participle": "iṣṭa"
      },
      "prefixes": ["ā", "abhi"],
      "generates_forms": 110,
      "generation_hints": {
        "overlap_with": "√icch but different origin",
        "variant_type": "convergent evolution",
        "usage": "strong desire"
      }
    },

    "√uṣ_variant_1": {
      "meaning": "to burn, be hot",
      "type": "morphophonological_variant",
      "base_root": "√uṣ",
      "frequency": "low",
      "attestation": "fire_contexts",
      "stems": {
        "present": "ossa",
        "aorist": "auṣi",
        "perfect": "uvoṣa",
        "passive": "ossīya",
        "causative": "ossāpe",
        "past_participle": "uṣṭa"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_change": "uṣ > oss",
        "variant_type": "sibilant gemination",
        "usage": "burning heat"
      }
    },

    "√dah_variant_1": {
      "meaning": "to burn, consume",
      "type": "voice_variant",
      "base_root": "√dah",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "dahe",
        "aorist": "adahi",
        "perfect": "dadāha",
        "passive": "dahīya",
        "causative": "dahāpe",
        "past_participle": "daḍḍha"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 120,
      "generation_hints": {
        "vs_standard": "dahate vs dahati",
        "variant_type": "middle voice burning",
        "usage": "self-consumption"
      }
    },

    "√plu_variant_1": {
      "meaning": "to swim, float",
      "type": "voice_variant",
      "base_root": "√plu",
      "frequency": "low",
      "attestation": "water_contexts",
      "stems": {
        "present": "plave",
        "aorist": "aplavi",
        "perfect": "puplāva",
        "passive": "plavīya",
        "causative": "plavāpe",
        "past_participle": "pluta"
      },
      "prefixes": ["ā", "ut"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "plavate vs plavati",
        "variant_type": "middle voice swimming",
        "usage": "swimming motion"
      }
    },

    "√sru_variant_2": {
      "meaning": "to flow, leak",
      "type": "voice_variant",
      "base_root": "√sru",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "save",
        "aorist": "asravi",
        "perfect": "susrāva",
        "passive": "savīya",
        "causative": "savāpe",
        "past_participle": "suta"
      },
      "prefixes": ["ā", "ni"],
      "generates_forms": 120,
      "generation_hints": {
        "vs_standard": "savate vs savati",
        "variant_type": "middle voice flowing",
        "usage": "outflow contexts"
      }
    },

    "√kṣar_variant_3": {
      "meaning": "to flow, trickle",
      "type": "voice_variant",
      "base_root": "√kṣar",
      "frequency": "low",
      "attestation": "liquid_contexts",
      "stems": {
        "present": "khare",
        "aorist": "akṣari",
        "perfect": "cakṣāra",
        "passive": "kharīya",
        "causative": "kharāpe",
        "past_participle": "kṣāra"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "kharate vs kharati",
        "variant_type": "middle voice flow",
        "usage": "gentle flowing"
      }
    },

    "√gal_variant_1": {
      "meaning": "to drop, drip",
      "type": "voice_variant",
      "base_root": "√gal",
      "frequency": "low",
      "attestation": "dripping_contexts",
      "stems": {
        "present": "gale",
        "aorist": "agali",
        "perfect": "jagāla",
        "passive": "galīya",
        "causative": "galāpe",
        "past_participle": "galita"
      },
      "prefixes": ["ā", "ni"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "galate vs galati",
        "variant_type": "middle voice dripping",
        "usage": "spontaneous dripping"
      }
    },

    "√pat_variant_2": {
      "meaning": "to fly, soar",
      "type": "semantic_variant",
      "base_root": "√pat",
      "frequency": "medium",
      "attestation": "flight_contexts",
      "stems": {
        "present": "paṭa",
        "aorist": "apaṭi",
        "perfect": "papaṭa",
        "passive": "paṭīya",
        "causative": "paṭāpe",
        "past_participle": "paṭita"
      },
      "prefixes": ["ā", "ud"],
      "generates_forms": 120,
      "generation_hints": {
        "vs_standard": "flying vs falling meaning",
        "variant_type": "semantic differentiation",
        "usage": "aerial movement"
      }
    },

    "√vṛt_variant_1": {
      "meaning": "to turn, revolve",
      "type": "voice_variant",
      "base_root": "√vṛt",
      "frequency": "high",
      "attestation": "canonical",
      "stems": {
        "present": "vatte",
        "aorist": "avartti",
        "perfect": "vavarta",
        "passive": "vattīya",
        "causative": "vattāpe",
        "past_participle": "vaṭṭa"
      },
      "prefixes": ["ā", "ni", "pra", "vi"],
      "generates_forms": 160,
      "generation_hints": {
        "vs_standard": "vattate vs vatteti",
        "variant_type": "middle voice turning",
        "usage": "self-revolving"
      }
    },

    "√jval_variant_1": {
      "meaning": "to burn, blaze",
      "type": "voice_variant",
      "base_root": "√jval",
      "frequency": "low",
      "attestation": "fire_contexts",
      "stems": {
        "present": "jale",
        "aorist": "ajvali",
        "perfect": "jajvāla",
        "passive": "jalīya",
        "causative": "jalāpe",
        "past_participle": "jvalita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "jalate vs jalati",
        "variant_type": "middle voice blazing",
        "usage": "self-ignition"
      }
    },

    "√kamp_variant_1": {
      "meaning": "to tremble, shake",
      "type": "voice_variant",
      "base_root": "√kamp",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "kampe",
        "aorist": "akampi",
        "perfect": "cakampa",
        "passive": "kampīya",
        "causative": "kampāpe",
        "past_participle": "kampita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 120,
      "generation_hints": {
        "vs_standard": "kampate vs kampati",
        "variant_type": "middle voice trembling",
        "usage": "involuntary shaking"
      }
    },

    "√cal_variant_1": {
      "meaning": "to move, stir",
      "type": "voice_variant",
      "base_root": "√cal",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "cale",
        "aorist": "acali",
        "perfect": "cacāla",
        "passive": "calīya",
        "causative": "calāpe",
        "past_participle": "calita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 120,
      "generation_hints": {
        "vs_standard": "calate vs calati",
        "variant_type": "middle voice movement",
        "usage": "self-movement"
      }
    },

    "√nṛt_variant_1": {
      "meaning": "to dance, perform",
      "type": "morphophonological_variant",
      "base_root": "√nṛt",
      "frequency": "low",
      "attestation": "performance_contexts",
      "stems": {
        "present": "nacca",
        "aorist": "anṛti",
        "perfect": "nanarta",
        "passive": "naccīya",
        "causative": "naccāpe",
        "past_participle": "nṛtta"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "naccati vs nṛtyati",
        "variant_type": "Pali adaptation",
        "usage": "dance performance"
      }
    },

    "√gai_variant_1": {
      "meaning": "to sing, chant",
      "type": "voice_variant",
      "base_root": "√gā",
      "frequency": "low",
      "attestation": "musical_contexts",
      "stems": {
        "present": "gāye",
        "aorist": "agāyi",
        "perfect": "jagau",
        "passive": "gāyīya",
        "causative": "gāyāpe",
        "past_participle": "gīta"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "gāyate vs gāyati",
        "variant_type": "middle voice singing",
        "usage": "melodic expression"
      }
    },

    "√kūj_variant_1": {
      "meaning": "to coo, warble",
      "type": "voice_variant",
      "base_root": "√kūj",
      "frequency": "low",
      "attestation": "bird_contexts",
      "stems": {
        "present": "kūje",
        "aorist": "akūji",
        "perfect": "cukūja",
        "passive": "kūjīya",
        "causative": "kūjāpe",
        "past_participle": "kūjita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 90,
      "generation_hints": {
        "vs_standard": "kūjate vs kūjati",
        "variant_type": "middle voice cooing",
        "usage": "bird sounds"
      }
    },

    "√hlād_variant_1": {
      "meaning": "to refresh, gladden",
      "type": "morphophonological_variant",
      "base_root": "√hlād",
      "frequency": "low",
      "attestation": "pleasure_contexts",
      "stems": {
        "present": "lāda",
        "aorist": "ahlādi",
        "perfect": "jahlāda",
        "passive": "lādīya",
        "causative": "lādāpe",
        "past_participle": "hlādita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 100,
      "generation_hints": {
        "pali_change": "hl > l",
        "variant_type": "initial cluster loss",
        "usage": "refreshment contexts"
      }
    },

    "√kṣud_variant_2": {
      "meaning": "to be hungry, starve",
      "type": "voice_variant",
      "base_root": "√kṣudh",
      "frequency": "low",
      "attestation": "hunger_contexts",
      "stems": {
        "present": "khude",
        "aorist": "akṣudhi",
        "perfect": "cukṣudha",
        "passive": "khudīya",
        "causative": "khudāpe",
        "past_participle": "kṣudhita"
      },
      "prefixes": ["ā"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "khudate vs khudhati",
        "variant_type": "middle voice hunger",
        "usage": "experiencing hunger"
      }
    },

    "√tṛṣ_variant_2": {
      "meaning": "to thirst, crave",
      "type": "voice_variant",
      "base_root": "√tṛṣ",
      "frequency": "medium",
      "attestation": "craving_contexts",
      "stems": {
        "present": "tasse",
        "aorist": "atṛṣi",
        "perfect": "tatṛṣa",
        "passive": "tassīya",
        "causative": "tassāpe",
        "past_participle": "tṛṣita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 110,
      "generation_hints": {
        "vs_standard": "tassate vs tassati", 
        "variant_type": "middle voice thirst",
        "usage": "craving states"
      }
    },

    "√mad_variant_1": {
      "meaning": "to be intoxicated, mad",
      "type": "voice_variant",
      "base_root": "√mad",
      "frequency": "medium",
      "attestation": "intoxication_contexts",
      "stems": {
        "present": "matte",
        "aorist": "amadi",
        "perfect": "mamāda",
        "passive": "mattīya",
        "causative": "mattāpe",
        "past_participle": "matta"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 120,
      "generation_hints": {
        "vs_standard": "mattate vs mattati",
        "variant_type": "middle voice intoxication",
        "usage": "being intoxicated"
      }
    },

    "√muh_variant_1": {
      "meaning": "to be confused, deluded",
      "type": "voice_variant",
      "base_root": "√muh",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "muhe",
        "aorist": "amuhi",
        "perfect": "mumuha",
        "passive": "muhīya",
        "causative": "mohāpe",
        "past_participle": "mūḷha"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "vs_standard": "muhate vs muhati",
        "variant_type": "middle voice confusion",
        "usage": "self-delusion"
      }
    },

    "√bhram_variant_1": {
      "meaning": "to wander, err",
      "type": "voice_variant",
      "base_root": "√bhram",
      "frequency": "medium",
      "attestation": "wandering_contexts",
      "stems": {
        "present": "bhame",
        "aorist": "abhrami",
        "perfect": "babhrāma",
        "passive": "bhamīya",
        "causative": "bhamāpe",
        "past_participle": "bhanta"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "vs_standard": "bhamate vs bhamati",
        "variant_type": "middle voice wandering",
        "usage": "aimless wandering"
      }
    },

    "√kṣubh_variant_1": {
      "meaning": "to be agitated, disturbed",
      "type": "voice_variant",
      "base_root": "√kṣubh",
      "frequency": "medium",
      "attestation": "emotional_contexts",
      "stems": {
        "present": "khubhe",
        "aorist": "akṣubhi",
        "perfect": "cukṣubha",
        "passive": "khubbhīya",
        "causative": "khobbhāpe",
        "past_participle": "kṣubdhita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 110,
      "generation_hints": {
        "vs_standard": "khubbhate vs khubbhati",
        "variant_type": "middle voice agitation",
        "usage": "being disturbed"
      }
    },

    "√kṛś_variant_1": {
      "meaning": "to become thin, emaciate",
      "type": "voice_variant",
      "base_root": "√kṛś",
      "frequency": "low",
      "attestation": "thinness_contexts",
      "stems": {
        "present": "kise",
        "aorist": "akṛśi",
        "perfect": "cakṛśa",
        "passive": "kisīya",
        "causative": "kisāpe",
        "past_participle": "kṛśa"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "kisate vs kisati",
        "variant_type": "middle voice thinning",
        "usage": "becoming emaciated"
      }
    },

    "√vyadh_variant_3": {
      "meaning": "to suffer, be in pain",
      "type": "semantic_variant",
      "base_root": "√vyadh",
      "frequency": "low",
      "attestation": "suffering_contexts",
      "stems": {
        "present": "byādhi",
        "aorist": "avyādhi",
        "perfect": "vivyādha",
        "passive": "byādhīya",
        "causative": "byādhāpe",
        "past_participle": "vyādhita"
      },
      "prefixes": ["ā"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "suffering vs piercing",
        "variant_type": "semantic specialization",
        "usage": "disease contexts"
      }
    },

    "√klis_variant_1": {
      "meaning": "to be troubled, afflicted",
      "type": "voice_variant",
      "base_root": "√klis",
      "frequency": "medium",
      "attestation": "suffering_contexts",
      "stems": {
        "present": "kilisse",
        "aorist": "aklisi",
        "perfect": "cikliśa",
        "passive": "kilissīya",
        "causative": "kilesāpe",
        "past_participle": "kiliṭṭha"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 120,
      "generation_hints": {
        "vs_standard": "kilissate vs kilissati",
        "variant_type": "middle voice affliction",
        "usage": "self-affliction"
      }
    },

    "√pīḍ_variant_1": {
      "meaning": "to suffer pain, ache",
      "type": "voice_variant",
      "base_root": "√pīḍ",
      "frequency": "medium",
      "attestation": "pain_contexts",
      "stems": {
        "present": "pīḷe",
        "aorist": "apīḍi",
        "perfect": "pipīḍa",
        "passive": "pīḷīya",
        "causative": "pīḷāpe",
        "past_participle": "pīḷita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 120,
      "generation_hints": {
        "vs_standard": "pīḷate vs pīḷati",
        "variant_type": "middle voice pain",
        "usage": "experiencing pain"
      }
    },

    "√śuc_variant_1": {
      "meaning": "to grieve, lament",
      "type": "voice_variant",
      "base_root": "√śuc",
      "frequency": "medium",
      "attestation": "grief_contexts",
      "stems": {
        "present": "soce",
        "aorist": "aśuci",
        "perfect": "śuśoca",
        "passive": "socīya",
        "causative": "socāpe",
        "past_participle": "śuddha"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "vs_standard": "socate vs socati",
        "variant_type": "middle voice grief",
        "usage": "lamenting"
      }
    },

    "√rud_variant_1": {
      "meaning": "to weep, cry",
      "type": "voice_variant",
      "base_root": "√rud",
      "frequency": "medium",
      "attestation": "crying_contexts",
      "stems": {
        "present": "rude",
        "aorist": "arudi",
        "perfect": "ruroda",
        "passive": "rudīya",
        "causative": "rodāpe",
        "past_participle": "rudita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "vs_standard": "rudate vs rudati",
        "variant_type": "middle voice weeping",
        "usage": "emotional crying"
      }
    },

    "√has_variant_1": {
      "meaning": "to laugh, smile",
      "type": "voice_variant",
      "base_root": "√has",
      "frequency": "medium",
      "attestation": "laughter_contexts",
      "stems": {
        "present": "hase",
        "aorist": "ahasi",
        "perfect": "jahāsa",
        "passive": "hasīya",
        "causative": "hāsāpe",
        "past_participle": "hasita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 120,
      "generation_hints": {
        "vs_standard": "hasate vs hasati",
        "variant_type": "middle voice laughter",
        "usage": "spontaneous laughter"
      }
    },

    "√krīḍ_variant_2": {
      "meaning": "to play, sport",
      "type": "voice_variant",
      "base_root": "√krīḍ",
      "frequency": "low",
      "attestation": "play_contexts",
      "stems": {
        "present": "kīḷe",
        "aorist": "akriḍi",
        "perfect": "cikrīḍa",
        "passive": "kīḷīya",
        "causative": "kīḷāpe",
        "past_participle": "krīḍita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "vs_standard": "kīḷate vs kīḷati",
        "variant_type": "middle voice playing",
        "usage": "recreational activity"
      }
    },

    "√ram_variant_1": {
      "meaning": "to enjoy, delight",
      "type": "voice_variant",
      "base_root": "√ram",
      "frequency": "medium",
      "attestation": "pleasure_contexts",
      "stems": {
        "present": "rame",
        "aorist": "arami",
        "perfect": "rarāma",
        "passive": "ramīya",
        "causative": "ramāpe",
        "past_participle": "rata"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 120,
      "generation_hints": {
        "vs_standard": "ramate vs ramati",
        "variant_type": "middle voice enjoyment",
        "usage": "taking pleasure"
      }
    },

    "√ās_variant_1": {
      "meaning": "to sit, remain",
      "type": "voice_variant",
      "base_root": "√ās",
      "frequency": "high",
      "attestation": "canonical",
      "stems": {
        "present": "āse",
        "aorist": "āsi",
        "perfect": "āsa",
        "passive": "āsīya",
        "causative": "āsāpe",
        "past_participle": "āsīna"
      },
      "prefixes": ["upa", "adhi"],
      "generates_forms": 140,
      "generation_hints": {
        "vs_standard": "āsate vs āsati",
        "variant_type": "middle voice sitting",
        "usage": "settling oneself"
      }
    },

    "√putt-aya": {
      "meaning": "to act like a son, be filial",
      "type": "denominative",
      "base_word": "putta (son)",
      "frequency": "low",
      "attestation": "family_contexts",
      "stems": {
        "present": "puttāya",
        "aorist": "aputtāyi",
        "perfect": "puputtāya",
        "passive": "puttāyīya",
        "causative": "puttāyāpe",
        "past_participle": "puttāyita"
      },
      "prefixes": ["ā", "anu"],
      "generates_forms": 100,
      "generation_hints": {
        "denominative_pattern": "noun + -āya",
        "usage": "family relationship contexts"
      }
    },

    "√dhīt-aya": {
      "meaning": "to act like a daughter, be daughterly",
      "type": "denominative",
      "base_word": "dhītā (daughter)",
      "frequency": "very_low",
      "attestation": "family_contexts",
      "stems": {
        "present": "dhītāya",
        "aorist": "adhītāyi",
        "perfect": "dadhītāya",
        "passive": "dhītāyīya",
        "causative": "dhītāyāpe",
        "past_participle": "dhītāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "noun + -āya",
        "usage": "daughter's behavior"
      }
    },

    "√mātṛ-aya": {
      "meaning": "to act motherly, nurture",
      "type": "denominative",
      "base_word": "mātā (mother)",
      "frequency": "low",
      "attestation": "care_contexts",
      "stems": {
        "present": "mātāya",
        "aorist": "amātāyi",
        "perfect": "mamātāya",
        "passive": "mātāyīya",
        "causative": "mātāyāpe",
        "past_participle": "mātāyita"
      },
      "prefixes": ["ā", "upa"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "kinship + -āya",
        "usage": "maternal behavior"
      }
    },

    "√pitṛ-aya": {
      "meaning": "to act fatherly, be paternal",
      "type": "denominative", 
      "base_word": "pitā (father)",
      "frequency": "low",
      "attestation": "guidance_contexts",
      "stems": {
        "present": "pitāya",
        "aorist": "apitāyi",
        "perfect": "papitāya",
        "passive": "pitāyīya",
        "causative": "pitāyāpe",
        "past_participle": "pitāyita"
      },
      "prefixes": ["ā", "upa"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "kinship + -āya",
        "usage": "paternal guidance"
      }
    },

    "√mittā-aya": {
      "meaning": "to befriend, act friendly",
      "type": "denominative",
      "base_word": "mitta (friend)",
      "frequency": "medium",
      "attestation": "social_contexts",
      "stems": {
        "present": "mittāya",
        "aorist": "amittāyi",
        "perfect": "mamittāya",
        "passive": "mittāyīya",
        "causative": "mittāyāpe",
        "past_participle": "mittāyita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 110,
      "generation_hints": {
        "denominative_pattern": "relationship + -āya",
        "usage": "friendship behavior"
      }
    },

    "√ār-aya": {
      "meaning": "to act as enemy, be hostile",
      "type": "denominative",
      "base_word": "ari (enemy)",
      "frequency": "low",
      "attestation": "conflict_contexts",
      "stems": {
        "present": "arāya",
        "aorist": "aarāyi",
        "perfect": "aarāya",
        "passive": "arāyīya",
        "causative": "arāyāpe",
        "past_participle": "arāyita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "relationship + -āya",
        "usage": "hostile behavior"
      }
    },

    "√rāj-aya": {
      "meaning": "to rule, act as king",
      "type": "denominative",
      "base_word": "rājā (king)",
      "frequency": "medium",
      "attestation": "political_contexts",
      "stems": {
        "present": "rājāya",
        "aorist": "arājāyi",
        "perfect": "rarājāya",
        "passive": "rājāyīya",
        "causative": "rājāyāpe",
        "past_participle": "rājāyita"
      },
      "prefixes": ["ā", "abhi"],
      "generates_forms": 120,
      "generation_hints": {
        "denominative_pattern": "title + -āya",
        "usage": "royal behavior"
      }
    },

    "√brāhmaṇ-aya": {
      "meaning": "to act like a brahmin",
      "type": "denominative",
      "base_word": "brāhmaṇa (brahmin)",
      "frequency": "low",
      "attestation": "caste_contexts",
      "stems": {
        "present": "brāhmaṇāya",
        "aorist": "abrāhmaṇāyi",
        "perfect": "babrāhmaṇāya",
        "passive": "brāhmaṇāyīya",
        "causative": "brāhmaṇāyāpe",
        "past_participle": "brāhmaṇāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "caste + -āya",
        "usage": "brahminical behavior"
      }
    },

    "√kṣatriy-aya": {
      "meaning": "to act like a warrior, be martial",
      "type": "denominative",
      "base_word": "khattiya (warrior)",
      "frequency": "low",
      "attestation": "martial_contexts",
      "stems": {
        "present": "khattiyāya",
        "aorist": "akhattiyāyi",
        "perfect": "cakhattiyāya",
        "passive": "khattiyāyīya",
        "causative": "khattiyāyāpe",
        "past_participle": "khattiyāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "caste + -āya",
        "usage": "warrior behavior"
      }
    },

    "√vaiśy-aya": {
      "meaning": "to act like a merchant",
      "type": "denominative",
      "base_word": "vessa (merchant)",
      "frequency": "very_low",
      "attestation": "trade_contexts",
      "stems": {
        "present": "vessāya",
        "aorist": "avessāyi",
        "perfect": "vavessāya",
        "passive": "vessāyīya",
        "causative": "vessāyāpe",
        "past_participle": "vessāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "caste + -āya",
        "usage": "mercantile behavior"
      }
    },

    "√śūdr-aya": {
      "meaning": "to act like a servant",
      "type": "denominative",
      "base_word": "sudda (servant)",
      "frequency": "very_low",
      "attestation": "service_contexts",
      "stems": {
        "present": "suddāya",
        "aorist": "asuddāyi",
        "perfect": "sasuddāya",
        "passive": "suddāyīya",
        "causative": "suddāyāpe",
        "past_participle": "suddāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "caste + -āya",
        "usage": "servile behavior"
      }
    },

    "√ācāriy-aya": {
      "meaning": "to teach, act as teacher",
      "type": "denominative",
      "base_word": "ācariya (teacher)",
      "frequency": "medium",
      "attestation": "educational_contexts",
      "stems": {
        "present": "ācariyāya",
        "aorist": "aācariyāyi",
        "perfect": "aācariyāya",
        "passive": "ācariyāyīya",
        "causative": "ācariyāyāpe",
        "past_participle": "ācariyāyita"
      },
      "prefixes": ["ā", "upa"],
      "generates_forms": 100,
      "generation_hints": {
        "denominative_pattern": "profession + -āya",
        "usage": "teaching behavior"
      }
    },

    "√antevas-aya": {
      "meaning": "to act as student, study",
      "type": "denominative", 
      "base_word": "antevāsī (student)",
      "frequency": "low",
      "attestation": "learning_contexts",
      "stems": {
        "present": "antevāsāya",
        "aorist": "aantevāsāyi",
        "perfect": "aantevāsāya",
        "passive": "antevāsāyīya",
        "causative": "antevāsāyāpe",
        "past_participle": "antevāsāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "student_role + -āya",
        "usage": "learning behavior"
      }
    },

    "√bhikṣu-aya": {
      "meaning": "to act as monk, be monastic",
      "type": "denominative",
      "base_word": "bhikkhu (monk)",
      "frequency": "medium",
      "attestation": "monastic_contexts",
      "stems": {
        "present": "bhikkhāya",
        "aorist": "abhikkhāyi",
        "perfect": "babhikkhāya",
        "passive": "bhikkhāyīya",
        "causative": "bhikkhāyāpe",
        "past_participle": "bhikkhāyita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 110,
      "generation_hints": {
        "denominative_pattern": "religious_role + -āya",
        "usage": "monastic behavior"
      }
    },

    "√bhikṣuṇ-aya": {
      "meaning": "to act as nun, be nunlike",
      "type": "denominative",
      "base_word": "bhikkhunī (nun)",
      "frequency": "low",
      "attestation": "female_monastic",
      "stems": {
        "present": "bhikkhunāya",
        "aorist": "abhikkhunāyi",
        "perfect": "babhikkhunāya",
        "passive": "bhikkhunāyīya",
        "causative": "bhikkhunāyāpe",
        "past_participle": "bhikkhunāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "female_religious + -āya",
        "usage": "female monastic behavior"
      }
    },

    "√upāsak-aya": {
      "meaning": "to act as lay devotee",
      "type": "denominative",
      "base_word": "upāsaka (lay devotee)",
      "frequency": "low",
      "attestation": "lay_religious",
      "stems": {
        "present": "upāsakāya",
        "aorist": "aupāsakāyi",
        "perfect": "uupāsakāya",
        "passive": "upāsakāyīya",
        "causative": "upāsakāyāpe",
        "past_participle": "upāsakāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "lay_religious + -āya",
        "usage": "lay devotion"
      }
    },

    "√śvet-aya": {
      "meaning": "to make white, whiten",
      "type": "denominative",
      "base_word": "seta (white)",
      "frequency": "low",
      "attestation": "color_contexts",
      "stems": {
        "present": "setāya",
        "aorist": "asetāyi",
        "perfect": "sasetāya",
        "passive": "setāyīya",
        "causative": "setāyāpe",
        "past_participle": "setāyita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "denominative_pattern": "color + -āya",
        "usage": "whitening processes"
      }
    },

    "√kṛṣṇ-aya": {
      "meaning": "to make black, blacken",
      "type": "denominative",
      "base_word": "kaṇha (black)",
      "frequency": "low",
      "attestation": "color_contexts",
      "stems": {
        "present": "kaṇhāya",
        "aorist": "akaṇhāyi",
        "perfect": "cakaṇhāya",
        "passive": "kaṇhāyīya",
        "causative": "kaṇhāyāpe",
        "past_participle": "kaṇhāyita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "denominative_pattern": "color + -āya",
        "usage": "blackening processes"
      }
    },

    "√rohit-aya": {
      "meaning": "to make red, redden",
      "type": "denominative",
      "base_word": "lohita (red)",
      "frequency": "low",
      "attestation": "color_contexts",
      "stems": {
        "present": "lohitāya",
        "aorist": "alohitāyi",
        "perfect": "lalohitāya",
        "passive": "lohitāyīya",
        "causative": "lohitāyāpe",
        "past_participle": "lohitāyita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "denominative_pattern": "color + -āya",
        "usage": "reddening processes"
      }
    },

    "√pīt-aya": {
      "meaning": "to make yellow, turn yellow",
      "type": "denominative",
      "base_word": "pīta (yellow)",
      "frequency": "low",
      "attestation": "color_contexts",
      "stems": {
        "present": "pītāya",
        "aorist": "apītāyi",
        "perfect": "papītāya",
        "passive": "pītāyīya",
        "causative": "pītāyāpe",
        "past_participle": "pītāyita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "denominative_pattern": "color + -āya",
        "usage": "yellowing processes"
      }
    },

    "√nīl-aya": {
      "meaning": "to make blue, turn blue",
      "type": "denominative",
      "base_word": "nīla (blue)",
      "frequency": "low",
      "attestation": "color_contexts",
      "stems": {
        "present": "nīlāya",
        "aorist": "anīlāyi",
        "perfect": "nanīlāya",
        "passive": "nīlāyīya",
        "causative": "nīlāyāpe",
        "past_participle": "nīlāyita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "denominative_pattern": "color + -āya",
        "usage": "bluing processes"
      }
    },

    "√harit-aya": {
      "meaning": "to make green, turn green",
      "type": "denominative",
      "base_word": "harita (green)",
      "frequency": "very_low",
      "attestation": "nature_contexts",
      "stems": {
        "present": "haritāya",
        "aorist": "aharitāyi",
        "perfect": "haharitāya",
        "passive": "haritāyīya",
        "causative": "haritāyāpe",
        "past_participle": "haritāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "color + -āya",
        "usage": "greening vegetation"
      }
    },

    "√siṃh-aya": {
      "meaning": "to act like a lion, be lionlike",
      "type": "denominative",
      "base_word": "sīha (lion)",
      "frequency": "low",
      "attestation": "heroic_contexts",
      "stems": {
        "present": "sīhāya",
        "aorist": "asīhāyi",
        "perfect": "sasīhāya",
        "passive": "sīhāyīya",
        "causative": "sīhāyāpe",
        "past_participle": "sīhāyita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "denominative_pattern": "animal + -āya",
        "usage": "brave behavior"
      }
    },

    "√vyāghr-aya": {
      "meaning": "to act like a tiger, be fierce",
      "type": "denominative",
      "base_word": "byaggha (tiger)",
      "frequency": "very_low",
      "attestation": "fierce_contexts",
      "stems": {
        "present": "byagghāya",
        "aorist": "abyagghāyi",
        "perfect": "babyagghāya",
        "passive": "byagghāyīya",
        "causative": "byagghāyāpe",
        "past_participle": "byagghāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "fierce_animal + -āya",
        "usage": "ferocious behavior"
      }
    },

    "√śṛgāl-aya": {
      "meaning": "to act like a jackal, be cunning",
      "type": "denominative",
      "base_word": "sigāla (jackal)",
      "frequency": "very_low",
      "attestation": "cunning_contexts",
      "stems": {
        "present": "sigālāya",
        "aorist": "asigālāyi",
        "perfect": "sasigālāya",
        "passive": "sigālāyīya",
        "causative": "sigālāyāpe",
        "past_participle": "sigālāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "cunning_animal + -āya",
        "usage": "deceptive behavior"
      }
    },

    "√gaj-aya": {
      "meaning": "to act like an elephant, be majestic",
      "type": "denominative",
      "base_word": "gaja (elephant)",
      "frequency": "low",
      "attestation": "majestic_contexts",
      "stems": {
        "present": "gajāya",
        "aorist": "agajāyi",
        "perfect": "jagajāya",
        "passive": "gajāyīya",
        "causative": "gajāyāpe",
        "past_participle": "gajāyita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "majestic_animal + -āya",
        "usage": "dignified behavior"
      }
    },

    "√aśv-aya": {
      "meaning": "to act like a horse, gallop",
      "type": "denominative",
      "base_word": "assa (horse)",
      "frequency": "low",
      "attestation": "speed_contexts",
      "stems": {
        "present": "assāya",
        "aorist": "aassāyi",
        "perfect": "aassāya",
        "passive": "assāyīya",
        "causative": "assāyāpe",
        "past_participle": "assāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "swift_animal + -āya",
        "usage": "swift movement"
      }
    },

    "√go-aya": {
      "meaning": "to act like a cow, be gentle",
      "type": "denominative",
      "base_word": "go (cow)",
      "frequency": "very_low",
      "attestation": "gentle_contexts",
      "stems": {
        "present": "gavāya",
        "aorist": "agavāyi",
        "perfect": "jagavāya",
        "passive": "gavāyīya",
        "causative": "gavāyāpe",
        "past_participle": "gavāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "domestic_animal + -āya",
        "usage": "gentle behavior"
      }
    },

    "√śvan-aya": {
      "meaning": "to act like a dog, be loyal",
      "type": "denominative",
      "base_word": "suna (dog)",
      "frequency": "very_low",
      "attestation": "loyalty_contexts",
      "stems": {
        "present": "sunāya",
        "aorist": "asunāyi",
        "perfect": "sasunāya",
        "passive": "sunāyīya",
        "causative": "sunāyāpe",
        "past_participle": "sunāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "loyal_animal + -āya",
        "usage": "faithful behavior"
      }
    },

    "√markaṭ-aya": {
      "meaning": "to act like a monkey, be mischievous",
      "type": "denominative",
      "base_word": "makkaṭa (monkey)",
      "frequency": "very_low",
      "attestation": "mischief_contexts",
      "stems": {
        "present": "makkaṭāya",
        "aorist": "amakkaṭāyi",
        "perfect": "mamakkaṭāya",
        "passive": "makkaṭāyīya",
        "causative": "makkaṭāyāpe",
        "past_participle": "makkaṭāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "playful_animal + -āya",
        "usage": "mischievous behavior"
      }
    },

    "√pakṣ-aya": {
      "meaning": "to act like a bird, flutter",
      "type": "denominative",
      "base_word": "pakkhī (bird)",
      "frequency": "very_low",
      "attestation": "flight_contexts",
      "stems": {
        "present": "pakkhāya",
        "aorist": "apakkhāyi",
        "perfect": "papakkhāya",
        "passive": "pakkhāyīya",
        "causative": "pakkhāyāpe",
        "past_participle": "pakkhāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "flying_creature + -āya",
        "usage": "bird-like movement"
      }
    },

    "√matsya-aya": {
      "meaning": "to act like a fish, swim",
      "type": "denominative",
      "base_word": "maccha (fish)",
      "frequency": "very_low",
      "attestation": "swimming_contexts",
      "stems": {
        "present": "macchāya",
        "aorist": "amacchāyi",
        "perfect": "mamacchāya",
        "passive": "macchāyīya",
        "causative": "macchāyāpe",
        "past_participle": "macchāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "aquatic_animal + -āya",
        "usage": "fish-like swimming"
      }
    },

    "√śir-aya": {
      "meaning": "to use the head, head-butt",
      "type": "denominative",
      "base_word": "sira (head)",
      "frequency": "very_low",
      "attestation": "physical_contexts",
      "stems": {
        "present": "sirāya",
        "aorist": "asirāyi",
        "perfect": "sasirāya",
        "passive": "sirāyīya",
        "causative": "sirāyāpe",
        "past_participle": "sirāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "body_part + -āya",
        "usage": "head actions"
      }
    },

    "√kar-aya": {
      "meaning": "to use hands, handle",
      "type": "denominative",
      "base_word": "kara (hand)",
      "frequency": "low",
      "attestation": "manual_contexts",
      "stems": {
        "present": "karāya",
        "aorist": "akarāyi",
        "perfect": "cakarāya",
        "passive": "karāyīya",
        "causative": "karāyāpe",
        "past_participle": "karāyita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "body_part + -āya",
        "usage": "manual manipulation"
      }
    },

    "√pād-aya": {
      "meaning": "to use feet, kick",
      "type": "denominative",
      "base_word": "pāda (foot)",
      "frequency": "low",
      "attestation": "movement_contexts",
      "stems": {
        "present": "pādāya",
        "aorist": "apādāyi",
        "perfect": "papādāya",
        "passive": "pādāyīya",
        "causative": "pādāyāpe",
        "past_participle": "pādāyita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "body_part + -āya",
        "usage": "foot actions"
      }
    },

    "√netr-aya": {
      "meaning": "to use eyes, stare",
      "type": "denominative",
      "base_word": "netta (eye)",
      "frequency": "very_low",
      "attestation": "vision_contexts",
      "stems": {
        "present": "nettāya",
        "aorist": "anettāyi",
        "perfect": "nanettāya",
        "passive": "nettāyīya",
        "causative": "nettāyāpe",
        "past_participle": "nettāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "sense_organ + -āya",
        "usage": "visual actions"
      }
    },

    "√mukh-aya": {
      "meaning": "to use mouth, speak with mouth",
      "type": "denominative",
      "base_word": "mukha (mouth)",
      "frequency": "very_low",
      "attestation": "speech_contexts",
      "stems": {
        "present": "mukhāya",
        "aorist": "amukhāyi",
        "perfect": "mamukhāya",
        "passive": "mukhāyīya",
        "causative": "mukhāyāpe",
        "past_participle": "mukhāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "facial_part + -āya",
        "usage": "oral actions"
      }
    },

    "√hṛd-aya": {
      "meaning": "to take to heart, feel deeply",
      "type": "denominative",
      "base_word": "hadaya (heart)",
      "frequency": "low",
      "attestation": "emotional_contexts",
      "stems": {
        "present": "hadayāya",
        "aorist": "ahadayāyi",
        "perfect": "hahadayāya",
        "passive": "hadayāyīya",
        "causative": "hadayāyāpe",
        "past_participle": "hadayāyita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "emotional_organ + -āya",
        "usage": "emotional responses"
      }
    },

    "√prāṇ-aya": {
      "meaning": "to breathe deeply, live fully",
      "type": "denominative",
      "base_word": "pāṇa (breath/life)",
      "frequency": "low",
      "attestation": "life_contexts",
      "stems": {
        "present": "pāṇāya",
        "aorist": "apāṇāyi",
        "perfect": "papāṇāya",
        "passive": "pāṇāyīya",
        "causative": "pāṇāyāpe",
        "past_participle": "pāṇāyita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "vital_force + -āya",
        "usage": "life processes"
      }
    },

    "√vīry-aya": {
      "meaning": "to show vigor, be energetic",
      "type": "denominative",
      "base_word": "vīriya (energy)",
      "frequency": "medium",
      "attestation": "spiritual_contexts",
      "stems": {
        "present": "vīriyāya",
        "aorist": "avīriyāyi",
        "perfect": "vavīriyāya",
        "passive": "vīriyāyīya",
        "causative": "vīriyāyāpe",
        "past_participle": "vīriyāyita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 110,
      "generation_hints": {
        "denominative_pattern": "spiritual_quality + -āya",
        "usage": "energetic effort"
      }
    },

    "√dhī-aya": {
      "meaning": "to show wisdom, be wise",
      "type": "denominative",
      "base_word": "dhī (wisdom)",
      "frequency": "low",
      "attestation": "wisdom_contexts",
      "stems": {
        "present": "dhīāya",
        "aorist": "adhīāyi",
        "perfect": "dadhīāya",
        "passive": "dhīāyīya",
        "causative": "dhīāyāpe",
        "past_participle": "dhīāyita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "mental_quality + -āya",
        "usage": "wise behavior"
      }
    },

    "√buddh-aya": {
      "meaning": "to act like Buddha, be enlightened",
      "type": "denominative",
      "base_word": "buddha (enlightened one)",
      "frequency": "low",
      "attestation": "religious_contexts",
      "stems": {
        "present": "buddhāya",
        "aorist": "abuddhāyi",
        "perfect": "babuddhāya",
        "passive": "buddhāyīya",
        "causative": "buddhāyāpe",
        "past_participle": "buddhāyita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 100,
      "generation_hints": {
        "denominative_pattern": "enlightened_being + -āya",
        "usage": "enlightened behavior"
      }
    },

    "√bodhisattv-aya": {
      "meaning": "to act like a bodhisattva",
      "type": "denominative",
      "base_word": "bodhisatta (enlightenment being)",
      "frequency": "low",
      "attestation": "mahayana_contexts",
      "stems": {
        "present": "bodhisattāya",
        "aorist": "abodhisattāyi",
        "perfect": "babodhisattāya",
        "passive": "bodhisattāyīya",
        "causative": "bodhisattāyāpe",
        "past_participle": "bodhisattāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "ideal_being + -āya",
        "usage": "compassionate behavior"
      }
    },

    "√arahat-aya": {
      "meaning": "to act like an arahant, be worthy",
      "type": "denominative",
      "base_word": "arahant (worthy one)",
      "frequency": "low",
      "attestation": "attainment_contexts",
      "stems": {
        "present": "arahantāya",
        "aorist": "aarahantāyi",
        "perfect": "aarahantāya",
        "passive": "arahantāyīya",
        "causative": "arahantāyāpe",
        "past_participle": "arahantāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "spiritual_attainment + -āya",
        "usage": "worthy behavior"
      }
    },

    "√dharm-aya": {
      "meaning": "to practice dharma, be righteous",
      "type": "denominative",
      "base_word": "dhamma (dharma)",
      "frequency": "medium",
      "attestation": "ethical_contexts",
      "stems": {
        "present": "dhammāya",
        "aorist": "adhammāyi",
        "perfect": "dadhammāya",
        "passive": "dhammāyīya",
        "causative": "dhammāyāpe",
        "past_participle": "dhammāyita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 110,
      "generation_hints": {
        "denominative_pattern": "spiritual_principle + -āya",
        "usage": "righteous behavior"
      }
    },

    "√karma-aya": {
      "meaning": "to create karma, act purposefully",
      "type": "denominative",
      "base_word": "kamma (karma/action)",
      "frequency": "medium",
      "attestation": "action_contexts",
      "stems": {
        "present": "kammāya",
        "aorist": "akammāyi",
        "perfect": "cakammāya",
        "passive": "kammāyīya",
        "causative": "kammāyāpe",
        "past_participle": "kammāyita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 110,
      "generation_hints": {
        "denominative_pattern": "action_principle + -āya",
        "usage": "intentional action"
      }
    },

    "√saṃsār-aya": {
      "meaning": "to wander in samsara, cycle",
      "type": "denominative",
      "base_word": "saṃsāra (cycle of existence)",
      "frequency": "low",
      "attestation": "cosmological_contexts",
      "stems": {
        "present": "saṃsārāya",
        "aorist": "asaṃsārāyi",
        "perfect": "sasaṃsārāya",
        "passive": "saṃsārāyīya",
        "causative": "saṃsārāyāpe",
        "past_participle": "saṃsārāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "cosmic_cycle + -āya",
        "usage": "cyclical existence"
      }
    },

    "√nirvāṇ-aya": {
      "meaning": "to attain nirvana, be liberated",
      "type": "denominative",
      "base_word": "nibbāna (nirvana)",
      "frequency": "low",
      "attestation": "liberation_contexts",
      "stems": {
        "present": "nibbānāya",
        "aorist": "anibbānāyi",
        "perfect": "nanibbānāya",
        "passive": "nibbānāyīya",
        "causative": "nibbānāyāpe",
        "past_participle": "nibbānāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "ultimate_goal + -āya",
        "usage": "liberation processes"
      }
    },

    "√yug-aya": {
      "meaning": "to behave according to age/era",
      "type": "denominative",
      "base_word": "yuga (age/era)",
      "frequency": "very_low",
      "attestation": "temporal_contexts",
      "stems": {
        "present": "yugāya",
        "aorist": "ayugāyi",
        "perfect": "yuyugāya",
        "passive": "yugāyīya",
        "causative": "yugāyāpe",
        "past_participle": "yugāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "time_period + -āya",
        "usage": "era-appropriate behavior"
      }
    },

    "√kāl-aya": {
      "meaning": "to time, schedule properly",
      "type": "denominative",
      "base_word": "kāla (time)",
      "frequency": "low",
      "attestation": "temporal_contexts",
      "stems": {
        "present": "kālāya",
        "aorist": "akālāyi",
        "perfect": "cakālāya",
        "passive": "kālāyīya",
        "causative": "kālāyāpe",
        "past_participle": "kālāyita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "time + -āya",
        "usage": "temporal coordination"
      }
    },

    "√deś-aya": {
      "meaning": "to behave according to place",
      "type": "denominative",
      "base_word": "desa (place/country)",
      "frequency": "low",
      "attestation": "spatial_contexts",
      "stems": {
        "present": "desāya",
        "aorist": "adesāyi",
        "perfect": "dadesāya",
        "passive": "desāyīya",
        "causative": "desāyāpe",
        "past_participle": "desāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "place + -āya",
        "usage": "location-appropriate behavior"
      }
    },

    "√gṛh-aya": {
      "meaning": "to act domestic, be homely",
      "type": "denominative",
      "base_word": "gaha (house)",
      "frequency": "low",
      "attestation": "domestic_contexts",
      "stems": {
        "present": "gahāya",
        "aorist": "agahāyi",
        "perfect": "jagahāya",
        "passive": "gahāyīya",
        "causative": "gahāyāpe",
        "past_participle": "gahāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "dwelling + -āya",
        "usage": "domestic behavior"
      }
    },

    "√van-aya": {
      "meaning": "to act wild, be forest-like",
      "type": "denominative",
      "base_word": "vana (forest)",
      "frequency": "very_low",
      "attestation": "wilderness_contexts",
      "stems": {
        "present": "vanāya",
        "aorist": "avanāyi",
        "perfect": "vavanāya",
        "passive": "vanāyīya",
        "causative": "vanāyāpe",
        "past_participle": "vanāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "natural_habitat + -āya",
        "usage": "wild behavior"
      }
    },

    "√parvat-aya": {
      "meaning": "to be mountain-like, be steady",
      "type": "denominative",
      "base_word": "pabbata (mountain)",
      "frequency": "very_low",
      "attestation": "stability_contexts",
      "stems": {
        "present": "pabbatāya",
        "aorist": "apabbatāyi",
        "perfect": "papabbatāya",
        "passive": "pabbatāyīya",
        "causative": "pabbatāyāpe",
        "past_participle": "pabbatāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "geographical_feature + -āya",
        "usage": "steadfast behavior"
      }
    },

    "√sāgar-aya": {
      "meaning": "to be ocean-like, be vast",
      "type": "denominative",
      "base_word": "sāgara (ocean)",
      "frequency": "very_low",
      "attestation": "vastness_contexts",
      "stems": {
        "present": "sāgarāya",
        "aorist": "asāgarāyi",
        "perfect": "sasāgarāya",
        "passive": "sāgarāyīya",
        "causative": "sāgarāyāpe",
        "past_participle": "sāgarāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "vast_body + -āya",
        "usage": "vast behavior"
      }
    },

    "√agni-aya": {
      "meaning": "to act like fire, burn fiercely",
      "type": "denominative",
      "base_word": "aggi (fire)",
      "frequency": "low",
      "attestation": "fire_contexts",
      "stems": {
        "present": "aggiāya",
        "aorist": "aaggiāyi",
        "perfect": "aaggiāya",
        "passive": "aggiāyīya",
        "causative": "aggiāyāpe",
        "past_participle": "aggiāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "element + -āya",
        "usage": "fiery behavior"
      }
    },

    "√āp-aya": {
      "meaning": "to act like water, flow",
      "type": "denominative",
      "base_word": "āpo (water)",
      "frequency": "very_low",
      "attestation": "water_contexts",
      "stems": {
        "present": "āpāya",
        "aorist": "aāpāyi",
        "perfect": "aāpāya",
        "passive": "āpāyīya",
        "causative": "āpāyāpe",
        "past_participle": "āpāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "element + -āya",
        "usage": "fluid behavior"
      }
    },

    "√vāyu-aya": {
      "meaning": "to act like wind, be swift",
      "type": "denominative",
      "base_word": "vāyo (wind)",
      "frequency": "very_low",
      "attestation": "speed_contexts",
      "stems": {
        "present": "vāyāya",
        "aorist": "avāyāyi",
        "perfect": "vavāyāya",
        "passive": "vāyāyīya",
        "causative": "vāyāyāpe",
        "past_participle": "vāyāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "element + -āya",
        "usage": "swift behavior"
      }
    },

    "√pṛthvī-aya": {
      "meaning": "to be earth-like, be stable",
      "type": "denominative",
      "base_word": "paṭhavī (earth)",
      "frequency": "very_low",
      "attestation": "stability_contexts",
      "stems": {
        "present": "paṭhavāya",
        "aorist": "apaṭhavāyi",
        "perfect": "papaṭhavāya",
        "passive": "paṭhavāyīya",
        "causative": "paṭhavāyāpe",
        "past_participle": "paṭhavāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "element + -āya",
        "usage": "stable behavior"
      }
    },

    "√sūry-aya": {
      "meaning": "to shine like sun, be radiant",
      "type": "denominative",
      "base_word": "suriya (sun)",
      "frequency": "low",
      "attestation": "radiance_contexts",
      "stems": {
        "present": "suriyāya",
        "aorist": "asuriyāyi",
        "perfect": "sasuriyāya",
        "passive": "suriyāyīya",
        "causative": "suriyāyāpe",
        "past_participle": "suriyāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "celestial_body + -āya",
        "usage": "brilliant behavior"
      }
    },

    "√candr-aya": {
      "meaning": "to be moon-like, be gentle",
      "type": "denominative",
      "base_word": "canda (moon)",
      "frequency": "low",
      "attestation": "gentleness_contexts",
      "stems": {
        "present": "candāya",
        "aorist": "acandāyi",
        "perfect": "cacandāya",
        "passive": "candāyīya",
        "causative": "candāyāpe",
        "past_participle": "candāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "celestial_body + -āya",
        "usage": "gentle behavior"
      }
    },

    "√nakṣatr-aya": {
      "meaning": "to twinkle like stars",
      "type": "denominative",
      "base_word": "nakkhatta (star)",
      "frequency": "very_low",
      "attestation": "poetic_contexts",
      "stems": {
        "present": "nakkhattāya",
        "aorist": "anakkhattāyi",
        "perfect": "nanakkhattāya",
        "passive": "nakkhattāyīya",
        "causative": "nakkhattāyāpe",
        "past_participle": "nakkhattāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "celestial_body + -āya",
        "usage": "twinkling behavior"
      }
    },

    "√ratna-aya": {
      "meaning": "to be gem-like, be precious",
      "type": "denominative",
      "base_word": "ratana (gem)",
      "frequency": "low",
      "attestation": "value_contexts",
      "stems": {
        "present": "ratanāya",
        "aorist": "aratanāyi",
        "perfect": "raratanāya",
        "passive": "ratanāyīya",
        "causative": "ratanāyāpe",
        "past_participle": "ratanāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "precious_object + -āya",
        "usage": "valuable behavior"
      }
    },

    "√maṇi-aya": {
      "meaning": "to sparkle like jewel",
      "type": "denominative",
      "base_word": "maṇi (jewel)",
      "frequency": "very_low",
      "attestation": "beauty_contexts",
      "stems": {
        "present": "maṇāya",
        "aorist": "amaṇāyi",
        "perfect": "mamaṇāya",
        "passive": "maṇāyīya",
        "causative": "maṇāyāpe",
        "past_participle": "maṇāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "precious_stone + -āya",
        "usage": "sparkling behavior"
      }
    },

    "√svarn-aya": {
      "meaning": "to be golden, shine like gold",
      "type": "denominative",
      "base_word": "suvaṇṇa (gold)",
      "frequency": "low",
      "attestation": "wealth_contexts",
      "stems": {
        "present": "suvaṇṇāya",
        "aorist": "asuvaṇṇāyi",
        "perfect": "sasuvaṇṇāya",
        "passive": "suvaṇṇāyīya",
        "causative": "suvaṇṇāyāpe",
        "past_participle": "suvaṇṇāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "precious_metal + -āya",
        "usage": "golden behavior"
      }
    },

    "√rajat-aya": {
      "meaning": "to be silvery, shine like silver",
      "type": "denominative",
      "base_word": "rajata (silver)",
      "frequency": "very_low",
      "attestation": "metal_contexts",
      "stems": {
        "present": "rajatāya",
        "aorist": "arajatāyi",
        "perfect": "rarajatāya",
        "passive": "rajatāyīya",
        "causative": "rajatāyāpe",
        "past_participle": "rajatāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "metal + -āya",
        "usage": "silvery behavior"
      }
    },

    "√puṣp-aya": {
      "meaning": "to bloom like flower, flourish",
      "type": "denominative",
      "base_word": "puppha (flower)",
      "frequency": "low",
      "attestation": "blooming_contexts",
      "stems": {
        "present": "pupphāya",
        "aorist": "apupphāyi",
        "perfect": "papupphāya",
        "passive": "pupphāyīya",
        "causative": "pupphāyāpe",
        "past_participle": "pupphāyita"
      },
      "prefixes": ["ā", "vi"],
      "generates_forms": 100,
      "generation_hints": {
        "denominative_pattern": "plant_part + -āya",
        "usage": "flourishing behavior"
      }
    },

    "√phal-aya": {
      "meaning": "to bear fruit, be fruitful",
      "type": "denominative",
      "base_word": "phala (fruit)",
      "frequency": "medium",
      "attestation": "result_contexts",
      "stems": {
        "present": "phalāya",
        "aorist": "aphalāyi",
        "perfect": "paphalāya",
        "passive": "phalāyīya",
        "causative": "phalāyāpe",
        "past_participle": "phalāyita"
      },
      "prefixes": ["ā", "sam"],
      "generates_forms": 110,
      "generation_hints": {
        "denominative_pattern": "result + -āya",
        "usage": "productive behavior"
      }
    },

    "√bīj-aya": {
      "meaning": "to seed, propagate",
      "type": "denominative",
      "base_word": "bīja (seed)",
      "frequency": "low",
      "attestation": "growth_contexts",
      "stems": {
        "present": "bījāya",
        "aorist": "abījāyi",
        "perfect": "babījāya",
        "passive": "bījāyīya",
        "causative": "bījāyāpe",
        "past_participle": "bījāyita"
      },
      "prefixes": ["ā", "pra"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "origin + -āya",
        "usage": "generative behavior"
      }
    },

    "√vṛkṣ-aya": {
      "meaning": "to be tree-like, stand firm",
      "type": "denominative",
      "base_word": "rukkha (tree)",
      "frequency": "very_low",
      "attestation": "stability_contexts",
      "stems": {
        "present": "rukkhāya",
        "aorist": "arukkhāyi",
        "perfect": "rarukkhāya",
        "passive": "rukkhāyīya",
        "causative": "rukkhāyāpe",
        "past_participle": "rukkhāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "plant + -āya",
        "usage": "steadfast behavior"
      }
    },

    "√latā-aya": {
      "meaning": "to climb like vine, creep",
      "type": "denominative",
      "base_word": "latā (vine)",
      "frequency": "very_low",
      "attestation": "climbing_contexts",
      "stems": {
        "present": "latāya",
        "aorist": "alatāyi",
        "perfect": "lalatāya",
        "passive": "latāyīya",
        "causative": "latāyāpe",
        "past_participle": "latāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "climbing_plant + -āya",
        "usage": "creeping behavior"
      }
    },

    "√anna-aya": {
      "meaning": "to act like food, nourish",
      "type": "denominative",
      "base_word": "anna (food)",
      "frequency": "low",
      "attestation": "nourishment_contexts",
      "stems": {
        "present": "annāya",
        "aorist": "aannāyi",
        "perfect": "aannāya",
        "passive": "annāyīya",
        "causative": "annāyāpe",
        "past_participle": "annāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "sustenance + -āya",
        "usage": "nourishing behavior"
      }
    },

    "√pān-aya": {
      "meaning": "to act like drink, refresh",
      "type": "denominative",
      "base_word": "pāna (drink)",
      "frequency": "very_low",
      "attestation": "refreshment_contexts",
      "stems": {
        "present": "pānāya",
        "aorist": "apānāyi",
        "perfect": "papānāya",
        "passive": "pānāyīya",
        "causative": "pānāyāpe",
        "past_participle": "pānāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "beverage + -āya",
        "usage": "refreshing behavior"
      }
    },

    "√auṣadh-aya": {
      "meaning": "to act like medicine, heal",
      "type": "denominative",
      "base_word": "osadha (medicine)",
      "frequency": "low",
      "attestation": "healing_contexts",
      "stems": {
        "present": "osadhāya",
        "aorist": "aosadhāyi",
        "perfect": "osadhāya",
        "passive": "osadhāyīya",
        "causative": "osadhāyāpe",
        "past_participle": "osadhāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "medicine + -āya",
        "usage": "healing behavior"
      }
    },

    "√viṣ-aya": {
      "meaning": "to act like poison, harm",
      "type": "denominative",
      "base_word": "visa (poison)",
      "frequency": "low",
      "attestation": "harmful_contexts",
      "stems": {
        "present": "visāya",
        "aorist": "avisāyi",
        "perfect": "vavisāya",
        "passive": "visāyīya",
        "causative": "visāyāpe",
        "past_participle": "visāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 90,
      "generation_hints": {
        "denominative_pattern": "harmful_substance + -āya",
        "usage": "toxic behavior"
      }
    },

    "√veṇu-aya": {
      "meaning": "to be bamboo-like, be flexible",
      "type": "denominative",
      "base_word": "veṇu (bamboo)",
      "frequency": "very_low",
      "attestation": "flexibility_contexts",
      "stems": {
        "present": "veṇāya",
        "aorist": "aveṇāyi",
        "perfect": "vaveṇāya",
        "passive": "veṇāyīya",
        "causative": "veṇāyāpe",
        "past_participle": "veṇāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "flexible_plant + -āya",
        "usage": "flexible behavior"
      }
    },

    "√dāru-aya": {
      "meaning": "to be wood-like, be hard",
      "type": "denominative",
      "base_word": "dāru (wood)",
      "frequency": "very_low",
      "attestation": "hardness_contexts",
      "stems": {
        "present": "dārāya",
        "aorist": "adārāyi",
        "perfect": "dadārāya",
        "passive": "dārāyīya",
        "causative": "dārāyāpe",
        "past_participle": "dārāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "material + -āya",
        "usage": "rigid behavior"
      }
    },

    "√śilā-aya": {
      "meaning": "to be stone-like, be hard",
      "type": "denominative",
      "base_word": "silā (stone)",
      "frequency": "very_low",
      "attestation": "hardness_contexts",
      "stems": {
        "present": "silāya",
        "aorist": "asilāyi",
        "perfect": "sasilāya",
        "passive": "silāyīya",
        "causative": "silāyāpe",
        "past_participle": "silāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "hard_material + -āya",
        "usage": "unyielding behavior"
      }
    },

    "√mṛttikā-aya": {
      "meaning": "to be clay-like, be moldable",
      "type": "denominative",
      "base_word": "mattikā (clay)",
      "frequency": "very_low",
      "attestation": "moldability_contexts",
      "stems": {
        "present": "mattikāya",
        "aorist": "amattikāyi",
        "perfect": "mamattikāya",
        "passive": "mattikāyīya",
        "causative": "mattikāyāpe",
        "past_participle": "mattikāyita"
      },
      "prefixes": ["ā"],
      "generates_forms": 80,
      "generation_hints": {
        "denominative_pattern": "malleable_material + -āya",
        "usage": "adaptable behavior"
      }
    },

  
    "√āgacch": {
      "meaning": "to come, arrive",
      "type": "prefix_dependent",
      "base_root": "√gam",
      "frequency": "very_high",
      "attestation": "canonical",
      "stems": {
        "present": "āgaccha",
        "aorist": "āgami",
        "perfect": "āgata",
        "passive": "āgacchīya",
        "causative": "āgame",
        "past_participle": "āgata"
      },
      "mandatory_prefix": "ā",
      "additional_prefixes": ["sam", "abhi"],
      "generates_forms": 180,
      "generation_hints": {
        "never_without_prefix": "√gacch requires ā- for 'coming'",
        "semantic_completion": "prefix essential for directional meaning",
        "usage": "arrival contexts only"
      }
    },

    "√upagacch": {
      "meaning": "to approach, go near",
      "type": "prefix_dependent",
      "base_root": "√gam",
      "frequency": "high",
      "attestation": "canonical",
      "stems": {
        "present": "upagaccha",
        "aorist": "upagami",
        "perfect": "upagata",
        "passive": "upagacchīya",
        "causative": "upagame",
        "past_participle": "upagata"
      },
      "mandatory_prefix": "upa",
      "additional_prefixes": ["sam"],
      "generates_forms": 160,
      "generation_hints": {
        "never_without_prefix": "requires upa- for approach meaning",
        "semantic_completion": "proximity sense from prefix",
        "usage": "approaching contexts"
      }
    },

    "√paṭigacch": {
      "meaning": "to go back, return",
      "type": "prefix_dependent",
      "base_root": "√gam",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "paṭigaccha",
        "aorist": "paṭigami",
        "perfect": "paṭigata",
        "passive": "paṭigacchīya",
        "causative": "paṭigame",
        "past_participle": "paṭigata"
      },
      "mandatory_prefix": "paṭi",
      "additional_prefixes": [],
      "generates_forms": 140,
      "generation_hints": {
        "never_without_prefix": "paṭi- essential for return meaning",
        "semantic_completion": "reversal from prefix",
        "usage": "returning contexts"
      }
    },

    "√anveti": {
      "meaning": "to follow, go after",
      "type": "prefix_dependent",
      "base_root": "√i",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "anveti",
        "aorist": "anvesi",
        "perfect": "anugata",
        "passive": "anvetīya",
        "causative": "anvesāpe",
        "past_participle": "anugata"
      },
      "mandatory_prefix": "anu",
      "additional_prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "never_without_prefix": "anu- required for following",
        "semantic_completion": "sequential motion from prefix",
        "usage": "following/pursuing contexts"
      }
    },

    "√adhigacch": {
      "meaning": "to attain, reach, understand",
      "type": "prefix_dependent",
      "base_root": "√gam",
      "frequency": "high",
      "attestation": "canonical",
      "stems": {
        "present": "adhigaccha",
        "aorist": "adhigami",
        "perfect": "adhigata",
        "passive": "adhigacchīya",
        "causative": "adhigame",
        "past_participle": "adhigata"
      },
      "mandatory_prefix": "adhi",
      "additional_prefixes": [],
      "generates_forms": 150,
      "generation_hints": {
        "never_without_prefix": "adhi- essential for attainment",
        "semantic_completion": "achievement sense from prefix",
        "usage": "spiritual/mental attainment"
      }
    },

    "√abhigacch": {
      "meaning": "to go towards, approach respectfully",
      "type": "prefix_dependent",
      "base_root": "√gam",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "abhigaccha",
        "aorist": "abhigami",
        "perfect": "abhigata",
        "passive": "abhigacchīya",
        "causative": "abhigame",
        "past_participle": "abhigata"
      },
      "mandatory_prefix": "abhi",
      "additional_prefixes": [],
      "generates_forms": 140,
      "generation_hints": {
        "never_without_prefix": "abhi- for respectful approach",
        "semantic_completion": "directional respect from prefix",
        "usage": "reverential approach"
      }
    },

    "√paṭipadajja": {
      "meaning": "to practice, follow a path",
      "type": "prefix_dependent",
      "base_root": "√pad",
      "frequency": "high",
      "attestation": "canonical",
      "stems": {
        "present": "paṭipajja",
        "aorist": "paṭipadi",
        "perfect": "paṭipanna",
        "passive": "paṭipajjīya",
        "causative": "paṭipādāpe",
        "past_participle": "paṭipanna"
      },
      "mandatory_prefix": "paṭi",
      "additional_prefixes": ["anu"],
      "generates_forms": 150,
      "generation_hints": {
        "never_without_prefix": "paṭi- essential for practice meaning",
        "semantic_completion": "methodical following from prefix",
        "usage": "spiritual practice contexts"
      }
    },

    "√upasaṃhar": {
      "meaning": "to collect, bring together",
      "type": "prefix_dependent",
      "base_root": "√har",
      "frequency": "low",
      "attestation": "canonical",
      "stems": {
        "present": "upasaṃhara",
        "aorist": "upasaṃhari",
        "perfect": "upasaṃhata",
        "passive": "upasaṃharīya",
        "causative": "upasaṃhārāpe",
        "past_participle": "upasaṃhata"
      },
      "mandatory_prefix": "upa+sam",
      "additional_prefixes": [],
      "generates_forms": 120,
      "generation_hints": {
        "never_without_prefix": "double prefix required",
        "semantic_completion": "gathering sense from prefixes",
        "usage": "collection contexts"
      }
    },

    "√saṃvattati": {
      "meaning": "to lead to, conduce to",
      "type": "prefix_dependent",
      "base_root": "√vṛt",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "saṃvatta",
        "aorist": "saṃvatti",
        "perfect": "saṃvatta",
        "passive": "saṃvattīya",
        "causative": "saṃvattāpe",
        "past_participle": "saṃvatta"
      },
      "mandatory_prefix": "sam",
      "additional_prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "never_without_prefix": "sam- essential for conducive meaning",
        "semantic_completion": "leading-to sense from prefix",
        "usage": "causal relationship contexts"
      }
    },

    "√parivattati": {
      "meaning": "to revolve, change, transform",
      "type": "prefix_dependent",
      "base_root": "√vṛt",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "parivatta",
        "aorist": "parivatti",
        "perfect": "parivatta",
        "passive": "parivattīya",
        "causative": "parivattāpe",
        "past_participle": "parivatta"
      },
      "mandatory_prefix": "pari",
      "additional_prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "never_without_prefix": "pari- for circular motion",
        "semantic_completion": "revolution from prefix",
        "usage": "transformation contexts"
      }
    },

    "√anuyuñjati": {
      "meaning": "to practice, apply oneself to",
      "type": "prefix_dependent",
      "base_root": "√yuj",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "anuyuñja",
        "aorist": "anuyuñji",
        "perfect": "anuyutta",
        "passive": "anuyuñjīya",
        "causative": "anuyojāpe",
        "past_participle": "anuyutta"
      },
      "mandatory_prefix": "anu",
      "additional_prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "never_without_prefix": "anu- for application meaning",
        "semantic_completion": "dedicated practice from prefix",
        "usage": "applied practice contexts"
      }
    },

    "√abhivadati": {
      "meaning": "to greet respectfully, salute",
      "type": "prefix_dependent",
      "base_root": "√vad",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "abhivada",
        "aorist": "abhivadi",
        "perfect": "abhivutta",
        "passive": "abhivadīya",
        "causative": "abhivādāpe",
        "past_participle": "abhivutta"
      },
      "mandatory_prefix": "abhi",
      "additional_prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "never_without_prefix": "abhi- for respectful speech",
        "semantic_completion": "reverent greeting from prefix",
        "usage": "formal greeting contexts"
      }
    },

    "√anumoda": {
      "meaning": "to rejoice in, approve",
      "type": "prefix_dependent",
      "base_root": "√mud",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "anumoda",
        "aorist": "anumodi",
        "perfect": "anumudita",
        "passive": "anumodīya",
        "causative": "anumodāpe",
        "past_participle": "anumudita"
      },
      "mandatory_prefix": "anu",
      "additional_prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "never_without_prefix": "anu- for sympathetic joy",
        "semantic_completion": "approval sense from prefix",
        "usage": "merit-sharing contexts"
      }
    },

    "√paṭisaṃvedeti": {
      "meaning": "to experience, feel",
      "type": "prefix_dependent",
      "base_root": "√vid",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "paṭisaṃvede",
        "aorist": "paṭisaṃvedi",
        "perfect": "paṭisaṃvedita",
        "passive": "paṭisaṃvedīya",
        "causative": "paṭisaṃvedāpe",
        "past_participle": "paṭisaṃvedita"
      },
      "mandatory_prefix": "paṭi+sam",
      "additional_prefixes": [],
      "generates_forms": 120,
      "generation_hints": {
        "never_without_prefix": "double prefix required",
        "semantic_completion": "experiential sense from prefixes",
        "usage": "direct experience contexts"
      }
    },

    "√abhiññā": {
      "meaning": "to know directly, have higher knowledge",
      "type": "prefix_dependent",
      "base_root": "√jñā",
      "frequency": "high",
      "attestation": "canonical",
      "stems": {
        "present": "abhijānā",
        "aorist": "abhiññāsi",
        "perfect": "abhiññāta",
        "passive": "abhiññāyīya",
        "causative": "abhiññāpe",
        "past_participle": "abhiññāta"
      },
      "mandatory_prefix": "abhi",
      "additional_prefixes": [],
      "generates_forms": 150,
      "generation_hints": {
        "never_without_prefix": "abhi- for direct knowledge",
        "semantic_completion": "higher knowledge from prefix",
        "usage": "supernormal knowledge contexts"
      }
    },

    "√parijānāti": {
      "meaning": "to understand fully, comprehend",
      "type": "prefix_dependent",
      "base_root": "√jñā",
      "frequency": "high",
      "attestation": "canonical",
      "stems": {
        "present": "parijānā",
        "aorist": "pariññāsi",
        "perfect": "pariññāta",
        "passive": "parijānīya",
        "causative": "pariññāpe",
        "past_participle": "pariññāta"
      },
      "mandatory_prefix": "pari",
      "additional_prefixes": [],
      "generates_forms": 150,
      "generation_hints": {
        "never_without_prefix": "pari- for complete understanding",
        "semantic_completion": "full comprehension from prefix",
        "usage": "wisdom contexts"
      }
    },

    "√saṃjānāti": {
      "meaning": "to perceive, be conscious of",
      "type": "prefix_dependent",
      "base_root": "√jñā",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "sañjānā",
        "aorist": "saññāsi",
        "perfect": "saññāta",
        "passive": "sañjānīya",
        "causative": "saññāpe",
        "past_participle": "saññāta"
      },
      "mandatory_prefix": "sam",
      "additional_prefixes": [],
      "generates_forms": 140,
      "generation_hints": {
        "never_without_prefix": "sam- for perception",
        "semantic_completion": "conscious awareness from prefix",
        "usage": "perception contexts"
      }
    },
     
"√vijānāti": {
      "meaning": "to discern, discriminate",
      "type": "prefix_dependent",
      "base_root": "√jñā",
      "frequency": "high",
      "attestation": "canonical",
      "stems": {
        "present": "vijānā",
        "aorist": "viññāsi",
        "perfect": "viññāta",
        "passive": "vijānīya",
        "causative": "viññāpe",
        "past_participle": "viññāta"
      },
      "mandatory_prefix": "vi",
      "additional_prefixes": [],
      "generates_forms": 150,
      "generation_hints": {
        "never_without_prefix": "vi- for discrimination",
        "semantic_completion": "analytical knowledge from prefix",
        "usage": "discriminative wisdom contexts"
      }
    },

    "√pajānāti": {
      "meaning": "to know clearly, understand well",
      "type": "prefix_dependent",
      "base_root": "√jñā",
      "frequency": "very_high",
      "attestation": "canonical",
      "stems": {
        "present": "pajānā",
        "aorist": "paññāsi",
        "perfect": "paññāta",
        "passive": "pajānīya",
        "causative": "paññāpe",
        "past_participle": "paññāta"
      },
      "mandatory_prefix": "pa",
      "additional_prefixes": [],
      "generates_forms": 160,
      "generation_hints": {
        "never_without_prefix": "pa- for clear knowledge",
        "semantic_completion": "clarity from prefix",
        "usage": "clear understanding contexts"
      }
    },

    "√anussarati": {
      "meaning": "to recollect, remember",
      "type": "prefix_dependent",
      "base_root": "√smṛ",
      "frequency": "high",
      "attestation": "canonical",
      "stems": {
        "present": "anussara",
        "aorist": "anussari",
        "perfect": "anussata",
        "passive": "anussarīya",
        "causative": "anussārāpe",
        "past_participle": "anussata"
      },
      "mandatory_prefix": "anu",
      "additional_prefixes": [],
      "generates_forms": 150,
      "generation_hints": {
        "never_without_prefix": "anu- for recollection",
        "semantic_completion": "following memory from prefix",
        "usage": "meditation recollection contexts"
      }
    },

    "√paṭisarati": {
      "meaning": "to remember, recall",
      "type": "prefix_dependent",
      "base_root": "√smṛ",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "paṭisara",
        "aorist": "paṭisari",
        "perfect": "paṭisata",
        "passive": "paṭisarīya",
        "causative": "paṭisārāpe",
        "past_participle": "paṭisata"
      },
      "mandatory_prefix": "paṭi",
      "additional_prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "never_without_prefix": "paṭi- for recall",
        "semantic_completion": "return to memory from prefix",
        "usage": "memory recall contexts"
      }
    },

    "√abhiramati": {
      "meaning": "to delight in, enjoy",
      "type": "prefix_dependent",
      "base_root": "√ram",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "abhirama",
        "aorist": "abhirami",
        "perfect": "abhirata",
        "passive": "abhiramīya",
        "causative": "abhiramāpe",
        "past_participle": "abhirata"
      },
      "mandatory_prefix": "abhi",
      "additional_prefixes": [],
      "generates_forms": 140,
      "generation_hints": {
        "never_without_prefix": "abhi- for intense delight",
        "semantic_completion": "deep enjoyment from prefix",
        "usage": "aesthetic pleasure contexts"
      }
    },

    "√adhimuccati": {
      "meaning": "to be intent on, incline towards",
      "type": "prefix_dependent",
      "base_root": "√muc",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "adhimucca",
        "aorist": "adhimucci",
        "perfect": "adhimutta",
        "passive": "adhimuccīya",
        "causative": "adhimocāpe",
        "past_participle": "adhimutta"
      },
      "mandatory_prefix": "adhi",
      "additional_prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "never_without_prefix": "adhi- for inclination",
        "semantic_completion": "mental direction from prefix",
        "usage": "devotional inclination contexts"
      }
    },

    "√abhinandati": {
      "meaning": "to rejoice, be pleased with",
      "type": "prefix_dependent",
      "base_root": "√nand",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "abhinanda",
        "aorist": "abhinandi",
        "perfect": "abhinandita",
        "passive": "abhinandīya",
        "causative": "abhinandāpe",
        "past_participle": "abhinandita"
      },
      "mandatory_prefix": "abhi",
      "additional_prefixes": [],
      "generates_forms": 140,
      "generation_hints": {
        "never_without_prefix": "abhi- for rejoicing",
        "semantic_completion": "intense joy from prefix",
        "usage": "approval contexts"
      }
    },

    "√paṭikūlati": {
      "meaning": "to be repelled by, find repulsive",
      "type": "prefix_dependent",
      "base_root": "√kūl",
      "frequency": "low",
      "attestation": "canonical",
      "stems": {
        "present": "paṭikūla",
        "aorist": "paṭikūli",
        "perfect": "paṭikūlita",
        "passive": "paṭikūlīya",
        "causative": "paṭikūlāpe",
        "past_participle": "paṭikūlita"
      },
      "mandatory_prefix": "paṭi",
      "additional_prefixes": [],
      "generates_forms": 120,
      "generation_hints": {
        "never_without_prefix": "paṭi- for repulsion",
        "semantic_completion": "opposition from prefix",
        "usage": "aversion contexts"
      }
    },

    "√samāpajjati": {
      "meaning": "to attain, enter (meditative state)",
      "type": "prefix_dependent",
      "base_root": "√pad",
      "frequency": "high",
      "attestation": "canonical",
      "stems": {
        "present": "samāpajja",
        "aorist": "samāpajji",
        "perfect": "samāpanna",
        "passive": "samāpajjīya",
        "causative": "samāpādāpe",
        "past_participle": "samāpanna"
      },
      "mandatory_prefix": "sam+ā",
      "additional_prefixes": [],
      "generates_forms": 150,
      "generation_hints": {
        "never_without_prefix": "double prefix required",
        "semantic_completion": "meditative entry from prefixes",
        "usage": "jhāna attainment contexts"
      }
    },

    "√vuṭṭhāti": {
      "meaning": "to emerge from, arise from",
      "type": "prefix_dependent",
      "base_root": "√sthā",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "vuṭṭhāha",
        "aorist": "vuṭṭhāsi",
        "perfect": "vuṭṭhita",
        "passive": "vuṭṭhāhīya",
        "causative": "vuṭṭhāpe",
        "past_participle": "vuṭṭhita"
      },
      "mandatory_prefix": "vi+ut",
      "additional_prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "never_without_prefix": "vi+ut- for emergence",
        "semantic_completion": "arising from prefixes",
        "usage": "emergence from meditation"
      }
    },

    "√adhiṭṭhāti": {
      "meaning": "to resolve, determine",
      "type": "prefix_dependent",
      "base_root": "√sthā",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "adhiṭṭhāha",
        "aorist": "adhiṭṭhāsi",
        "perfect": "adhiṭṭhita",
        "passive": "adhiṭṭhāhīya",
        "causative": "adhiṭṭhāpe",
        "past_participle": "adhiṭṭhita"
      },
      "mandatory_prefix": "adhi",
      "additional_prefixes": [],
      "generates_forms": 140,
      "generation_hints": {
        "never_without_prefix": "adhi- for determination",
        "semantic_completion": "mental resolve from prefix",
        "usage": "determination contexts"
      }
    },

    "√upasaṃharati": {
      "meaning": "to compare, bring together",
      "type": "prefix_dependent",
      "base_root": "√har",
      "frequency": "low",
      "attestation": "canonical",
      "stems": {
        "present": "upasaṃhara",
        "aorist": "upasaṃhari",
        "perfect": "upasaṃhata",
        "passive": "upasaṃharīya",
        "causative": "upasaṃhārāpe",
        "past_participle": "upasaṃhata"
      },
      "mandatory_prefix": "upa+sam",
      "additional_prefixes": [],
      "generates_forms": 120,
      "generation_hints": {
        "never_without_prefix": "double prefix required",
        "semantic_completion": "comparison from prefixes",
        "usage": "analytical comparison"
      }
    },

    "√paṭisandahati": {
      "meaning": "to be reborn, reconnect",
      "type": "prefix_dependent",
      "base_root": "√dhā",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "paṭisandaha",
        "aorist": "paṭisandahi",
        "perfect": "paṭisandahita",
        "passive": "paṭisandahīya",
        "causative": "paṭisandahāpe",
        "past_participle": "paṭisandahita"
      },
      "mandatory_prefix": "paṭi+sam",
      "additional_prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "never_without_prefix": "double prefix for rebirth",
        "semantic_completion": "reconnection from prefixes",
        "usage": "rebirth contexts only"
      }
    },

    "√abhisaṃkhāroti": {
      "meaning": "to form, construct mentally",
      "type": "prefix_dependent",
      "base_root": "√kar",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "abhisaṃkhāro",
        "aorist": "abhisaṃkhāri",
        "perfect": "abhisaṃkhata",
        "passive": "abhisaṃkhārīya",
        "causative": "abhisaṃkhārāpe",
        "past_participle": "abhisaṃkhata"
      },
      "mandatory_prefix": "abhi+sam",
      "additional_prefixes": [],
      "generates_forms": 140,
      "generation_hints": {
        "never_without_prefix": "double prefix for formation",
        "semantic_completion": "mental construction from prefixes",
        "usage": "karmic formation contexts"
      }
    },

    "√abhisambujjhati": {
      "meaning": "to fully awaken, become enlightened",
      "type": "prefix_dependent",
      "base_root": "√budh",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "abhisambujjha",
        "aorist": "abhisambujjhi",
        "perfect": "abhisambuddha",
        "passive": "abhisambujjhīya",
        "causative": "abhisambodhāpe",
        "past_participle": "abhisambuddha"
      },
      "mandatory_prefix": "abhi+sam",
      "additional_prefixes": [],
      "generates_forms": 140,
      "generation_hints": {
        "never_without_prefix": "double prefix for full awakening",
        "semantic_completion": "complete enlightenment from prefixes",
        "usage": "Buddha's enlightenment"
      }
    },

    "√paṭivijjhati": {
      "meaning": "to penetrate, comprehend deeply",
      "type": "prefix_dependent",
      "base_root": "√vyadh",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "paṭivijjha",
        "aorist": "paṭivijjhi",
        "perfect": "paṭividdha",
        "passive": "paṭivijjhīya",
        "causative": "paṭivejjhāpe",
        "past_participle": "paṭividdha"
      },
      "mandatory_prefix": "paṭi",
      "additional_prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "never_without_prefix": "paṭi- for penetration",
        "semantic_completion": "deep understanding from prefix",
        "usage": "insight penetration contexts"
      }
    },
     "√samannāharati": {
      "meaning": "to consider, reflect upon",
      "type": "prefix_dependent",
      "base_root": "√har",
      "frequency": "low",
      "attestation": "canonical",
      "stems": {
        "present": "samannāhara",
        "aorist": "samannāhari",
        "perfect": "samannāhata",
        "passive": "samannāharīya",
        "causative": "samannāhārāpe",
        "past_participle": "samannāhata"
      },
      "mandatory_prefix": "sam+anu+ā",
      "additional_prefixes": [],
      "generates_forms": 110,
      "generation_hints": {
        "never_without_prefix": "triple prefix required",
        "semantic_completion": "comprehensive consideration from prefixes",
        "usage": "philosophical reflection"
      }
    },

    "√upasaṅkamati": {
      "meaning": "to approach, go to visit",
      "type": "prefix_dependent",
      "base_root": "√kam",
      "frequency": "high",
      "attestation": "canonical",
      "stems": {
        "present": "upasaṅkama",
        "aorist": "upasaṅkami",
        "perfect": "upasaṅkanta",
        "passive": "upasaṅkamīya",
        "causative": "upasaṅkamāpe",
        "past_participle": "upasaṅkanta"
      },
      "mandatory_prefix": "upa+sam",
      "additional_prefixes": [],
      "generates_forms": 150,
      "generation_hints": {
        "never_without_prefix": "double prefix for formal approach",
        "semantic_completion": "respectful visit from prefixes",
        "usage": "formal visitation contexts"
      }
    },

    "√abhivandati": {
      "meaning": "to salute respectfully",
      "type": "prefix_dependent",
      "base_root": "√vand",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "abhivanda",
        "aorist": "abhivandi",
        "perfect": "abhivandita",
        "passive": "abhivandīya",
        "causative": "abhivandāpe",
        "past_participle": "abhivandita"
      },
      "mandatory_prefix": "abhi",
      "additional_prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "never_without_prefix": "abhi- for respectful salutation",
        "semantic_completion": "reverent greeting from prefix",
        "usage": "formal respect contexts"
      }
    },

    "√paṭikaroti": {
      "meaning": "to counteract, remedy",
      "type": "prefix_dependent",
      "base_root": "√kar",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "paṭikaro",
        "aorist": "paṭikari",
        "perfect": "paṭikata",
        "passive": "paṭikarīya",
        "causative": "paṭikārāpe",
        "past_participle": "paṭikata"
      },
      "mandatory_prefix": "paṭi",
      "additional_prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "never_without_prefix": "paṭi- for counteraction",
        "semantic_completion": "remedial action from prefix",
        "usage": "antidote contexts"
      }
    },

    "√viharati": {
      "meaning": "to dwell, abide (in a state)",
      "type": "prefix_dependent",
      "base_root": "√har",
      "frequency": "very_high",
      "attestation": "canonical",
      "stems": {
        "present": "vihara",
        "aorist": "vihari",
        "perfect": "vihata",
        "passive": "viharīya",
        "causative": "vihārāpe",
        "past_participle": "vihata"
      },
      "mandatory_prefix": "vi",
      "additional_prefixes": [],
      "generates_forms": 170,
      "generation_hints": {
        "never_without_prefix": "vi- for dwelling",
        "semantic_completion": "abiding state from prefix",
        "usage": "meditative dwelling contexts"
      }
    },

    "√upavicarati": {
      "meaning": "to investigate, examine closely",
      "type": "prefix_dependent",
      "base_root": "√car",
      "frequency": "low",
      "attestation": "canonical",
      "stems": {
        "present": "upavicara",
        "aorist": "upavicari",
        "perfect": "upavicarita",
        "passive": "upavicarīya",
        "causative": "upavicārāpe",
        "past_participle": "upavicarita"
      },
      "mandatory_prefix": "upa+vi",
      "additional_prefixes": [],
      "generates_forms": 120,
      "generation_hints": {
        "never_without_prefix": "double prefix for investigation",
        "semantic_completion": "close examination from prefixes",
        "usage": "analytical investigation"
      }
    },

    "√saṃvijjati": {
      "meaning": "to exist, be found",
      "type": "prefix_dependent",
      "base_root": "√vid",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "saṃvijja",
        "aorist": "saṃvijji",
        "perfect": "saṃvutta",
        "passive": "saṃvijjīya",
        "causative": "saṃvijjāpe",
        "past_participle": "saṃvutta"
      },
      "mandatory_prefix": "sam",
      "additional_prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "never_without_prefix": "sam- for existence",
        "semantic_completion": "being found from prefix",
        "usage": "existence verification"
      }
    },

    "√anupassati": {
      "meaning": "to contemplate, observe closely",
      "type": "prefix_dependent",
      "base_root": "√paś",
      "frequency": "very_high",
      "attestation": "canonical",
      "stems": {
        "present": "anupassa",
        "aorist": "anupassi",
        "perfect": "anupassita",
        "passive": "anupassīya",
        "causative": "anupassāpe",
        "past_participle": "anupassita"
      },
      "mandatory_prefix": "anu",
      "additional_prefixes": [],
      "generates_forms": 160,
      "generation_hints": {
        "never_without_prefix": "anu- for contemplation",
        "semantic_completion": "continuous observation from prefix",
        "usage": "vipassanā contexts"
      }
    },

    "√samanupassati": {
      "meaning": "to regard as, consider",
      "type": "prefix_dependent",
      "base_root": "√paś",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "samanupassa",
        "aorist": "samanupassi",
        "perfect": "samanupassita",
        "passive": "samanupassīya",
        "causative": "samanupassāpe",
        "past_participle": "samanupassita"
      },
      "mandatory_prefix": "sam+anu",
      "additional_prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "never_without_prefix": "double prefix for consideration",
        "semantic_completion": "regarding as from prefixes",
        "usage": "philosophical consideration"
      }
    },

    "√abhiṇhaṃ": {
      "meaning": "to do repeatedly, frequently",
      "type": "prefix_dependent",
      "base_root": "√han",
      "frequency": "low",
      "attestation": "canonical",
      "stems": {
        "present": "abhiṇha",
        "aorist": "abhiṇhi",
        "perfect": "abhiṇhata",
        "passive": "abhiṇhīya",
        "causative": "abhiṇhāpe",
        "past_participle": "abhiṇhata"
      },
      "mandatory_prefix": "abhi",
      "additional_prefixes": [],
      "generates_forms": 110,
      "generation_hints": {
        "never_without_prefix": "abhi- for repetition",
        "semantic_completion": "frequency from prefix",
        "usage": "repeated action contexts"
      }
    },

    "√pariyāpuṇāti": {
      "meaning": "to master, learn thoroughly",
      "type": "prefix_dependent",
      "base_root": "√āp",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "pariyāpuṇā",
        "aorist": "pariyāpuṇi",
        "perfect": "pariyāpuṇṇa",
        "passive": "pariyāpuṇīya",
        "causative": "pariyāpuṇāpe",
        "past_participle": "pariyāpuṇṇa"
      },
      "mandatory_prefix": "pari+ā",
      "additional_prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "never_without_prefix": "double prefix for mastery",
        "semantic_completion": "complete learning from prefixes",
        "usage": "scriptural mastery contexts"
      }
    },

    "√upanissāya": {
      "meaning": "to depend on, rely upon",
      "type": "prefix_dependent",
      "base_root": "√śri",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "upanissāya",
        "aorist": "upanissāyi",
        "perfect": "upanissita",
        "passive": "upanissāyīya",
        "causative": "upanissāyāpe",
        "past_participle": "upanissita"
      },
      "mandatory_prefix": "upa+ni",
      "additional_prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "never_without_prefix": "double prefix for dependence",
        "semantic_completion": "reliance from prefixes",
        "usage": "causal dependence contexts"
      }
    },

    "√āpajjati": {
      "meaning": "to commit (offense), fall into",
      "type": "prefix_dependent",
      "base_root": "√pad",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "āpajja",
        "aorist": "āpajji",
        "perfect": "āpanna",
        "passive": "āpajjīya",
        "causative": "āpādāpe",
        "past_participle": "āpanna"
      },
      "mandatory_prefix": "ā",
      "additional_prefixes": [],
      "generates_forms": 140,
      "generation_hints": {
        "never_without_prefix": "ā- for falling into",
        "semantic_completion": "transgression from prefix",
        "usage": "vinaya offense contexts"
      }
    },

    "√paṭideseti": {
      "meaning": "to confess, acknowledge",
      "type": "prefix_dependent",
      "base_root": "√diś",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "paṭidese",
        "aorist": "paṭidesi",
        "perfect": "paṭidesita",
        "passive": "paṭidesīya",
        "causative": "paṭidesāpe",
        "past_participle": "paṭidesita"
      },
      "mandatory_prefix": "paṭi",
      "additional_prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "never_without_prefix": "paṭi- for confession",
        "semantic_completion": "acknowledgment from prefix",
        "usage": "vinaya confession contexts"
      }
    },

    "√adhivāseti": {
      "meaning": "to consent, accept (invitation)",
      "type": "prefix_dependent",
      "base_root": "√vas",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "adhivāse",
        "aorist": "adhivāsesi",
        "perfect": "adhivāsita",
        "passive": "adhivāsīya",
        "causative": "adhivāsāpe",
        "past_participle": "adhivāsita"
      },
      "mandatory_prefix": "adhi",
      "additional_prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "never_without_prefix": "adhi- for consent",
        "semantic_completion": "acceptance from prefix",
        "usage": "invitation acceptance"
      }
    },

    "√paṭibhāti": {
      "meaning": "to occur to, appear to mind",
      "type": "prefix_dependent",
      "base_root": "√bhā",
      "frequency": "low",
      "attestation": "canonical",
      "stems": {
        "present": "paṭibhā",
        "aorist": "paṭibhāsi",
        "perfect": "paṭibhāta",
        "passive": "paṭibhāyīya",
        "causative": "paṭibhāpe",
        "past_participle": "paṭibhāta"
      },
      "mandatory_prefix": "paṭi",
      "additional_prefixes": [],
      "generates_forms": 120,
      "generation_hints": {
        "never_without_prefix": "paṭi- for mental appearance",
        "semantic_completion": "spontaneous arising from prefix",
        "usage": "inspiration contexts"
      }
    },

    "√saṃharati": {
      "meaning": "to collect, contract",
      "type": "prefix_dependent",
      "base_root": "√har",
      "frequency": "low",
      "attestation": "canonical",
      "stems": {
        "present": "saṃhara",
        "aorist": "saṃhari",
        "perfect": "saṃhata",
        "passive": "saṃharīya",
        "causative": "saṃhārāpe",
        "past_participle": "saṃhata"
      },
      "mandatory_prefix": "sam",
      "additional_prefixes": [],
      "generates_forms": 120,
      "generation_hints": {
        "never_without_prefix": "sam- for collection",
        "semantic_completion": "gathering from prefix",
        "usage": "contraction contexts"
      }
    },
     "√vyākaroti": {
      "meaning": "to explain, predict",
      "type": "prefix_dependent",
      "base_root": "√kar",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "byākaro",
        "aorist": "byākari",
        "perfect": "byākata",
        "passive": "byākarīya",
        "causative": "byākārāpe",
        "past_participle": "byākata"
      },
      "mandatory_prefix": "vi+ā",
      "additional_prefixes": [],
      "generates_forms": 140,
      "generation_hints": {
        "never_without_prefix": "vi+ā- for explanation",
        "pali_change": "vy > by",
        "semantic_completion": "detailed exposition from prefixes",
        "usage": "doctrinal explanation contexts"
      }
    },

    "√paṭisaṃharati": {
      "meaning": "to withdraw, put away",
      "type": "prefix_dependent",
      "base_root": "√har",
      "frequency": "low",
      "attestation": "canonical",
      "stems": {
        "present": "paṭisaṃhara",
        "aorist": "paṭisaṃhari",
        "perfect": "paṭisaṃhata",
        "passive": "paṭisaṃharīya",
        "causative": "paṭisaṃhārāpe",
        "past_participle": "paṭisaṃhata"
      },
      "mandatory_prefix": "paṭi+sam",
      "additional_prefixes": [],
      "generates_forms": 120,
      "generation_hints": {
        "never_without_prefix": "double prefix for withdrawal",
        "semantic_completion": "retraction from prefixes",
        "usage": "monastic rule contexts"
      }
    },

    "√sakkhikaroti": {
      "meaning": "to realize, experience for oneself",
      "type": "prefix_dependent",
      "base_root": "√kar",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "sakkhikaro",
        "aorist": "sakkhikari",
        "perfect": "sakkhikata",
        "passive": "sakkhikarīya",
        "causative": "sakkhikārāpe",
        "past_participle": "sakkhikata"
      },
      "mandatory_prefix": "sakkhi",
      "additional_prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "never_without_prefix": "adverbial prefix 'sakkhi' required",
        "semantic_completion": "direct experience",
        "usage": "realization of Nibbāna"
      }
    },

    "√ajjhāvasati": {
      "meaning": "to inhabit, dwell in",
      "type": "prefix_dependent",
      "base_root": "√vas",
      "frequency": "low",
      "attestation": "canonical",
      "stems": {
        "present": "ajjhāvasa",
        "aorist": "ajjhāvasī",
        "perfect": "ajjhāvuttha",
        "passive": "ajjhāvasīya",
        "causative": "ajjhāvāsāpe",
        "past_participle": "ajjhāvuttha"
      },
      "mandatory_prefix": "adhi+ā",
      "additional_prefixes": [],
      "generates_forms": 120,
      "generation_hints": {
        "never_without_prefix": "double prefix for inhabiting",
        "semantic_completion": "dwelling within from prefixes",
        "usage": "inhabitation contexts"
      }
    },

    "√paccavekkhati": {
      "meaning": "to review, reflect upon",
      "type": "prefix_dependent",
      "base_root": "√īkṣ",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "paccavekkha",
        "aorist": "paccavekkhi",
        "perfect": "paccavekkhita",
        "passive": "paccavekkhīya",
        "causative": "paccavekkhāpe",
        "past_participle": "paccavekkhita"
      },
      "mandatory_prefix": "paṭi+ava",
      "additional_prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "never_without_prefix": "double prefix for reviewing",
        "semantic_completion": "retrospective analysis from prefixes",
        "usage": "monastic reflection"
      }
    },

    "√pariyesati": {
      "meaning": "to seek, search for",
      "type": "prefix_dependent",
      "base_root": "√iṣ",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "pariyesa",
        "aorist": "pariyesi",
        "perfect": "pariyesita",
        "passive": "pariyesīya",
        "causative": "pariyesāpe",
        "past_participle": "pariyesita"
      },
      "mandatory_prefix": "pari",
      "additional_prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "never_without_prefix": "pari- for thorough searching",
        "semantic_completion": "complete seeking from prefix",
        "usage": "quest/search contexts"
      }
    },

    "√ajjhokāsati": {
      "meaning": "to reside in the open air",
      "type": "prefix_dependent",
      "base_root": "√kāś",
      "frequency": "low",
      "attestation": "monastic_contexts",
      "stems": {
        "present": "ajjhokāsa",
        "aorist": "ajjhokāsi",
        "perfect": "ajjhokāsita",
        "passive": "ajjhokāsīya",
        "causative": "ajjhokāsāpe",
        "past_participle": "ajjhokāsita"
      },
      "mandatory_prefix": "adhi+ava",
      "additional_prefixes": [],
      "generates_forms": 110,
      "generation_hints": {
        "never_without_prefix": "double prefix for open-air dwelling",
        "semantic_completion": "outdoor residence",
        "usage": "ascetic practices"
      }
    },

    "√paccupaṭṭhāti": {
      "meaning": "to be present, to attend",
      "type": "prefix_dependent",
      "base_root": "√sthā",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "paccupaṭṭhāha",
        "aorist": "paccupaṭṭhāsi",
        "perfect": "paccupaṭṭhita",
        "passive": "paccupaṭṭhāhīya",
        "causative": "paccupaṭṭhāpe",
        "past_participle": "paccupaṭṭhita"
      },
      "mandatory_prefix": "paṭi+upa",
      "additional_prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "never_without_prefix": "double prefix for presence",
        "semantic_completion": "being present before",
        "usage": "attendance contexts"
      }
    },

    "√paripucchati": {
      "meaning": "to inquire, question thoroughly",
      "type": "prefix_dependent",
      "base_root": "√pucch",
      "frequency": "low",
      "attestation": "canonical",
      "stems": {
        "present": "paripuccha",
        "aorist": "paripucchi",
        "perfect": "paripuṭṭha",
        "passive": "paripucchīya",
        "causative": "paripucchāpe",
        "past_participle": "paripuṭṭha"
      },
      "mandatory_prefix": "pari",
      "additional_prefixes": [],
      "generates_forms": 120,
      "generation_hints": {
        "never_without_prefix": "pari- for thorough inquiry",
        "semantic_completion": "complete questioning",
        "usage": "philosophical inquiry"
      }
    },

    "√ajjhappekhati": {
      "meaning": "to look upon with equanimity, be indifferent",
      "type": "prefix_dependent",
      "base_root": "√īkṣ",
      "frequency": "low",
      "attestation": "canonical",
      "stems": {
        "present": "ajjhappekkha",
        "aorist": "ajjhappekkhi",
        "perfect": "ajjhappekkhita",
        "passive": "ajjhappekkhīya",
        "causative": "ajjhappekkhāpe",
        "past_participle": "ajjhappekkhita"
      },
      "mandatory_prefix": "adhi+upa",
      "additional_prefixes": [],
      "generates_forms": 110,
      "generation_hints": {
        "never_without_prefix": "double prefix for equanimity",
        "semantic_completion": "indifferent observation",
        "usage": "meditative states"
      }
    },

    "√ajjhācarati": {
      "meaning": "to transgress, behave improperly",
      "type": "prefix_dependent",
      "base_root": "√car",
      "frequency": "low",
      "attestation": "canonical",
      "stems": {
        "present": "ajjhācara",
        "aorist": "ajjhācari",
        "perfect": "ajjhācarita",
        "passive": "ajjhācarīya",
        "causative": "ajjhācārāpe",
        "past_participle": "ajjhācarita"
      },
      "mandatory_prefix": "adhi+ā",
      "additional_prefixes": [],
      "generates_forms": 120,
      "generation_hints": {
        "never_without_prefix": "double prefix for transgression",
        "semantic_completion": "improper conduct",
        "usage": "ethical contexts"
      }
    },

    "√saṃvasati": {
      "meaning": "to live together, co-reside",
      "type": "prefix_dependent",
      "base_root": "√vas",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "saṃvasa",
        "aorist": "saṃvasī",
        "perfect": "saṃvuttha",
        "passive": "saṃvasīya",
        "causative": "saṃvāsāpe",
        "past_participle": "saṃvuttha"
      },
      "mandatory_prefix": "sam",
      "additional_prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "never_without_prefix": "sam- for co-residence",
        "semantic_completion": "living together",
        "usage": "community living"
      }
    },

    "√paridahati": {
      "meaning": "to put on, wear (clothes)",
      "type": "prefix_dependent",
      "base_root": "√dhā",
      "frequency": "low",
      "attestation": "canonical",
      "stems": {
        "present": "paridaha",
        "aorist": "paridahi",
        "perfect": "paridahita",
        "passive": "paridahīya",
        "causative": "paridahāpe",
        "past_participle": "paridahita"
      },
      "mandatory_prefix": "pari",
      "additional_prefixes": [],
      "generates_forms": 120,
      "generation_hints": {
        "never_without_prefix": "pari- for wearing",
        "semantic_completion": "wearing around",
        "usage": "clothing contexts"
      }
    },

    "√paṭinissajjati": {
      "meaning": "to abandon, renounce",
      "type": "prefix_dependent",
      "base_root": "√sṛj",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "paṭinissajja",
        "aorist": "paṭinissajji",
        "perfect": "paṭinissaṭṭha",
        "passive": "paṭinissajjīya",
        "causative": "paṭinissajjāpe",
        "past_participle": "paṭinissaṭṭha"
      },
      "mandatory_prefix": "paṭi+ni",
      "additional_prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "never_without_prefix": "double prefix for renunciation",
        "semantic_completion": "complete giving up",
        "usage": "renunciation contexts"
      }
    },

    "√samādahati": {
      "meaning": "to concentrate, compose the mind",
      "type": "prefix_dependent",
      "base_root": "√dhā",
      "frequency": "high",
      "attestation": "canonical",
      "stems": {
        "present": "samādaha",
        "aorist": "samādahi",
        "perfect": "samāhita",
        "passive": "samādahīya",
        "causative": "samādahāpe",
        "past_participle": "samāhita"
      },
      "mandatory_prefix": "sam+ā",
      "additional_prefixes": [],
      "generates_forms": 150,
      "generation_hints": {
        "never_without_prefix": "double prefix for concentration",
        "semantic_completion": "mental composure",
        "usage": "meditation contexts"
      }
    },

    "√ajjhupagacchati": {
      "meaning": "to consent, agree to",
      "type": "prefix_dependent",
      "base_root": "√gam",
      "frequency": "low",
      "attestation": "canonical",
      "stems": {
        "present": "ajjhupagaccha",
        "aorist": "ajjhupagami",
        "perfect": "ajjhupagata",
        "passive": "ajjhupagacchīya",
        "causative": "ajjhupagame",
        "past_participle": "ajjhupagata"
      },
      "mandatory_prefix": "adhi+upa",
      "additional_prefixes": [],
      "generates_forms": 120,
      "generation_hints": {
        "never_without_prefix": "double prefix for consent",
        "semantic_completion": "agreement",
        "usage": "consent contexts"
      }
    },

    "√samudācarati": {
      "meaning": "to address, speak to",
      "type": "prefix_dependent",
      "base_root": "√car",
      "frequency": "low",
      "attestation": "canonical",
      "stems": {
        "present": "samudācara",
        "aorist": "samudācari",
        "perfect": "samudācarita",
        "passive": "samudācarīya",
        "causative": "samudācārāpe",
        "past_participle": "samudācarita"
      },
      "mandatory_prefix": "sam+ud+ā",
      "additional_prefixes": [],
      "generates_forms": 110,
      "generation_hints": {
        "never_without_prefix": "triple prefix for addressing",
        "semantic_completion": "formal address",
        "usage": "speech contexts"
      }
    },

    "√paṭisaṃvedayati": {
      "meaning": "to feel, experience personally",
      "type": "prefix_dependent",
      "base_root": "√vid",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "paṭisaṃvedaya",
        "aorist": "paṭisaṃvedi",
        "perfect": "paṭisaṃvedita",
        "passive": "paṭisaṃvedayīya",
        "causative": "paṭisaṃvedāpe",
        "past_participle": "paṭisaṃvedita"
      },
      "mandatory_prefix": "paṭi+sam",
      "additional_prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "never_without_prefix": "double prefix for personal experience",
        "semantic_completion": "direct feeling",
        "usage": "experiential contexts"
      }
    },

    "√ajjhāruhati": {
      "meaning": "to ascend, climb upon",
      "type": "prefix_dependent",
      "base_root": "√ruh",
      "frequency": "low",
      "attestation": "canonical",
      "stems": {
        "present": "ajjhāruha",
        "aorist": "ajjhāruhi",
        "perfect": "ajjhārūḷha",
        "passive": "ajjhāruhīya",
        "causative": "ajjhāropāpe",
        "past_participle": "ajjhārūḷha"
      },
      "mandatory_prefix": "adhi+ā",
      "additional_prefixes": [],
      "generates_forms": 120,
      "generation_hints": {
        "never_without_prefix": "double prefix for ascending",
        "semantic_completion": "climbing upon",
        "usage": "ascending contexts"
      }
    },

    "√paccāgacchati": {
      "meaning": "to return, come back",
      "type": "prefix_dependent",
      "base_root": "√gam",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "paccāgaccha",
        "aorist": "paccāgami",
        "perfect": "paccāgata",
        "passive": "paccāgacchīya",
        "causative": "paccāgame",
        "past_participle": "paccāgata"
      },
      "mandatory_prefix": "paṭi+ā",
      "additional_prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "never_without_prefix": "double prefix for returning",
        "semantic_completion": "coming back",
        "usage": "return journey contexts"
      }
    },

    "√ajjhogaheti": {
      "meaning": "to immerse, plunge into",
      "type": "prefix_dependent",
      "base_root": "√gah",
      "frequency": "low",
      "attestation": "canonical",
      "stems": {
        "present": "ajjhogahe",
        "aorist": "ajjhogahesi",
        "perfect": "ajjhogahita",
        "passive": "ajjhogahīya",
        "causative": "ajjhogāhāpe",
        "past_participle": "ajjhogahita"
      },
      "mandatory_prefix": "adhi+ava",
      "additional_prefixes": [],
      "generates_forms": 110,
      "generation_hints": {
        "never_without_prefix": "double prefix for immersion",
        "semantic_completion": "plunging into",
        "usage": "immersion contexts"
      }
    },

    "√samudeti": {
      "meaning": "to arise, originate together",
      "type": "prefix_dependent",
      "base_root": "√i",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "samude",
        "aorist": "samudesi",
        "perfect": "samudita",
        "passive": "samudīya",
        "causative": "samudāpe",
        "past_participle": "samudita"
      },
      "mandatory_prefix": "sam+ud",
      "additional_prefixes": [],
      "generates_forms": 120,
      "generation_hints": {
        "never_without_prefix": "double prefix for origination",
        "semantic_completion": "co-arising",
        "usage": "dependent origination contexts"
      }
    },

    "√abhivassati": {
      "meaning": "to rain upon, shower",
      "type": "prefix_dependent",
      "base_root": "√vass",
      "frequency": "low",
      "attestation": "canonical",
      "stems": {
        "present": "abhivassa",
        "aorist": "abhivassi",
        "perfect": "abhivuttha",
        "passive": "abhivassīya",
        "causative": "abhivassāpe",
        "past_participle": "abhivuttha"
      },
      "mandatory_prefix": "abhi",
      "additional_prefixes": [],
      "generates_forms": 110,
      "generation_hints": {
        "never_without_prefix": "abhi- for raining upon",
        "semantic_completion": "showering",
        "usage": "poetic rain descriptions"
      }
    },

    "√paccakkhāti": {
      "meaning": "to refuse, reject",
      "type": "prefix_dependent",
      "base_root": "√khyā",
      "frequency": "low",
      "attestation": "canonical",
      "stems": {
        "present": "paccakkhā",
        "aorist": "paccakkhāsi",
        "perfect": "paccakkhāta",
        "passive": "paccakkhāyīya",
        "causative": "paccakkhāpe",
        "past_participle": "paccakkhāta"
      },
      "mandatory_prefix": "paṭi+ā",
      "additional_prefixes": [],
      "generates_forms": 120,
      "generation_hints": {
        "never_without_prefix": "double prefix for rejection",
        "semantic_completion": "refusal",
        "usage": "rejection contexts"
      }
    },

    "√ajjhottharati": {
      "meaning": "to overwhelm, overcome",
      "type": "prefix_dependent",
      "base_root": "√tṛ",
      "frequency": "low",
      "attestation": "canonical",
      "stems": {
        "present": "ajjhotthara",
        "aorist": "ajjhotthari",
        "perfect": "ajjhotthata",
        "passive": "ajjhottharīya",
        "causative": "ajjhotthārāpe",
        "past_participle": "ajjhotthata"
      },
      "mandatory_prefix": "adhi+ava",
      "additional_prefixes": [],
      "generates_forms": 110,
      "generation_hints": {
        "never_without_prefix": "double prefix for overwhelming",
        "semantic_completion": "overcoming",
        "usage": "overwhelming emotion"
      }
    },

    "√samādiyati": {
      "meaning": "to take upon oneself, undertake",
      "type": "prefix_dependent",
      "base_root": "√dā",
      "frequency": "medium",
      "attestation": "canonical",
      "stems": {
        "present": "samādiya",
        "aorist": "samādiyi",
        "perfect": "samādinna",
        "passive": "samādiyīya",
        "causative": "samādāpe",
        "past_participle": "samādinna"
      },
      "mandatory_prefix": "sam+ā",
      "additional_prefixes": [],
      "generates_forms": 130,
      "generation_hints": {
        "never_without_prefix": "double prefix for undertaking",
        "semantic_completion": "undertaking vows",
        "usage": "precept observance"
      }
    }
  }
  
 
     
  
    
 


     

     
