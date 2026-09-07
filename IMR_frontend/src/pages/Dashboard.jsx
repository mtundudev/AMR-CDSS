import { useState } from "react";
import { Link } from "react-router-dom";
import StatCard from "../components/statcard";
import { getAnalyses } from "../service/api";

function Dashboard() {
    const [analyses] = useState(getAnalyses());

    const total = analyses.length;
    const susceptible = analyses.filter((a) => a.result === "Susceptible").length;
    const resistant = analyses.filter((a) => a.result === "Resistant").length;
    const recent = analyses.slice(0, 5);

    return (
        <div className="mx-auto max-w-7xl">
            {/* Welcome */}
            <section>
                <h1 className="text-3xl font-bold tracking-tight text-slate-900">
                    Welcome back, Doctor
                </h1>

                <p className="mt-2 max-w-2xl text-slate-500">
                    Analyze biological samples using AI-assisted
                    antimicrobial susceptibility assessment.
                </p>
            </section>

            {/* Stats */}
            <section className="mt-8 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
                <StatCard
                    label="Total Analyses"
                    value={String(total)}
                    description="Samples analyzed"
                />

                <StatCard
                    label="Susceptible"
                    value={String(susceptible)}
                    description="Predicted susceptible"
                />

                <StatCard
                    label="Resistant"
                    value={String(resistant)}
                    description="Predicted resistant"
                />
            </section>

            {/* Quick action */}
            <section className="mt-8 rounded-xl bg-slate-900 p-8">
                <div className="max-w-2xl">
                    <p className="text-sm font-medium text-teal-400">
                        NEW ANALYSIS
                    </p>

                    <h2 className="mt-2 text-2xl font-bold text-white">
                        Analyze a new sample
                    </h2>

                    <p className="mt-2 text-slate-300">
                        Upload a sample image and provide the antimicrobial
                        being considered for AI-assisted analysis.
                    </p>

                    <Link
                        to="/new-analysis"
                        className="mt-6 inline-block rounded-lg bg-teal-500 px-5 py-3 text-sm font-semibold text-white transition hover:bg-teal-600"
                    >
                        + Start New Analysis
                    </Link>
                </div>
            </section>

            {/* Recent analyses */}
            <section className="mt-8">
                <div className="flex items-center justify-between">
                    <h2 className="text-lg font-semibold text-slate-900">
                        Recent Analyses
                    </h2>

                    <Link
                        to="/history"
                        className="text-sm font-medium text-teal-600 hover:text-teal-700"
                    >
                        View all
                    </Link>
                </div>

                {recent.length === 0 ? (
                    <div className="mt-4 rounded-xl border border-dashed border-slate-300 bg-white p-10 text-center">
                        <p className="text-sm text-slate-500">
                            No analyses yet. Start your first analysis.
                        </p>
                    </div>
                ) : (
                    <div className="mt-4 overflow-hidden rounded-xl border border-slate-200 bg-white">
                        <div className="grid grid-cols-3 border-b border-slate-200 px-6 py-4 text-xs font-semibold uppercase tracking-wide text-slate-400">
                            <span>Sample</span>
                            <span>Medicine</span>
                            <span>Result</span>
                        </div>

                        {recent.map((analysis, index) => {
                            const treatmentEffectiveness =
                                analysis.results?.treatmentEffectiveness ||
                                analysis.result;

                            return (
                                <div
                                    key={analysis.id}
                                    className={`grid grid-cols-3 px-6 py-5 text-sm ${
                                        index > 0 ? "border-t border-slate-100" : ""
                                    }`}
                                >
                                    <span className="font-medium text-slate-900">
                                        {analysis.id}
                                    </span>

                                    <span className="text-slate-500">
                                        {analysis.medicine}
                                    </span>

                                    <span
                                        className={`font-medium ${
                                            treatmentEffectiveness === "Resistant"
                                                ? "text-red-600"
                                                : "text-teal-600"
                                        }`}
                                    >
                                        {treatmentEffectiveness}
                                    </span>
                                </div>
                            );
                        })}
                    </div>
                )}
            </section>
        </div>
    );
}

export default Dashboard;