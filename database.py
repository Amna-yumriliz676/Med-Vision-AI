"""
MediScan AI - Built-in database
Medicines, interactions, and verified pharmacies
"""

# ============================================================
# MEDICINES DATABASE
# ============================================================
MEDICINES = [
    {
        "name": "Panadol",
        "generic": "Paracetamol",
        "uses": "Fever, mild to moderate pain, headache, body ache",
        "side_effects": "Nausea, liver damage (overdose), allergic reaction",
        "dosage": "500mg every 4-6 hours, max 4g/day",
        "interactions": "Warfarin, alcohol, isoniazid",
        "category": "Analgesic / Antipyretic",
        "manufacturer": "GSK Pakistan",
        "barcode": "8901234567890"
    },
    {
        "name": "Brufen",
        "generic": "Ibuprofen",
        "uses": "Pain, inflammation, fever, arthritis",
        "side_effects": "Stomach upset, ulcers, kidney issues, high BP",
        "dosage": "200-400mg every 4-6 hours after food",
        "interactions": "Aspirin, warfarin, ACE inhibitors, lithium",
        "category": "NSAID",
        "manufacturer": "Abbott Pakistan",
        "barcode": "8901234567891"
    },
    {
        "name": "Augmentin",
        "generic": "Amoxicillin + Clavulanic Acid",
        "uses": "Bacterial infections: chest, urinary, skin, dental",
        "side_effects": "Diarrhea, nausea, rash, allergic reaction",
        "dosage": "625mg every 8-12 hours",
        "interactions": "Methotrexate, warfarin, allopurinol",
        "category": "Antibiotic",
        "manufacturer": "GSK Pakistan",
        "barcode": "8901234567892"
    },
    {
        "name": "Glucophage",
        "generic": "Metformin",
        "uses": "Type 2 diabetes, blood sugar control",
        "side_effects": "Nausea, diarrhea, vitamin B12 deficiency",
        "dosage": "500mg twice daily with meals",
        "interactions": "Alcohol, contrast dyes, diuretics",
        "category": "Antidiabetic",
        "manufacturer": "Merck Pakistan",
        "barcode": "8901234567893"
    },
    {
        "name": "Concor",
        "generic": "Bisoprolol",
        "uses": "High blood pressure, heart failure, angina",
        "side_effects": "Fatigue, cold extremities, slow heart rate",
        "dosage": "2.5-10mg once daily",
        "interactions": "Verapamil, diltiazem, insulin, NSAIDs",
        "category": "Beta Blocker",
        "manufacturer": "Merck Pakistan",
        "barcode": "8901234567894"
    },
    {
        "name": "Lipitor",
        "generic": "Atorvastatin",
        "uses": "High cholesterol, cardiovascular prevention",
        "side_effects": "Muscle pain, liver issues, digestive problems",
        "dosage": "10-80mg once daily at night",
        "interactions": "Grapefruit, clarithromycin, warfarin",
        "category": "Statin",
        "manufacturer": "Pfizer Pakistan",
        "barcode": "8901234567895"
    },
    {
        "name": "Warf",
        "generic": "Warfarin",
        "uses": "Blood thinning, clot prevention",
        "side_effects": "Bleeding, bruising, rare skin necrosis",
        "dosage": "Varies (INR-based), usually 2-10mg/day",
        "interactions": "Aspirin, NSAIDs, antibiotics, vitamin K",
        "category": "Anticoagulant",
        "manufacturer": "Getz Pharma",
        "barcode": "8901234567896"
    },
    {
        "name": "Zoloft",
        "generic": "Sertraline",
        "uses": "Depression, anxiety, OCD, PTSD",
        "side_effects": "Nausea, insomnia, sexual dysfunction",
        "dosage": "50-200mg once daily",
        "interactions": "MAOIs, NSAIDs, warfarin, tramadol",
        "category": "SSRI Antidepressant",
        "manufacturer": "Pfizer Pakistan",
        "barcode": "8901234567897"
    },
    {
        "name": "Ventolin",
        "generic": "Salbutamol",
        "uses": "Asthma, COPD, bronchospasm",
        "side_effects": "Tremor, palpitations, headache",
        "dosage": "100-200mcg inhaler as needed",
        "interactions": "Beta blockers, diuretics, digoxin",
        "category": "Bronchodilator",
        "manufacturer": "GSK Pakistan",
        "barcode": "8901234567898"
    },
    {
        "name": "Risek",
        "generic": "Omeprazole",
        "uses": "Acid reflux, GERD, ulcers, heartburn",
        "side_effects": "Headache, diarrhea, B12 deficiency",
        "dosage": "20-40mg once daily before meal",
        "interactions": "Clopidogrel, methotrexate, ketoconazole",
        "category": "Proton Pump Inhibitor",
        "manufacturer": "Getz Pharma",
        "barcode": "8901234567899"
    },
    {
        "name": "Calpol",
        "generic": "Paracetamol (Syrup)",
        "uses": "Fever and pain in children",
        "side_effects": "Nausea, liver damage (overdose)",
        "dosage": "10-15mg/kg every 4-6 hours",
        "interactions": "Warfarin, alcohol",
        "category": "Pediatric Analgesic",
        "manufacturer": "GSK Pakistan",
        "barcode": "8901234567800"
    },
    {
        "name": "Ponstan",
        "generic": "Mefenamic Acid",
        "uses": "Pain, menstrual cramps, inflammation",
        "side_effects": "Stomach upset, diarrhea, headache",
        "dosage": "250-500mg three times daily after food",
        "interactions": "Warfarin, aspirin, lithium",
        "category": "NSAID",
        "manufacturer": "Pfizer Pakistan",
        "barcode": "8901234567801"
    }
]


# ============================================================
# DRUG INTERACTIONS
# ============================================================
INTERACTIONS = [
    {"drug_a": "Warfarin", "drug_b": "Aspirin", "severity": "SEVERE",
     "risk": "Increased bleeding risk", 
     "action": "Consult doctor immediately. Do not combine without supervision."},
    {"drug_a": "Warfarin", "drug_b": "Ibuprofen", "severity": "SEVERE",
     "risk": "Increased bleeding and GI ulcer risk",
     "action": "Avoid combination. Use Paracetamol instead for pain."},
    {"drug_a": "Warfarin", "drug_b": "Mefenamic Acid", "severity": "SEVERE",
     "risk": "Severe bleeding risk", 
     "action": "Avoid. Consult hematologist."},
    {"drug_a": "Ibuprofen", "drug_b": "Aspirin", "severity": "MODERATE",
     "risk": "Reduced aspirin cardioprotective effect + GI issues",
     "action": "Take at different times. Monitor for stomach issues."},
    {"drug_a": "Metformin", "drug_b": "Alcohol", "severity": "MODERATE",
     "risk": "Lactic acidosis risk", 
     "action": "Limit alcohol intake. Monitor blood sugar."},
    {"drug_a": "Atorvastatin", "drug_b": "Clarithromycin", "severity": "SEVERE",
     "risk": "Increased risk of muscle damage (rhabdomyolysis)",
     "action": "Consult doctor. May need dose adjustment."},
    {"drug_a": "Sertraline", "drug_b": "Tramadol", "severity": "SEVERE",
     "risk": "Serotonin syndrome risk", 
     "action": "Avoid combination. Consult psychiatrist."},
    {"drug_a": "Bisoprolol", "drug_b": "Verapamil", "severity": "SEVERE",
     "risk": "Severe bradycardia, heart block",
     "action": "Do not combine. Consult cardiologist."},
    {"drug_a": "Omeprazole", "drug_b": "Clopidogrel", "severity": "MODERATE",
     "risk": "Reduced clopidogrel effectiveness",
     "action": "Use Pantoprazole instead. Consult doctor."},
    {"drug_a": "Paracetamol", "drug_b": "Alcohol", "severity": "MODERATE",
     "risk": "Liver damage risk",
     "action": "Avoid alcohol while taking Paracetamol."},
    {"drug_a": "Salbutamol", "drug_b": "Bisoprolol", "severity": "MODERATE",
     "risk": "Reduced bronchodilator effect, bronchospasm",
     "action": "Use cardioselective beta blocker. Consult doctor."},
    {"drug_a": "Mefenamic Acid", "drug_b": "Aspirin", "severity": "MODERATE",
     "risk": "Increased GI bleeding risk",
     "action": "Take with food. Monitor for stomach issues."},
    {"drug_a": "Paracetamol", "drug_b": "Warfarin", "severity": "MODERATE",
     "risk": "Enhanced anticoagulant effect",
     "action": "Monitor INR regularly. Consult doctor."},
]


# ============================================================
# VERIFIED PHARMACIES (Karachi demo data)
# ============================================================
PHARMACIES = [
    {"name": "Aga Khan Pharmacy", "area": "Stadium Road", "city": "Karachi",
     "lat": 24.8930, "lng": 67.0740, "phone": "+92-21-3486-1234",
     "verified": True, "rating": 4.8, "timings": "24/7"},
    {"name": "D.Watson Chemist", "area": "Clifton", "city": "Karachi",
     "lat": 24.8138, "lng": 67.0300, "phone": "+92-21-3583-1234",
     "verified": True, "rating": 4.6, "timings": "9 AM - 11 PM"},
    {"name": "Fazal Din Pharma Plus", "area": "DHA Phase 5", "city": "Karachi",
     "lat": 24.8005, "lng": 67.0625, "phone": "+92-21-3584-1234",
     "verified": True, "rating": 4.7, "timings": "9 AM - 12 AM"},
    {"name": "Green Cross Pharmacy", "area": "Gulshan-e-Iqbal", "city": "Karachi",
     "lat": 24.9200, "lng": 67.0900, "phone": "+92-21-3498-1234",
     "verified": True, "rating": 4.5, "timings": "8 AM - 11 PM"},
    {"name": "Bilal Medical Store", "area": "Saddar", "city": "Karachi",
     "lat": 24.8607, "lng": 67.0011, "phone": "+92-21-3221-1234",
     "verified": True, "rating": 4.4, "timings": "9 AM - 10 PM"},
    {"name": "Shifa Pharmacy", "area": "North Nazimabad", "city": "Karachi",
     "lat": 24.9430, "lng": 67.0450, "phone": "+92-21-3672-1234",
     "verified": True, "rating": 4.6, "timings": "24/7"},
    {"name": "PIMS Pharmacy", "area": "PECHS", "city": "Karachi",
     "lat": 24.8700, "lng": 67.0650, "phone": "+92-21-3455-1234",
     "verified": True, "rating": 4.7, "timings": "9 AM - 11 PM"},
    {"name": "Sehat Pharmacy", "area": "Malir", "city": "Karachi",
     "lat": 24.8937, "lng": 67.2000, "phone": "+92-21-3450-1234",
     "verified": True, "rating": 4.3, "timings": "9 AM - 10 PM"},
]


# ============================================================
# HELPER FUNCTIONS
# ============================================================
def search_medicine(query: str):
    """Search medicines by name, generic, or uses."""
    query = query.lower().strip()
    return [
        m for m in MEDICINES
        if (query in m["name"].lower() 
            or query in m["generic"].lower()
            or query in m["uses"].lower()
            or query in m["category"].lower())
    ]


def find_medicine_by_name(name: str):
    """Exact match by name (case-insensitive)."""
    name = name.lower().strip()
    for m in MEDICINES:
        if m["name"].lower() == name or m["generic"].lower() == name:
            return m
    return None


def find_medicine_by_barcode(barcode: str):
    """Find medicine by barcode."""
    barcode = barcode.strip()
    for m in MEDICINES:
        if m["barcode"] == barcode:
            return m
    return None


def check_interaction(drug_a: str, drug_b: str):
    """Check if two drugs interact."""
    a = drug_a.lower().strip()
    b = drug_b.lower().strip()
    
    for i in INTERACTIONS:
        da = i["drug_a"].lower()
        db = i["drug_b"].lower()
        if (da == a and db == b) or (da == b and db == a):
            return i
    
    return {
        "drug_a": drug_a,
        "drug_b": drug_b,
        "severity": "SAFE",
        "risk": "No known interaction in our database",
        "action": "Safe to take together. Still consult your doctor if unsure."
    }


def get_all_medicine_names():
    """Return list of all medicine names."""
    return [m["name"] for m in MEDICINES]


def get_all_pharmacies():
    """Return all pharmacies."""
    return PHARMACIES
