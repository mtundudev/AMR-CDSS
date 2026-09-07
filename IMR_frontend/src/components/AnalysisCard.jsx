import { getRecommendation } from "../utils/resultMessages";

function AnalysisCard({ analysis, onDelete }) {
    const results = analysis.results || {
        treatmentEffectiveness: analysis.result === "Resistant" ? "Resistant" : "Susceptible",
        adverseReactionRisk: "Low",
    };

    const recommendation = getRecommendation(
        results.treatmentEffectiveness,
        results.adverseReactionRisk,
        analysis.medicine
    );

    const isGood = recommendation.result === "Low risk";

    return (
        <div className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
            <div className="flex items-start justify-between gap-4">
                <div className="min-w-0">
                    <div className="flex items-center gap-2">
                        <span className="font-semibold text-slate-900">
                            {analysis.id}
                        </span>

                        <span className="rounded-full bg-slate-100 px-2.5 py-0.5 text-xs font-semibold text-slate-600">
                            {new Date(analysis.createdAt).toLocaleString()}
                        </span>
                    </div>

                    {/* Single AI answer */}
                    <div
                        className={`mt-3 rounded-lg border p-3 ${
                            isGood
                                ? "border-teal-200 bg-teal-50/60"
                                : "border-red-200 bg-red-50/60"
                        }`}
                    >
                        <div className="flex items-center justify-between gap-3">
                            <p className="text-xs font-semibold text-slate-700">
                                Recommendation
                            </p>

                            <span
                                className={`shrink-0 rounded-full px-2.5 py-0.5 text-xs font-bold ${
                                    isGood
                                        ? "bg-teal-100 text-teal-700"
                                        : "bg-red-100 text-red-600"
                                }`}
                            >
                                {recommendation.result}
                            </span>
                        </div>

                        <p className="mt-2 text-sm leading-relaxed text-slate-700">
                            {recommendation.message}
                        </p>
                    </div>

                    <div className="mt-4 grid gap-3 sm:grid-cols-3">
                        <div>
                            <p className="text-xs text-slate-400">Patient ID</p>
                            <p className="mt-0.5 text-sm font-medium text-slate-900">
                                {analysis.patientId}
                            </p>
                        </div>

                        <div>
                            <p className="text-xs text-slate-400">Medicine</p>
                            <p className="mt-0.5 text-sm font-medium text-slate-900">
                                {analysis.medicine}
                            </p>
                        </div>

                        <div>
                            <p className="text-xs text-slate-400">Disease</p>
                            <p className="mt-0.5 text-sm font-medium text-slate-900">
                                {analysis.disease}
                            </p>
                        </div>
                    </div>
                </div>

                {onDelete && (
                    <button
                        type="button"
                        onClick={() => onDelete(analysis.id)}
                        className="shrink-0 rounded-lg px-3 py-2 text-sm font-medium text-red-600 transition hover:bg-red-50"
                    >
                        Delete
                    </button>
                )}
            </div>
        </div>
    );
}

export default AnalysisCard;