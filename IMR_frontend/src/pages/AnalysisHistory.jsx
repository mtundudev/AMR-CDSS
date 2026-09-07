import { useState } from "react";
import { Link } from "react-router-dom";
import AnalysisCard from "../components/AnalysisCard";
import { getAnalyses, deleteAnalysis, clearAnalyses } from "../service/api";

function AnalysisHistory() {
    const [analyses, setAnalyses] = useState(getAnalyses());

    const handleDelete = (id) => {
        deleteAnalysis(id);
        setAnalyses(getAnalyses());
    };

    const handleClearAll = () => {
        clearAnalyses();
        setAnalyses([]);
    };

    return (
        <div className="mx-auto max-w-5xl">
            {/* Page heading */}
            <div className="flex flex-wrap items-end justify-between gap-4">
                <div>
                    <p className="text-sm font-medium text-teal-600">
                        ANALYSIS HISTORY
                    </p>

                    <h1 className="mt-2 text-3xl font-bold tracking-tight text-slate-900">
                        Analysis History
                    </h1>

                    <p className="mt-2 max-w-2xl text-slate-500">
                        View all previously analyzed samples and their results.
                    </p>
                </div>

                {analyses.length > 0 && (
                    <button
                        type="button"
                        onClick={handleClearAll}
                        className="rounded-lg border border-red-200 px-4 py-2 text-sm font-medium text-red-600 transition hover:bg-red-50"
                    >
                        Clear All
                    </button>
                )}
            </div>

            {/* Content */}
            <div className="mt-8">
                {analyses.length === 0 ? (
                    <div className="rounded-xl border border-dashed border-slate-300 bg-white p-12 text-center">
                        <p className="text-lg font-semibold text-slate-900">
                            No analyses yet
                        </p>

                        <p className="mt-2 text-sm text-slate-500">
                            Start a new analysis to see results here.
                        </p>

                        <Link
                            to="/new-analysis"
                            className="mt-6 inline-block rounded-lg bg-teal-500 px-5 py-3 text-sm font-semibold text-white transition hover:bg-teal-600"
                        >
                            + Start New Analysis
                        </Link>
                    </div>
                ) : (
                    <div className="grid gap-5">
                        {analyses.map((analysis) => (
                            <AnalysisCard
                                key={analysis.id}
                                analysis={analysis}
                                onDelete={handleDelete}
                            />
                        ))}
                    </div>
                )}
            </div>
        </div>
    );
}

export default AnalysisHistory;