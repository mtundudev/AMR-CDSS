import { NavLink } from "react-router-dom";

const navItems = [
    { to: "/", label: "Dashboard" },
    { to: "/new-analysis", label: "New Analysis" },
    { to: "/history", label: "Analysis History" },
];

function Sidebar() {
    return (
        <aside className="fixed inset-y-0 left-0 hidden w-64 border-r border-slate-200 bg-white lg:block">
            <div className="flex h-full flex-col">
                {/* Logo */}
                <div className="flex h-20 items-center border-b border-slate-200 px-6">
                    <div>
                        <h1 className="text-xl font-bold text-slate-900">
                            AMR<span className="text-teal-500">AI</span>
                        </h1>

                        <p className="text-xs text-slate-500">
                            Diagnostic Assistant
                        </p>
                    </div>
                </div>

                {/* Navigation */}
                <nav className="flex-1 space-y-2 p-4">
                    {navItems.map((item) => (
                        <NavLink
                            key={item.to}
                            to={item.to}
                            end={item.to === "/"}
                            className={({ isActive }) =>
                                `flex items-center gap-3 rounded-lg px-4 py-3 text-sm font-medium transition ${
                                    isActive
                                        ? "bg-teal-50 text-teal-600"
                                        : "text-slate-600 hover:bg-slate-50"
                                }`
                            }
                        >
                            {item.label}
                        </NavLink>
                    ))}
                </nav>

                {/* Bottom */}
                <div className="border-t border-slate-200 p-4">
                    <p className="text-xs text-slate-400">
                        AI-assisted decision support
                    </p>
                </div>
            </div>
        </aside>
    );
}

export default Sidebar;