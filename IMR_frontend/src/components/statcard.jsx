function StatCard({ label, value, description }) {
    return (
        <div className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm">

            <p className="text-sm font-medium text-slate-500">
                {label}
            </p>

            <p className="mt-3 text-3xl font-bold text-slate-900">
                {value}
            </p>

            <p className="mt-1 text-xs text-slate-400">
                {description}
            </p>

        </div>
    );
}

export default StatCard;