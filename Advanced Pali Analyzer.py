"""
Advanced Pali Analyzer - Local Streamlit Application
Complete implementation with debugging, tracing, and error handling
"""

import streamlit as st
import requests
import json
import hashlib
import time
import sqlite3
import re
import pickle
import base64
import logging
import traceback
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, asdict
from pathlib import Path
import pandas as pd
from functools import lru_cache
import xml.etree.ElementTree as ET
from datetime import datetime
import io
import sys
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('pali_analyzer.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# ==================== DATA MODELS ====================

@dataclass
class MorphologicalAnalysis:
    surface_form: str
    lemma: str
    root: str
    pos: str
    features: Dict[str, str]
    confidence: float
    meaning: Optional[str] = None
    alternatives: List[Dict] = None

    def to_dict(self):
        return asdict(self)

@dataclass
class TranslationResult:
    text: str
    confidence: float
    method: str
    alternatives: List[Dict] = None
    word_alignments: List[Tuple[str, str]] = None

@dataclass
class AnalysisResult:
    morphology: List[MorphologicalAnalysis]
    translation: Optional[TranslationResult]
    sandhi_resolution: Optional[Dict]
    semantic_analysis: Optional[Dict]
    neural_enhancement: Optional[Dict]
    processing_time: float
    cache_hit: bool

# ==================== ERROR HANDLING & DEBUGGING ====================

class PaliAnalyzerError(Exception):
    """Base exception for Pali Analyzer"""
    pass

class DictionaryError(PaliAnalyzerError):
    """Dictionary-related errors"""
    pass

class NetworkError(PaliAnalyzerError):
    """Network and API-related errors"""
    pass

class CacheError(PaliAnalyzerError):
    """Cache-related errors"""
    pass

def debug_trace(func):
    """Decorator for debugging function calls"""
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        logger.debug(f"Entering {func_name} with args: {args[:2]}...")  # Limit args for readability
        
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            execution_time = time.time() - start_time
            logger.debug(f"Exiting {func_name} successfully in {execution_time:.3f}s")
            return result
        except Exception as e:
            execution_time = time.time() - start_time
            logger.error(f"Error in {func_name} after {execution_time:.3f}s: {str(e)}")
            logger.error(f"Traceback: {traceback.format_exc()}")
            raise
    return wrapper

def safe_execute(func, default_value=None, error_message="Operation failed"):
    """Safely execute function with error handling"""
    try:
        return func()
    except Exception as e:
        logger.error(f"{error_message}: {str(e)}")
        if st.session_state.get('debug_mode', False):
            st.error(f"Debug: {error_message}: {str(e)}")
        return default_value

# ==================== CACHING SYSTEM ====================

class LocalCache:
    """Local file-based caching system"""
    
    def __init__(self, cache_dir: str = ".cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
        self.hits = 0
        self.misses = 0
        
    @debug_trace
    def get(self, key: str) -> Optional[Any]:
        """Get item from cache"""
        try:
            cache_file = self.cache_dir / f"{hashlib.md5(key.encode()).hexdigest()}.pkl"
            
            if cache_file.exists():
                with open(cache_file, 'rb') as f:
                    data = pickle.load(f)
                    
                # Check expiry
                if data.get('expiry', 0) > time.time():
                    self.hits += 1
                    logger.debug(f"Cache hit for key: {key[:50]}...")
                    return data['value']
                else:
                    cache_file.unlink()  # Remove expired
                    
        except Exception as e:
            logger.warning(f"Cache get error: {e}")
            
        self.misses += 1
        return None
        
    @debug_trace
    def set(self, key: str, value: Any, ttl: int = 3600):
        """Set item in cache"""
        try:
            cache_file = self.cache_dir / f"{hashlib.md5(key.encode()).hexdigest()}.pkl"
            
            data = {
                'value': value,
                'expiry': time.time() + ttl,
                'created': time.time()
            }
            
            with open(cache_file, 'wb') as f:
                pickle.dump(data, f)
                
            logger.debug(f"Cached item with key: {key[:50]}...")
            
        except Exception as e:
            logger.warning(f"Cache set error: {e}")
            
    def stats(self) -> Dict:
        """Get cache statistics"""
        total = self.hits + self.misses
        hit_rate = (self.hits / total * 100) if total > 0 else 0
        
        return {
            'hits': self.hits,
            'misses': self.misses,
            'hit_rate': hit_rate,
            'total_requests': total
        }

# ==================== DICTIONARY SYSTEM ====================

class PaliDictionary:
    """Comprehensive Pali dictionary with multiple sources"""
    
    def __init__(self):
        self.entries = {}
        self.loaded_sources = []
        self.load_embedded_dictionary()
        
    @debug_trace
    def load_embedded_dictionary(self):
        """Load embedded dictionary data"""
        try:
            # Embedded basic dictionary
            basic_entries = {
                'dhamma': {
                    'meaning': 'doctrine, truth, phenomenon, teaching',
                    'pos': 'noun',
                    'gender': 'masculine/neuter',
                    'root': 'dhṛ',
                    'sanskrit': 'dharma'
                },
                'buddha': {
                    'meaning': 'awakened one, enlightened one',
                    'pos': 'noun',
                    'gender': 'masculine',
                    'root': 'budh',
                    'sanskrit': 'buddha'
                },
                'saṅgha': {
                    'meaning': 'community, assembly',
                    'pos': 'noun',
                    'gender': 'masculine',
                    'root': 'saṃ + gam',
                    'sanskrit': 'saṅgha'
                },
                'dukkha': {
                    'meaning': 'suffering, unsatisfactoriness, pain',
                    'pos': 'noun',
                    'gender': 'neuter',
                    'root': 'dus + kṛ',
                    'sanskrit': 'duḥkha'
                },
                'anicca': {
                    'meaning': 'impermanent, transient',
                    'pos': 'adjective',
                    'root': 'na + nicca',
                    'sanskrit': 'anitya'
                },
                'anattā': {
                    'meaning': 'not-self, without soul',
                    'pos': 'adjective',
                    'root': 'na + ātman',
                    'sanskrit': 'anātman'
                },
                'nibbāna': {
                    'meaning': 'extinguishing, liberation, nirvana',
                    'pos': 'noun',
                    'gender': 'neuter',
                    'root': 'nir + vā',
                    'sanskrit': 'nirvāṇa'
                },
                'sati': {
                    'meaning': 'mindfulness, awareness, memory',
                    'pos': 'noun',
                    'gender': 'feminine',
                    'root': 'smṛ',
                    'sanskrit': 'smṛti'
                },
                'samādhi': {
                    'meaning': 'concentration, absorption',
                    'pos': 'noun',
                    'gender': 'masculine',
                    'root': 'sam + ā + dhā',
                    'sanskrit': 'samādhi'
                },
                'paññā': {
                    'meaning': 'wisdom, understanding',
                    'pos': 'noun',
                    'gender': 'feminine',
                    'root': 'pra + jñā',
                    'sanskrit': 'prajñā'
                },
                'kamma': {
                    'meaning': 'action, deed, karma',
                    'pos': 'noun',
                    'gender': 'neuter',
                    'root': 'kṛ',
                    'sanskrit': 'karma'
                },
                'sabbe': {
                    'meaning': 'all, every',
                    'pos': 'adjective',
                    'root': 'sarva',
                    'sanskrit': 'sarva'
                },
                'saṅkhārā': {
                    'meaning': 'formations, conditioned things',
                    'pos': 'noun',
                    'gender': 'masculine',
                    'root': 'saṃ + kṛ',
                    'sanskrit': 'saṃskāra'
                }
            }
            
            self.entries.update(basic_entries)
            self.loaded_sources.append('embedded_basic')
            logger.info(f"Loaded {len(basic_entries)} embedded dictionary entries")
            
        except Exception as e:
            logger.error(f"Error loading embedded dictionary: {e}")
            raise DictionaryError(f"Failed to load embedded dictionary: {e}")
            
    @debug_trace
    def lookup(self, word: str) -> Optional[Dict]:
        """Look up word in dictionary"""
        # Try exact match first
        if word in self.entries:
            return self.entries[word]
            
        # Try lowercase
        if word.lower() in self.entries:
            return self.entries[word.lower()]
            
        # Try without diacritics (basic)
        simplified = self.simplify_word(word)
        for key, entry in self.entries.items():
            if self.simplify_word(key) == simplified:
                return entry
                
        return None
        
    def simplify_word(self, word: str) -> str:
        """Simplify word by removing diacritics"""
        # Basic diacritic removal
        replacements = {
            'ā': 'a', 'ī': 'i', 'ū': 'u',
            'ṅ': 'n', 'ñ': 'n', 'ṇ': 'n',
            'ṭ': 't', 'ḍ': 'd', 'ḷ': 'l'
        }
        
        result = word.lower()
        for old, new in replacements.items():
            result = result.replace(old, new)
            
        return result
        
    def get_stats(self) -> Dict:
        """Get dictionary statistics"""
        return {
            'total_entries': len(self.entries),
            'sources': self.loaded_sources
        }

# ==================== MORPHOLOGICAL ANALYZER ====================

class RuleBasedMorphologyAnalyzer:
    """Rule-based morphological analyzer for Pali"""
    
    def __init__(self, dictionary: PaliDictionary):
        self.dictionary = dictionary
        self.declensions = self._load_declension_patterns()
        self.conjugations = self._load_conjugation_patterns()
        
    def _load_declension_patterns(self) -> Dict:
        """Load Pali declension patterns"""
        return {
            'a_stem_m': {
                'nom_sg': ['o', 'a'],
                'acc_sg': ['aṃ'],
                'ins_sg': ['ena'],
                'dat_sg': ['āya', 'assa'],
                'abl_sg': ['ā', 'asmā'],
                'gen_sg': ['assa'],
                'loc_sg': ['e', 'asmiṃ'],
                'voc_sg': ['a'],
                'nom_pl': ['ā'],
                'acc_pl': ['e'],
                'ins_pl': ['ehi', 'ebhi'],
                'dat_pl': ['ānaṃ'],
                'abl_pl': ['ehi', 'ebhi'],
                'gen_pl': ['ānaṃ'],
                'loc_pl': ['esu'],
                'voc_pl': ['ā']
            }
        }
        
    def _load_conjugation_patterns(self) -> Dict:
        """Load Pali conjugation patterns"""
        return {
            'present_1st': {
                '1sg': ['āmi', 'e'],
                '2sg': ['asi', 'e'],
                '3sg': ['ati', 'e'],
                '1pl': ['āma', 'ema'],
                '2pl': ['atha', 'etha'],
                '3pl': ['anti', 'enti']
            }
        }
        
    @debug_trace
    def analyze(self, word: str) -> List[MorphologicalAnalysis]:
        """Analyze morphology of a word"""
        analyses = []
        
        try:
            # Check if word is in dictionary as-is
            dict_entry = self.dictionary.lookup(word)
            if dict_entry:
                analyses.append(MorphologicalAnalysis(
                    surface_form=word,
                    lemma=word,
                    root=dict_entry.get('root', word),
                    pos=dict_entry.get('pos', 'unknown'),
                    features={'form': 'citation'},
                    confidence=1.0,
                    meaning=dict_entry.get('meaning', '')
                ))
                
            # Try morphological analysis
            inflected_analyses = self._analyze_inflections(word)
            analyses.extend(inflected_analyses)
            
            # If no analyses found, create unknown analysis
            if not analyses:
                analyses.append(MorphologicalAnalysis(
                    surface_form=word,
                    lemma=word,
                    root=word,
                    pos='unknown',
                    features={},
                    confidence=0.1
                ))
                
        except Exception as e:
            logger.error(f"Error analyzing word '{word}': {e}")
            # Return minimal analysis
            analyses.append(MorphologicalAnalysis(
                surface_form=word,
                lemma=word,
                root=word,
                pos='unknown',
                features={'error': str(e)},
                confidence=0.0
            ))
            
        return analyses
        
    def _analyze_inflections(self, word: str) -> List[MorphologicalAnalysis]:
        """Analyze possible inflected forms"""
        analyses = []
        
        # Try removing common endings
        for decl_type, patterns in self.declensions.items():
            for case_num, endings in patterns.items():
                for ending in endings:
                    if word.endswith(ending) and len(word) > len(ending):
                        stem = word[:-len(ending)]
                        
                        # Check if stem exists in dictionary
                        # Try adding citation form ending
                        if decl_type == 'a_stem_m':
                            lemma = stem + 'a'
                        else:
                            lemma = stem
                            
                        dict_entry = self.dictionary.lookup(lemma)
                        if dict_entry:
                            case, number = case_num.split('_')
                            analyses.append(MorphologicalAnalysis(
                                surface_form=word,
                                lemma=lemma,
                                root=dict_entry.get('root', stem),
                                pos=dict_entry.get('pos', 'noun'),
                                features={
                                    'case': case,
                                    'number': number,
                                    'declension': decl_type
                                },
                                confidence=0.8,
                                meaning=dict_entry.get('meaning', '')
                            ))
                            
        return analyses

# ==================== SANDHI RESOLVER ====================

class SandhiResolver:
    """Pali sandhi resolution"""
    
    def __init__(self):
        self.rules = self._load_sandhi_rules()
        
    def _load_sandhi_rules(self) -> List[Dict]:
        """Load Pali sandhi rules"""
        return [
            {
                'pattern': r'([aā])\s+([aā])',
                'replacement': r'ā',
                'description': 'a/ā + a/ā → ā'
            },
            {
                'pattern': r'([aā])\s+([iī])',
                'replacement': r'e',
                'description': 'a/ā + i/ī → e'
            },
            {
                'pattern': r'([aā])\s+([uū])',
                'replacement': r'o',
                'description': 'a/ā + u/ū → o'
            },
            {
                'pattern': r'([iī])\s+([aā])',
                'replacement': r'yā',
                'description': 'i/ī + a/ā → yā'
            },
            {
                'pattern': r'([uū])\s+([aā])',
                'replacement': r'vā',
                'description': 'u/ū + a/ā → vā'
            }
        ]
        
    @debug_trace
    def resolve(self, text: str) -> Dict:
        """Resolve sandhi in text"""
        try:
            original = text
            resolved = text
            applied_rules = []
            
            for rule in self.rules:
                pattern = rule['pattern']
                replacement = rule['replacement']
                
                if re.search(pattern, resolved):
                    new_resolved = re.sub(pattern, replacement, resolved)
                    if new_resolved != resolved:
                        applied_rules.append({
                            'rule': rule['description'],
                            'before': resolved,
                            'after': new_resolved
                        })
                        resolved = new_resolved
                        
            return {
                'original': original,
                'resolved': resolved,
                'rules_applied': applied_rules,
                'tokens': resolved.split()
            }
            
        except Exception as e:
            logger.error(f"Error in sandhi resolution: {e}")
            return {
                'original': text,
                'resolved': text,
                'rules_applied': [],
                'tokens': text.split(),
                'error': str(e)
            }

# ==================== NEURAL API CLIENT ====================

class NeuralAPIClient:
    """Client for communicating with Kaggle neural server"""
    
    def __init__(self):
        self.base_url = None
        self.session = requests.Session()
        self.session.timeout = 30
        self._connection_status = False
        self.request_count = 0
        self.error_count = 0
        
    @debug_trace
    def set_url(self, url: str) -> bool:
        """Set and validate API URL"""
        try:
            if not url:
                return False
                
            self.base_url = url.rstrip('/')
            
            # Test connection
            response = self.session.get(f"{self.base_url}/health", timeout=5)
            
            if response.status_code == 200:
                self._connection_status = True
                logger.info(f"Successfully connected to neural API at {self.base_url}")
                return True
            else:
                logger.warning(f"Neural API health check failed: {response.status_code}")
                return False
                
        except Exception as e:
            logger.error(f"Failed to connect to neural API: {e}")
            self._connection_status = False
            return False
            
    def is_connected(self) -> bool:
        """Check if connected to neural API"""
        return self._connection_status and self.base_url is not None
        
    @debug_trace
    def analyze_neural(self, text: str, local_context: Dict, 
                      mode: str = 'quick') -> Optional[Dict]:
        """Send text for neural analysis"""
        
        if not self.is_connected():
            logger.warning("Neural API not connected")
            return None
            
        try:
            self.request_count += 1
            
            payload = {
                'text': text,
                'local_context': local_context,
                'mode': mode,
                'tasks': ['disambiguation', 'translation', 'uncertainty']
            }
            
            response = self.session.post(
                f"{self.base_url}/analyze",
                json=payload,
                timeout=60 if mode == 'full' else 30
            )
            
            if response.status_code == 200:
                result = response.json()
                logger.info(f"Neural analysis successful for text: {text[:50]}...")
                return result
            else:
                self.error_count += 1
                logger.error(f"Neural API error {response.status_code}: {response.text}")
                return None
                
        except requests.exceptions.Timeout:
            self.error_count += 1
            logger.error("Neural API request timed out")
            return None
        except Exception as e:
            self.error_count += 1
            logger.error(f"Neural API error: {e}")
            return None
            
    def get_stats(self) -> Dict:
        """Get API client statistics"""
        success_rate = (self.request_count - self.error_count) / self.request_count * 100 if self.request_count > 0 else 0
        
        return {
            'connected': self.is_connected(),
            'base_url': self.base_url,
            'requests': self.request_count,
            'errors': self.error_count,
            'success_rate': success_rate
        }

# ==================== MAIN ANALYZER ====================

class PaliAnalyzer:
    """Main analyzer orchestrating all components"""
    
    def __init__(self):
        self.cache = LocalCache()
        self.dictionary = PaliDictionary()
        self.morphology = RuleBasedMorphologyAnalyzer(self.dictionary)
        self.sandhi = SandhiResolver()
        self.neural_client = NeuralAPIClient()
        
    @debug_trace
    def analyze(self, text: str, use_neural: bool = False, 
                mode: str = 'quick') -> AnalysisResult:
        """Perform complete analysis"""
        
        start_time = time.time()
        cache_key = f"analysis:{hashlib.md5((text + str(use_neural) + mode).encode()).hexdigest()}"
        
        # Check cache first
        cached_result = self.cache.get(cache_key)
        if cached_result:
            logger.info("Returning cached analysis result")
            return AnalysisResult(**cached_result, cache_hit=True)
            
        try:
            # Local analysis
            local_result = self._analyze_local(text)
            
            # Neural enhancement if requested
            neural_result = None
            if use_neural and self.neural_client.is_connected():
                neural_result = self._analyze_neural(text, local_result, mode)
                
            # Combine results
            final_result = self._combine_results(local_result, neural_result)
            
            processing_time = time.time() - start_time
            
            result = AnalysisResult(
                **final_result,
                processing_time=processing_time,
                cache_hit=False
            )
            
            # Cache the result
            self.cache.set(cache_key, result.to_dict() if hasattr(result, 'to_dict') else asdict(result))
            
            return result
            
        except Exception as e:
            logger.error(f"Error in analysis: {e}")
            # Return minimal result
            return AnalysisResult(
                morphology=[],
                translation=None,
                sandhi_resolution=None,
                semantic_analysis=None,
                neural_enhancement=None,
                processing_time=time.time() - start_time,
                cache_hit=False
            )
            
    def _analyze_local(self, text: str) -> Dict:
        """Perform local analysis"""
        try:
            # Sandhi resolution
            sandhi_result = self.sandhi.resolve(text)
            tokens = sandhi_result['tokens']
            
            # Morphological analysis
            morphology_results = []
            for token in tokens:
                analyses = self.morphology.analyze(token)
                if analyses:
                    morphology_results.append(analyses[0])  # Take best analysis
                    
            # Basic translation
            translation_words = []
            for morph in morphology_results:
                if morph.meaning:
                    # Take first meaning
                    meaning = morph.meaning.split(',')[0].strip()
                    translation_words.append(meaning)
                else:
                    translation_words.append(morph.surface_form)
                    
            translation = TranslationResult(
                text=' '.join(translation_words),
                confidence=0.7,
                method='rule_based'
            )
            
            return {
                'morphology': morphology_results,
                'translation': translation,
                'sandhi_resolution': sandhi_result,
                'semantic_analysis': None
            }
            
        except Exception as e:
            logger.error(f"Error in local analysis: {e}")
            raise
            
    def _analyze_neural(self, text: str, local_context: Dict, 
                       mode: str) -> Optional[Dict]:
        """Perform neural analysis"""
        try:
            return self.neural_client.analyze_neural(text, local_context, mode)
        except Exception as e:
            logger.error(f"Error in neural analysis: {e}")
            return None
            
    def _combine_results(self, local_result: Dict, 
                        neural_result: Optional[Dict]) -> Dict:
        """Combine local and neural results"""
        combined = local_result.copy()
        
        if neural_result:
            # Enhance translation if available
            if 'translation' in neural_result:
                neural_trans = neural_result['translation']
                combined['translation'] = TranslationResult(
                    text=neural_trans.get('text', combined['translation'].text),
                    confidence=neural_trans.get('confidence', combined['translation'].confidence),
                    method='neural_enhanced',
                    alternatives=neural_trans.get('alternatives', [])
                )
                
            combined['neural_enhancement'] = neural_result
            
        return combined

# ==================== STREAMLIT UI ====================

class StreamlitUI:
    """Main Streamlit user interface"""
    
    def __init__(self):
        self.analyzer = None
        self.initialize_session_state()
        
    def initialize_session_state(self):
        """Initialize Streamlit session state"""
        if 'analyzer' not in st.session_state:
            st.session_state.analyzer = PaliAnalyzer()
            
        if 'analysis_history' not in st.session_state:
            st.session_state.analysis_history = []
            
        if 'debug_mode' not in st.session_state:
            st.session_state.debug_mode = False
            
        if 'neural_url' not in st.session_state:
            st.session_state.neural_url = ""
            
        self.analyzer = st.session_state.analyzer
        
    def run(self):
        """Run the Streamlit application"""
        
        # Page configuration
        st.set_page_config(
            page_title="Advanced Pali Analyzer",
            page_icon="🕉️",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        
        # Custom CSS
        self._inject_custom_css()
        
        # Header
        st.title("🕉️ Advanced Pali Analyzer")
        st.markdown("*Comprehensive morphological analysis and translation of Pali texts*")
        
        # Sidebar
        self._render_sidebar()
        
        # Main content
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "📝 Analyze", "📚 Dictionary", "📊 Statistics", 
            "🔧 Debug", "ℹ️ About"
        ])
        
        with tab1:
            self._render_analysis_tab()
            
        with tab2:
            self._render_dictionary_tab()
            
        with tab3:
            self._render_statistics_tab()
            
        with tab4:
            self._render_debug_tab()
            
        with tab5:
            self._render_about_tab()
            
    def _inject_custom_css(self):
        """Inject custom CSS"""
        st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        }
        
        .pali-word {
            font-family: 'Noto Sans', serif;
            font-size: 1.1em;
            color: #8B4513;
            font-weight: bold;
        }
        
        .translation-box {
            background: #f0f8ff;
            padding: 1rem;
            border-radius: 10px;
            border-left: 5px solid #4CAF50;
            margin: 1rem 0;
        }
        
        .analysis-card {
            background: white;
            padding: 1rem;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin: 0.5rem 0;
        }
        
        .metric-card {
            background: #ffffff;
            padding: 1rem;
            border-radius: 8px;
            text-align: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
        .error-box {
            background: #ffe6e6;
            border: 1px solid #ff9999;
            padding: 1rem;
            border-radius: 5px;
            margin: 0.5rem 0;
        }
        
        .success-box {
            background: #e6ffe6;
            border: 1px solid #99ff99;
            padding: 1rem;
            border-radius: 5px;
            margin: 0.5rem 0;
        }
        </style>
        """, unsafe_allow_html=True)
        
    def _render_sidebar(self):
        """Render sidebar"""
        with st.sidebar:
            st.header("⚙️ Settings")
            
            # Neural API configuration
            st.subheader("🧠 Neural API")
            
            neural_url = st.text_input(
                "Kaggle API URL:",
                value=st.session_state.neural_url,
                placeholder="https://xyz.ngrok.io",
                help="Enter the ngrok URL from your Kaggle notebook"
            )
            
            if neural_url != st.session_state.neural_url:
                st.session_state.neural_url = neural_url
                if neural_url:
                    if self.analyzer.neural_client.set_url(neural_url):
                        st.success("✅ Connected to neural API")
                    else:
                        st.error("❌ Failed to connect")
                        
            # Connection status
            if self.analyzer.neural_client.is_connected():
                st.success("🟢 Neural API Connected")
            else:
                st.warning("🔴 Neural API Offline")
                
            # Analysis options
            st.subheader("🔍 Analysis Options")
            
            use_neural = st.checkbox(
                "Enable Neural Features",
                value=False,
                disabled=not self.analyzer.neural_client.is_connected(),
                help="Requires connection to Kaggle neural server"
            )
            
            analysis_mode = st.selectbox(
                "Analysis Mode:",
                ["quick", "full"],
                help="Quick mode for faster analysis, full mode for comprehensive results"
            )
            
            # Debug options
            st.subheader("🐛 Debug")
            
            st.session_state.debug_mode = st.checkbox(
                "Debug Mode",
                value=st.session_state.debug_mode
            )
            
            if st.button("Clear Cache"):
                self.analyzer.cache = LocalCache()
                st.success("Cache cleared")
                
            # Statistics
            st.subheader("📊 Statistics")
            
            cache_stats = self.analyzer.cache.stats()
            dict_stats = self.analyzer.dictionary.get_stats()
            
            st.metric("Cache Hit Rate", f"{cache_stats['hit_rate']:.1f}%")
            st.metric("Dictionary Entries", dict_stats['total_entries'])
            
            if self.analyzer.neural_client.is_connected():
                api_stats = self.analyzer.neural_client.get_stats()
                st.metric("API Success Rate", f"{api_stats['success_rate']:.1f}%")
                
    def _render_analysis_tab(self):
        """Render main analysis tab"""
        
        st.header("📝 Text Analysis")
        
        # Text input
        text_input = st.text_area(
            "Enter Pali text:",
            height=150,
            placeholder="Sabbe saṅkhārā aniccā...",
            help="Enter Pali text for comprehensive analysis"
        )
        
        # Analysis controls
        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            analyze_button = st.button(
                "🔍 Analyze Text",
                type="primary",
                disabled=not text_input.strip()
            )
            
        with col2:
            use_neural = st.checkbox(
                "Neural Enhancement",
                disabled=not self.analyzer.neural_client.is_connected()
            )
            
        with col3:
            mode = st.selectbox("Mode:", ["quick", "full"])
            
        # Perform analysis
        if analyze_button and text_input.strip():
            
            with st.spinner("Analyzing text..."):
                try:
                    result = self.analyzer.analyze(
                        text_input.strip(),
                        use_neural=use_neural,
                        mode=mode
                    )
                    
                    # Store in history
                    st.session_state.analysis_history.append({
                        'text': text_input.strip(),
                        'result': result,
                        'timestamp': datetime.now()
                    })
                    
                    # Display results
                    self._display_analysis_results(result)
                    
                except Exception as e:
                    logger.error(f"Analysis error: {e}")
                    st.error(f"Analysis failed: {str(e)}")
                    
                    if st.session_state.debug_mode:
                        st.code(traceback.format_exc())
                        
    def _display_analysis_results(self, result: AnalysisResult):
        """Display analysis results"""
        
        # Performance metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Processing Time", f"{result.processing_time:.2f}s")
        with col2:
            st.metric("Cache Hit", "Yes" if result.cache_hit else "No")
        with col3:
            st.metric("Words Analyzed", len(result.morphology))
        with col4:
            if result.neural_enhancement:
                st.metric("Neural Enhanced", "Yes")
            else:
                st.metric("Neural Enhanced", "No")
                
        # Translation
        if result.translation:
            st.markdown("### 🌐 Translation")
            
            st.markdown(f"""
            <div class="translation-box">
                <h4>{result.translation.text}</h4>
                <small>Method: {result.translation.method} | Confidence: {result.translation.confidence:.2%}</small>
            </div>
            """, unsafe_allow_html=True)
            
            # Alternative translations
            if result.translation.alternatives:
                with st.expander("Alternative translations"):
                    for i, alt in enumerate(result.translation.alternatives):
                        st.write(f"{i+1}. {alt.get('text', '')} (confidence: {alt.get('confidence', 0):.2%})")
                        
        # Morphological analysis
        if result.morphology:
            st.markdown("### 📖 Morphological Analysis")
            
            for i, morph in enumerate(result.morphology):
                with st.expander(f"**{morph.surface_form}** ({morph.pos})", expanded=False):
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.write(f"**Lemma:** {morph.lemma}")
                        st.write(f"**Root:** {morph.root}")
                        st.write(f"**Part of Speech:** {morph.pos}")
                        st.write(f"**Confidence:** {morph.confidence:.2%}")
                        
                    with col2:
                        if morph.meaning:
                            st.write(f"**Meaning:** {morph.meaning}")
                            
                        if morph.features:
                            st.write("**Features:**")
                            for key, value in morph.features.items():
                                st.write(f"  • {key}: {value}")
                                
                        if morph.alternatives:
                            st.write("**Alternatives:**")
                            for alt in morph.alternatives[:3]:  # Show top 3
                                st.write(f"  • {alt}")
                                
        # Sandhi resolution
        if result.sandhi_resolution:
            st.markdown("### 🔀 Sandhi Resolution")
            
            sandhi = result.sandhi_resolution
            
            if sandhi['rules_applied']:
                st.write("**Rules Applied:**")
                for rule in sandhi['rules_applied']:
                    st.write(f"• {rule['rule']}")
                    st.write(f"  Before: `{rule['before']}`")
                    st.write(f"  After: `{rule['after']}`")
            else:
                st.write("No sandhi rules applied.")
                
        # Neural enhancement details
        if result.neural_enhancement:
            st.markdown("### 🧠 Neural Enhancement")
            
            neural = result.neural_enhancement
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if 'confidence' in neural:
                    st.metric("Overall Confidence", f"{neural['confidence']:.2%}")
                    
            with col2:
                if 'ambiguity' in neural:
                    st.metric("Ambiguity Score", f"{neural['ambiguity']:.2f}")
                    
            with col3:
                if 'time' in neural:
                    st.metric("Neural Processing", f"{neural['time']:.2f}s")
                    
            # Uncertainty map
            if 'uncertainty_map' in neural:
                st.write("**Uncertainty Analysis:**")
                uncertainty = neural['uncertainty_map']
                
                # Create uncertainty visualization
                if uncertainty:
                    df = pd.DataFrame([
                        {'Word': word, 'Uncertainty': unc}
                        for word, unc in uncertainty.items()
                    ])
                    
                    st.bar_chart(df.set_index('Word'))
                    
    def _render_dictionary_tab(self):
        """Render dictionary lookup tab"""
        
        st.header("📚 Dictionary Lookup")
        
        # Search input
        search_word = st.text_input(
            "Look up Pali word:",
            placeholder="Enter word to search..."
        )
        
        if search_word:
            entry = self.analyzer.dictionary.lookup(search_word)
            
            if entry:
                st.markdown(f"### 📖 {search_word}")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write(f"**Meaning:** {entry.get('meaning', 'N/A')}")
                    st.write(f"**Part of Speech:** {entry.get('pos', 'N/A')}")
                    
                with col2:
                    if 'gender' in entry:
                        st.write(f"**Gender:** {entry['gender']}")
                    if 'root' in entry:
                        st.write(f"**Root:** {entry['root']}")
                    if 'sanskrit' in entry:
                        st.write(f"**Sanskrit:** {entry['sanskrit']}")
                        
                # Morphological analysis
                if st.button("Analyze Morphology"):
                    analyses = self.analyzer.morphology.analyze(search_word)
                    
                    if analyses:
                        st.write("**Morphological Analyses:**")
                        for analysis in analyses:
                            st.json(analysis.to_dict())
                            
            else:
                st.warning(f"Word '{search_word}' not found in dictionary.")
                
                # Suggest similar words
                st.write("**Suggestions:**")
                similar_words = self._find_similar_words(search_word)
                for word in similar_words[:5]:
                    if st.button(word, key=f"suggest_{word}"):
                        st.text_input("", value=word, key="search_word_suggested")
                        
    def _find_similar_words(self, word: str) -> List[str]:
        """Find similar words in dictionary"""
        similar = []
        word_lower = word.lower()
        
        for dict_word in self.analyzer.dictionary.entries.keys():
            # Simple similarity based on common prefixes/suffixes
            if (dict_word.startswith(word_lower[:3]) or 
                word_lower.startswith(dict_word[:3]) or
                dict_word.endswith(word_lower[-3:]) or
                word_lower.endswith(dict_word[-3:])):
                similar.append(dict_word)
                
        return similar[:10]
        
    def _render_statistics_tab(self):
        """Render statistics tab"""
        
        st.header("📊 System Statistics")
        
        # Cache statistics
        st.subheader("💾 Cache Performance")
        
        cache_stats = self.analyzer.cache.stats()
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Cache Hits", cache_stats['hits'])
        with col2:
            st.metric("Cache Misses", cache_stats['misses'])
        with col3:
            st.metric("Hit Rate", f"{cache_stats['hit_rate']:.1f}%")
            
        # Dictionary statistics
        st.subheader("📚 Dictionary Statistics")
        
        dict_stats = self.analyzer.dictionary.get_stats()
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Total Entries", dict_stats['total_entries'])
        with col2:
            st.write("**Sources:**")
            for source in dict_stats['sources']:
                st.write(f"• {source}")
                
        # Neural API statistics
        if self.analyzer.neural_client.is_connected():
            st.subheader("🧠 Neural API Statistics")
            
            api_stats = self.analyzer.neural_client.get_stats()
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Total Requests", api_stats['requests'])
            with col2:
                st.metric("Errors", api_stats['errors'])
            with col3:
                st.metric("Success Rate", f"{api_stats['success_rate']:.1f}%")
                
        # Analysis history
        if st.session_state.analysis_history:
            st.subheader("📝 Analysis History")
            
            history_df = pd.DataFrame([
                {
                    'Text': item['text'][:50] + '...' if len(item['text']) > 50 else item['text'],
                    'Words': len(item['result'].morphology),
                    'Time': f"{item['result'].processing_time:.2f}s",
                    'Timestamp': item['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
                }
                for item in st.session_state.analysis_history[-10:]  # Last 10
            ])
            
            st.dataframe(history_df, use_container_width=True)
            
            if st.button("Clear History"):
                st.session_state.analysis_history = []
                st.success("History cleared")
                st.rerun()
                
    def _render_debug_tab(self):
        """Render debug tab"""
        
        st.header("🔧 Debug Information")
        
        if not st.session_state.debug_mode:
            st.warning("Debug mode is disabled. Enable it in the sidebar to see debug information.")
            return
            
        # System information
        st.subheader("🖥️ System Information")
        
        debug_info = {
            "Python Version": sys.version,
            "Streamlit Version": st.__version__,
            "Cache Directory": str(self.analyzer.cache.cache_dir),
            "Dictionary Entries": len(self.analyzer.dictionary.entries),
            "Neural API URL": self.analyzer.neural_client.base_url or "Not set",
            "Neural API Connected": self.analyzer.neural_client.is_connected()
        }
        
        for key, value in debug_info.items():
            st.text(f"{key}: {value}")
            
        # Log viewer
        st.subheader("📜 Recent Logs")
        
        try:
            if os.path.exists('pali_analyzer.log'):
                with open('pali_analyzer.log', 'r') as f:
                    logs = f.readlines()[-50:]  # Last 50 lines
                    
                log_text = ''.join(logs)
                st.text_area("Logs", log_text, height=300)
            else:
                st.info("No log file found")
                
        except Exception as e:
            st.error(f"Error reading logs: {e}")
            
        # Test functions
        st.subheader("🧪 Test Functions")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Test Dictionary"):
                test_word = "dhamma"
                entry = self.analyzer.dictionary.lookup(test_word)
                if entry:
                    st.success(f"Dictionary test passed: {test_word} found")
                    st.json(entry)
                else:
                    st.error(f"Dictionary test failed: {test_word} not found")
                    
        with col2:
            if st.button("Test Neural API"):
                if self.analyzer.neural_client.is_connected():
                    try:
                        response = self.analyzer.neural_client.session.get(
                            f"{self.analyzer.neural_client.base_url}/health",
                            timeout=5
                        )
                        st.success(f"Neural API test passed: {response.status_code}")
                        st.json(response.json())
                    except Exception as e:
                        st.error(f"Neural API test failed: {e}")
                else:
                    st.warning("Neural API not connected")
                    
        # Cache operations
        st.subheader("💾 Cache Operations")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("View Cache Stats"):
                stats = self.analyzer.cache.stats()
                st.json(stats)
                
        with col2:
            if st.button("Clear All Cache"):
                self.analyzer.cache = LocalCache()
                st.success("All cache cleared")
                
        with col3:
            cache_size = sum(
                f.stat().st_size for f in self.analyzer.cache.cache_dir.glob('*.pkl')
            ) / 1024  # KB
            st.metric("Cache Size", f"{cache_size:.1f} KB")
            
    def _render_about_tab(self):
        """Render about tab"""
        
        st.header("ℹ️ About")
        
        st.markdown("""
        ## Advanced Pali Analyzer
        
        A comprehensive tool for morphological analysis and translation of Pali texts, 
        combining traditional rule-based linguistics with modern neural approaches.
        
        ### Features
        
        #### 🔍 Local Analysis (Always Available)
        - **Dictionary Lookup**: Comprehensive Pali-English dictionary
        - **Morphological Analysis**: Rule-based analysis of word forms
        - **Sandhi Resolution**: Automatic resolution of phonetic changes
        - **Basic Translation**: Rule-based word-by-word translation
        - **Caching**: Fast retrieval of previous analyses
        
        #### 🧠 Neural Enhancement (Kaggle Connection Required)
        - **Advanced Translation**: Neural machine translation
        - **Disambiguation**: Context-aware morphological disambiguation
        - **Uncertainty Quantification**: Confidence scores for all analyses
        - **Alternative Suggestions**: Multiple translation/analysis options
        
        ### Architecture
        
        The system uses a hybrid architecture:
        
        1. **Local Components** (Fast, Always Available)
           - Run on your local machine
           - Provide instant basic analysis
           - Work offline
           
        2. **Neural Components** (Advanced, Cloud-Based)
           - Run on Kaggle with GPU acceleration
           - Provide sophisticated AI-enhanced analysis
           - Require internet connection
           
        ### Usage Instructions
        
        1. **Basic Usage**: Simply enter Pali text and click "Analyze"
        2. **Neural Enhancement**: 
           - Set up Kaggle notebook with neural server
           - Copy the ngrok URL to the sidebar
           - Enable "Neural Enhancement" checkbox
        3. **Dictionary Lookup**: Use the Dictionary tab for word lookups
        4. **Debug**: Enable debug mode in sidebar for detailed information
        
        ### Technical Details
        
        - **Frontend**: Streamlit with custom CSS
        - **Backend**: FastAPI server on Kaggle
        - **Neural Models**: Transformer-based architecture
        - **Communication**: REST API over ngrok tunnel
        - **Caching**: Local file-based caching
        - **Error Handling**: Comprehensive error recovery
        
        ### Data Sources
        
        - Embedded Pali dictionary with common terms
        - Extensible for additional dictionary sources
        - Neural models trained on Pali-English parallel data
        
        ### Development
        
        This is an open-source project designed for:
        - Buddhist scholars and practitioners
        - Computational linguistics researchers
        - Students learning Pali
        - Digital humanities projects
        
        ### Support
        
        For issues, suggestions, or contributions, please refer to the project documentation.
        
        ---
        
        *Built with ❤️ for preserving and understanding ancient wisdom*
        """)
        
        # System information
        st.subheader("🔧 System Information")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.info(f"""
            **Local System**
            - Dictionary Entries: {len(self.analyzer.dictionary.entries)}
            - Cache Hit Rate: {self.analyzer.cache.stats()['hit_rate']:.1f}%
            - Debug Mode: {'Enabled' if st.session_state.debug_mode else 'Disabled'}
            """)
            
        with col2:
            if self.analyzer.neural_client.is_connected():
                api_stats = self.analyzer.neural_client.get_stats()
                st.success(f"""
                **Neural API**
                - Status: Connected ✅
                - Success Rate: {api_stats['success_rate']:.1f}%
                - Total Requests: {api_stats['requests']}
                """)
            else:
                st.warning("""
                **Neural API**
                - Status: Disconnected ❌
                - Setup required for advanced features
                """)

# ==================== MAIN APPLICATION ====================

def main():
    """Main application entry point"""
    
    try:
        # Initialize and run UI
        ui = StreamlitUI()
        ui.run()
        
    except Exception as e:
        logger.critical(f"Critical error in main application: {e}")
        logger.critical(f"Traceback: {traceback.format_exc()}")
        
        st.error("Critical application error occurred. Please check logs.")
        
        if st.button("Restart Application"):
            st.rerun()

if __name__ == "__main__":
    main()
