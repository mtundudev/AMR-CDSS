const STORAGE_KEY = "amr_analyses";

/**
 * Read all analyses from localStorage.
 * @returns {Array} Array of analysis records.
 */
export function getAnalyses() {
    try {
        const raw = localStorage.getItem(STORAGE_KEY);
        return raw ? JSON.parse(raw) : [];
    } catch (error) {
        console.error("Failed to read analyses from localStorage:", error);
        return [];
    }
}

/**
 * Save a new analysis record to localStorage.
 * @param {Object} data - Analysis data (patientId, age, sex, disease, medicine, imageName, results).
 * @returns {Object} The saved analysis record with id and createdAt.
 */
export function saveAnalysis(data) {
    const analyses = getAnalyses();

    const nextNumber = analyses.length + 1;
    const record = {
        id: `AMR-${String(nextNumber).padStart(3, "0")}`,
        ...data,
        createdAt: new Date().toISOString(),
    };

    analyses.unshift(record);
    localStorage.setItem(STORAGE_KEY, JSON.stringify(analyses));

    return record;
}

/**
 * Delete a single analysis by id.
 * @param {string} id - The analysis id to remove.
 */
export function deleteAnalysis(id) {
    const analyses = getAnalyses().filter((item) => item.id !== id);
    localStorage.setItem(STORAGE_KEY, JSON.stringify(analyses));
}

/**
 * Remove all analyses from localStorage.
 */
export function clearAnalyses() {
    localStorage.removeItem(STORAGE_KEY);
}