"""
MediScan AI - Medicine Verifier
Checks if a medicine is genuine based on barcode / name
"""

from database import find_medicine_by_barcode, find_medicine_by_name


def verify_by_barcode(barcode: str):
    """
    Verify medicine using barcode.
    In production, this would query DRAP database or manufacturer API.
    """
    if not barcode or not barcode.strip():
        return {
            "status": "INVALID",
            "message": "Please enter a barcode.",
            "medicine": None
        }
    
    medicine = find_medicine_by_barcode(barcode.strip())
    
    if medicine:
        return {
            "status": "GENUINE",
            "message": f"✅ Verified! This is {medicine['name']} by {medicine['manufacturer']}.",
            "medicine": medicine,
            "confidence": 0.95
        }
    else:
        return {
            "status": "SUSPICIOUS",
            "message": "⚠️ Barcode not found in our verified database. Could be fake or unregistered.",
            "medicine": None,
            "confidence": 0.7
        }


def verify_by_name(name: str):
    """Verify medicine by name."""
    if not name or not name.strip():
        return {
            "status": "INVALID",
            "message": "Please enter a medicine name.",
            "medicine": None
        }
    
    medicine = find_medicine_by_name(name.strip())
    
    if medicine:
        return {
            "status": "GENUINE",
            "message": f"✅ Verified! {medicine['name']} — Manufactured by {medicine['manufacturer']}.",
            "medicine": medicine,
            "confidence": 0.95
        }
    else:
        return {
            "status": "SUSPICIOUS",
            "message": "⚠️ Medicine not found in our database. May not be registered in Pakistan.",
            "medicine": None,
            "confidence": 0.6
        }


def get_verification_checklist():
    """Returns a checklist for manual visual verification."""
    return [
        "Check the hologram on the packaging",
        "Verify batch number and expiry date are printed clearly",
        "Compare font and colors with the manufacturer's official packaging",
        "Check for spelling mistakes on the label",
        "Verify the medicine seal is intact",
        "Check if price matches DRAP-approved rate",
        "Look for DRAP registration number on the pack"
    ]
