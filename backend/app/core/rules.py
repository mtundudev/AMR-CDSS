from app.schemas.plate_analysis import SusceptibilityStatus

# Official CLSI Standard Zone Diameter Interpretive Standards (in mm)
CLSI_ZONE_THRESHOLDS = {
    "Ciprofloxacin": {"susceptible_min": 21.0, "resistant_max": 15.0},
    "Ampicillin": {"susceptible_min": 17.0, "resistant_max": 13.0},
    "Gentamicin": {"susceptible_min": 15.0, "resistant_max": 12.0},
    "Ceftriaxone": {"susceptible_min": 23.0, "resistant_max": 19.0},
}

def classify_zone(antibiotic: str, diameter_mm: float) -> SusceptibilityStatus:
    """Classifies a measured diameter into S/I/R according to clinical tables."""
    rules = CLSI_ZONE_THRESHOLDS.get(antibiotic)
    
    # Default fallback if antibiotic isn't in standard rule table
    if not rules:
        return SusceptibilityStatus.SUSCEPTIBLE if diameter_mm >= 18.0 else SusceptibilityStatus.RESISTANT
    
    if diameter_mm >= rules["susceptible_min"]:
        return SusceptibilityStatus.SUSCEPTIBLE
    elif diameter_mm <= rules["resistant_max"]:
        return SusceptibilityStatus.RESISTANT
    else:
        return SusceptibilityStatus.INTERMEDIATE