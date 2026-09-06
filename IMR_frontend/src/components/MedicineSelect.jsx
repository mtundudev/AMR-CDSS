const MEDICINES = [
    { value: "amoxicillin", label: "Amoxicillin" },
    { value: "ciprofloxacin", label: "Ciprofloxacin" },
    { value: "doxycycline", label: "Doxycycline" },
    { value: "azithromycin", label: "Azithromycin" },
];

function MedicineSelect({ value, onChange, error }) {
    return (
        <div>
            <label
                htmlFor="medicine"
                className="text-sm font-medium text-slate-700"
            >
                Medicine
            </label>

            <select
                id="medicine"
                value={value}
                onChange={(event) => onChange(event.target.value)}
                className={`mt-2 w-full rounded-lg border bg-white px-4 py-3 text-sm outline-none transition focus:ring-2 ${
                    error
                        ? "border-red-400 focus:border-red-500 focus:ring-red-100"
                        : "border-slate-300 focus:border-teal-500 focus:ring-teal-100"
                }`}
            >
                <option value="">Select medicine</option>
                {MEDICINES.map((medicine) => (
                    <option key={medicine.value} value={medicine.value}>
                        {medicine.label}
                    </option>
                ))}
            </select>

            {error && (
                <p className="mt-1 text-xs text-red-600">
                    {error}
                </p>
            )}
        </div>
    );
}

export default MedicineSelect;