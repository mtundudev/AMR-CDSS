import { useLocation } from "react-router-dom";

const pageMeta = {
    "/": { title: "Dashboard", subtitle: "Antimicrobial analysis overview" },
    "/new-analysis": { title: "New Analysis", subtitle: "Create a new sample analysis" },
    "/history": { title: "Analysis History", subtitle: "View all past analyses" },
};

function Header() {
    const location = useLocation();
    const meta = pageMeta[location.pathname] || pageMeta["/"];

    return (
        <header className="flex h-20 items-center justify-between border-b border-slate-200 bg-white px-6 lg:px-8">
            <div>
                <h2 className="text-lg font-semibold text-slate-900">
                    {meta.title}
                </h2>

                <p className="text-sm text-slate-500">
                    {meta.subtitle}
                </p>
            </div>

            <div className="flex items-center gap-3">
                <div className="hidden text-right sm:block">
                    <p className="text-sm font-medium text-slate-900">
                        Dr. Alfred
                    </p>

                    <p className="text-xs text-slate-500">
                        Healthcare Professional
                    </p>
                </div>

                <div className="flex h-10 w-10 items-center justify-center rounded-full bg-teal-100 font-semibold text-teal-700">
                    DA
                </div>
            </div>
        </header>
    );
}

export default Header;