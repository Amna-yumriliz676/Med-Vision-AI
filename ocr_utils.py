"""
MediScan AI - Prescription OCR
Reads handwriting from prescription images
"""

import streamlit as st
from PIL import Image
import pytesseract
import re
from database import MEDICINES, get_all_medicine_names


@st.cache_data(show_spinner=False)
def extract_text_from_image(image_bytes):
    """Run OCR on uploaded image."""
    try:
        img = Image.open(image_bytes)
        # Convert to grayscale for better OCR
        img = img.convert("L")
        # OCR
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"OCR_ERROR: {str(e)}"


def extract_medicine_names(text: str):
    """
    Extract medicine names from OCR text using fuzzy matching.
    Returns list of dicts with medicine info and confidence.
    """
    if not text or "OCR_ERROR" in text:
        return []
    
    text_lower = text.lower()
    found = []
    
    all_meds = get_all_medicine_names()
    all_generics = [m["generic"].split()[0] for m in MEDICINES]
    
    for med in MEDICINES:
        med_name = med["name"].lower()
        generic = med["generic"].lower().split()[0]
        
        # Check if medicine name appears in text
        if med_name in text_lower or generic in text_lower:
            found.append({
                "medicine": med["name"],
                "generic": med["generic"],
                "confidence": 0.95,
                "matched_text": med["name"] if med_name in text_lower else med["generic"]
            })
    
    # If no exact match, try fuzzy
    if not found:
        words = re.findall(r'\b[a-zA-Z]{4,}\b', text)
        for word in words:
            word_lower = word.lower()
            for med in MEDICINES:
                med_lower = med["name"].lower()
                # Simple similarity: common substring
                if len(word_lower) >= 4 and (
                    word_lower in med_lower or med_lower in word_lower
                ):
                    found.append({
                        "medicine": med["name"],
                        "generic": med["generic"],
                        "confidence": 0.65,
                        "matched_text": word
                    })
                    break
    
    # Deduplicate
    seen = set()
    unique = []
    for f in found:
        if f["medicine"] not in seen:
            seen.add(f["medicine"])
            unique.append(f)
    
    return unique


def suggest_alternatives(word: str, top_k=3):
    """
    If OCR can't clearly read a medicine name, suggest top K alternatives
    based on string similarity.
    """
    from difflib import SequenceMatcher
    
    word_lower = word.lower()
    scores = []
    for med in MEDICINES:
        sim = SequenceMatcher(None, word_lower, med["name"].lower()).ratio()
        scores.append((med["name"], sim))
    
    scores.sort(key=lambda x: -x[1])
    return scores[:top_k]
