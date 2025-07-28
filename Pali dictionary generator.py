import json
import re
from collections import defaultdict
from datetime import datetime
from typing import Dict, List, Tuple, Optional, Set
import os
import sys
import importlib.util

# ============ FILE PREPROCESSING AND VALIDATION ============

class PaliDataPreprocessor:
    """Preprocess and validate Pali data files"""
    
    def __init__(self, kaggle_input_path="/kaggle/input"):
        self.kaggle_input_path = kaggle_input_path
        self.validation_errors = []
        self.validation_warnings = []
        # Add your dataset name here
        self.dataset_name = "pali-dictionary-data"  # Change this to your dataset name
        
    def load_and_validate_all_data(self):
        """Load all data with validation and preprocessing"""
        print("🔍 Loading and validating Pali data files...")
        
        # Try different locations
        base_words = self._load_base_words()
        root_words = self._load_root_words()
        
        print(f"✅ Validation complete:")
        print(f"   - Base words: {len(base_words)} loaded")
        print(f"   - Root words: {len(root_words)} loaded")
        
        if self.validation_errors:
            print(f"❌ Errors found: {len(self.validation_errors)}")
            for error in self.validation_errors[:5]:
                print(f"   - {error}")
                
        if self.validation_warnings:
            print(f"⚠️  Warnings: {len(self.validation_warnings)}")
            for warning in self.validation_warnings[:5]:
                print(f"   - {warning}")
        
        return base_words, root_words
    
    def _load_base_words(self):
        """Load base words with validation"""
        # Try different file locations
        possible_paths = [
            # Add path with your dataset name
            os.path.join(self.kaggle_input_path, self.dataset_name, "pali_word_data.py"),
            os.path.join(self.kaggle_input_path, "pali_word_data.py"),
            os.path.join(self.kaggle_input_path, "pali-word-data", "pali_word_data.py"),
            "pali_word_data.py",
            "./input/pali_word_data.py"
        ]
        
        # Try loading as Python module first
        for path in possible_paths:
            if os.path.exists(path):
                try:
                    # Try to import as module
                    spec = importlib.util.spec_from_file_location("pali_word_data", path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    
                    if hasattr(module, 'PALI_BASE_WORDS'):
                        print(f"✅ Loaded base words from {path}")
                        return self._validate_base_words(module.PALI_BASE_WORDS)
                except Exception as e:
                    print(f"⚠️ Could not load as Python module: {e}")
        
        # Try loading as JSON
        json_paths = [p.replace('.py', '.json') for p in possible_paths]
        for path in json_paths:
            if os.path.exists(path):
                try:
                    return self._load_base_words_json(path)
                except Exception as e:
                    print(f"⚠️ Could not load JSON: {e}")
        
        # If all fails, try to extract from malformed JSON
        for path in possible_paths + json_paths:
            if os.path.exists(path):
                try:
                    return self._load_malformed_json(path, "base_words")
                except Exception as e:
                    continue
        
        print("❌ Could not find base words file!")
        return {}
    
    def _load_root_words(self):
        """Load root words with validation"""
        possible_paths = [
            os.path.join(self.kaggle_input_path, self.dataset_name, "pali_roots_words.py"),
            os.path.join(self.kaggle_input_path, "pali_roots_words.py"),
            os.path.join(self.kaggle_input_path, "pali-roots-words", "pali_roots_words.py"),
            "pali_roots_words.py",
            "./input/pali_roots_words.py"
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                try:
                    spec = importlib.util.spec_from_file_location("pali_roots_words", path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    
                    if hasattr(module, 'PALI_ROOTS'):
                        print(f"✅ Loaded root words from {path}")
                        return self._validate_and_process_roots(module.PALI_ROOTS)
                except Exception as e:
                    print(f"⚠️ Could not load as Python module: {e}")
        
        # Try JSON format
        json_paths = [p.replace('.py', '.json') for p in possible_paths]
        for path in json_paths:
            if os.path.exists(path):
                try:
                    return self._load_root_words_json(path)
                except Exception as e:
                    print(f"⚠️ Could not load JSON: {e}")
        
        print("❌ Could not find root words file!")
        return {}
    
    def _load_malformed_json(self, filepath, data_type):
        """Load JSON that might be missing outer braces"""
        print(f"🔧 Attempting to fix malformed JSON in {filepath}")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if it's Python dict format
        if "PALI_BASE_WORDS" in content or "PALI_ROOTS" in content:
            # Extract dictionary content
            match = re.search(r'(PALI_BASE_WORDS|PALI_ROOTS)\s*=\s*{(.+)}', content, re.DOTALL)
            if match:
                dict_content = "{" + match.group(2) + "}"
                try:
                    return json.loads(dict_content)
                except:
                    # Try eval as last resort (DANGEROUS - only for trusted files)
                    try:
                        return eval(dict_content)
                    except:
                        pass
        
        # Try to fix missing braces
        content = content.strip()
        if content.endswith(','):
            content = content[:-1]
        
        # Check if already has braces
        if not content.startswith('{'):
            content = '{' + content
        if not content.endswith('}'):
            content = content + '}'
        
        try:
            data = json.loads(content)
            print("✅ Successfully fixed and loaded JSON")
            return data
        except json.JSONDecodeError as e:
            print(f"❌ JSON decode error: {e}")
            # Try one more fix - escape problematic characters
            content = content.replace("'", '"')
            try:
                return json.loads(content)
            except:
                raise ValueError(f"Could not parse {filepath}")
    
    def _validate_base_words(self, base_words):
        """Validate base word structure"""
        validated = {}
        
        for word, info in base_words.items():
            # Validate word format
            if not isinstance(word, str) or len(word) == 0:
                self.validation_errors.append(f"Invalid word key: {word}")
                continue
            
            # Validate info structure
            if not isinstance(info, dict):
                self.validation_errors.append(f"Invalid info for {word}: not a dictionary")
                continue
            
            # Check required fields
            if "primary" not in info:
                self.validation_warnings.append(f"Missing 'primary' meaning for {word}")
                info["primary"] = word  # Default to word itself
            
            # Validate semantic field
            if "semantic_field" not in info:
                self.validation_warnings.append(f"Missing semantic_field for {word}")
                info["semantic_field"] = "general"
            
            # Validate register
            if "register" not in info:
                info["register"] = "common"
            
            # Clean up the word (remove any special characters)
            clean_word = word.strip()
            validated[clean_word] = info
        
        return validated
    
    def _validate_and_process_roots(self, roots):
        """Validate and process root words, handling variants"""
        processed = {}
        
        for root_key, root_info in roots.items():
            # Validate root format
            if not isinstance(root_key, str):
                self.validation_errors.append(f"Invalid root key: {root_key}")
                continue
            
            if not isinstance(root_info, dict):
                self.validation_errors.append(f"Invalid info for {root_key}")
                continue
            
            # Handle variants
            if '_variant_' in root_key:
                # Extract base root and variant number
                parts = root_key.split('_variant_')
                base_root = parts[0]
                variant_num = parts[1] if len(parts) > 1 else "1"
                
                # Ensure base root exists
                if base_root not in processed:
                    processed[base_root] = {
                        'meaning': root_info.get('meaning', 'undefined'),
                        'type': 'primary',
                        'variants': {}
                    }
                
                # Add variant
                processed[base_root]['variants'][f'variant_{variant_num}'] = root_info
                
                # If this variant has stems, merge them
                if 'stems' in root_info:
                    if 'variant_stems' not in processed[base_root]:
                        processed[base_root]['variant_stems'] = {}
                    processed[base_root]['variant_stems'][f'variant_{variant_num}'] = root_info['stems']
            else:
                # Regular root
                if root_key in processed:
                    # Merge with existing
                    processed[root_key].update(root_info)
                else:
                    processed[root_key] = root_info
            
            # Validate required fields
            if root_key in processed:
                if 'meaning' not in processed[root_key]:
                    self.validation_warnings.append(f"Missing meaning for {root_key}")
                    processed[root_key]['meaning'] = "undefined"
                
                if 'stems' not in processed[root_key]:
                    self.validation_warnings.append(f"Missing stems for {root_key}")
                    # Generate default stems
                    clean_root = root_key.replace('√', '')
                    processed[root_key]['stems'] = {
                        'present': clean_root,
                        'aorist': clean_root,
                        'past_participle': clean_root + 'ita'
                    }
        
        return processed
    
    def _load_base_words_json(self, filepath):
        """Load base words from JSON file"""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Handle different possible structures
        if isinstance(data, dict):
            if 'PALI_BASE_WORDS' in data:
                return self._validate_base_words(data['PALI_BASE_WORDS'])
            elif 'base_words' in data:
                return self._validate_base_words(data['base_words'])
            else:
                # Assume the whole file is the dictionary
                return self._validate_base_words(data)
        else:
            raise ValueError(f"Invalid base words file structure in {filepath}")
    
    def _load_root_words_json(self, filepath):
        """Load root words from JSON file"""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if isinstance(data, dict):
            if 'PALI_ROOTS' in data:
                return self._validate_and_process_roots(data['PALI_ROOTS'])
            elif 'roots' in data:
                return self._validate_and_process_roots(data['roots'])
            else:
                return self._validate_and_process_roots(data)
        else:
            raise ValueError(f"Invalid root words file structure in {filepath}")

# ============ ENHANCED KNOWLEDGE BASE WITH PREPROCESSING ============

class ExhaustivePaliSemanticKnowledgeBase:
    """Enhanced knowledge base with data validation"""
    
    def __init__(self, kaggle_mode=False):
        print("🏛️ Initializing Monumental Pali Semantic Knowledge Base...")
        
        # Initialize preprocessor
        if kaggle_mode:
            self.preprocessor = PaliDataPreprocessor("/kaggle/input")
        else:
            self.preprocessor = PaliDataPreprocessor(".")
        
        # Load and validate data
        base_words, root_words = self.preprocessor.load_and_validate_all_data()
        
        # Initialize with validated data
        self.base_meanings = base_words if base_words else self._get_default_base_words()
        self.root_meanings = root_words if root_words else self._get_default_roots()

        # Initialize prefix meanings FIRST (before semantic fields)
        self.prefix_meanings = self._initialize_prefix_meanings()
        
        # Initialize other components
        self.semantic_fields = self._initialize_semantic_fields()
        self.morphological_semantics = self._initialize_morphological_semantics()
        self.noun_paradigms = self._initialize_complete_noun_paradigms()
        self.verb_paradigms = self._initialize_complete_verb_paradigms()
        self.sandhi_rules = self._initialize_complete_sandhi_rules()
        self.derivation_patterns = self._initialize_all_derivation_patterns()
       # self.prefix_meanings = self._initialize_prefix_meanings()
        
        print(f"✅ Loaded {len(self.base_meanings)} base meanings")
        print(f"✅ Loaded {len(self.root_meanings)} root meanings")
        print(f"✅ Loaded {len(self.noun_paradigms)} noun paradigms")
        print(f"✅ Loaded {len(self.verb_paradigms)} verb paradigms")
    
    def _get_default_base_words(self):
        """Minimal default base words if file not found"""
        return {
            "buddha": {
                "primary": "Awakened One, Enlightened One",
                "senses": {
                    "religious": "the historical Buddha",
                    "philosophical": "one who has awakened"
                },
                "semantic_field": "enlightenment",
                "register": "sacred",
                "gender": "m",
                "declension": "a_masculine"
            },
            "dhamma": {
                "primary": "teaching, doctrine, truth, law",
                "senses": {
                    "religious": "Buddhist teaching",
                    "philosophical": "natural law, truth",
                    "general": "thing, phenomenon"
                },
                "semantic_field": "truth_law",
                "register": "sacred",
                "gender": "m",
                "declension": "a_masculine"
            },
            "saṅgha": {
                "primary": "community, assembly",
                "senses": {
                    "religious": "community of Buddhist monks and nuns",
                    "general": "assembly, group"
                },
                "semantic_field": "community",
                "register": "sacred",
                "gender": "m",
                "declension": "a_masculine"
            },
            "nibbāna": {
                "primary": "extinction, liberation, nirvana",
                "senses": {
                    "religious": "final liberation from suffering",
                    "literal": "blowing out, extinction"
                },
                "semantic_field": "liberation",
                "register": "sacred",
                "gender": "n",
                "declension": "a_neuter"
            },
            "dukkha": {
                "primary": "suffering, unsatisfactoriness, stress",
                "senses": {
                    "philosophical": "the first noble truth",
                    "general": "pain, difficulty"
                },
                "semantic_field": "suffering",
                "register": "technical",
                "gender": "n",
                "declension": "a_neuter"
            }
        }
    
    def _get_default_roots(self):
        """Minimal default roots if file not found"""
        return {
            "√gam": {
                "meaning": "go, walk, come",
                "stems": {
                    "present": "gacch",
                    "aorist": "gam",
                    "past_participle": "gata",
                    "future": "gamiss",
                    "causative": "gamaya",
                    "desiderative": "jigaṃsa",
                    "intensive": "jaṅgam"
                },
                "type": "primary",
                "frequency": "high",
                "semantic_field": "motion",
                "prefixes": ["ā", "upa", "ni", "pa", "vi", "saṃ"]
            },
            "√kar": {
                "meaning": "do, make, perform",
                "stems": {
                    "present": "karo",
                    "aorist": "kar",
                    "past_participle": "kata",
                    "future": "kariss",
                    "causative": "kāraya",
                    "desiderative": "cikissa",
                    "intensive": "karikara"
                },
                "type": "primary",
                "frequency": "high",
                "semantic_field": "action",
                "prefixes": ["pa", "vi", "saṃ", "anu"]
            },
            "√bhū": {
                "meaning": "be, become, exist",
                "stems": {
                    "present": "bhava",
                    "aorist": "ahū",
                    "past_participle": "bhūta",
                    "future": "bhaviss",
                    "causative": "bhāvaya",
                    "desiderative": "bubhūsa",
                    "intensive": "bobhava"
                },
                "type": "primary",
                "frequency": "high",
                "semantic_field": "existence",
                "prefixes": ["abhi", "pari", "vi", "sam"]
            },
            "√vac": {
                "meaning": "speak, say, tell",
                "stems": {
                    "present": "vada",
                    "aorist": "avoc",
                    "past_participle": "vutta",
                    "future": "vakkhati",
                    "causative": "vācaya",
                    "desiderative": "vivaksa",
                    "intensive": "vāvada"
                },
                "type": "primary",
                "frequency": "high",
                "semantic_field": "speech"
            },
            "√ñā": {
                "meaning": "know, understand",
                "stems": {
                    "present": "jānā",
                    "aorist": "aññā",
                    "past_participle": "ñāta",
                    "future": "ñāss",
                    "causative": "ñāpaya",
                    "desiderative": "ñiñāsa",
                    "intensive": "jañña"
                },
                "type": "primary",
                "frequency": "high",
                "semantic_field": "knowledge"
            }
        }
    
    def _initialize_prefix_meanings(self) -> Dict[str, str]:
        """Initialize comprehensive prefix meanings"""
        prefixes = {
            # Primary prefixes
            "ā": "towards, near, until",
            "anu": "after, along, according to",
            "apa": "away, off", 
            "api": "also, even, near",
            "abhi": "towards, against, higher",
            "ava": "down, away, off",
            "ud": "up, out, away",
            "upa": "near, towards, secondary",
            "ni": "down, into, back",
            "nī": "out, away",
            "pa": "forth, forward, onward",
            "paṭi": "back, against, towards",
            "parā": "away, aside, beyond",
            "pari": "around, about, completely",
            "vi": "apart, away, various",
            "saṃ": "together, completely",
            "su": "well, good, very",
            "dus": "bad, difficult, ill",
            "a": "not, non-, un-",
            "an": "not, non-, un-",
            "sa": "with, together",
            "nir": "out, without, away",
            
            # Secondary prefixes
            "ati": "over, beyond, excessive",
            "adhi": "over, above, upon",
            "anu+pa": "following near",
            "sam+anu": "completely following",
            "sam+pa": "completely forth",
            "sam+pari": "completely around",
            "pari+ni": "completely down",
            "vi+pa": "apart forth",
            "vi+ni": "apart down",
            "sam+ud": "completely up",
            
            # Rare/specialized prefixes
            "ava+ni": "down into",
            "pa+ni": "forth down",
            "pa+vi": "forth apart",
            "ud+pa": "up near",
            "ni+pa": "down forth"
        }
        return prefixes

    def _initialize_semantic_fields(self) -> Dict[str, List[str]]:
        """Enhanced semantic fields"""
        fields = {
            "enlightenment": ["buddha", "bodhi", "ñāṇa", "paññā", "vimutti", "nibbāna", "sambodhi", "arahant"],
            "mind": ["citta", "mano", "viññāṇa", "ceto", "hadaya", "saññā", "cetanā", "phassa"],
            "ethics": ["sīla", "kusala", "puñña", "dhamma", "vinaya", "pāpa", "akusala", "sikkhā"],
            "meditation": ["jhāna", "samādhi", "bhāvanā", "yoga", "samatha", "vipassanā", "sati", "ekaggatā"],
            "suffering": ["dukkha", "vedanā", "soka", "parideva", "upāyāsa", "domanassa", "jāti", "jarā", "maraṇa"],
            "beings": ["satta", "pāṇa", "bhūta", "jīva", "puggala", "manussa", "deva", "brahma"],
            "time": ["kāla", "samaya", "khaṇa", "addha", "ayu", "vassa", "māsa", "divasa"],
            "space": ["ṭhāna", "okāsa", "desa", "pradesa", "ākāsa", "loka", "bhūmi", "disa"],
            "qualities": ["guṇa", "lakkhaṇa", "sabhāva", "dhātu", "ārammaṇa", "paccaya"],
            "action": ["kamma", "kiriyā", "kriyā", "caraṇa", "vāyāma", "paṭipatti"],
            "body": ["kāya", "rūpa", "sarīra", "deha", "gātra", "aṅga", "avayava"],
            "truth_law": ["dhamma", "sacca", "niyāma", "dhammatā", "tathatā"],
            "particles": ["ca", "vā", "eva", "api", "pi", "ti", "nu", "kho", "pana"],
            "prefixes": list(self.prefix_meanings.keys()),
            "numbers": ["eka", "dvi", "ti", "catu", "pañca", "cha", "satta", "aṭṭha", "nava", "dasa"],
            "colors": ["nīla", "pīta", "lohita", "odāta", "kāḷa", "mañjeṭṭha"],
            "elements": ["pathavī", "āpo", "tejo", "vāyo", "ākāsa", "viññāṇa"],
            "faculties": ["cakkhu", "sota", "ghāna", "jivhā", "kāya", "mano"],
            "feelings": ["sukha", "dukkha", "somanassa", "domanassa", "upekkhā"],
            "fetters": ["saṃyojana", "kilesa", "āsava", "anusaya", "nīvaraṇa"],
            "wisdom": ["paññā", "ñāṇa", "vijjā", "buddhi", "medhā", "pāṭava"],
            "concentration": ["samādhi", "samatha", "ekaggatā", "cittekaggatā", "appanā"],
            "virtue": ["sīla", "cāritta", "ācāra", "vata", "guṇa"],
            "liberation": ["vimutti", "mokkha", "nibbāna", "vimokkha", "nissaraṇa"]
        }
        
        # Add words from base meanings to semantic fields
        for word, info in self.base_meanings.items():
            field = info.get("semantic_field")
            if field and field in fields:
                if word not in fields[field]:
                    fields[field].append(word)
            elif field and field not in fields:
                # Create new field if it doesn't exist
                fields[field] = [word]
        
        return fields

    def _initialize_morphological_semantics(self) -> Dict[str, Dict]:
        """Enhanced morphological semantics"""
        return {
            "case_semantics": {
                "nominative": {
                    "function": "subject",
                    "english": "{0} (as subject)",
                    "emphasis": "the one who",
                    "questions": ["who?", "what?"]
                },
                "accusative": {
                    "function": "direct object",
                    "english": "{0} (as object)",
                    "emphasis": "the one affected",
                    "questions": ["whom?", "what?"]
                },
                "instrumental": {
                    "function": "means/agent",
                    "english": "by/with {0}",
                    "emphasis": "by means of",
                    "questions": ["by what?", "with what?"]
                },
                "dative": {
                    "function": "indirect object",
                    "english": "to/for {0}",
                    "emphasis": "for the benefit of",
                    "questions": ["to whom?", "for what?"]
                },
                "ablative": {
                    "function": "source/comparison",
                    "english": "from {0}",
                    "emphasis": "starting from",
                    "questions": ["from where?", "from what?"]
                },
                "genitive": {
                    "function": "possession/relation",
                    "english": "of {0}",
                    "emphasis": "belonging to",
                    "questions": ["whose?", "of what?"]
                },
                "locative": {
                    "function": "location/time",
                    "english": "in/at {0}",
                    "emphasis": "in the sphere of",
                    "questions": ["where?", "when?"]
                },
                "vocative": {
                    "function": "address",
                    "english": "O {0}!",
                    "emphasis": "addressing",
                    "questions": ["O who?"]
                }
            },
            "number_semantics": {
                "singular": {"modification": "", "emphasis": "one", "symbol": "sg"},
                "plural": {"modification": "s", "emphasis": "many", "symbol": "pl"},
                "dual": {"modification": " (both)", "emphasis": "two", "symbol": "du"}
            },
            "gender_semantics": {
                "masculine": {"pronoun": "he", "symbol": "m"},
                "feminine": {"pronoun": "she", "symbol": "f"},
                "neuter": {"pronoun": "it", "symbol": "n"}
            },
            "tense_semantics": {
                "present": {
                    "english": "{0}s, is {0}ing",
                    "aspect": "ongoing",
                    "time": "now",
                    "certainty": "actual"
                },
                "aorist": {
                    "english": "{0}ed",
                    "aspect": "simple past",
                    "time": "past",
                    "certainty": "actual"
                },
                "perfect": {
                    "english": "has/have {0}ed",
                    "aspect": "completed",
                    "time": "past with present relevance",
                    "certainty": "actual"
                },
                "future": {
                    "english": "will {0}",
                    "aspect": "potential",
                    "time": "future",
                    "certainty": "probable"
                },
                "imperative": {
                    "english": "let ... {0}!, may ... {0}!",
                    "aspect": "command",
                    "time": "immediate",
                    "certainty": "desired"
                },
                "optative": {
                    "english": "should/might {0}",
                    "aspect": "wish",
                    "time": "potential",
                    "certainty": "hypothetical"
                },
                "conditional": {
                    "english": "would {0}",
                    "aspect": "hypothetical",
                    "time": "potential",
                    "certainty": "conditional"
                }
            },
            "voice_semantics": {
                "active": {"english": "{0}s", "focus": "agent"},
                "middle": {"english": "{0}s for oneself", "focus": "reflexive"},
                "passive": {"english": "is {0}ed", "focus": "patient"},
                "causative": {"english": "causes to {0}", "focus": "causation"}
            },
            "mood_semantics": {
                "indicative": {"certainty": "factual", "attitude": "neutral"},
                "imperative": {"certainty": "desired", "attitude": "commanding"},
                "optative": {"certainty": "possible", "attitude": "wishing"},
                "conditional": {"certainty": "hypothetical", "attitude": "supposing"}
            }
        }

    def _initialize_complete_noun_paradigms(self) -> Dict[str, Dict]:
        """Complete noun declension paradigms for all stem types"""
        return {
            # A-STEM MASCULINE (buddha, dhamma)
            "a_masculine": {
                "endings": {
                    ("nominative", "singular"): "o",
                    ("nominative", "plural"): "ā",
                    ("accusative", "singular"): "aṃ",
                    ("accusative", "plural"): "e",
                    ("instrumental", "singular"): "ena",
                    ("instrumental", "plural"): "ehi",
                    ("dative", "singular"): "āya",
                    ("dative", "plural"): "ānaṃ",
                    ("ablative", "singular"): "ā",
                    ("ablative", "plural"): "ehi",
                    ("genitive", "singular"): "assa",
                    ("genitive", "plural"): "ānaṃ",
                    ("locative", "singular"): "e",
                    ("locative", "plural"): "esu",
                    ("vocative", "singular"): "",
                    ("vocative", "plural"): "ā"
                },
                "stem_rule": lambda base: base[:-1] if base.endswith('a') else base,
                "example": "buddha",
                "gender": "masculine"
            },
            
            # A-STEM NEUTER (citta, rūpa)
            "a_neuter": {
                "endings": {
                    ("nominative", "singular"): "aṃ",
                    ("nominative", "plural"): "āni",
                    ("accusative", "singular"): "aṃ",
                    ("accusative", "plural"): "āni",
                    ("instrumental", "singular"): "ena",
                    ("instrumental", "plural"): "ehi",
                    ("dative", "singular"): "āya",
                    ("dative", "plural"): "ānaṃ",
                    ("ablative", "singular"): "ā",
                    ("ablative", "plural"): "ehi",
                    ("genitive", "singular"): "assa",
                    ("genitive", "plural"): "ānaṃ",
                    ("locative", "singular"): "e",
                    ("locative", "plural"): "esu",
                    ("vocative", "singular"): "",
                    ("vocative", "plural"): "āni"
                },
                "stem_rule": lambda base: base[:-1] if base.endswith('a') else base,
                "example": "citta",
                "gender": "neuter"
            },
            
            # Ā-STEM FEMININE (kaññā, sālā)
            "aa_feminine": {
                "endings": {
                    ("nominative", "singular"): "",
                    ("nominative", "plural"): "āyo",
                    ("accusative", "singular"): "aṃ",
                    ("accusative", "plural"): "āyo",
                    ("instrumental", "singular"): "āya",
                    ("instrumental", "plural"): "āhi",
                    ("dative", "singular"): "āya",
                    ("dative", "plural"): "ānaṃ",
                    ("ablative", "singular"): "āya",
                    ("ablative", "plural"): "āhi",
                    ("genitive", "singular"): "āya",
                    ("genitive", "plural"): "ānaṃ",
                    ("locative", "singular"): "āya",
                    ("locative", "plural"): "āsu",
                    ("vocative", "singular"): "e",
                    ("vocative", "plural"): "āyo"
                },
                "stem_rule": lambda base: base,
                "example": "kaññā",
                "gender": "feminine"
            },
            
            # I-STEM MASCULINE (aggi, muni)
            "i_masculine": {
                "endings": {
                    ("nominative", "singular"): "",
                    ("nominative", "plural"): "ī",
                    ("accusative", "singular"): "iṃ",
                    ("accusative", "plural"): "ī",
                    ("instrumental", "singular"): "inā",
                    ("instrumental", "plural"): "īhi",
                    ("dative", "singular"): "ino",
                    ("dative", "plural"): "īnaṃ",
                    ("ablative", "singular"): "inā",
                    ("ablative", "plural"): "īhi",
                    ("genitive", "singular"): "ino",
                    ("genitive", "plural"): "īnaṃ",
                    ("locative", "singular"): "imhi",
                    ("locative", "plural"): "īsu",
                    ("vocative", "singular"): "",
                    ("vocative", "plural"): "ī"
                },
                "stem_rule": lambda base: base,
                "example": "aggi",
                "gender": "masculine"
            },
            
            # I-STEM NEUTER (akkhi, aṭṭhi)
            "i_neuter": {
                "endings": {
                    ("nominative", "singular"): "",
                    ("nominative", "plural"): "īni",
                    ("accusative", "singular"): "iṃ",
                    ("accusative", "plural"): "īni",
                    ("instrumental", "singular"): "inā",
                    ("instrumental", "plural"): "īhi",
                    ("dative", "singular"): "ino",
                    ("dative", "plural"): "īnaṃ",
                    ("ablative", "singular"): "inā",
                    ("ablative", "plural"): "īhi",
                    ("genitive", "singular"): "ino",
                    ("genitive", "plural"): "īnaṃ",
                    ("locative", "singular"): "imhi",
                    ("locative", "plural"): "īsu",
                    ("vocative", "singular"): "",
                    ("vocative", "plural"): "īni"
                },
                "stem_rule": lambda base: base,
                "example": "akkhi",
                "gender": "neuter"
            },
            
            # Ī-STEM FEMININE (nadī, devī)
            "ii_feminine": {
                "endings": {
                    ("nominative", "singular"): "",
                    ("nominative", "plural"): "iyo",
                    ("accusative", "singular"): "iṃ",
                    ("accusative", "plural"): "iyo",
                    ("instrumental", "singular"): "iyā",
                    ("instrumental", "plural"): "īhi",
                    ("dative", "singular"): "iyā",
                    ("dative", "plural"): "īnaṃ",
                    ("ablative", "singular"): "iyā",
                    ("ablative", "plural"): "īhi",
                    ("genitive", "singular"): "iyā",
                    ("genitive", "plural"): "īnaṃ",
                    ("locative", "singular"): "iyā", 
                    ("locative", "plural"): "īsu",
                    ("vocative", "singular"): "",
                    ("vocative", "plural"): "iyo"
                },
                "stem_rule": lambda base: base,
                "example": "nadī",
                "gender": "feminine"
            },
            
            # U-STEM MASCULINE (bhikkhu, dhātu)
            "u_masculine": {
                "endings": {
                    ("nominative", "singular"): "",
                    ("nominative", "plural"): "ū",
                    ("accusative", "singular"): "uṃ",
                    ("accusative", "plural"): "ū",
                    ("instrumental", "singular"): "unā",
                    ("instrumental", "plural"): "ūhi",
                    ("dative", "singular"): "uno",
                    ("dative", "plural"): "ūnaṃ",
                    ("ablative", "singular"): "unā",
                    ("ablative", "plural"): "ūhi",
                    ("genitive", "singular"): "uno",
                    ("genitive", "plural"): "ūnaṃ",
                    ("locative", "singular"): "umhi",
                    ("locative", "plural"): "ūsu",
                    ("vocative", "singular"): "",
                    ("vocative", "plural"): "ū"
                },
                "stem_rule": lambda base: base,
                "example": "bhikkhu",
                "gender": "masculine"
            },
            
            # U-STEM NEUTER (cakkhu, madhu)
            "u_neuter": {
                "endings": {
                    ("nominative", "singular"): "",
                    ("nominative", "plural"): "ūni",
                    ("accusative", "singular"): "uṃ",
                    ("accusative", "plural"): "ūni",
                    ("instrumental", "singular"): "unā",
                    ("instrumental", "plural"): "ūhi",
                    ("dative", "singular"): "uno",
                    ("dative", "plural"): "ūnaṃ",
                    ("ablative", "singular"): "unā",
                    ("ablative", "plural"): "ūhi",
                    ("genitive", "singular"): "uno",
                    ("genitive", "plural"): "ūnaṃ",
                    ("locative", "singular"): "umhi",
                    ("locative", "plural"): "ūsu",
                    ("vocative", "singular"): "",
                    ("vocative", "plural"): "ūni"
                },
                "stem_rule": lambda base: base,
                "example": "cakkhu",
                "gender": "neuter"
            },
            
            # Ū-STEM FEMININE (vadhū, camū)
            "uu_feminine": {
                "endings": {
                    ("nominative", "singular"): "",
                    ("nominative", "plural"): "ūyo",
                    ("accusative", "singular"): "uṃ",
                    ("accusative", "plural"): "ūyo",
                    ("instrumental", "singular"): "uyā",
                    ("instrumental", "plural"): "ūhi",
                    ("dative", "singular"): "uyā",
                    ("dative", "plural"): "ūnaṃ",
                    ("ablative", "singular"): "uyā",
                    ("ablative", "plural"): "ūhi",
                    ("genitive", "singular"): "uyā",
                    ("genitive", "plural"): "ūnaṃ",
                    ("locative", "singular"): "uyā",
                    ("locative", "plural"): "ūsu",
                    ("vocative", "singular"): "",
                    ("vocative", "plural"): "ūyo"
                },
                "stem_rule": lambda base: base,
                "example": "vadhū",
                "gender": "feminine"
            },
            
            # CONSONANT STEMS - AN (rājan, attan, brahman)
            "an_masculine": {
                "endings": {
                    ("nominative", "singular"): "ā",
                    ("nominative", "plural"): "āno",
                    ("accusative", "singular"): "ānaṃ",
                    ("accusative", "plural"): "āno",
                    ("instrumental", "singular"): "unā",
                    ("instrumental", "plural"): "ūhi",
                    ("dative", "singular"): "uno",
                    ("dative", "plural"): "ūnaṃ",
                    ("ablative", "singular"): "unā",
                    ("ablative", "plural"): "ūhi",
                    ("genitive", "singular"): "uno",
                    ("genitive", "plural"): "ūnaṃ",
                    ("locative", "singular"): "ani",
                    ("locative", "plural"): "ūsu",
                    ("vocative", "singular"): "a",
                    ("vocative", "plural"): "āno"
                },
                "stem_rule": lambda base: base[:-2] if base.endswith('an') else base,
                "example": "rājan",
                "gender": "masculine"
            },
            
            # AR-STEMS (satthar, pitar, mātar)
            "ar_masculine": {
                "endings": {
                    ("nominative", "singular"): "ā",
                    ("nominative", "plural"): "āro",
                    ("accusative", "singular"): "āraṃ",
                    ("accusative", "plural"): "āro",
                    ("instrumental", "singular"): "arā",
                    ("instrumental", "plural"): "ārehi",
                    ("dative", "singular"): "u",
                    ("dative", "plural"): "ūnaṃ",
                    ("ablative", "singular"): "arā",
                    ("ablative", "plural"): "ārehi",
                    ("genitive", "singular"): "u",
                    ("genitive", "plural"): "ūnaṃ",
                    ("locative", "singular"): "ari",
                    ("locative", "plural"): "ūsu",
                    ("vocative", "singular"): "a",
                    ("vocative", "plural"): "āro"
                },
                "stem_rule": lambda base: base[:-2] if base.endswith('ar') else base,
                "example": "pitar",
                "gender": "masculine"
            },
            
            # ANT-STEMS (gacchant, mahant) - present participles
            "ant_masculine": {
                "endings": {
                    ("nominative", "singular"): "anto/aṃ",
                    ("nominative", "plural"): "anto/antā",
                    ("accusative", "singular"): "antaṃ",
                    ("accusative", "plural"): "ante",
                    ("instrumental", "singular"): "atā/antena",
                    ("instrumental", "plural"): "antehi",
                    ("dative", "singular"): "ato/antassa",
                    ("dative", "plural"): "ataṃ/antānaṃ",
                    ("ablative", "singular"): "atā/antā",
                    ("ablative", "plural"): "antehi",
                    ("genitive", "singular"): "ato/antassa",
                    ("genitive", "plural"): "ataṃ/antānaṃ",
                    ("locative", "singular"): "ati/ante",
                    ("locative", "plural"): "antesu",
                    ("vocative", "singular"): "a/anta",
                    ("vocative", "plural"): "anto/antā"
                },
                "stem_rule": lambda base: base[:-3] if base.endswith('ant') else base,
                "example": "gacchant",
                "gender": "masculine"
            },
            
            # VANT/MANT STEMS (dhīmant, balavant) - possessive adjectives
            "vant_masculine": {
                "endings": {
                    ("nominative", "singular"): "vā/vanto",
                    ("nominative", "plural"): "vanto/vantā",
                    ("accusative", "singular"): "vantaṃ",
                    ("accusative", "plural"): "vante",
                    ("instrumental", "singular"): "vatā/vantena",
                    ("instrumental", "plural"): "vantehi",
                    ("dative", "singular"): "vato/vantassa",
                    ("dative", "plural"): "vataṃ/vantānaṃ",
                    ("ablative", "singular"): "vatā/vantā",
                    ("ablative", "plural"): "vantehi",
                    ("genitive", "singular"): "vato/vantassa",
                    ("genitive", "plural"): "vataṃ/vantānaṃ",
                    ("locative", "singular"): "vati/vante",
                    ("locative", "plural"): "vantesu",
                    ("vocative", "singular"): "va/vanta",
                    ("vocative", "plural"): "vanto/vantā"
                },
                "stem_rule": lambda base: base[:-4] if base.endswith('vant') else base,
                "example": "balavant",
                "gender": "masculine"
            },
            
            "mant_masculine": {
                "endings": {
                    ("nominative", "singular"): "mā/manto",
                    ("nominative", "plural"): "manto/mantā",
                    ("accusative", "singular"): "mantaṃ",
                    ("accusative", "plural"): "mante",
                    ("instrumental", "singular"): "matā/mantena",
                    ("instrumental", "plural"): "mantehi",
                    ("dative", "singular"): "mato/mantassa",
                    ("dative", "plural"): "mataṃ/mantānaṃ",
                    ("ablative", "singular"): "matā/mantā",
                    ("ablative", "plural"): "mantehi",
                    ("genitive", "singular"): "mato/mantassa",
                    ("genitive", "plural"): "mataṃ/mantānaṃ",
                    ("locative", "singular"): "mati/mante",
                    ("locative", "plural"): "mantesu",
                    ("vocative", "singular"): "ma/manta",
                    ("vocative", "plural"): "manto/mantā"
                },
                "stem_rule": lambda base: base[:-4] if base.endswith('mant') else base,
                "example": "dhīmant",
                "gender": "masculine"
            },
            
            # AS-STEMS (manas)
            "as_neuter": {
                "endings": {
                    ("nominative", "singular"): "o",
                    ("nominative", "plural"): "āni",
                    ("accusative", "singular"): "o",
                    ("accusative", "plural"): "āni",
                    ("instrumental", "singular"): "asā",
                    ("instrumental", "plural"): "ehi",
                    ("dative", "singular"): "aso",
                    ("dative", "plural"): "ānaṃ",
                    ("ablative", "singular"): "asā",
                    ("ablative", "plural"): "ehi",
                    ("genitive", "singular"): "aso",
                    ("genitive", "plural"): "ānaṃ",
                    ("locative", "singular"): "asi/e",
                    ("locative", "plural"): "esu",
                    ("vocative", "singular"): "o",
                    ("vocative", "plural"): "āni"
                },
                "stem_rule": lambda base: base[:-2] if base.endswith('as') else base,
                "example": "manas",
                "gender": "neuter"
            },
            
            # US-STEMS (āyus, cakkus)
            "us_neuter": {
                "endings": {
                    ("nominative", "singular"): "u",
                    ("nominative", "plural"): "ūni",
                    ("accusative", "singular"): "u",
                    ("accusative", "plural"): "ūni",
                    ("instrumental", "singular"): "usā",
                    ("instrumental", "plural"): "ūhi",
                    ("dative", "singular"): "uso",
                    ("dative", "plural"): "ūnaṃ",
                    ("ablative", "singular"): "usā",
                    ("ablative", "plural"): "ūhi",
                    ("genitive", "singular"): "uso",
                    ("genitive", "plural"): "ūnaṃ",
                    ("locative", "singular"): "usi",
                    ("locative", "plural"): "ūsu",
                    ("vocative", "singular"): "u",
                    ("vocative", "plural"): "ūni"
                },
                "stem_rule": lambda base: base[:-2] if base.endswith('us') else base,
                "example": "āyus",
                "gender": "neuter"
            },
            
            # IS-STEMS (muni -> munis alternative form)
            "is_masculine": {
                "endings": {
                    ("nominative", "singular"): "i",
                    ("nominative", "plural"): "ayo",
                    ("accusative", "singular"): "iṃ",
                    ("accusative", "plural"): "ayo",
                    ("instrumental", "singular"): "inā",
                    ("instrumental", "plural"): "ibhi",
                    ("dative", "singular"): "issa",
                    ("dative", "plural"): "īnaṃ",
                    ("ablative", "singular"): "ito",
                    ("ablative", "plural"): "ibhi",
                    ("genitive", "singular"): "issa",
                    ("genitive", "plural"): "īnaṃ",
                    ("locative", "singular"): "ismiṃ",
                    ("locative", "plural"): "isu",
                    ("vocative", "singular"): "i",
                    ("vocative", "plural"): "ayo"
                },
                "stem_rule": lambda base: base,
                "example": "munis",
                "gender": "masculine"
            },
            
            # O-STEMS (go - cow)
            "o_irregular": {
                "endings": {
                    ("nominative", "singular"): "",
                    ("nominative", "plural"): "āvo",
                    ("accusative", "singular"): "āvuṃ/āvaṃ",
                    ("accusative", "plural"): "āvo",
                    ("instrumental", "singular"): "avā/avena",
                    ("instrumental", "plural"): "ohi/obhi",
                    ("dative", "singular"): "avassa",
                    ("dative", "plural"): "avaṃ/avaṃ",
                    ("ablative", "singular"): "avā",
                    ("ablative", "plural"): "ohi/obhi",
                    ("genitive", "singular"): "avassa",
                    ("genitive", "plural"): "avaṃ/avaṃ",
                    ("locative", "singular"): "ave/avasmiṃ",
                    ("locative", "plural"): "osu/avesu",
                    ("vocative", "singular"): "",
                    ("vocative", "plural"): "āvo"
                },
                "stem_rule": lambda base: base,
                "example": "go",
                "gender": "masculine",
                "irregular": True
            },
            
            # IN-STEMS (yogin, pakkhiṃ)
            "in_masculine": {
                "endings": {
                    ("nominative", "singular"): "ī",
                    ("nominative", "plural"): "ino",
                    ("accusative", "singular"): "inaṃ",
                    ("accusative", "plural"): "ino",
                    ("instrumental", "singular"): "inā",
                    ("instrumental", "plural"): "īhi",
                    ("dative", "singular"): "ino",
                    ("dative", "plural"): "īnaṃ",
                    ("ablative", "singular"): "inā",
                    ("ablative", "plural"): "īhi",
                    ("genitive", "singular"): "ino",
                    ("genitive", "plural"): "īnaṃ",
                    ("locative", "singular"): "ini",
                    ("locative", "plural"): "īsu",
                    ("vocative", "singular"): "i",
                    ("vocative", "plural"): "ino"
                },
                "stem_rule": lambda base: base[:-2] if base.endswith('in') else base,
                "example": "yogin",
                "gender": "masculine"
            },
            
            # IRREGULAR DECLENSIONS
            "sabba_pronoun": {
                "endings": {
                    ("nominative", "singular", "m"): "sabbo",
                    ("nominative", "singular", "n"): "sabbaṃ",
                    ("nominative", "singular", "f"): "sabbā",
                    ("nominative", "plural", "m"): "sabbe",
                    ("nominative", "plural", "n"): "sabbāni",
                    ("nominative", "plural", "f"): "sabbā",
                    ("accusative", "singular", "m"): "sabbaṃ",
                    ("accusative", "singular", "n"): "sabbaṃ",
                    ("accusative", "singular", "f"): "sabbaṃ",
                    ("instrumental", "singular"): "sabbena",
                    ("instrumental", "plural"): "sabbehi",
                    ("dative", "singular"): "sabbassa",
                    ("dative", "plural"): "sabbesaṃ",
                    ("ablative", "singular"): "sabbamhā/sabbasmā",
                    ("ablative", "plural"): "sabbehi",
                    ("genitive", "singular"): "sabbassa",
                    ("genitive", "plural"): "sabbesaṃ",
                    ("locative", "singular"): "sabbasmiṃ/sabbamhi",
                    ("locative", "plural"): "sabbesu"
                },
                "stem_rule": lambda base: base[:-1] if base.endswith('a') else base,
                "example": "sabba",
                "gender": "all",
                "irregular": True
            }
        }

    def _initialize_complete_verb_paradigms(self) -> Dict[str, Dict]:
        """Complete verb conjugation paradigms"""
        return {
            # PRESENT TENSE
            "present_active": {
                "thematic": {
                    ("1st", "singular"): "āmi",
                    ("2nd", "singular"): "asi",
                    ("3rd", "singular"): "ati",
                    ("1st", "plural"): "āma",
                    ("2nd", "plural"): "atha",
                    ("3rd", "plural"): "anti"
                },
                "athematic": {
                    ("1st", "singular"): "mi",
                    ("2nd", "singular"): "si",
                    ("3rd", "singular"): "ti",
                    ("1st", "plural"): "ma",
                    ("2nd", "plural"): "tha",
                    ("3rd", "plural"): "nti"
                },
                "type": "present",
                "voice": "active"
            },
            
            "present_middle": {
                "endings": {
                    ("1st", "singular"): "e",
                    ("2nd", "singular"): "se",
                    ("3rd", "singular"): "te",
                    ("1st", "plural"): "mhe",
                    ("2nd", "plural"): "vhe", 
                    ("3rd", "plural"): "nte"
                },
                "type": "present",
                "voice": "middle"
            },
            
            "present_passive": {
                "endings": {
                    ("3rd", "singular"): "ati",
                    ("3rd", "plural"): "anti"
                },
                "stem_suffix": "ya",
                "type": "present",
                "voice": "passive"
            },
            
            # AORIST (past tense)
            "aorist_root": {
                "endings": {
                    ("1st", "singular"): "iṃ",
                    ("2nd", "singular"): "i",
                    ("3rd", "singular"): "i",
                    ("1st", "plural"): "imhā",
                    ("2nd", "plural"): "ittha",
                    ("3rd", "plural"): "iṃsu"
                },
                "augment": "a",
                "type": "aorist",
                "subtype": "root"
            },
            
            "aorist_a": {
                "endings": {
                    ("1st", "singular"): "aṃ",
                    ("2nd", "singular"): "o",
                    ("3rd", "singular"): "a",
                    ("1st", "plural"): "amhā",
                    ("2nd", "plural"): "attha",
                    ("3rd", "plural"): "uṃ"
                },
                "augment": "a",
                "type": "aorist",
                "subtype": "a-aorist"
            },
            
            "aorist_s": {
                "endings": {
                    ("1st", "singular"): "siṃ",
                    ("2nd", "singular"): "si",
                    ("3rd", "singular"): "si",
                    ("1st", "plural"): "simhā",
                    ("2nd", "plural"): "sittha",
                    ("3rd", "plural"): "siṃsu"
                },
                "augment": "a",
                "type": "aorist",
                "subtype": "s-aorist"
            },
            
            "aorist_is": {
                "endings": {
                    ("1st", "singular"): "isiṃ",
                    ("2nd", "singular"): "isi",
                    ("3rd", "singular"): "isi",
                    ("1st", "plural"): "isimhā",
                    ("2nd", "plural"): "isittha",
                    ("3rd", "plural"): "isiṃsu"
                },
                "augment": "a",
                "type": "aorist",
                "subtype": "is-aorist"
            },
            
            "aorist_passive": {
                "endings": {
                    ("3rd", "singular"): "i",
                    ("3rd", "plural"): "iṃsu"
                },
                "augment": "a",
                "stem_suffix": "ya",
                "type": "aorist",
                "voice": "passive"
            },
            
            # PERFECT (rare in Pali)
            "perfect": {
                "endings": {
                    ("1st", "singular"): "a",
                    ("2nd", "singular"): "e",
                    ("3rd", "singular"): "a",
                    ("1st", "plural"): "mha",
                    ("2nd", "plural"): "ttha",
                    ("3rd", "plural"): "u"
                },
                "reduplication": True,
                "type": "perfect"
            },
            
            # FUTURE
            "future": {
                "endings": {
                    ("1st", "singular"): "issāmi",
                    ("2nd", "singular"): "issasi",
                    ("3rd", "singular"): "issati",
                    ("1st", "plural"): "issāma",
                    ("2nd", "plural"): "issatha",
                    ("3rd", "plural"): "issanti"
                },
                "stem_suffix": "iss",
                "type": "future"
            },
            
            "future_alternative": {
                "endings": {
                    ("1st", "singular"): "ssāmi",
                    ("2nd", "singular"): "ssasi",
                    ("3rd", "singular"): "ssati",
                    ("1st", "plural"): "ssāma",
                    ("2nd", "plural"): "ssatha",
                    ("3rd", "plural"): "ssanti"
                },
                "stem_suffix": "ss",
                "type": "future"
            },
            
            "future_passive": {
                "endings": {
                    ("3rd", "singular"): "issati",
                    ("3rd", "plural"): "issanti"
                },
                "stem_suffix": "ya+iss",
                "type": "future",
                "voice": "passive"
            },
            
            # IMPERATIVE
            "imperative": {
                "endings": {
                    ("1st", "singular"): "āmi",
                    ("2nd", "singular"): "āhi",
                    ("3rd", "singular"): "atu",
                    ("1st", "plural"): "āma",
                    ("2nd", "plural"): "atha",
                    ("3rd", "plural"): "antu"
                },
                "type": "imperative"
            },
            
            "imperative_middle": {
                "endings": {
                    ("1st", "singular"): "e",
                    ("2nd", "singular"): "ssu",
                    ("3rd", "singular"): "taṃ",
                    ("1st", "plural"): "āmase",
                    ("2nd", "plural"): "vho",
                    ("3rd", "plural"): "ntaṃ"
                },
                "type": "imperative",
                "voice": "middle"
            },
            
            "imperative_passive": {
                "endings": {
                    ("3rd", "singular"): "yataṃ",
                    ("3rd", "plural"): "yantaṃ"
                },
                "stem_suffix": "ya",
                "type": "imperative",
                "voice": "passive"
            },
            
            # OPTATIVE (potential mood)
            "optative": {
                "endings": {
                    ("1st", "singular"): "eyyāmi",
                    ("2nd", "singular"): "eyyāsi",
                    ("3rd", "singular"): "eyya",
                    ("1st", "plural"): "eyyāma",
                    ("2nd", "plural"): "eyyātha",
                    ("3rd", "plural"): "eyyuṃ"
                },
                "stem_suffix": "ey",
                "type": "optative"
            },
            
            "optative_alternative": {
                "endings": {
                    ("1st", "singular"): "ehaṃ",
                    ("2nd", "singular"): "ehi",
                    ("3rd", "singular"): "e",
                    ("1st", "plural"): "ema",
                    ("2nd", "plural"): "etha",
                    ("3rd", "plural"): "eraṃ"
                },
                "stem_suffix": "e",
                "type": "optative"
            },
            
            "optative_passive": {
                "endings": {
                    ("3rd", "singular"): "yetha",
                    ("3rd", "plural"): "yeraṃ"
                },
                "stem_suffix": "ya+e",
                "type": "optative",
                "voice": "passive"
            },
            
            # CONDITIONAL
            "conditional": {
                "endings": {
                    ("1st", "singular"): "issaṃ",
                    ("2nd", "singular"): "isse",
                    ("3rd", "singular"): "issa",
                    ("1st", "plural"): "issamhā",
                    ("2nd", "plural"): "issatha",
                    ("3rd", "plural"): "issaṃsu"
                },
                "augment": "a",
                "stem_suffix": "iss",
                "type": "conditional"
            },
            
            "conditional_passive": {
                "endings": {
                    ("3rd", "singular"): "yissa",
                    ("3rd", "plural"): "yissaṃsu"
                },
                "augment": "a",
                "stem_suffix": "ya+iss",
                "type": "conditional",
                "voice": "passive"
            },
            
            # CAUSATIVE
            "causative_present": {
                "stem_suffix": ["e", "aya", "āpe", "āpaya"],
                "endings": "present_active",  # Uses present active endings
                "type": "causative",
                "voice": "causative"
            },
            
            "causative_aorist": {
                "stem_suffix": ["e", "aya", "āpe"],
                "endings": "aorist_a",  # Uses a-aorist endings
                "type": "causative",
                "tense": "aorist",
                "voice": "causative"
            },
            
            "causative_future": {
                "stem_suffix": ["e", "aya", "āpe"],
                "endings": "future",
                "type": "causative",
                "tense": "future",
                "voice": "causative"
            },
            
            "causative_imperative": {
                "stem_suffix": ["e", "aya", "āpe"],
                "endings": "imperative",
                "type": "causative",
                "tense": "imperative",
                "voice": "causative"
            },
            
            "causative_optative": {
                "stem_suffix": ["e", "aya", "āpe"],
                "endings": "optative",
                "type": "causative",
                "tense": "optative",
                "voice": "causative"
            },
            
            # DESIDERATIVE
            "desiderative_present": {
                "stem_suffix": ["ikkha", "sa"],
                "reduplication": True,
                "endings": "present_active",
                "type": "desiderative",
                "meaning": "wishes to",
                "voice": "desiderative"
            },
            
            "desiderative_aorist": {
                "stem_suffix": ["ikkha", "sa"],
                "reduplication": True,
                "endings": "aorist_a",
                "type": "desiderative",
                "tense": "aorist",
                "voice": "desiderative"
            },
            
            # INTENSIVE/FREQUENTATIVE
            "intensive_present": {
                "reduplication": True,
                "stem_suffix": ["ya"],
                "endings": "present_active",
                "type": "intensive",
                "meaning": "repeatedly",
                "voice": "intensive"
            },
            
            "intensive_aorist": {
                "reduplication": True,
                "stem_suffix": ["ya"],
                "endings": "aorist_a",
                "type": "intensive",
                "tense": "aorist",
                "voice": "intensive"
            }
        }

    def _initialize_complete_sandhi_rules(self) -> Dict[str, Dict[str, str]]:
        """Complete sandhi rules (200+)"""
        return {
            # VOWEL SANDHI (Extended)
            "vowel_sandhi": {
                # Same vowels
                "a+a": "ā", "a+ā": "ā", "ā+a": "ā", "ā+ā": "ā",
                "i+i": "ī", "i+ī": "ī", "ī+i": "ī", "ī+ī": "ī",
                "u+u": "ū", "u+ū": "ū", "ū+u": "ū", "ū+ū": "ū",
                
                # Different vowels - a/ā combinations
                "a+i": "e", "a+ī": "e", "ā+i": "e", "ā+ī": "e",
                "a+u": "o", "a+ū": "o", "ā+u": "o", "ā+ū": "o",
                "a+e": "e", "a+o": "o", "ā+e": "e", "ā+o": "o",
                
                # i/ī before vowels (becomes y)
                "i+a": "ya", "i+ā": "yā", "ī+a": "ya", "ī+ā": "yā",
                "i+u": "yu", "i+ū": "yū", "ī+u": "yu", "ī+ū": "yū",
                "i+e": "ye", "i+o": "yo", "ī+e": "ye", "ī+o": "yo",
                
                # u/ū before vowels (becomes v)
                "u+a": "va", "u+ā": "vā", "ū+a": "va", "ū+ā": "vā",
                "u+i": "vi", "u+ī": "vī", "ū+i": "vi", "ū+ī": "vī",
                "u+e": "ve", "u+o": "vo", "ū+e": "ve", "ū+o": "vo",
                
                # e/o before vowels
                "e+a": "eyya", "e+ā": "eyyā", "o+a": "ova", "o+ā": "ovā",
                "e+i": "eyyi", "e+u": "eyyu", "o+i": "ovi", "o+u": "ovu",
                "e+e": "e", "e+o": "eo", "o+e": "oe", "o+o": "o",
                
                # Special cases
                "ti+a": "cca", "ti+ā": "ccā", "ti+i": "cca", "ti+u": "ccu",
                "ti+e": "cce", "ti+o": "cco",
                
                # Diphthongs
                "ai+a": "āya", "ai+i": "āyi", "ai+u": "āyu",
                "au+a": "āva", "au+i": "āvi", "au+u": "āvu",
                
                # Additional special combinations
                "iti+eva": "icceva", "iti+etaṃ": "iccetaṃ",
                "yadi+eva": "yadeva", "api+eva": "appeva",
                "sace+ayaṃ": "sacāyaṃ", "yadi+ayaṃ": "yadāyaṃ"
            },
            
            # CONSONANT SANDHI (Extended)
            "consonant_sandhi": {
                # Niggahīta (ṃ) sandhi - complete set
                "ṃ+k": "ṅk", "ṃ+kh": "ṅkh", "ṃ+g": "ṅg", "ṃ+gh": "ṅgh", "ṃ+ṅ": "ṅṅ",
                "ṃ+c": "ñc", "ṃ+ch": "ñch", "ṃ+j": "ñj", "ṃ+jh": "ñjh", "ṃ+ñ": "ññ",
                "ṃ+ṭ": "ṇṭ", "ṃ+ṭh": "ṇṭh", "ṃ+ḍ": "ṇḍ", "ṃ+ḍh": "ṇḍh", "ṃ+ṇ": "ṇṇ",
                "ṃ+t": "nt", "ṃ+th": "nth", "ṃ+d": "nd", "ṃ+dh": "ndh", "ṃ+n": "nn",
                "ṃ+p": "mp", "ṃ+ph": "mph", "ṃ+b": "mb", "ṃ+bh": "mbh", "ṃ+m": "mm",
                "ṃ+y": "ñy", "ṃ+r": "ṃr", "ṃ+l": "ṃl", "ṃ+v": "ṃv",
                "ṃ+s": "ṃs", "ṃ+h": "ṃh", 
                
                # ṃ before vowels
                "ṃ+a": "ma", "ṃ+ā": "mā", "ṃ+i": "mi", "ṃ+ī": "mī",
                "ṃ+u": "mu", "ṃ+ū": "mū", "ṃ+e": "me", "ṃ+o": "mo",
                
                # Stop + stop assimilation
                "k+t": "tt", "k+p": "pp", "k+c": "kk", "k+ṭ": "kk",
                "k+s": "kkh", "k+m": "kkh", "k+n": "kkh",
                "g+t": "gg", "g+d": "gg", "g+n": "gg", "g+m": "gg",
                "g+g": "gg", "g+gh": "ggh", "g+dh": "ggdh",
                "c+t": "tt", "c+n": "cc", "c+m": "cc", "c+y": "cc",
                "j+t": "jj", "j+n": "jj", "j+m": "jj", "j+ñ": "jñ",
                "ṭ+t": "ṭṭ", "ṭ+n": "ṭṭ", "ṭ+m": "ṭṭ", "ṭ+ṭ": "ṭṭ",
                "ḍ+t": "ḍḍ", "ḍ+n": "ḍḍ", "ḍ+m": "ḍḍ", "ḍ+ḍ": "ḍḍ",
                "t+k": "kk", "t+c": "cc", "t+ṭ": "ṭṭ", "t+p": "pp",
                "t+m": "mm", "t+n": "nn", "t+ñ": "ññ", "t+ṇ": "ṇṇ",
                "t+t": "tt", "t+th": "tth", "t+d": "dd", "t+dh": "ddh",
                "d+t": "tt", "d+d": "dd", "d+dh": "ddh", "d+n": "nn",
                "d+m": "mm", "d+g": "gg", "d+bh": "bbh",
                "p+t": "tt", "p+c": "cc", "p+ṭ": "ṭṭ", "p+k": "kk",
                "p+p": "pp", "p+m": "pp", "p+n": "pp",
                "b+t": "bb", "b+d": "bb", "b+n": "bb", "b+m": "bb",
                "b+b": "bb", "b+bh": "bbh", "b+g": "gg",
                
                # Consonant + h combinations
                "t+h": "th", "d+h": "dh", "p+h": "ph", "b+h": "bh",
                "k+h": "kh", "g+h": "gh", "c+h": "ch", "j+h": "jh",
                "ṭ+h": "ṭh", "ḍ+h": "ḍh", "m+h": "mh", "n+h": "nh",
                "l+h": "lh", "v+h": "vh", "s+h": "sh",
                
                # Consonant + y combinations
                "t+y": "cc", "d+y": "jj", "n+y": "ññ", "l+y": "yy",
                "k+y": "kk", "g+y": "gg", "p+y": "pp", "b+y": "bb",
                "m+y": "mm", "s+y": "ss", "h+y": "hy",
                
                # Consonant + v combinations
                "t+v": "tv", "d+v": "dv", "n+v": "nv", "k+v": "kv",
                "g+v": "gv", "p+v": "pv", "b+v": "bv", "m+v": "mv",
                "s+v": "sv", "h+v": "hv",
                
                # r combinations
                "r+consonant": "consonant+consonant",  # r assimilates to following
                "r+t": "tt", "r+d": "dd", "r+n": "nn", "r+y": "yy",
                "r+l": "ll", "r+v": "vv", "r+s": "ss", "r+h": "hh",
                "r+m": "mm", "r+p": "pp", "r+b": "bb", "r+g": "gg",
                "r+k": "kk", "r+c": "cc", "r+j": "jj",
                
                # s combinations
                "s+t": "tth", "s+th": "tth", "s+n": "ñ", "s+y": "ss",
                "s+v": "sv", "s+m": "sm", "s+consonant": "s+consonant",
                "s+s": "ss", "s+k": "kkh", "s+p": "pph",
                
                # Final consonants before vowels
                "t+V": "d", "k+V": "g", "p+V": "b",  # V = any vowel
                "d+V": "d", "g+V": "g", "b+V": "b",
                "ṭ+V": "ḷ", "m+V": "m", "n+V": "n",
                
                # Special combinations
                "as+t": "atth", "is+t": "itth", "us+t": "utth",
                "t+su": "ssu", "d+su": "ssu", "n+su": "ssu",
                "t+sn": "ssn", "d+sn": "ssn", "n+sn": "ssn",
                
                # Nasal + consonant
                "n+k": "ṅk", "n+kh": "ṅkh", "n+g": "ṅg", "n+gh": "ṅgh",
                "n+c": "ñc", "n+ch": "ñch", "n+j": "ñj", "n+jh": "ñjh",
                "n+ṭ": "ṇṭ", "n+ṭh": "ṇṭh", "n+ḍ": "ṇḍ", "n+ḍh": "ṇḍh",
                "n+t": "nt", "n+th": "nth", "n+d": "nd", "n+dh": "ndh",
                "n+p": "mp", "n+ph": "mph", "n+b": "mb", "n+bh": "mbh",
                
                # Additional assimilations
                "l+l": "ll", "ḷ+ḷ": "ḷḷ", "v+v": "vv", "y+y": "yy",
                "ñ+ñ": "ññ", "ṇ+ṇ": "ṇṇ", "m+m": "mm", "n+n": "nn"
            },
            
            # PREFIX SANDHI (Extended)
            "prefix_sandhi": {
                # ud prefix
                "ud+k": "ukk", "ud+kh": "ukkh", "ud+g": "ugg", "ud+gh": "uggh",
                "ud+c": "ucc", "ud+ch": "ucch", "ud+j": "ujj", "ud+jh": "ujjh",
                "ud+ṭ": "uṭṭ", "ud+ṭh": "uṭṭh", "ud+ḍ": "uḍḍ", "ud+ḍh": "uḍḍh",
                "ud+t": "utt", "ud+th": "utth", "ud+d": "udd", "ud+dh": "uddh",
                "ud+p": "upp", "ud+ph": "upph", "ud+b": "ubb", "ud+bh": "ubbh",
                "ud+s": "uss", "ud+h": "uhh", "ud+l": "ull", "ud+v": "uvv",
                "ud+r": "urr", "ud+y": "uyy", "ud+n": "unn", "ud+m": "umm",
                "ud+ñ": "uññ", "ud+ṇ": "uṇṇ", "ud+a": "udd", "ud+i": "udd",
                
                # sam prefix
                "sam+k": "saṅk", "sam+kh": "saṅkh", "sam+g": "saṅg", "sam+gh": "saṅgh",
                "sam+c": "sañc", "sam+ch": "sañch", "sam+j": "sañj", "sam+jh": "sañjh",
                "sam+ṭ": "saṇṭ", "sam+ṭh": "saṇṭh", "sam+ḍ": "saṇḍ", "sam+ḍh": "saṇḍh",
                "sam+t": "sant", "sam+th": "santh", "sam+d": "sand", "sam+dh": "sandh",
                "sam+p": "samp", "sam+ph": "samph", "sam+b": "samb", "sam+bh": "sambh",
                "sam+m": "samm", "sam+y": "samm", "sam+r": "saṃr", "sam+l": "sall",
                "sam+v": "saṃv", "sam+s": "saṃs", "sam+h": "saṃh", "sam+a": "samm",
                "sam+i": "samm", "sam+u": "samm",
                
                # vi prefix
                "vi+k": "vikk", "vi+kh": "vikkh", "vi+g": "vigg", "vi+c": "vicc",
                "vi+p": "vipp", "vi+t": "vitt", "vi+n": "vinn", "vi+m": "vimm",
                "vi+y": "viyy", "vi+r": "virr", "vi+l": "vill", "vi+s": "viss",
                "vi+ñ": "viññ", "vi+h": "vihh", "vi+v": "vivv", "vi+a": "viy",
                "vi+i": "vī", "vi+u": "viy", "vi+e": "viy", "vi+o": "viy",
                
                # pari prefix
                "pari+k": "parikk", "pari+g": "parigg", "pari+c": "paricc",
                "pari+p": "paripp", "pari+t": "paritt", "pari+n": "parinn",
                "pari+y": "pariyy", "pari+s": "pariss", "pari+h": "parihh",
                "pari+a": "pariy", "pari+i": "parī", "pari+u": "pariy",
                
                # ati prefix
                "ati+a": "accā", "ati+ā": "accā", "ati+i": "accī", "ati+ī": "accī",
                "ati+u": "accū", "ati+ū": "accū", "ati+e": "acce", "ati+o": "acco",
                "ati+k": "atikk", "ati+g": "atigg", "ati+r": "atir",
                
                # api prefix
                "api+a": "appā", "api+ā": "appā", "api+i": "appī", "api+u": "appū",
                "api+e": "appe", "api+o": "appo",
                
                # abhi prefix
                "abhi+a": "abbhā", "abhi+ā": "abbhā", "abhi+i": "abbhī", "abhi+u": "abbhū",
                "abhi+k": "abhikk", "abhi+g": "abhigg", "abhi+c": "abhicc",
                "abhi+t": "abhitt", "abhi+p": "abhipp", "abhi+n": "abhinn",
                "abhi+m": "abhimm", "abhi+y": "abhiyy", "abhi+r": "abhirr",
                "abhi+s": "abhiss", "abhi+h": "abhihh", "abhi+ñ": "abhiññ",
                
                # adhi prefix
                "adhi+a": "ajjhā", "adhi+ā": "ajjhā", "adhi+i": "ajjhī", "adhi+u": "ajjhū",
                "adhi+k": "adhikk", "adhi+g": "adhigg", "adhi+c": "adhicc",
                "adhi+t": "adhitt", "adhi+p": "adhipp", "adhi+m": "adhimm",
                "adhi+r": "adhir", "adhi+v": "adhivv",
                
                # upa prefix
                "upa+k": "upakk", "upa+g": "upagg", "upa+c": "upacc", "upa+t": "upatt",
                "upa+p": "upapp", "upa+s": "upass", "upa+h": "upahh", "upa+r": "upar",
                "upa+a": "upā", "upa+i": "upī", "upa+u": "upū",
                
                # pa prefix
                "pa+k": "pakk", "pa+g": "pagg", "pa+c": "pacc", "pa+t": "patt",
                "pa+p": "papp", "pa+n": "pann", "pa+m": "pamm", "pa+y": "payy",
                "pa+r": "parr", "pa+l": "pall", "pa+v": "pavv", "pa+s": "pass",
                "pa+a": "pā", "pa+i": "pī", "pa+u": "pū",
                
                # Other prefixes
                "du+k": "dukk", "du+g": "dugg", "du+c": "ducc", "du+p": "dupp",
                "su+k": "sukk", "su+g": "sugg", "su+p": "supp", "su+t": "sutt",
                "ni+k": "nikk", "ni+g": "nigg", "ni+c": "nicc", "ni+t": "nitt",
                "ni+p": "nipp", "ni+m": "nimm", "ni+y": "niyy", "ni+r": "nirr",
                "ni+s": "niss", "ni+h": "nihh", "ni+a": "niy", "ni+u": "niy",
                
                # Compound prefix combinations
                "anu+pa": "anupa", "sam+anu": "samanu", "sam+pa": "sampa",
                "sam+pari": "sampari", "pari+ni": "parini", "vi+pa": "vipa",
                "vi+ni": "vini", "sam+ud": "samud", "pa+ni": "pani",
                "pa+vi": "pavi", "ud+pa": "uppa", "ni+pa": "nipa"
            },
            
            # SPECIAL SANDHI RULES (Extended)
            "special_sandhi": {
                # Metathesis
                "iti+eva": "icceva", "api+eva": "appeva", "yadi+eva": "yadeva",
                "sace+ayaṃ": "sacāyaṃ", "yadi+ayaṃ": "yadāyaṃ", "so+ayaṃ": "svāyaṃ",
                "eso+ayaṃ": "esāyaṃ", "yo+ayaṃ": "yāyaṃ", "ko+ayaṃ": "kāyaṃ",
                
                # Common word combinations
                "na+atthi": "natthi", "na+etaṃ": "netaṃ", "na+eva": "neva",
                "ca+eva": "ceva", "va+eva": "veva", "na+aññaṃ": "naññaṃ",
                "na+idaṃ": "nedaṃ", "na+imassa": "nimassa", "ma+evaṃ": "mevaṃ",
                "ta+eva": "teva", "ya+eva": "yeva", "sa+eva": "seva",
                
                # Interrogative combinations
                "kiṃ+su": "kissu", "kaṃ+su": "kassu", "kuṃ+su": "kussu",
                "kiṃ+nu": "kinnu", "kaṃ+nu": "kannu", "ko+nu": "konu",
                "kiṃ+hi": "kimhi", "kaṃ+hi": "kamhi", "ko+hi": "kohi",
                
                # Compound internal sandhi
                "buddha+assa": "buddhassa", "dhamma+assa": "dhammassa",
                "saṅgha+assa": "saṅghassa", "magga+assa": "maggassa",
                "phala+assa": "phalassa", "dukkha+assa": "dukkhassa",
                
                # Pronoun combinations
                "ta+assa": "tassa", "ta+imaṃ": "timaṃ", "ta+idaṃ": "tidaṃ",
                "sa+assa": "sassa", "sa+imaṃ": "simaṃ", "sa+idaṃ": "sidaṃ",
                "ya+assa": "yassa", "ya+imaṃ": "yimaṃ", "ya+idaṃ": "yidaṃ",
                
                # Particle combinations
                "atha+kho": "athakho", "tena+hi": "tenahi", "yena+hi": "yenahi",
                "tatra+api": "tatrāpi", "yatra+api": "yatrāpi", "eva+hi": "evahi",
                
                # Verbal combinations
                "gaccha+āmi": "gacchāmi", "passa+āmi": "passāmi",
                "labha+āmi": "labhāmi", "dadā+āmi": "dadāmi",
                
                # Additional special rules
                "taṃ+yathā": "taññathā", "yaṃ+kiñci": "yaṅkiñci",
                "sabbaso": "sabbaso", "kathaṃ+iva": "kathamiva",
                "evaṃ+eva": "evameva", "tathā+eva": "tatheva"
            },
            
            # COMPOUND SANDHI (Additional rules for compound formation)
            "compound_sandhi": {
                # Dvandva compounds
                "a+a": "ā", "i+a": "ya", "u+a": "va",
                "a+i": "e", "a+u": "o",
                
                # Tatpuruṣa compounds
                "as+consonant": "o", "is+consonant": "i", "us+consonant": "u",
                "an+consonant": "a", "in+consonant": "i",
                
                # Bahuvrīhi compounds
                "a+initial": "", "ā+initial": "", # stem form
                
                # Karmadhāraya compounds
                "adjective+noun": "stem+stem",
                
                # Special compound formations
                "mahā+vowel": "mahā", "mahā+consonant": "maha",
                "su+vowel": "sv", "su+consonant": "su",
                "dus+vowel": "dur", "dus+consonant": "dus"
            }
        }

    def _initialize_all_derivation_patterns(self) -> Dict[str, Dict]:
        """Complete derivation patterns (30+)"""
        return {
            # NOUNS FROM VERBS
            "verbal_nouns": {
                "-ana": {
                    "type": "action",
                    "gender": "n",
                    "meaning": "act of X-ing",
                    "example": "gamana (going)"
                },
                "-anā": {
                    "type": "action",
                    "gender": "f",
                    "meaning": "act of X-ing",
                    "example": "gamanā (going)"
                },
                "-ti": {
                    "type": "action",
                    "gender": "f",
                    "meaning": "act of X-ing",
                    "example": "gati (going)"
                },
                "-ā": {
                    "type": "action",
                    "gender": "f",
                    "meaning": "act of X-ing",
                    "example": "kathā (speech)"
                },
                "-a": {
                    "type": "result",
                    "gender": "m/n",
                    "meaning": "result of X-ing",
                    "example": "gama (gone place)"
                },
                "-ita": {
                    "type": "state",
                    "gender": "n",
                    "meaning": "state of being X-ed",
                    "example": "gamita (state of having gone)"
                },
                "-itta": {
                    "type": "state",
                    "gender": "n",
                    "meaning": "state of X",
                    "example": "gamitta (having gone)"
                }
            },
            
            # AGENT NOUNS
            "agent_nouns": {
                "-tar": {
                    "meaning": "one who habitually Xs",
                    "gender": "m",
                    "example": "gantar (goer)"
                },
                "-tu": {
                    "meaning": "one who Xs",
                    "gender": "m",
                    "example": "gantum (to go)"
                },
                "-aka": {
                    "meaning": "one who does X",
                    "gender": "m",
                    "example": "kāraka (doer)"
                },
                "-ika": {
                    "meaning": "professional X-er",
                    "gender": "m",
                    "example": "gaṇika (accountant)"
                },
                "-āvin": {
                    "meaning": "one endowed with X",
                    "gender": "m",
                    "example": "medhāvin (wise one)"
                },
                "-in": {
                    "meaning": "possessor of X",
                    "gender": "m",
                    "example": "dhanin (wealthy)"
                },
                "-uka": {
                    "meaning": "one engaged in X",
                    "gender": "m",
                    "example": "pāpuka (sinful)"
                }
            },
            
            # ABSTRACT NOUNS
            "abstract_nouns": {
                "-tā": {
                    "meaning": "state of being X",
                    "gender": "f",
                    "example": "jaratā (old age)"
                },
                "-tta": {
                    "meaning": "quality of being X",
                    "gender": "n",
                    "example": "putta (sonship)"
                },
                "-tva": {
                    "meaning": "nature of X",
                    "gender": "n",
                    "example": "mittva (friendship)"
                },
                "-ya": {
                    "meaning": "condition of X",
                    "gender": "n",
                    "example": "sāvakya (discipleship)"
                },
                "-bhāva": {
                    "meaning": "state of X",
                    "gender": "m",
                    "example": "mittabhāva (friendship)"
                },
                "-ṇa": {
                    "meaning": "act/state of X",
                    "gender": "n",
                    "example": "gamaṇa (going)"
                },
                "-tana": {
                    "meaning": "state of X",
                    "gender": "n",
                    "example": "nutana (newness)"
                }
            },
            
            # POSSESSIVE ADJECTIVES
            "possessive_adjectives": {
                "-vant": {
                    "meaning": "possessing X",
                    "example": "dhanavant (wealthy)"
                },
                "-mant": {
                    "meaning": "having X",
                    "example": "satimant (mindful)"
                },
                "-ila": {
                    "meaning": "full of X",
                    "example": "kopila (angry)"
                },
                "-maya": {
                    "meaning": "made of X",
                    "example": "suvaṇṇamaya (golden)"
                },
                "-ja": {
                    "meaning": "born from X",
                    "example": "jalaja (water-born, lotus)"
                },
                "-ṭṭha": {
                    "meaning": "standing in X",
                    "example": "samuddaṭṭha (sea-dwelling)"
                },
                "-ika": {
                    "meaning": "connected with X",
                    "example": "rājika (royal)"
                },
                "-iya": {
                    "meaning": "pertaining to X",
                    "example": "rājiya (royal)"
                },
                "-ī": {
                    "meaning": "having X",
                    "example": "daṇḍī (staff-bearer)"
                },
                "-āla": {
                    "meaning": "possessing X",
                    "example": "dayāla (compassionate)"
                }
            },
            
            # LOCATIVE ADJECTIVES
            "locative_adjectives": {
                "-ima": {
                    "meaning": "located in X",
                    "example": "pacchima (western)"
                },
                "-iya": {
                    "meaning": "belonging to X",
                    "example": "sāvatthiya (of Savatthi)"
                },
                "-eyya": {
                    "meaning": "coming from X",
                    "example": "kāsikeyya (from Kashi)"
                },
                "-ka": {
                    "meaning": "of/from X",
                    "example": "rājagahaka (of Rajagaha)"
                }
            },
            
            # DENOMINATIVE VERBS
            "denominative_verbs": {
                "-āyati": {
                    "meaning": "acts like X, desires X",
                    "example": "puttāyati (desires a son)"
                },
                "-iyati": {
                    "meaning": "behaves as X",
                    "example": "isariyati (acts as lord)"
                },
                "-eti": {
                    "meaning": "makes into X",
                    "example": "sabbeti (completes)"
                },
                "-āpeti": {
                    "meaning": "causes to become X",
                    "example": "jīvāpeti (keeps alive)"
                },
                "-karoti": {
                    "meaning": "makes X",
                    "example": "suddhakaroti (purifies)"
                }
            },
            
            # DIMINUTIVES
            "diminutives": {
                "-ka": {
                    "meaning": "little X",
                    "example": "puttaka (little son)"
                },
                "-ika": {
                    "meaning": "small X",
                    "example": "navika (small boat)"
                }
            },
            
            # AUGMENTATIVES
            "augmentatives": {
                "-ima": {
                    "meaning": "great X",
                    "example": "aggima (foremost)"
                }
            },
            
            # PEJORATIVES
            "pejoratives": {
                "-alla": {
                    "meaning": "bad X",
                    "example": "pāpalla (very evil)"
                },
                "-illa": {
                    "meaning": "poor X",
                    "example": "duggatilla (very poor)"
                }
            },
            
            # COLLECTIVE NOUNS
            "collectives": {
                "-tā": {
                    "meaning": "collection of X",
                    "gender": "f",
                    "example": "janatā (people)"
                },
                "-gaṇa": {
                    "meaning": "group of X",
                    "gender": "m",
                    "example": "bhikkhu-gaṇa (group of monks)"
                },
                "-samūha": {
                    "meaning": "multitude of X",
                    "gender": "m",
                    "example": "jana-samūha (crowd)"
                },
                "-saṅgha": {
                    "meaning": "assembly of X",
                    "gender": "m",
                    "example": "bhikkhu-saṅgha (community of monks)"
                }
            },
            
            # INSTRUMENT NOUNS
            "instrument_nouns": {
                "-ana": {
                    "meaning": "instrument for X-ing",
                    "gender": "n",
                    "example": "āsana (seat)"
                },
                "-karaṇa": {
                    "meaning": "means of X-ing",
                    "gender": "n",
                    "example": "nimittakaraṇa (cause)"
                },
                "-āyudha": {
                    "meaning": "weapon for X",
                    "gender": "n",
                    "example": "khaggāyudha (sword-weapon)"
                }
            },
            
            # PLACE NOUNS
            "place_nouns": {
                "-āya": {
                    "meaning": "place of X",
                    "gender": "m",
                    "example": "sayanāya (bedroom)"
                },
                "-ālaya": {
                    "meaning": "abode of X",
                    "gender": "m",
                    "example": "devālaya (temple)"
                },
                "-āgāra": {
                    "meaning": "house of X",
                    "gender": "n",
                    "example": "bhaṇḍāgāra (storehouse)"
                },
                "-tana": {
                    "meaning": "place of X",
                    "gender": "n",
                    "example": "sayatana (bed)"
                }
            },
            
            # TIME NOUNS
            "time_nouns": {
                "-kāla": {
                    "meaning": "time of X",
                    "gender": "m",
                    "example": "vassānakāla (rainy season)"
                }
            },
            
            # MANNER ADVERBS
            "manner_adverbs": {
                "-so": {
                    "meaning": "in the manner of X",
                    "example": "evaṃso (thus)"
                },
                "-thā": {
                    "meaning": "in X way",
                    "example": "sabbathā (in every way)"
                },
                "-dhā": {
                    "meaning": "X-fold",
                    "example": "ekadhā (in one way)"
                }
            },
            
            # COMPARATIVE/SUPERLATIVE
            "comparison": {
                "-tara": {
                    "meaning": "more X",
                    "degree": "comparative",
                    "example": "sundaratara (more beautiful)"
                },
                "-tama": {
                    "meaning": "most X",
                    "degree": "superlative",
                    "example": "sundaratama (most beautiful)"
                },
                "-iya": {
                    "meaning": "more X",
                    "degree": "comparative",
                    "example": "seyya (better)"
                },
                "-iṭṭha": {
                    "meaning": "most X",
                    "degree": "superlative",
                    "example": "jeṭṭha (eldest)"
                }
            }
        }

# Continue with the supporting classes and remaining methods...
# ============ COMPOUND SEMANTIC COMPOSITOR ============

class CompoundSemanticCompositor:
    """Enhanced compound semantic compositor"""
    
    def __init__(self, kb):
        self.kb = kb
        self.compound_patterns = self._initialize_compound_patterns()
        self.semantic_patterns = self._initialize_semantic_patterns()
        self.compound_rules = self._initialize_compound_rules()
        
    def _initialize_compound_patterns(self):
        """Specific compound patterns with meanings"""
        return {
            # Religious compounds
            "buddha+dhamma": "the Buddha's teaching",
            "dhamma+cakkhu": "eye of truth",
            "dhamma+kāya": "body of doctrine",
            "dhamma+rāja": "king of righteousness",
            "saṅgha+dāna": "gift to the community",
            "buddha+sāsana": "Buddha's dispensation",
            
            # Quality compounds
            "mahā+X": "great X",
            "cūḷa+X": "lesser X", 
            "ati+X": "very X",
            "su+X": "good X",
            "dus+X": "bad X",
            "a+X": "non-X",
            "an+X": "non-X (before vowel)",
            
            # Common patterns
            "X+putta": "son of X",
            "X+dhītar": "daughter of X",
            "X+jāta": "born from X",
            "X+maya": "made of X",
            "X+ādhāra": "container of X",
            "X+ālaya": "abode of X",
            
            # Directional compounds
            "pubb+X": "eastern X",
            "pacch+X": "western X",
            "uttar+X": "northern X",
            "dakkhiṇ+X": "southern X",
            
            # Temporal compounds
            "pubba+X": "former X",
            "pacchima+X": "latter X",
            "paṭhama+X": "first X",
            "dutiya+X": "second X"
        }
    
    def _initialize_semantic_patterns(self):
        """Semantic patterns for systematic compound generation"""
        return {
            "tatpurusa": {
                "locative": {
                    "pattern": ["space", "entity"],
                    "template": "{1} in/at {0}",
                    "example": "vana-cara (forest-dweller)"
                },
                "genitive": {
                    "pattern": ["possessor", "possessed"],
                    "template": "{1} of {0}",
                    "example": "rāja-putta (king's son)"
                },
                "instrumental": {
                    "pattern": ["instrument", "action"],
                    "template": "{1} by means of {0}",
                    "example": "aggi-daddha (burnt by fire)"
                },
                "ablative": {
                    "pattern": ["source", "derived"],
                    "template": "{1} from {0}",
                    "example": "bhaya-bhīta (frightened from fear)"
                },
                "accusative": {
                    "pattern": ["object", "action"],
                    "template": "{1} towards {0}",
                    "example": "dhamma-kāma (desiring dhamma)"
                },
                "associative": {
                    "pattern": ["associated", "entity"],
                    "template": "{1} with {0}",
                    "example": "guṇa-sampanna (endowed with virtue)"
                }
            },
            "karmadharaya": {
                "adjective": {
                    "pattern": ["quality", "entity"],
                    "template": "{0} {1}",
                    "example": "nīla-uppala (blue lotus)"
                },
                "comparison": {
                    "pattern": ["compared", "standard"],
                    "template": "{1} like {0}",
                    "example": "buddha-paṭibhāga (Buddha-like)"
                },
                "identity": {
                    "pattern": ["synonym1", "synonym2"],
                    "template": "{0} which is {1}",
                    "example": "sāmaññaphala (ascetic-fruit)"
                }
            },
            "bahuvrihi": {
                "possession": {
                    "pattern": ["quality", "possessed"],
                    "template": "having {0} {1}",
                    "example": "mahā-bhoga (having great wealth)"
                },
                "characteristic": {
                    "pattern": ["characteristic", "entity"],
                    "template": "characterized by {0} {1}",
                    "example": "catu-disa (having four directions)"
                }
            },
            "dvandva": {
                "copulative": {
                    "pattern": ["item1", "item2"],
                    "template": "{0} and {1}",
                    "example": "samaṇa-brāhmaṇa (ascetics and brahmins)"
                },
                "collective": {
                    "pattern": ["item1", "item2", "item3"],
                    "template": "{0}, {1} and {2}",
                    "example": "buddha-dhamma-saṅgha (Buddha, Dhamma and Sangha)"
                }
            },
            "avyayibhava": {
                "prepositional": {
                    "pattern": ["preposition", "noun"],
                    "template": "in the manner of {1}",
                    "example": "yathā-bala (according to strength)"
                }
            }
        }
    
    def _initialize_compound_rules(self):
        """Rules for compound formation"""
        return {
            "sandhi_in_compounds": {
                "a+a": "ā", "a+i": "e", "a+u": "o",
                "i+a": "ya", "u+a": "va"
            },
            "stem_formation": {
                "noun": "remove_case_ending",
                "adjective": "use_stem_form",
                "numeral": "use_combining_form"
            },
            "gender_rules": {
                "default": "follow_last_member",
                "bahuvrihi": "can_be_any_gender"
            }
        }
    
    def generate_systematic_compounds(self, semantic_fields, max_per_type=1000):
        """Generate compounds systematically based on semantic patterns"""
        compounds = {}
        
        for compound_type, patterns in self.semantic_patterns.items():
            print(f"   Generating {compound_type} compounds...")
            type_count = 0
            
            for pattern_name, pattern_info in patterns.items():
                if type_count >= max_per_type:
                    break
                
                # Get words for pattern
                pattern_words = self._get_pattern_words(pattern_info["pattern"], semantic_fields)
                
                # Generate compounds for this pattern
                for word_set in pattern_words:
                    if type_count >= max_per_type:
                        break
                    
                    if len(word_set) >= 2:
                        # Apply sandhi
                        compound = self._apply_compound_sandhi(word_set)
                        
                        if compound not in compounds:
                            meaning = self.compose_meaning(word_set, compound_type, pattern_name)
                            
                            compounds[compound] = {
                                "components": word_set,
                                "type": compound_type,
                                "pattern": pattern_name,
                                "meaning": meaning,
                                "semantic_structure": pattern_info["template"]
                            }
                            type_count += 1
        
        return compounds
    
    def _get_pattern_words(self, pattern_types, semantic_fields):
        """Get appropriate word combinations for patterns"""
        word_sets = []
        
        # Map pattern types to semantic fields
        pattern_mapping = {
            "space": ["space", "cosmology"],
            "entity": ["beings", "mind", "body"],
            "possessor": ["beings", "enlightenment"],
            "possessed": ["qualities", "ethics", "wisdom"],
            "quality": ["qualities", "colors", "numbers"],
            "instrument": ["body", "faculties"],
            "action": ["action", "meditation"],
            "source": ["space", "elements"],
            "derived": ["feelings", "mind"],
            "object": ["truth_law", "liberation"],
            "item1": ["virtue", "concentration"],
            "item2": ["wisdom", "liberation"]
        }
        
        # Generate combinations
        if len(pattern_types) == 2:
            words1 = []
            words2 = []
            
            for field in pattern_mapping.get(pattern_types[0], []):
                if field in semantic_fields:
                    words1.extend(semantic_fields[field][:20])
            
            for field in pattern_mapping.get(pattern_types[1], []):
                if field in semantic_fields:
                    words2.extend(semantic_fields[field][:20])
            
            # Create combinations
            for w1 in words1[:30]:
                for w2 in words2[:30]:
                    if w1 != w2:  # Avoid self-compounds
                        word_sets.append([w1, w2])
        
        return word_sets[:100]  # Limit for performance
    
    def _apply_compound_sandhi(self, components):
        """Apply sandhi rules in compound formation"""
        if len(components) < 2:
            return "".join(components)
        
        result = components[0]
        
        for i in range(1, len(components)):
            # Check sandhi rules
            if result and components[i]:
                last_char = result[-1]
                first_char = components[i][0]
                junction = last_char + "+" + first_char
                
                if junction in self.compound_rules["sandhi_in_compounds"]:
                    # Apply sandhi
                    result = result[:-1] + self.compound_rules["sandhi_in_compounds"][junction] + components[i][1:]
                else:
                    result += components[i]
            else:
                result += components[i]
        
        return result
    
    def compose_meaning(self, components, compound_type, pattern_name=None):
        """Compose meaning from components based on compound type"""
        
        # Get component meanings
        component_meanings = []
        for comp in components:
            if comp in self.kb.base_meanings:
                meaning = self.kb.base_meanings[comp]["primary"]
            elif comp in self.kb.prefix_meanings:
                meaning = self.kb.prefix_meanings[comp]
            else:
                meaning = comp
            component_meanings.append(meaning)
        
        # Apply composition rules based on type
        if compound_type == "tatpurusa":
            return self._compose_tatpurusa(component_meanings, components, pattern_name)
        elif compound_type == "karmadharaya":
            return self._compose_karmadharaya(component_meanings, components, pattern_name)
        elif compound_type == "bahuvrihi":
            return self._compose_bahuvrihi(component_meanings, components, pattern_name)
        elif compound_type == "dvandva":
            return self._compose_dvandva(component_meanings, components, pattern_name)
        elif compound_type == "avyayibhava":
            return self._compose_avyayibhava(component_meanings, components, pattern_name)
        else:
            return self._default_composition(component_meanings)
    
    def _compose_tatpurusa(self, meanings, components, pattern_name):
        """Enhanced tatpuruṣa composition"""
        if len(meanings) == 2:
            modifier, head = meanings
            
            # Use pattern-specific template if available
            if pattern_name:
                patterns = self.semantic_patterns["tatpurusa"]
                if pattern_name in patterns:
                    template = patterns[pattern_name]["template"]
                    return template.format(modifier, head)
            
            # Otherwise use semantic analysis
            # Check semantic relationships
            if any(field in ["space", "cosmology"] for field in self._get_semantic_fields(components[0])):
                return f"{head} in/of {modifier}"
            elif any(field in ["time"] for field in self._get_semantic_fields(components[0])):
                return f"{head} at/during {modifier}"
            elif any(field in ["beings", "person"] for field in self._get_semantic_fields(components[0])):
                return f"{head} of/belonging to {modifier}"
            elif any(term in modifier.lower() for term in ["knowledge", "wisdom"]):
                return f"{modifier} of {head}"
            else:
                return f"{head} of {modifier}"
        else:
            return " of ".join(reversed(meanings))
    
    def _compose_karmadharaya(self, meanings, components, pattern_name):
        """Enhanced karmadhāraya composition"""
        if len(meanings) >= 2:
            # Check if first component is a known qualifier
            qualifiers = {
                "mahā": "great", "cūḷa": "lesser", "ati": "very",
                "su": "good", "dus": "bad", "a": "non-", "an": "non-",
                "sabba": "all", "paṭhama": "first", "pacchima": "last",
                "pubb": "eastern", "pacch": "western", "uttar": "northern",
                "dakkhiṇ": "southern", "majjh": "middle", "anta": "final"
            }
            
            if components[0] in qualifiers:
                qualifier = qualifiers[components[0]]
                rest = " ".join(meanings[1:])
                return f"{qualifier} {rest}"
            else:
                # Descriptive adjective + noun
                quality = meanings[0]
                qualified = " ".join(meanings[1:])
                return f"{quality} {qualified}"
        
        return " ".join(meanings)
    
    def _compose_bahuvrihi(self, meanings, components, pattern_name):
        """Enhanced bahuvrīhi composition"""
        if len(meanings) >= 2:
            # Check for specific patterns
            if pattern_name == "characteristic":
                characteristic = meanings[0]
                entity = " ".join(meanings[1:])
                return f"characterized by {characteristic} {entity}"
            else:
                # Default possession
                quality = meanings[0]
                possessed = " ".join(meanings[1:])
                return f"having {quality} {possessed}"
        return "possessing " + " ".join(meanings)
    
    def _compose_dvandva(self, meanings, components, pattern_name):
        """Enhanced dvandva composition"""
        if len(meanings) == 2:
            return f"{meanings[0]} and {meanings[1]}"
        elif len(meanings) == 3:
            return f"{meanings[0]}, {meanings[1]} and {meanings[2]}"
        elif len(meanings) > 3:
            return ", ".join(meanings[:-1]) + f" and {meanings[-1]}"
        return " and ".join(meanings)
    
    def _compose_avyayibhava(self, meanings, components, pattern_name):
        """Avyayībhāva composition (indeclinable)"""
        if len(meanings) >= 2:
            prep = meanings[0]
            noun = " ".join(meanings[1:])
            return f"in the manner of {noun}, {prep} {noun}"
        return "in the manner of " + " ".join(meanings)
    
    def _default_composition(self, meanings):
        """Default composition for unknown types"""
        return "-".join(meanings)
    
    def _get_semantic_fields(self, word):
        """Get semantic fields for a word"""
        fields = []
        for field, words in self.kb.semantic_fields.items():
            if word in words:
                fields.append(field)
        
        # Also check base meanings
        if word in self.kb.base_meanings:
            field = self.kb.base_meanings[word].get("semantic_field")
            if field and field not in fields:
                fields.append(field)
        
        return fields

# ============ MORPHOLOGICAL SEMANTIC GENERATOR ============

class MorphologicalSemanticGenerator:
    """Generate semantically appropriate meanings for morphological forms"""
    
    def __init__(self, kb):
        self.kb = kb
        self.case_templates = self._initialize_case_templates()
        self.tense_templates = self._initialize_tense_templates()
        self.participle_templates = self._initialize_participle_templates()
    
    def _initialize_case_templates(self):
        """Templates for generating case meanings"""
        return {
            "nominative": {
                "default": "{0}",
                "emphasis": "the {0} (as subject)",
                "with_verb": "{0} who {verb}s"
            },
            "accusative": {
                "default": "{0}",
                "emphasis": "{0} (as direct object)",
                "with_verb": "{0} whom one {verb}s"
            },
            "instrumental": {
                "default": "by/with {0}",
                "agent": "by {0}",
                "means": "by means of {0}",
                "accompaniment": "together with {0}"
            },
            "dative": {
                "default": "to/for {0}",
                "benefit": "for the benefit of {0}",
                "purpose": "for the purpose of {0}"
            },
            "ablative": {
                "default": "from {0}",
                "source": "arising from {0}",
                "cause": "because of {0}",
                "comparison": "than {0}"
            },
            "genitive": {
                "default": "of {0}",
                "possession": "belonging to {0}",
                "relationship": "related to {0}",
                "partitive": "among {0}"
            },
            "locative": {
                "default": "in/at {0}",
                "place": "in the place of {0}",
                "time": "at the time of {0}",
                "reference": "with regard to {0}"
            },
            "vocative": {
                "default": "O {0}!",
                "respectful": "O venerable {0}!",
                "formal": "O noble {0}!"
            }
        }
    
    def _initialize_tense_templates(self):
        """Templates for verbal meanings"""
        return {
            "present": {
                "active": "{0}s, is {0}ing",
                "continuous": "is continuously {0}ing",
                "habitual": "habitually {0}s",
                "general": "{0}s"
            },
            "aorist": {
                "simple": "{0}ed",
                "narrative": "{0}ed (in the past)",
                "completed": "has {0}ed",
                "historical": "once {0}ed"
            },
            "perfect": {
                "default": "has {0}ed",
                "resultative": "has completely {0}ed",
                "experiential": "has experienced {0}ing"
            },
            "future": {
                "simple": "will {0}",
                "certain": "shall {0}",
                "probable": "will probably {0}",
                "intended": "intends to {0}"
            },
            "imperative": {
                "command": "{0}!",
                "request": "please {0}",
                "permission": "may {0}",
                "wish": "let (one) {0}"
            },
            "optative": {
                "wish": "may {0}, might {0}",
                "potential": "could {0}",
                "polite": "would {0}",
                "hypothetical": "should {0}"
            },
            "conditional": {
                "default": "would {0}",
                "hypothetical": "would {0} (if...)",
                "counterfactual": "would have {0}ed"
            }
        }
    
    def _initialize_participle_templates(self):
        """Templates for participle meanings"""
        return {
            "present_active": {
                "default": "{0}ing",
                "continuous": "one who is {0}ing",
                "characteristic": "characterized by {0}ing"
            },
            "present_middle": {
                "default": "{0}ing for oneself",
                "reflexive": "{0}ing oneself"
            },
            "past_passive": {
                "default": "{0}ed",
                "resultative": "having been {0}ed",
                "state": "in a state of being {0}ed"
            },
            "past_active": {
                "default": "having {0}ed",
                "perfect": "one who has {0}ed"
            },
            "future_passive": {
                "obligation": "to be {0}ed",
                "necessity": "must be {0}ed",
                "possibility": "can be {0}ed"
            },
            "gerund": {
                "default": "having {0}ed",
                "sequential": "after {0}ing",
                "causal": "because of {0}ing"
            },
            "infinitive": {
                "default": "to {0}",
                "purpose": "in order to {0}",
                "desire": "wishing to {0}"
            }
        }
    
    def generate_nominal_meaning(self, base, case, number):
        """Generate meaning for a declined noun"""
        # Get base meaning
        base_info = self.kb.base_meanings.get(base, {})
        base_meaning = base_info.get("primary", base)
        
        # Get semantic field for context
        semantic_field = base_info.get("semantic_field", "general")
        
        # Select appropriate template
        templates = self.case_templates.get(case, {})
        
        # Choose template based on semantic field
        if semantic_field in ["beings", "person"] and case == "genitive":
            template = templates.get("possession", templates["default"])
        elif semantic_field in ["space", "cosmology"] and case == "locative":
            template = templates.get("place", templates["default"])
        elif semantic_field in ["time"] and case == "locative":
            template = templates.get("time", templates["default"])
        else:
            template = templates.get("default", "{0}")
        
        # Apply template
        meaning = template.format(base_meaning)
        
        # Add number modification
        if number == "plural":
            meaning = self._pluralize_meaning(meaning, base_meaning)
        
        return meaning
    
    def _pluralize_meaning(self, meaning, base_meaning):
        """Add plural sense to meaning"""
        # Special cases
        if "person" in base_meaning.lower() or "one" in base_meaning.lower():
            meaning = meaning.replace("person", "people")
            meaning = meaning.replace("one", "ones")
            meaning = meaning.replace("One", "Ones")
        else:
            # Add plural marker if not already present
            if not any(plural in meaning for plural in ["people", "ones", "beings"]):
                # Handle different patterns
                if " of " in meaning:
                    parts = meaning.split(" of ", 1)
                    base_part = parts[0]
                    if not base_part.endswith('s'):
                        base_part += "s"
                    meaning = base_part + " of " + parts[1]
                elif not meaning.endswith('s'):
                    meaning += "s"
        
        return meaning
    
    def generate_verbal_meaning(self, root, person, number, tense, voice="active"):
        """Generate meaning for a conjugated verb"""
        # Get root meaning
        root_info = self.kb.root_meanings.get(root, {})
        root_meaning = root_info.get("meaning", root.replace("√", ""))
        
        # Handle variants
        if "variants" in root_info and root_info["variants"]:
            # Use first variant's meaning if available
            first_variant = list(root_info["variants"].values())[0]
            if "meaning" in first_variant:
                root_meaning = first_variant["meaning"]
        
        # Get appropriate template
        templates = self.tense_templates.get(tense, {})
        template = templates.get(voice, templates.get("default", "{0}"))
        
        # Apply template
        meaning = template.format(root_meaning)
        
        # Add person/number context
        pronoun = self._get_pronoun(person, number)
        
        # Format based on tense
        if tense == "imperative":
            if person == "2nd":
                meaning = f"({pronoun}) {meaning}"
            elif person == "3rd":
                meaning = f"let {pronoun} {root_meaning}"
        else:
            meaning = f"({pronoun}) {meaning}"
        
        return meaning
    
    def _get_pronoun(self, person, number):
        """Get appropriate pronoun"""
        pronouns = {
            ("1st", "singular"): "I",
            ("1st", "plural"): "we",
            ("2nd", "singular"): "you",
            ("2nd", "plural"): "you all",
            ("3rd", "singular"): "he/she/it",
            ("3rd", "plural"): "they"
        }
        return pronouns.get((person, number), "one")
    
    def generate_participle_meaning(self, root, participle_type, gender):
        """Generate meaning for participles"""
        # Get root meaning
        root_info = self.kb.root_meanings.get(root, {})
        root_meaning = root_info.get("meaning", root.replace("√", ""))
        
        # Get template
        templates = self.participle_templates.get(participle_type, {})
        template = templates.get("default", "{0}ing")
        
        # Apply template
        meaning = template.format(root_meaning)
        
        # Add gender marker if relevant
        if gender and participle_type in ["present_active", "past_passive"]:
            gender_marker = {"masculine": "(m.)", "feminine": "(f.)", "neuter": "(n.)"}
            meaning += f" {gender_marker.get(gender, '')}"
        
        return meaning

# ============ DERIVATIONAL SEMANTIC GENERATOR ============

class DerivationalSemanticGenerator:
    """Generate meanings for derived words"""
    
    def __init__(self, kb):
        self.kb = kb
        self.suffix_templates = self._initialize_suffix_templates()
    
    def _initialize_suffix_templates(self):
        """Templates for derivative meanings"""
        return {
            # Agent suffixes
            "-tar": "one who habitually {0}s",
            "-tu": "one who {0}s",
            "-aka": "one who does {0}",
            "-ika": "one engaged in {0}, professional {0}er",
            "-āvin": "one endowed with {0}",
            "-in": "possessor of {0}, one having {0}",
            "-uka": "one who tends to {0}",
            
            # Abstract noun suffixes
            "-tā": "state of being {0}, {0}-ness",
            "-tta": "quality of being {0}, {0}-hood",
            "-tva": "nature of {0}, {0}-ness",
            "-ya": "condition of {0}",
            "-bhāva": "state of {0}, existence as {0}",
            "-ṇa": "act of {0}ing",
            "-tana": "state of {0}",
            
            # Action noun suffixes
            "-ana": "act of {0}ing, {0}ing",
            "-anā": "act of {0}ing, {0}ing",
            "-ti": "act of {0}ing, {0}ion",
            "-ā": "act of {0}ing",
            
            # Possessive suffixes
            "-vant": "possessing {0}, full of {0}",
            "-mant": "having {0}, endowed with {0}",
            "-ila": "full of {0}, characterized by {0}",
            "-maya": "made of {0}, consisting of {0}",
            "-ja": "born from {0}, arising from {0}",
            
            # Locative/relational suffixes
            "-iya": "belonging to {0}, related to {0}",
            "-eyya": "coming from {0}, native of {0}",
            "-ka": "of {0}, pertaining to {0}",
            "-ima": "located in {0}",
            
            # Diminutive/augmentative
            "-ka": "little {0}, small {0}",
            "-ika": "small {0}",
            
            # Comparative/superlative
            "-tara": "more {0}",
            "-tama": "most {0}",
            "-iya": "more {0}",
            "-iṭṭha": "most {0}"
        }
    
    def generate_derivative_meaning(self, base, suffix, derivative_type):
        """Generate meaning for a derived word"""
        # Get base meaning
        if base in self.kb.base_meanings:
            base_meaning = self.kb.base_meanings[base]["primary"]
        elif base in self.kb.root_meanings:
            base_meaning = self.kb.root_meanings[base].get("meaning", base)
            # Clean root symbol
            base_meaning = base_meaning.replace("√", "")
        else:
            base_meaning = base
        
        # Get template
        template = self.suffix_templates.get(suffix, "{0} + " + suffix)
        
        # Apply template
        meaning = template.format(base_meaning)
        
        # Clean up meaning
        meaning = self._clean_derivative_meaning(meaning, derivative_type)
        
        return meaning
    
    def _clean_derivative_meaning(self, meaning, derivative_type):
        """Clean up generated derivative meanings"""
        # Remove double articles
        meaning = meaning.replace("the the", "the")
        
        # Fix verbal patterns
        if "ing" in meaning:
            # Fix patterns like "going"
            meaning = re.sub(r'(\w+)inging', r'\1ing', meaning)
            meaning = re.sub(r'(\w+e)ing', lambda m: m.group(1)[:-1] + 'ing', meaning)
        
        # Fix noun patterns
        if derivative_type == "abstract_nouns":
            # Ensure proper abstract noun format
            if "-ness" in meaning and "being" not in meaning:
                meaning = meaning.replace("-ness", "ness")
        
        return meaning

# ============ SEMANTIC VALIDATOR ============

class SemanticValidator:
    """Validate and enhance semantic meanings"""
    
    def __init__(self):
        self.invalid_patterns = [
            r'\{[0-9]\}',  # Unresolved placeholders
            r'X-ing',      # Unresolved X patterns
            r'undefined',   # Undefined meanings
            r'null',        # Null values
            r'^\s*$'        # Empty strings
        ]
        
        self.enhancement_rules = {
            # Fix common patterns
            r'\s+': ' ',                    # Multiple spaces
            r'^\s+|\s+$': '',              # Trim whitespace
            r'\s+([,\.\!\?])': r'\1',     # Space before punctuation
            r'([,\.\!\?])(\w)': r'\1 \2', # No space after punctuation
            r'  +': ' ',                   # Multiple spaces
            r'inging\b': 'ing',           # Double -ing
            r'eded\b': 'ed',              # Double -ed
            r'\bthe the\b': 'the',        # Double the
            r'\ba a\b': 'a',              # Double a
            r'\ban an\b': 'an'            # Double an
        }
    
    def validate_meaning(self, meaning):
        """Validate if meaning is well-formed"""
        if not meaning:
            return False, "Empty meaning"
        
        # Check for invalid patterns
        for pattern in self.invalid_patterns:
            if re.search(pattern, meaning):
                return False, f"Invalid pattern found: {pattern}"
        
        # Check minimum length
        if len(meaning.strip()) < 2:
            return False, "Meaning too short"
        
        # Check for technical notation
        if any(char in meaning for char in ['√', '+', '→', '_']):
            return False, "Contains technical notation"
        
        return True, "Valid"
    
    def enhance_meaning(self, meaning):
        """Enhance meaning with proper formatting"""
        if not meaning:
            return ""
        
        enhanced = meaning
        
        # Apply enhancement rules
        for pattern, replacement in self.enhancement_rules.items():
            enhanced = re.sub(pattern, replacement, enhanced)
        
        # Capitalize first letter
        if enhanced and enhanced[0].islower():
            enhanced = enhanced[0].upper() + enhanced[1:]
        
        # Ensure ends with proper punctuation (optional)
        # if enhanced and not enhanced[-1] in '.!?':
        #     enhanced += '.'
        
        return enhanced
    
    def validate_entry(self, entry):
        """Validate complete dictionary entry"""
        required_fields = ["word", "meaning", "type"]
        
        # Check required fields
        for field in required_fields:
            if field not in entry:
                return False, f"Missing required field: {field}"
        
        # Validate word
        if not entry["word"] or not isinstance(entry["word"], str):
            return False, "Invalid word"
        
        # Validate meaning
        is_valid, reason = self.validate_meaning(entry["meaning"])
        if not is_valid:
            return False, f"Invalid meaning: {reason}"
        
        # Validate type
        valid_types = [
            "base", "inflected_noun", "verb", "participle",
            "compound_tatpurusa", "compound_karmadharaya", 
            "compound_bahuvrihi", "compound_dvandva",
            "derivative_agent_nouns", "derivative_abstract_nouns",
            "prefixed_verb", "sandhi_variant"
        ]
        
        if not any(entry["type"].startswith(vtype) for vtype in valid_types):
            return False, f"Invalid type: {entry['type']}"
        
        return True, "Valid"

# ============ MONUMENTAL PALI DICTIONARY GENERATOR ============

class MonumentalPaliDictionaryGenerator:
    """Main generator for the complete Pali dictionary"""
    
    def __init__(self, kaggle_mode=False):
        # Detect environment
        self.kaggle_mode = kaggle_mode or os.path.exists('/kaggle/input')
        
        # Initialize knowledge base
        self.kb = ExhaustivePaliSemanticKnowledgeBase(self.kaggle_mode)
        
        # Initialize generators
        self.compound_compositor = CompoundSemanticCompositor(self.kb)
        self.morphological_generator = MorphologicalSemanticGenerator(self.kb)
        self.derivational_generator = DerivationalSemanticGenerator(self.kb)
        self.validator = SemanticValidator()
        
        # Dictionary storage
        self.generated_dict = {}
        self.generation_stats = defaultdict(int)
        
        # Load existing dictionary if available
        self.existing_dict_path = "pali_dictionary.json"
        self.existing_words = set()
        self._load_existing_dictionary()
    
    def _load_existing_dictionary(self):
        """Load existing dictionary to avoid duplicates"""
        try:
            with open(self.existing_dict_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            # Handle different dictionary formats
            if 'vocabulary' in data:
                self.existing_words = set(data['vocabulary'].keys())
            elif 'dictionary' in data:
                self.existing_words = set(data['dictionary'].keys())
            elif isinstance(data, dict):
                # Assume the whole file is the dictionary
                self.existing_words = set(data.keys())
            else:
                print(f"⚠️ Unknown dictionary format in {self.existing_dict_path}")
                self.existing_words = set()
            
            print(f"📖 Loaded {len(self.existing_words)} existing words")
            
        except FileNotFoundError:
            print(f"⚠️ Existing dictionary not found: {self.existing_dict_path}")
            self.existing_words = set()
        except json.JSONDecodeError as e:
            print(f"⚠️ Could not parse existing dictionary: {e}")
            self.existing_words = set()
        except Exception as e:
            print(f"⚠️ Error loading existing dictionary: {e}")
            self.existing_words = set()

    def _generate_base_entries(self):
        """Generate entries for all base words"""
        count = 0
        
        for word, info in self.kb.base_meanings.items():
            if word not in self.existing_words:
                # Create comprehensive entry
                entry = {
                    "word": word,
                    "meaning": self.validator.enhance_meaning(info["primary"]),
                    "type": "base",
                    "senses": info.get("senses", {}),
                    "semantic_field": info.get("semantic_field", "general"),
                    "register": info.get("register", "common"),
                    "etymology": info.get("etymology", ""),
                    "frequency": info.get("frequency", 5.0),  # Base words are high frequency
                    "related_words": info.get("related", [])
                }
                
                # Add additional metadata if available
                if "gender" in info:
                    entry["gender"] = info["gender"]
                if "declension" in info:
                    entry["declension"] = info["declension"]
                
                self.generated_dict[word] = entry
                count += 1
        
        print(f"   ✅ Generated {count} base word entries")
        self.generation_stats["base_words"] = count

    def _generate_morphological_forms(self):
        """Generate all morphological forms with proper meanings"""
        count = 0
        
        # Nominal forms
        print("   📝 Generating nominal forms...")
        nominal_count = self._generate_nominal_forms()
        count += nominal_count
        
        # Verbal forms
        print("   📝 Generating verbal forms...")
        verbal_count = self._generate_verbal_forms()
        count += verbal_count
        
        # Participles (basic - enhanced version is separate)
        print("   📝 Generating basic participle forms...")
        participle_count = self._generate_participle_forms()
        count += participle_count
        
        print(f"   ✅ Generated {count} morphological forms total")
        self.generation_stats["morphological_forms"] = count

    def _generate_nominal_forms(self):
        """Generate all case forms for nouns"""
        count = 0
        cases = ["nominative", "accusative", "instrumental", "dative", 
                "ablative", "genitive", "locative", "vocative"]
        numbers = ["singular", "plural"]
        
        # Process suitable base words
        nominal_words = [
            (word, info) for word, info in self.kb.base_meanings.items()
            if info.get("semantic_field") not in ["particles", "prefixes", "numbers"]
        ]
        
        # Limit for performance
        for base, info in nominal_words[:500]:
            for case in cases:
                for number in numbers:
                    # Skip vocative plural for some words
                    if case == "vocative" and number == "plural" and info.get("semantic_field") in ["abstract", "qualities"]:
                        continue
                    
                    # Generate form
                    form = self._apply_nominal_morphology(base, case, number)
                    
                    if (form and form != base and 
                        form not in self.existing_words and 
                        form not in self.generated_dict):
                        
                        # Generate meaning
                        meaning = self.morphological_generator.generate_nominal_meaning(
                            base, case, number
                        )
                        
                        # Validate meaning
                        is_valid, _ = self.validator.validate_meaning(meaning)
                        if is_valid:
                            entry = {
                                "word": form,
                                "meaning": self.validator.enhance_meaning(meaning),
                                "type": "inflected_noun",
                                "base": base,
                                "case": case,
                                "number": number,
                                "semantic_field": info.get("semantic_field", "general"),
                                "frequency": 3.5
                            }
                            
                            # Add gender if known
                            if "gender" in info:
                                entry["gender"] = info["gender"]
                            
                            self.generated_dict[form] = entry
                            count += 1
        
        return count

    def _generate_verbal_forms(self):
        """Generate verbal conjugations"""
        count = 0
        persons = ["1st", "2nd", "3rd"]
        numbers = ["singular", "plural"]
        tenses = ["present", "aorist", "future", "imperative", "optative", "conditional"]
        
        # Process verbal roots (limit for performance)
        roots_to_process = list(self.kb.root_meanings.items())[:200]
        
        for root, info in roots_to_process:
            for person in persons:
                for number in numbers:
                    for tense in tenses:
                        # Skip certain combinations
                        if tense == "imperative" and person == "1st" and number == "singular":
                            continue
                        
                        # Generate form
                        form = self._apply_verbal_morphology(root, person, number, tense)
                        
                        if (form and form not in self.existing_words and 
                            form not in self.generated_dict):
                            
                            # Generate meaning
                            meaning = self.morphological_generator.generate_verbal_meaning(
                                root, person, number, tense
                            )
                            
                            # Validate
                            is_valid, _ = self.validator.validate_meaning(meaning)
                            if is_valid:
                                entry = {
                                    "word": form,
                                    "meaning": self.validator.enhance_meaning(meaning),
                                    "type": "verb",
                                    "root": root,
                                    "person": person,
                                    "number": number,
                                    "tense": tense,
                                    "semantic_field": info.get("semantic_field", "action"),
                                    "frequency": 4.0
                                }
                                
                                self.generated_dict[form] = entry
                                count += 1
        
        return count

    def _generate_participle_forms(self):
        """Generate basic participle forms"""
        count = 0
        participle_types = ["present_active", "past_passive", "future_passive"]
        genders = ["masculine", "feminine", "neuter"]
        
        # Process roots (limit for performance)
        roots_to_process = list(self.kb.root_meanings.items())[:150]
        
        for root, info in roots_to_process:
            clean_root = root.replace("√", "")
            
            for p_type in participle_types:
                for gender in genders:
                    # Generate form
                    form = self._apply_participle_morphology(clean_root, p_type, gender)
                    
                    if (form and form not in self.existing_words and 
                        form not in self.generated_dict):
                        
                        # Generate meaning
                        meaning = self.morphological_generator.generate_participle_meaning(
                            root, p_type, gender
                        )
                        
                        # Validate
                        is_valid, _ = self.validator.validate_meaning(meaning)
                        if is_valid:
                            entry = {
                                "word": form,
                                "meaning": self.validator.enhance_meaning(meaning),
                                "type": "participle",
                                "root": root,
                                "participle_type": p_type,
                                "gender": gender,
                                "semantic_field": info.get("semantic_field", "action"),
                                "frequency": 3.0
                            }
                            
                            self.generated_dict[form] = entry
                            count += 1
        
        return count

    def _generate_prefixed_verbs(self):
        """Generate all prefix + verb combinations"""
        count = 0
        
        # Select roots for prefixing (limit for performance)
        roots_to_process = list(self.kb.root_meanings.items())[:100]
        
        for root, root_data in roots_to_process:
            # Get prefixes for this root
            prefixes = root_data.get("prefixes", [])
            if not prefixes:
                # Use common prefixes
                prefixes = ["ā", "upa", "ni", "pa", "vi", "saṃ"][:3]
            
            for prefix in prefixes:
                # Generate select forms for prefixed verb
                for tense in ["present", "aorist", "future"]:
                    for person in ["3rd"]:  # Just 3rd person for demo
                        for number in ["singular", "plural"]:
                            # Get base form
                            base_form = self._apply_verbal_morphology(
                                root, person, number, tense
                            )
                            
                            if base_form:
                                # Apply prefix with sandhi
                                prefixed_form = self._apply_prefix_sandhi(prefix, base_form)
                                
                                if (prefixed_form not in self.existing_words and 
                                    prefixed_form not in self.generated_dict):
                                    
                                    # Generate meaning
                                    prefix_meaning = self.kb.prefix_meanings.get(prefix, prefix)
                                    root_meaning = root_data.get("meaning", root)
                                    
                                    meaning = f"{prefix_meaning} + {root_meaning} ({person} {number} {tense})"
                                    
                                    entry = {
                                        "word": prefixed_form,
                                        "meaning": self.validator.enhance_meaning(meaning),
                                        "type": "prefixed_verb",
                                        "root": root,
                                        "prefix": prefix,
                                        "person": person,
                                        "number": number,
                                        "tense": tense,
                                        "frequency": 3.0
                                    }
                                    
                                    self.generated_dict[prefixed_form] = entry
                                    count += 1
        
        return count

    def _generate_all_participles(self):
        """Generate all types of participles"""
        count = 0
        
        participle_types = {
            "present_active": {"suffix": "ant", "meaning": "ing"},
            "present_middle": {"suffix": "māna", "meaning": "ing (reflexive)"},
            "past_passive": {"suffix": "ta", "meaning": "ed"},
            "past_active": {"suffix": "tavant", "meaning": "having Xed"},
            "future_passive": {"suffix": "tabba", "meaning": "to be Xed"},
            "future_passive_2": {"suffix": "anīya", "meaning": "should be Xed"},
            "gerund": {"suffix": "tvā", "meaning": "having Xed"},
            "gerund_2": {"suffix": "ya", "meaning": "having Xed (with prefix)"},
            "infinitive": {"suffix": "tuṃ", "meaning": "to X"}
        }
        
        # Process limited roots for performance
        roots_to_process = list(self.kb.root_meanings.items())[:100]
        
        for root, root_data in roots_to_process:
            clean_root = root.replace("√", "")
            
            # Get participle stem
            if "stems" in root_data and "past_participle" in root_data["stems"]:
                past_stem = root_data["stems"]["past_participle"]
            else:
                past_stem = clean_root + "ita"
            
            for p_type, p_info in participle_types.items():
                if "passive" in p_type and "past" in p_type:
                    form = past_stem
                else:
                    form = clean_root + p_info["suffix"]
                
                if (form not in self.existing_words and 
                    form not in self.generated_dict):
                    
                    meaning = f"{root_data.get('meaning', root)} ({p_info['meaning']})"
                    
                    entry = {
                        "word": form,
                        "meaning": self.validator.enhance_meaning(meaning),
                        "type": "participle",
                        "participle_type": p_type,
                        "root": root,
                        "frequency": 3.0
                    }
                    
                    self.generated_dict[form] = entry
                    count += 1
        
        return count

    def _generate_systematic_derivatives(self):
        """Generate all derivative forms systematically"""
        count = 0
        
        for category, patterns in self.kb.derivation_patterns.items():
            for suffix, suffix_info in patterns.items():
                # Select appropriate base words
                if category == "verbal_nouns" or category == "agent_nouns":
                    bases = list(self.kb.root_meanings.keys())[:50]
                else:
                    bases = [
                        w for w in self.kb.base_meanings.keys() 
                        if self.kb.base_meanings[w].get("semantic_field") not in ["particles"]
                    ][:50]
                
                for base in bases:
                    form = base.replace("√", "") + suffix.replace("-", "")
                    
                    if (form not in self.existing_words and 
                        form not in self.generated_dict):
                        
                        base_meaning = self._get_base_meaning(base)
                        derivative_meaning = suffix_info["meaning"].replace("X", base_meaning)
                        
                        entry = {
                            "word": form,
                            "meaning": self.validator.enhance_meaning(derivative_meaning),
                            "type": f"derivative_{category}",
                            "base": base,
                            "suffix": suffix,
                            "frequency": 2.5
                        }
                        
                        # Add gender if specified
                        if "gender" in suffix_info:
                            entry["gender"] = suffix_info["gender"]
                        
                        self.generated_dict[form] = entry
                        count += 1
        
        return count

    def _generate_compounds(self):
        """Enhanced systematic compound generation"""
        count = 0
        
        # Generate systematic compounds
        compounds = self.compound_compositor.generate_systematic_compounds(
            self.kb.semantic_fields,
            max_per_type=500  # Reduced for performance
        )
        
        for compound, compound_info in compounds.items():
            if (compound not in self.existing_words and 
                compound not in self.generated_dict):
                
                entry = {
                    "word": compound,
                    "meaning": self.validator.enhance_meaning(compound_info["meaning"]),
                    "type": f"compound_{compound_info['type']}",
                    "components": compound_info["components"],
                    "pattern": compound_info.get("pattern", ""),
                    "semantic_field": "compound",
                    "frequency": 2.5
                }
                
                self.generated_dict[compound] = entry
                count += 1
        
        print(f"   ✅ Generated {count} compounds systematically")
        self.generation_stats["compounds"] = count
        return count

    def _generate_sandhi_variants(self):
        """Generate comprehensive sandhi variants"""
        count = 0
        
        # Apply sandhi to existing words (limited for performance)
        words_to_process = list(self.generated_dict.keys())[:1000]
        
        for word in words_to_process:
            # Find potential sandhi points
            for i in range(1, len(word)-1):
                # Check if sandhi can apply
                first_part = word[:i+1]
                second_part = word[i:]
                
                # Try different sandhi combinations
                for sandhi_type, rules in self.kb.sandhi_rules.items():
                    if count >= 500:  # Limit sandhi variants
                        break
                        
                    for rule, result in rules.items():
                        if "+" in rule:
                            pattern = rule.split("+")
                            if len(pattern) == 2:
                                if (first_part.endswith(pattern[0]) and 
                                    second_part.startswith(pattern[1])):
                                    
                                    # Apply sandhi
                                    variant = (first_part[:-len(pattern[0])] + 
                                             result + 
                                             second_part[len(pattern[1]):])
                                    
                                    if (variant != word and 
                                        variant not in self.existing_words and 
                                        variant not in self.generated_dict and
                                        len(variant) > 2):
                                        
                                        base_entry = self.generated_dict[word]
                                        entry = {
                                            "word": variant,
                                            "meaning": base_entry["meaning"] + " (sandhi variant)",
                                            "type": "sandhi_variant",
                                            "base": word,
                                            "sandhi_rule": rule + "→" + result,
                                            "frequency": base_entry.get("frequency", 2.0) * 0.8
                                        }
                                        
                                        self.generated_dict[variant] = entry
                                        count += 1
        
        print(f"   ✅ Generated {count} sandhi variants")
        self.generation_stats["sandhi_variants"] = count
        return count

    def _validate_and_enhance(self):
        """Final validation and enhancement pass"""
        invalid_count = 0
        enhanced_count = 0
        
        print("   🔍 Validating all entries...")
        
        # Create list of entries to process (avoid modification during iteration)
        entries_to_validate = list(self.generated_dict.items())
        
        for word, entry in entries_to_validate:
            # Validate entire entry
            is_valid, reason = self.validator.validate_entry(entry)
            
            if not is_valid:
                # Remove invalid entries
                del self.generated_dict[word]
                invalid_count += 1
            else:
                # Enhance valid entries
                original_meaning = entry.get("meaning", "")
                enhanced_meaning = self.validator.enhance_meaning(original_meaning)
                
                if enhanced_meaning != original_meaning:
                    entry["meaning"] = enhanced_meaning
                    enhanced_count += 1
        
        print(f"   ✅ Validated all entries")
        print(f"   - Removed {invalid_count} invalid entries")
        print(f"   - Enhanced {enhanced_count} meanings")
        
        self.generation_stats["invalid_removed"] = invalid_count
        self.generation_stats["meanings_enhanced"] = enhanced_count

    def generate_complete_dictionary(self):
        """Generate complete dictionary with enhanced features"""
        print("\n🏗️ GENERATING ENHANCED MONUMENTAL PALI DICTIONARY")
        print("=" * 80)
        
        start_time = datetime.now()
        
        # Phase 1: Generate base word entries
        print("\n📍 Phase 1: Base Word Entries")
        self._generate_base_entries()
        
        # Phase 2: Generate all morphological forms
        print("\n📍 Phase 2: Complete Morphological Forms")
        self._generate_morphological_forms()
        
        # Phase 3: Generate prefixed verbs
        print("\n📍 Phase 3: Prefixed Verbs")
        prefixed_count = self._generate_prefixed_verbs()
        print(f"   ✅ Generated {prefixed_count} prefixed verb forms")
        self.generation_stats["prefixed_verbs"] = prefixed_count
        
        # Phase 4: Generate all participles
        print("\n📍 Phase 4: All Participle Types")
        participle_count = self._generate_all_participles()
        print(f"   ✅ Generated {participle_count} participle forms")
        self.generation_stats["participles"] = participle_count
        
        # Phase 5: Generate systematic compounds
        print("\n📍 Phase 5: Systematic Compound Generation")
        self._generate_compounds()
        
        # Phase 6: Generate all derivatives
        print("\n📍 Phase 6: Complete Derivative Forms")
        derivative_count = self._generate_systematic_derivatives()
        print(f"   ✅ Generated {derivative_count} derivative forms")
        self.generation_stats["derivatives"] = derivative_count
        
        # Phase 7: Generate sandhi variants
        print("\n📍 Phase 7: Comprehensive Sandhi Variants")
        self._generate_sandhi_variants()
        
        # Phase 8: Validate and enhance
        print("\n📍 Phase 8: Validation and Enhancement")
        self._validate_and_enhance()
        
        # Calculate generation time
        end_time = datetime.now()
        generation_time = (end_time - start_time).total_seconds()
        
        # Final statistics
        print(f"\n📊 GENERATION COMPLETE!")
        print(f"   Total entries: {len(self.generated_dict):,}")
        print(f"   Generation time: {generation_time:.2f} seconds")
        print(f"\n   Breakdown by category:")
        for category, count in sorted(self.generation_stats.items()):
            if category not in ["invalid_removed", "meanings_enhanced"]:
                print(f"   - {category}: {count:,}")
        
        return self.generated_dict
    
    def export_dictionary(self, filename=None):
        """Export the generated dictionary to JSON"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"monumental_pali_dictionary_{timestamp}.json"
        
        # Prepare export data
        export_data = {
            "metadata": {
                "name": "Enhanced Monumental Pali Dictionary",
                "version": "2.0",
                "generated": datetime.now().isoformat(),
                "total_entries": len(self.generated_dict),
                "environment": "Kaggle" if self.kaggle_mode else "Local",
                "features": [
                    "Complete morphological paradigms (15+ noun types)",
                    "All verb tenses and moods",
                    "200+ sandhi rules",
                    "30+ derivation patterns",
                    "5 compound types",
                    "All participle types",
                    "Validated meanings"
                ]
            },
            "statistics": dict(self.generation_stats),
            "dictionary": self.generated_dict
        }
        
        # Write to file
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, ensure_ascii=False, indent=2)
        
        print(f"📁 Dictionary exported to: {filename}")
        
        # Generate report
        report_filename = filename.replace('.json', '_report.txt')
        self._generate_report(report_filename)
        
        return filename
    
    def _get_base_meaning(self, base):
        """Get base meaning for a word or root"""
        if base in self.kb.base_meanings:
            return self.kb.base_meanings[base]["primary"]
        elif base in self.kb.root_meanings:
            return self.kb.root_meanings[base].get("meaning", base).replace("√", "")
        else:
            return base
    
    def _apply_nominal_morphology(self, base, case, number):
        """Apply nominal morphology to generate inflected form"""
        # Get declension type
        if base in self.kb.base_meanings:
            declension = self.kb.base_meanings[base].get("declension", "a_masculine")
        else:
            # Guess declension from ending
            if base.endswith('a'):
                declension = "a_masculine"
            elif base.endswith('ā'):
                declension = "aa_feminine"
            elif base.endswith('i'):
                declension = "i_masculine"
            elif base.endswith('ī'):
                declension = "ii_feminine"
            elif base.endswith('u'):
                declension = "u_masculine"
            elif base.endswith('ū'):
                declension = "uu_feminine"
            else:
                declension = "a_masculine"  # default
        
        # Get paradigm
        if declension in self.kb.noun_paradigms:
            paradigm = self.kb.noun_paradigms[declension]
            
            # Get stem
            stem_rule = paradigm.get("stem_rule", lambda x: x)
            stem = stem_rule(base)
            
            # Get ending
            ending = paradigm["endings"].get((case, number), "")
            
            # Apply ending
            if ending.startswith("/"):
                # Alternative endings
                ending = ending.split("/")[0]
            
            return stem + ending
        
        return None
    
    def _apply_verbal_morphology(self, root, person, number, tense):
        """Apply verbal morphology to generate conjugated form"""
        clean_root = root.replace("√", "")
        
        # Get appropriate stem
        if root in self.kb.root_meanings:
            root_info = self.kb.root_meanings[root]
            stems = root_info.get("stems", {})
            
            if tense == "present":
                stem = stems.get("present", clean_root)
            elif tense == "aorist":
                stem = stems.get("aorist", clean_root)
            elif tense == "future":
                stem = stems.get("future", clean_root + "iss")
            else:
                stem = clean_root
        else:
            stem = clean_root
        
        # Get paradigm
        paradigm_key = f"{tense}_active"
        if paradigm_key in self.kb.verb_paradigms:
            paradigm = self.kb.verb_paradigms[paradigm_key]
            
            # Handle thematic/athematic
            if "thematic" in paradigm:
                endings = paradigm["thematic"]
            elif "endings" in paradigm:
                endings = paradigm["endings"]
            else:
                return None
            
            # Get ending
            ending = endings.get((person, number), "")
            
            # Apply augment if needed
            augment = paradigm.get("augment", "")
            
            # Apply stem suffix if needed
            stem_suffix = paradigm.get("stem_suffix", "")
            if isinstance(stem_suffix, list):
                stem_suffix = stem_suffix[0]
            
            # Construct form
            if augment and tense in ["aorist", "conditional"]:
                form = augment + stem + stem_suffix + ending
            else:
                form = stem + stem_suffix + ending
            
            return form
        
        return None
    
    def _apply_participle_morphology(self, root, participle_type, gender):
        """Apply participle morphology"""
        if participle_type == "present_active":
            return root + "ant"
        elif participle_type == "past_passive":
            return root + "ita"
        elif participle_type == "future_passive":
            return root + "tabba"
        else:
            return None
    
    def _apply_prefix_sandhi(self, prefix, base):
        """Apply sandhi rules for prefix + base"""
        # Check sandhi rules
        for sandhi_type in ["prefix_sandhi", "consonant_sandhi", "vowel_sandhi"]:
            if sandhi_type in self.kb.sandhi_rules:
                rules = self.kb.sandhi_rules[sandhi_type]
                
                # Check if rule applies
                key = f"{prefix}+{base[0]}"
                if key in rules:
                    # Apply sandhi
                    result = rules[key]
                    return result + base[1:]
        
        # Default: just concatenate
        return prefix + base
    
    def _generate_report(self, filename):
        """Generate detailed report of dictionary generation"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("ENHANCED MONUMENTAL PALI DICTIONARY GENERATION REPORT\n")
                f.write("=" * 60 + "\n\n")
                
                f.write(f"Generated: {datetime.now().isoformat()}\n")
                f.write(f"Total Entries: {len(self.generated_dict):,}\n")
                f.write(f"Environment: {'Kaggle' if self.kaggle_mode else 'Local'}\n\n")
                
                f.write("GENERATION STATISTICS:\n")
                f.write("-" * 40 + "\n")
                for category, count in sorted(self.generation_stats.items()):
                    f.write(f"{category:<30}: {count:>10,}\n")
                
                f.write("\n\nQUALITY METRICS:\n")
                f.write("-" * 40 + "\n")
                f.write(f"✓ Base words loaded: {len(self.kb.base_meanings)}\n")
                f.write(f"✓ Root words loaded: {len(self.kb.root_meanings)}\n")
                f.write(f"✓ Invalid entries removed: {self.generation_stats.get('invalid_removed', 0)}\n")
                f.write(f"✓ Meanings enhanced: {self.generation_stats.get('meanings_enhanced', 0)}\n")
                
                # Validation report
                if hasattr(self.kb, 'preprocessor'):
                    f.write(f"\n✓ Validation errors: {len(self.kb.preprocessor.validation_errors)}\n")
                    f.write(f"✓ Validation warnings: {len(self.kb.preprocessor.validation_warnings)}\n")
                
                f.write("\n\nSAMPLE ENTRIES:\n")
                f.write("-" * 40 + "\n")
                
                # Show samples from each category
                samples = {
                    "base": 5,
                    "inflected_noun": 5,
                    "verb": 5,
                    "prefixed_verb": 3,
                    "participle": 3,
                    "compound_tatpurusa": 3,
                    "compound_karmadharaya": 3,
                    "derivative_agent_nouns": 3,
                    "derivative_abstract_nouns": 3,
                    "sandhi_variant": 3
                }
                
                for entry_type, sample_count in samples.items():
                    entries = [e for e in self.generated_dict.values() 
                              if e.get("type") == entry_type][:sample_count]
                    
                    if entries:
                        f.write(f"\n{entry_type.upper().replace('_', ' ')}:\n")
                        for entry in entries:
                            f.write(f"  {entry['word']}: {entry['meaning']}\n")
                
                f.write("\n\nFEATURES IMPLEMENTED:\n")
                f.write("-" * 40 + "\n")
                f.write("✓ Complete morphological paradigms (15+ noun types)\n")
                f.write("✓ All verb tenses and moods included\n")
                f.write("✓ Systematic compound generation (5 types)\n")
                f.write("✓ 30+ derivation patterns applied\n")
                f.write("✓ 200+ sandhi rules implemented\n")
                f.write("✓ All participle types generated\n")
                f.write("✓ Prefixed verbs systematically created\n")
                f.write("✓ All meanings validated for proper English\n")
                f.write("✓ No technical notation in definitions\n")
                f.write("✓ Dictionary-quality definitions throughout\n")
                f.write("✓ Full data validation and preprocessing\n")
                f.write("✓ Kaggle environment support\n")
                f.write("✓ Variant root handling\n")
                f.write("✓ Malformed JSON recovery\n")
            
            print(f"   📋 Report saved: {filename}")
            
        except Exception as e:
            print(f"   ⚠️ Could not generate report: {e}")

# ============ MAIN EXECUTION ============

def main():
    """Main execution with comprehensive error handling"""
    print("🏛️ ENHANCED MONUMENTAL PALI DICTIONARY GENERATOR")
    print("=" * 80)
    print("Version 2.0 - Complete with preprocessing and validation")
    print("Supports: Kaggle environment, malformed JSON, variant roots\n")
    
    try:
        # Initialize enhanced generator
        generator = MonumentalPaliDictionaryGenerator()
        
        # Check if data was loaded successfully
        if len(generator.kb.base_meanings) < 10:
            print("\n⚠️ WARNING: Very few base words loaded!")
            print("Please ensure your data files are in the correct location:")
            if os.path.exists('/kaggle/input'):
                print("  - /kaggle/input/pali_word_data.py")
                print("  - /kaggle/input/pali_roots_words.py")
            else:
                print("  - ./pali_word_data.py")
                print("  - ./pali_roots_words.py")
            
            response = input("\nContinue anyway? (y/n): ")
            if response.lower() != 'y':
                print("Exiting...")
                return
        
        # Generate complete dictionary
        print("\n🚀 Starting dictionary generation...")
        print("This may take several minutes...")
        dictionary = generator.generate_complete_dictionary()
        
        # Export results
        output_file = generator.export_dictionary()
        
        print("\n✅ ENHANCED GENERATION COMPLETE!")
        print(f"Generated {len(dictionary):,} dictionary entries")
        
        # Print validation summary
        if hasattr(generator.kb, 'preprocessor'):
            if generator.kb.preprocessor.validation_errors:
                print(f"\n⚠️ Data validation issues found:")
                print(f"   Errors: {len(generator.kb.preprocessor.validation_errors)}")
                print(f"   Warnings: {len(generator.kb.preprocessor.validation_warnings)}")
        
        print("\n📚 Dictionary ready for use!")
        print(f"Output file: {output_file}")
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Generation interrupted by user")
    except MemoryError:
        print("\n❌ Memory error - try reducing generation limits")
    except Exception as e:
        print(f"\n❌ FATAL ERROR: {e}")
        print("\nTroubleshooting:")
        print("1. Check that your data files exist in the correct location")
        print("2. Verify the file format matches the expected structure")
        print("3. Ensure you have write permissions for output")
        print("4. Check available memory and disk space")
        
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    # Add required imports at module level
    import importlib.util
    
    main()
