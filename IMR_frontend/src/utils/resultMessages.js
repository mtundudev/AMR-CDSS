/**
 * Build ONE simple, AI-style answer based on the two model predictions.
 *
 * Priority:
 *   1. Resistant          → only the resistant recommendation
 *   2. High risk          → only the adverse-reaction warning
 *   3. Susceptible + Low  → the susceptible (low-risk) recommendation
 *
 * @param {"Resistant"|"Susceptible"} treatment - Treatment effectiveness prediction.
 * @param {"High"|"Low"} risk - Adverse reaction risk prediction.
 * @param {string} medicine - Name of the antimicrobial.
 * @returns {{ result: string, message: string }}
 */
export function getRecommendation(treatment, risk, medicine) {
    if (treatment === "Resistant") {
        return {
            result: "Resistant",
            message: `This sample is resistant to ${medicine}. This medicine may not work. Try another medicine.`,
        };
    }

    if (risk === "High") {
        return {
            result: "High risk",
            message: `${medicine} may cause bad side effects for this patient. Talk to a doctor before using this medicine.`,
        };
    }

    return {
        result: "Low risk",
        message: `This sample is not resistant to ${medicine}. The medicine should work. No strong risk of a bad reaction was predicted.`,
    };
}